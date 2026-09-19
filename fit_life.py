import sys

WATER_FOR_1KG = 30
WATER_IN_LITERS = 1000

user_name = input('Здравствуйте, назовите ваше имя, пожалуйста! ')
print(f'Приветствую вас, {user_name}')

try:
    user_age = int(input('Сколько вам лет? '))
except ValueError:
    print('Ожидалось целое число, программа завершена')
    sys.exit

try:
    user_weight = float(input('Каков ваш вес (в кг)? '))
except ValueError:
    print('Ожидалось число с плавающей точкой, программа завершена')
    sys.exit

try:
    user_height = float(input('Укажите ваш рост (в метрах, пример: 1.75)! '))
except ValueError:
    print('Ожидалось число с плавающей точкой, программа завершена')
    sys.exit


def calculate_bmi(user_weight, user_height):
    """Считает индекс массы тела"""
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


def water_needed(user_weight):
    """Считает норму воды"""
    water_ml = user_weight * WATER_FOR_1KG
    return water_ml / WATER_IN_LITERS


bmi = calculate_bmi(user_weight, user_height)
water_liters = water_needed(user_weight)
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_liters} л. в день")
print("Расчет окончен. Будьте здоровы!")
