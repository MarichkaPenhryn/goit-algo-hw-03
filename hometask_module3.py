#-------------------------------------------------------------------------------------------------
#--------------- TASK 1 --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

import datetime
from datetime import datetime

# Функція: рахуємо порядковий номер введеного дня та сьогоднішнього, повертаємо різницю
# !!! питання: чи сьогоднішній день вважається повним? Тобто яка різниця між сьогодні та завтра? 
# Якщо хочемо бачити 0 днів (між сьогодні та завтра), то при отриманні difference < 0 треба додати 1 до результату

def get_days_from_today(date):
    date_inputed = datetime(year = int(date[:4]), month = int(date[5:7]), day = int(date[8:])).toordinal()
    date_now = datetime.now().toordinal()
    difference = date_now - date_inputed
    return difference
    
# зчитування даних

date = input('Date: ')

try:
    
    # Переводимо str в  datetime
    date_to_datetime = datetime(year = int(date[:4]), month = int(date[5:7]), day = int(date[8:]))
    #print(get_days_from_today(date))
except ValueError:
    print('Invalid date!')
    
#-------------------------------------------------------------------------------------------------
#--------------- TASK 2 --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

import random

def get_numbers_ticket(min, max, quantity):
# Створення змінної set
    my_set = set()
# Додавати числа поки довжина сету не буде quantity
    while len(my_set) < quantity :
        my_set.add(random.randint(min, max))
# Сортуємо set
    lst = sorted(my_set)
    return lst
    
#-------------------------------------------------------------------------------------------------
#--------------- TASK 3 --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

import re

def normalize_phone(phone_number):
    # Вибираємо в номері тільки цифри
    pattern = r"\d+"
    matches = re.findall(pattern, phone_number)
    number = ''
    # Складаємо шматки номера в один
    for j in matches:
        number += j
    # Дописуємо потрібні частинки
    if len(number) == 12: 
        number = '+' + number
    elif len(number) == 10: 
        number = '+38' + number
    return number
    
#raw_numbers = [
#                "067\\t123 4567",
#                "(095) 234-5678\\n",
#                "+380 44 123 4567",
#                "380501234567",
#                "    +38(050)123-32-34",
#                "     0503451234",
#                "(050)8889900",
#                "38050-111-22-22",
#                "38050 111 22 11   ",
#                ]


#sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
#print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#-------------------------------------------------------------------------------------------------
#--------------- TASK 4 --------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------

import datetime
from datetime import datetime

def get_upcoming_birthdays(users):
    # Створюємо datetime сьогоднішнього дня
    now = datetime.now()

    # Створюємо порядковий день сьогоднішнього дня
    date = datetime(year=now.year, month=now.month, day=now.day)
    now_ordinal_number = date.toordinal()

    # Створюємо список привітань
    congatulation_list = list()
    
    # Проходимось по кожному юзеру
    for user in users:
        congatulation_dict = {}
        # Перетворюємо ДН юзера в datetime
        user_birth = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Створюємо ДН в цього року
        user_birth_this_year = datetime(year=now.year, month=user_birth.month, day=user_birth.day)
        
        # Cтворюємо макет "вітального дня"
        user_congrats_day = datetime(year=now.year, month=user_birth.month, day=user_birth.day)
        
        # Якщо ДН протягом тижня то беремо його в обробку
        if (user_birth_this_year.toordinal() < now_ordinal_number + 8) and (user_birth_this_year.toordinal() >= now_ordinal_number):  
            
            # Якщо ДН - субота, то "вітальний день" переносимо на понеділок, створюємо словник юзера
            if user_congrats_day.weekday() == 5:
                user_congrats_day = datetime(year=user_congrats_day.year, month=user_birth.month, day=user_birth.day+2)
                congatulation_dict = dict(name =user["name"], congratulation_date = user_congrats_day.strftime("%Y-%m-%d"))
        
            # Якщо ДН - неділя, то "вітальний день" переносимо на понеділок, створюємо словник юзера
            elif user_congrats_day.weekday() == 6:
                user_congrats_day = datetime(year=user_congrats_day.year , month=user_birth.month, day=user_birth.day+1)
                congatulation_dict = dict(name =user["name"], congratulation_date = user_congrats_day.strftime("%Y-%m-%d"))
        
            # Якщо ДН - робочий день, то просто створюємо словник юзера
            else:
                congatulation_dict = dict(name =user["name"], congratulation_date = user_congrats_day.strftime("%Y-%m-%d"))
        
        # Додаємо до списку словник юзера 
        #(тільки якщо його словник не пустий тобто його ДН на цьому тижні)
        if congatulation_dict == {}:
            continue
        else:
            congatulation_list.append(congatulation_dict)
    return congatulation_list
    

