import requests
import json

def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    try:
        url = f"https://api.frankfurter.app/latest?from={from_currency.upper()}&to={to_currency.upper()}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        converted = data['rates']
        return json.dumps({
            "status": "success",
            "converted_amount": converted,
            "message": f"Converted {amount} {from_currency} to {converted} {to_currency}"
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "message": str(e)
        })