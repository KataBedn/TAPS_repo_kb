from datetime import datetime
import requests
import json
import time
import csv


def create_csv():
    with open('kurs.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Data", "Czas wykonania", "Kurs euro"])


def append_rate_csv(rate, req_time, duration):
    with open('kurs.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([str(req_time), str(duration), rate])


def currency():
    try:
        start_time = time.time()
        r = requests.get('https://api.ratesapi.io/api/latest?base=EUR&symbols=PLN')
        end_time = time.time()
        data = r.text
        parse = json.loads(data)
        rate = str(parse['rates']['PLN'])
        print('Kurs euro: ' + rate)
        req_time = datetime.now()
        req_duration = int((end_time - start_time) * 1000)
        duration = req_duration
        print('Data i godzina: ' + str(req_time))
        print('Czas wykonania zapytania: ' + str(duration) + ' ms')
        print('----------------------')
        append_rate_csv(rate, req_time, duration)
    except requests.exceptions.Timeout:
        print('Serwis chwilowo niedostępny - spróbuj ponownie później')


create_csv()
while True:
    currency()
    time.sleep(15)