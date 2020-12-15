
import requests
import datetime
import time
import csv
from selenium.common.exceptions import TimeoutException


with open('ExchangeRate.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Kurs", "Data i godzina", "Czas"])


def exchangeRate():
        r = requests.get('http://api.frankfurter.app/latest?from=GBP')
        r_json = r.json()
        kurs = r_json['rates']['PLN']
        print("Kurs GBP:", kurs)
        data = r.headers['Date']
        print("Data i godzina:",data)
        durinms = datetime.datetime.strptime(str(r.elapsed),"%H:%M:%S.%f")
        czas = durinms.microsecond
        print("Czas wykonania zapytania:", czas,'ms')
        print('----------------------------------------------------')

        with open('ExchangeRate.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([kurs, data, czas])



def getRate():
    while True:
        exchangeRate()
        time.sleep(15)

try:
    getRate()
except TimeoutException:
     print('Timeout exception')




