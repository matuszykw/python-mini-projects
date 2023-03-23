import requests
import smtplib

MY_EMAIL = "pythont50@gmail.com"
MY_PASSWORD = "xeecyttyfxgwvixh"

endpoint = "https://api.weatherapi.com/v1/forecast.json"
api_key = "145c72fcf77545cf90d145748232303"

parameters = {
    "key": api_key,
    "q": "49.601200,21.043619",
    "days": 1,
    "alerts": "no",
    "aqi": "no",
    "lang": "pl"
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
daily_forecast = weather_data['forecast']['forecastday'][0]["day"]
chance_of_rain = daily_forecast["daily_chance_of_rain"]
temp = daily_forecast["avgtemp_c"]
conditions = daily_forecast["condition"]['text']

alert_text = f"Dzisiejsza pogoda \n{conditions}, \n{temp}C \nSzansa opadow: {chance_of_rain}%"



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=MY_EMAIL, 
        msg=f"Subject: Pogoda.\n\nDzisiejsza pogoda {conditions}, {temp}C Szansa opadow: {chance_of_rain}"
    )