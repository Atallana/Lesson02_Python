n = int(input("Введите месяц (1-12): "))

def month_to_season(n):
        if n in [1, 2, 12]:
            print("Зима")
        elif n in [3, 4, 5]:
            print("Весна")
        elif n in [6, 7, 8]:
            print("Лето")
        elif n in [9, 10, 11]:
            print("Осень")
        else:
            print("Неверный номер месяца")

month_to_season(n)