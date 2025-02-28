import requests
class CurrencyConverter:
    def __init__(self):
        self.api_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            data = response.json()
            for currency in data:
                if currency['cc'] == 'USD':
                    return currency['rate']
            raise ValueError('Курс долара не знайдено.')
        except (requests.RequestException, ValueError) as e:
            print(f'Помилка при отриманні курсу : {e}')
            return None
    def convert_to_usd(self, amount_uah):
        if self.usd_rate is None:
            print('Неможливо виконати конвертацію без курсу долара')
            return None
        return amount_uah / self.usd_rate
if __name__ == '__main__':
    converter = CurrencyConverter()
    if converter.usd_rate:
        try:
            amount_uah = float(input('Введіть суму в гривнях: '))
            amount_usd = converter.convert_to_usd(amount_uah)
            print(f'{amount_uah} грн = {amount_usd:.2f} доларів')
        except ValueError:
            print('Введіть коректне числове значення')
