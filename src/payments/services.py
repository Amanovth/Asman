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
