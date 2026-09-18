# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# Просим пользователя ввести свое имя
user_name = input('Здравствуйте, назовите ваше имя, пожалуйста! ')
print(f"Приветствую вас, {user_name}")

# Просим пользователя ввести свой возраст
user_age = int(input('Сколько вам лет? '))


# 2. Сбор данных
# Просим пользователя ввести вес в кг
user_weight = float(input('Каков ваш вес (в кг)? '))

# Просим пользователя ввести рост в метрах
user_height = float(input('Укажите ваш рост (в метрах, пример: 1.75)! '))
print("Спасибо, идет расчёт данных")


# Рассчет индекса массы тела (ИМТ)
def calculate_bmi(user_weight, user_height):
    """Считает индекс массы тела"""
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


WATER_FOR_1KG = 30  # Количество воды на 1 кг массы тела в мл
WATER_IN_LITERS = 1000  # Число для перевода мл в литры


# Подсчет воды: вес * 30 мл
def water_needed(user_weight):
    """Считает норму воды"""
    water_ml = user_weight * WATER_FOR_1KG
    water_l = water_ml / WATER_IN_LITERS
    return water_l


# 4. Вывод красивого результата
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш индекс массы тела: {calculate_bmi(user_weight, user_height)}")
print(f"Рекомендуемая норма воды: {water_needed(user_weight)} л. в день")
print("Расчет окончен. Будьте здоровы!")
