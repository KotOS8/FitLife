import sys

user_name = input('Здравствуйте, назовите ваше имя, пожалуйста! ')
print(f"Приветствую вас, {user_name}")


def int_input(question):
    """Чтение стандартного ввода, возврат int"""
    try:
        return int(input(question))
    except ValueError:
        print("Ожидалось целое число, программа завершена!")
        sys.exit()


def float_input(question):
    """Чтение стандартного ввода, возвращает float"""
    try:
        return float(input(question))
    except ValueError:
        print("Ожидалось число с плавающей точкой, программа завершена!")
        sys.exit()


user_age = int_input("Сколько вам лет? ")
user_weight = float_input('Каков ваш вес (в кг)? ')
user_height = float_input('Укажите ваш рост (в метрах, пример: 1.75)! ')

WATER_FOR_1KG = 30
WATER_IN_LITERS = 1000


# Рассчет индекса массы тела (ИМТ)
def calculate_bmi(user_weight, user_height):
    """Считает индекс массы тела"""
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


# Подсчет воды: вес * 30 мл
def water_needed(user_weight):
    """Считает норму воды"""
    water_ml = user_weight * WATER_FOR_1KG
    return water_ml / WATER_IN_LITERS


# 4. Вывод красивого результата
bmi = calculate_bmi(user_weight, user_height)
water_liters = water_needed(user_weight)
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_liters} л. в день")
print("Расчет окончен. Будьте здоровы!")
