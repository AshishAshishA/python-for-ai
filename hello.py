
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

name = "dave john"
len(name)
age = 19
has_license = True
drunk = True
can_vote = age >= 18 and has_license and not drunk

temperature = 25
if temperature > 30:
    print("It's hot outside.")
elif temperature < 10:
    print("It's cold outside.")
else:
    print("The weather is pleasant.")

for i in range(1, 6, 2):
    print("hello!"+str(i))

while temperature > 20:
    print("It's warm outside.")
    temperature -= 1

list = [1, 2, 3, 4, 5, "banana", "apple", False]
len(list)
list[0:3]
list.append("orange")
list.insert(2, "grape")
list.remove("banana")
list.pop()
del list[1]
print(list)
list.clear()

person = {
    "name": "dave john",
    "age": 19,
    "has_license": True,
    "drunk": True
}

person["name"] = "dave"
person["email"] = "dave@example.com"

del person["email"]
print(person)

tuple = (1, 2, 3, 4, 5)
print(tuple[0])

# tuple[0] = 2 not allowed
# print(tuple)

discount = 0.1
def printName(name, age):
    i = 0
    while i<5:
        print(name+"got discounted by "+str(discount)) 
        i += 1
    return True, discount

print(printName(name="dave", age=20))

from math import sqrt, pi
print(sqrt(16))
print(pi)

import requests
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude


url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

response = requests.get(url)
data = response.json()
print(data["current"]["temperature_2m"])


import requests
import pandas as pd
from datetime import datetime, timedelta
from pprint import pprint

today = datetime.now()
weekago = today - timedelta(days=7)

start_date = weekago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
pprint(data)


print(data.keys())

daily_data = data["daily"]

df =pd.DataFrame({
    "date": daily_data["time"],
    "max_temp":daily_data["temperature_2m_max"],
    "min_temp":daily_data["temperature_2m_min"]
})

df["date"] = pd.to_datetime(df["date"])

print(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.plot(
    df["date"],
    df["max_temp"],
    marker='o',
    label='Max Temp'
)

plt.plot(
    df["date"],
    df["min_temp"],
    marker='o',
    label='Min Temp'
)
plt.xlabel("Date")
plt.ylabel("Temp (°C)")
plt.title("Paris weather last 7 days")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

import os

if not os.path.exists("data"):
    os.makedirs("data")

df.to_csv("data/paris_weather.csv", index=False)
plt.savefig("data/weather_chart.png")
print("Data saved to data/paris_weather.csv")


# End of script