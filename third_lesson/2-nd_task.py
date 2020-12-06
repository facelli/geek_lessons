# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def func(name, surname, borndate, homecity, email, phone):
    print(f"Hello, {name} {surname}, i know all about you!\n Look, you was born in {borndate}, \nand you live in {homecity}, your phone number is {phone} and email is {email}.")

func(phone="123456789",
     email="example@example.hell",
     homecity="Night City",
     borndate="1861",
     surname="Prokhorov",
     name="Eugene")