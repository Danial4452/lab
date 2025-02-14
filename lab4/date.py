from datetime import datetime, timedelta


#Task 1
# Получаем нынешнюю дату плюс время
current_date = datetime.now()

# Минус 5 дней
new_date = current_date - timedelta(days=5)

print("Сейчас че? ", current_date)
print("А вот 5 дней назад у нас было:", new_date,"тогда ты был моложе и глупее.")

#Task 2
# Получаем текущую дату и даем имя тудей
today = datetime.now()

# То что не вернуть
yesterday = today - timedelta(days=1)

# То что искал чел из Семейки Крудс
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday,"было время.. помню как вчера")
print("Сегодня:", today)
print("Завтра:", tomorrow,"будет время..")


#Task 3


#Куррент дейт уже есть, продолжаем с ним, юзаем функ реплейс чтоб просто млсек заменить на ноль
current_date_without_sec = current_date.replace(microsecond=0)

print("Без фигни:", current_date_without_sec)


#Task 4

date1 = current_date
date2 = datetime(2006,8,24,12,0,0)

skok_mne = date1 - date2

#Юзаем тотал секондс для конверта
sec = skok_mne.total_seconds()

print("Сколь же мне секунд?",sec,"Вау,пол миллиарда секунд.....")


#Даже как то грустно стало 