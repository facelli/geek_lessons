# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons = {
    (12, 1, 2): "зима",
    (3, 4, 5): "весна",
    (6, 7, 8): "лето",
    (9, 10, 11): "осень"
}
month = int(input("Введите номер месяца:\n").lower())

for value in seasons.keys():
    for digits in value:
        digits = int(digits)
        if digits == month:
            value=tuple(value)
            print(f"это {seasons.get(value)}")