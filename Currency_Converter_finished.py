
import requests


KEY="13dd9eac23c49a13399d06f1"


AMOUNT=str(input('choose the amount to convert: '))

from_cur=str(input("choose the currency to convert from, eg.(USD or IRR ): ")).upper()


to_cur=str(input("choose the currency to convert to eg.( IRR or USD ): ")).upper()

URL=f"https://v6.exchangerate-api.com/v6/{KEY}/pair/{from_cur}/{to_cur}/{AMOUNT}"

response=requests.get(URL)

data=response.json()

convertion=data["conversion_result"]

final=f"{AMOUNT} {from_cur} = {convertion} {to_cur}"

print(final)


