from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import csv

# INPUT DATE FORMAT FOR USER
date_format = "%d/%m/%Y"

# FUNCTION TO DETERMINATE PAYMENT DATE
# @param delivery_date: date_format which is input user date
# @return output_date: date which is payment date
def payment_date(delivery_date):
    check_error = delivery_date
    try:
        delivery_date = datetime.strptime(delivery_date, date_format)
        delivery_date = delivery_date.date()
        x = delivery_date + timedelta(30)
    except:
        with open("error.txt", "a") as txtfile:
            txtfile.write(f"\nWrong format {check_error}, Required: dd/mm/yyyy, at {datetime.today()}")
    
    # WRITE PAYMENT DATE IN CSV FILE IN EXCEL FORMAT
    # WRITE ERROR IN TXT FILE
    with open("data.csv", "a") as csvfile:
        writer = csv.writer(csvfile, dialect="excel", delimiter=" ")
        input_date = delivery_date.strftime(date_format)

        # header = ["Date de livraison", "Date de paiement"]
        # writer.writerow(header)

        if x.day <= 10:
            output_date = date(x.year, x.month, 10).strftime(date_format)
            line = [input_date, output_date]
            writer.writerow(line)
            return output_date
        else:
            y = x + relativedelta(months=1)
            output_date = date(x.year, y.month, 10).strftime(date_format)
            line = [input_date, output_date]
            writer.writerow(line)
            return output_date


while True:
    scanf = input("Entrez une date au format dd/mm/yyyy\n")
    payment_date(scanf)

    user_answer = input("Arreter ? O ou N\n")
    if user_answer == "O":
        break

