import datetime as dt


class Record:
<<<<<<< HEAD

    def __init__(self, amount, comment, date=None):
        self.amount = float(amount)
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()
=======
    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = float(amount)
        self.comment = comment
        if isinstance(date, dt.date) == False:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = date
>>>>>>> c85d78afbfb350d3436fbe05811b27ca98d13a74


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
<<<<<<< HEAD
        self.records.append(new_record)

    def get_today_stats(self):
        today = dt.date.today()
        today_amount = sum([record.amount for record in self.records if record.date == today])
        return today_amount

    def get_week_stats(self):
        today = dt.date.today()
        time_delta = dt.timedelta(days=7)
        week_amount = float(
            sum([record.amount for record in self.records if today - time_delta <= record.date <= today]))
        return week_amount

    def get_today_remained(self):
        today_amount = self.get_today_stats()
        balance = round(self.limit - today_amount, 2)
        return balance


class CashCalculator(Calculator):

    USD_RATE = 60.0
    EURO_RATE = 70.0
    RUB_RATE = 1.0

    currencies = {
        'eur': ('Euro', EURO_RATE),
        'usd': ('USD', USD_RATE),
        'rub': ('руб', RUB_RATE),
    }

    def get_today_cash_remained(self, currency):
        today_remained = self.get_today_remained()
        today_remained_currency = abs(round(today_remained / CashCalculator.currencies[currency][1], 2))

        if not today_remained:
            return 'Денег нет, держись'
        elif today_remained > 0:
            return (f'На сегодня осталось {today_remained_currency} {CashCalculator.currencies[currency][0]}')
        else:
            return (
                f'Денег нет, держись: твой долг - {today_remained_currency} {CashCalculator.currencies[currency][0]}')
=======
        self.new_record = new_record
        self.records.append(new_record)

    def get_today_stats(self):
        today_amount = 0
        for record in self.records:
            if record.date == dt.date.today():
                today_amount += abs(record.amount)
        return float(today_amount)

    def get_week_stats(self):
        week_amount = 0
        for record in self.records:
            if record.date >= (dt.date.today() - dt.timedelta(days=7)) and record.date <= dt.date.today():
                week_amount += abs(record.amount)
        return float(week_amount)


class CashCalculator(Calculator):
    USD_RATE = 60.0
    EURO_RATE = 70.0

    def get_today_cash_remained(self, currency):
        self.currency = currency
        today_limit = self.get_today_stats()
        if today_limit < self.limit:
            if currency == 'rub':
                return (f'На сегодня осталось {round((self.limit - today_limit), 2)} руб')
            elif currency == 'usd':
                return (
                    f'На сегодня осталось {round(((self.limit - today_limit) / CashCalculator.USD_RATE), 2)} USD')
            elif currency == 'eur':
                return (
                    f'На сегодня осталось {round(((self.limit - today_limit) / CashCalculator.EURO_RATE), 2)} Euro')



        elif today_limit == self.limit:
            return ('Денег нет, держись')

        elif today_limit > self.limit:
            if currency == 'rub':
                return (f'Денег нет, держись: твой долг - {round((today_limit - self.limit), 2)} руб')
            elif currency == 'usd':
                return (
                    f'Денег нет, держись: твой долг - {round(((today_limit - self.limit) / CashCalculator.USD_RATE), 2)} USD')
            elif currency == 'eur':
                return (
                    f'Денег нет, держись: твой долг - {round(((today_limit - self.limit) / CashCalculator.EURO_RATE), 2)} Euro')
>>>>>>> c85d78afbfb350d3436fbe05811b27ca98d13a74


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
<<<<<<< HEAD
        today_remained = self.get_today_remained()

        if today_remained > 0:
            today_remained = int(today_remained)
            return (
                f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {today_remained} кКал')
        else:
            return 'Хватит есть!'
=======
        today_limit = int(self.get_today_stats())
        if self.limit > today_limit:
            return (
                f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {int(self.limit - today_limit)} кКал')
        else:
            return ('Хватит есть!')
>>>>>>> c85d78afbfb350d3436fbe05811b27ca98d13a74
