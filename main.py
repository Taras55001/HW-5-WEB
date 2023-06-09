import aiohttp
import asyncio
import sys
import datetime
import json


class Currency:
    def __init__(self, name,saleRate,purchaseRate):
        self.name = name
        self.sale_rate = saleRate
        self.purchase_rate = purchaseRate


class Record:
    currency_dict = {}
    def __init__(self, date: datetime):
        self.date = date
    
    def add_currency(self, currency:Currency):
        self.currency_dict[currency.name] = [currency.sale_rate, currency.purchase_rate]
    
    def get_currency(self, currency):
        for i in self.currency_dict.keys():
            if currency == i:
                return f'Date: {self.date.strftime("%d-%m-%Y")}, Currency: "{i}", Sale Rate: {self.currency_dict.get(i)[0]}, Purchase Rate: {self.currency_dict.get(i)[1]}'
    


API_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date="


async def fetch_exchange_rate(session, date):
    async with session.get(API_URL + date) as response:
        return await response.text()


async def get_exchange_rates(dates):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for date in dates:
            task = asyncio.create_task(fetch_exchange_rate(session, date))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        return results


def parse_exchange_rate(response):
    try:
        data = json.loads(response)
    except Exception as error:
        raise error
    exchange_rates = data["exchangeRate"]
    
    day = datetime.datetime.strptime(data["date"], '%d.%m.%Y').date()
    rec = Record(day)
    for rate in exchange_rates:
        currency = Currency(rate.get("currency"),rate.get("saleRate"),rate.get("purchaseRate"))
        rec.add_currency(currency)

    return rec

def print_main_currency(exchange_rates):
    for day in exchange_rates:
        data = parse_exchange_rate(day)
        print(data.get_currency("EUR") + '\n')
        print(data.get_currency("USD") + '\n' + '-' * 80)

def get_recent_dates(num_days):
    today = datetime.date.today()
    dates = []
    for i in range(num_days):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime("%d.%m.%Y"))
    return dates[:10]


async def main():
    num_days = int(sys.argv[1])
    if num_days > 10:
        raise ValueError("Maximum number of days exceeded.")
    
    dates = get_recent_dates(num_days)
    exchange_rates = await get_exchange_rates(dates)
    print_main_currency(exchange_rates)

    


if __name__ == "__main__":
    asyncio.run(main())