import smtplib
import datetime as dt
import random
import pandas

data = pandas.read_csv('persondetails.csv')
person_dict = {'name', 'email'}
data_list = data.to_dict(orient='records')
# print(len(data_list))
dict_name = []
dict_mail = []
for i in range(len(data_list)):
    data_dict = data_list[i]
    dict_name.append(data_dict['name'])
    # print(dict_name)
    dict_mail.append(data_dict['email'])

# print(dict_name, dict_mail)

my_email = 'sahilshah062018@gmail.com'
password = 'tvrztjbkboyogbna'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0 or weekday == 1 or weekday == 2 or weekday == 3 or weekday == 4 or weekday == 5 or weekday == 6:
    with open('quotes.txt') as quotes_file:
        all_quotes = quotes_file.readlines()
        random_quote = random.choice(all_quotes)

    for i in range(len(dict_mail)):
        email = dict_mail[i]
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=email, msg=f'Subject: {dt.datetime.today().strftime("%A")}  Motivation\n\n'
                                                                                            f'{random_quote}')

