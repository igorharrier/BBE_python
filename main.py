print('')
print('Добро пожаловать в Найт Сити Банк!')
print('')
print('Для начала работы с сервисом требуется регистрация в системе.')
print('')пше

accounts = {}


def save_accounts_to_file():
    with open('accounts_data.txt', 'w') as file:
        for account_key, account_value in accounts.items():
            file.write(f'{account_key}: {account_value}\n')


def load_accounts_from_file():
    try:
        with open('accounts_data.txt', 'r') as file:
            for line in file:
                account_key, account_value = line.strip().split(': ', 1)
                accounts[account_key] = eval(account_value)
    except FileNotFoundError:
        print("Файл с данными аккаунтов не найден, загрузка пропущена.")


load_accounts_from_file()

while True:
    print('Выберите операцию:')
    print('')
    print('1. Создать аккаунт')
    print('2. Положить деньги на счет')
    print('3. Снять деньги')
    print('4. Вывести баланс на экран')
    print('5. Выставление ожидаемого пополнения (транзакция)')
    print('6. Установить лимит на счет')
    print('7. Применить транзакции')
    print('8. Статистика по ожидаемым пополнениям')
    print('9. Выйти из программы')
    print('')
    choice = input('Введите номер операции: ')

    if choice == '1':
        full_name = input('Введите ФИО: ')
        birth_year = int(input('Введите год рождения: '))
        password = input('Создайте пароль для аккаунта: ')
        accounts['current'] = {'full_name': full_name, 'birth_year': birth_year, 'balance': 0, 'password': password,
                               'transactions': [], 'limit': float('inf')}
        print('Создан аккаунт:', full_name, '(', 2024 - birth_year, 'лет)')
        print('')
    elif choice == '2':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
            print('')
        else:
            amount = int(input('Введите сумму пополнения: '))
            accounts['current']['balance'] += amount
            print('Счёт успешно пополнен! Новый баланс:', accounts['current']['balance'], 'руб.')
            print('')
    elif choice == '3':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
            print('')
        else:
            password = input('Введите пароль: ')
            if password == accounts['current']['password']:
                print('Ваш баланс:', accounts['current']['balance'], 'руб.')
                amount = int(input('Введите сумму для снятия: '))
                print('')
                if amount > accounts['current']['balance']:
                    print('Недостаточно средств на счете.')
                    print('')
                else:
                    accounts['current']['balance'] -= amount
                    print('Снятие успешно завершено, ваш баланс:', accounts['current']['balance'], 'руб.')
                    print('')
            else:
                print('Неверный пароль.')
                print('')
    elif choice == '4':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
            print('')
        else:
            password = input('Введите пароль: ')
            if password == accounts['current']['password']:
                print('Ваш баланс:', accounts['current']['balance'], 'руб.')
                print('')
            else:
                print('Неверный пароль.')
                print('')
    elif choice == '5':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
        else:
            amount = int(input('Введите сумму будущего пополнения: '))
            comment = input('Введите комментарий к транзакции: ')
            accounts['current']['transactions'].append({'amount': amount, 'comment': comment})
            print(f'Транзакция добавлена. Всего ожидаемых пополнений: {len(accounts["current"]["transactions"])}.')

    elif choice == '6':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
        else:
            limit = float(input('Установите лимит на счет: '))
            accounts['current']['limit'] = limit
            print(f'Лимит в размере {limit} руб. успешно установлен.')

    elif choice == '7':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
        else:
            for transaction in accounts['current']['transactions'][:]:
                if accounts['current']['balance'] + transaction['amount'] <= accounts['current']['limit']:
                    accounts['current']['balance'] += transaction['amount']
                    print(
                        f'Транзакция "{transaction["comment"]}" на сумму {transaction["amount"]} руб. успешно применена.')
                    accounts['current']['transactions'].remove(transaction)
                else:
                    print(
                        f'Транзакция "{transaction["comment"]}" на сумму {transaction["amount"]} руб. не может быть применена (превышен лимит).')
            print('Все возможные транзакции обработаны.')

    elif choice == '8':
        if 'current' not in accounts:
            print('Сначала создайте аккаунт.')
        else:
            transaction_amounts = {}
            for transaction in accounts['current']['transactions']:
                if transaction['amount'] in transaction_amounts:
                    transaction_amounts[transaction['amount']] += 1
                else:
                    transaction_amounts[transaction['amount']] = 1
            for amount, count in transaction_amounts.items():
                print(f'{amount} руб: {count} платеж(а)')

    elif choice == '9':
        save_accounts_to_file()
        print('')
        print('Благодарим за использование Найт Сити Банка!')
        print('Ждем вас снова и отличного дня.')
        print('')
        break
    else:
        print('Неверная команда. Попробуйте еще раз.')
        print('')
