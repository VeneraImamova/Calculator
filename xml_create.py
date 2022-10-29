import csv
from datetime import datetime as dt


def write_ex(operation, num1, num2, result):
    # try:
        with open('calculate_operation.csv', 'a', encoding='utf-8', newline='') as file:
            date = dt.now().date()
            time = dt.now().strftime('%H:%M')
            writer = csv.writer(file, delimiter=";")
            writer.writerow([time, date, operation, num1, num2, result])
        return file

