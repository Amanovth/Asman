from django.utils import timezone
from src.accounts.services import calculate_user_status
from .models import Payment, AsmanRate


def get_payment_type(payment_type):
    payment_types = {
        1: 'Покупка Asman',
        2: 'Ввод Asman',
        3: 'Вывод Asman',
        4: 'Покупка услуги',
        5: 'Перевод между пользователями'
    }
    return payment_types.get(payment_type, 'Неизвестный тип платежа')


def make_transfer(instance):
    amount = instance.amount
    payer = instance.payer
    recipient = instance.recipient

    payer.balance -= amount
    recipient.balance += amount

    payer.save()
    recipient.save()

    return


def make_payment(instance):
    amount = instance.partner.cost_of_visit
    user = instance.user
    partner = instance.partner

    user.balance -= amount
    partner.total_visits += 1

    user.save()
    partner.save()

    return


def payment_limit(request):
    user = request.user

    last_payment = Payment.objects.filter(user=user)

    if not last_payment.exists():
        return {'response': True}

    asman_rate = AsmanRate.objects.first()

    user_status = calculate_user_status(user.balance, asman_rate)

    days_since_last_payment = (timezone.now() - last_payment.order_by('-operation_time').first().operation_time).days

    if user_status == 'VIP' and days_since_last_payment < 2:
        return {'response': False, 'days': 2 - days_since_last_payment}
    elif user_status == 'Золото' and days_since_last_payment < 2:
        return {'response': False, 'days': 2 - days_since_last_payment}
    elif user_status == 'Серебро' and days_since_last_payment < 3:
        return {'response': False, 'days': 3 - days_since_last_payment}
    elif user_status == 'Бронза' and days_since_last_payment < 3:
        return {'response': False, 'days': 3 - days_since_last_payment}
    elif user_status == 'Стандарт' and days_since_last_payment < 4:
        return {'response': False, 'days': 4 - days_since_last_payment}
    else:
        return {'response': True}
