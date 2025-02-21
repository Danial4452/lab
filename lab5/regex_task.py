import re



# 1. найти строки, в которых после а идет б 
print(bool(re.match(r"ab*", "Ablai khan was Khan of the Middle Jüz",re.IGNORECASE)))  # Первые две буквы подходят а наш паттерн выполняет задание полностью

# 2. теперь две три буквы б
pattern = r"\bab{2,3}\b" #Чисто чтоб в тексте 2 или 3 буквы б принимало 
text_abb = "Ayy, Mustard on the beat, ho , abbbb,Deebo any rap nigga, he a free throw"
print(bool(re.search(pattern, text_abb)))  

# 3. Ищем змей
print(re.findall(r"[a-z]+_[a-z]+", "Man down, call an amberlamps, tell_him, \"Breathe, bro\"")) #Возвращает листом

# 4. зАглавных букв
print(re.findall(r"[A-Z][a-z]+", "Nail a nigga to the cross, he walk around like Teezo, What's up with these jabroni-ass niggas tryna see Compton?"))

# 5. a________b
notlikeus = "The industry can hate me, fuck 'em all and they mama"
print(bool(re.search(r"a.*b", notlikeus)))  

# 6. Replace 

print(re.sub(r"[ ,.?']", ":", "How many opps you really got? I mean, it's too many options"))  

# 7. змею на верблюда
def snake_to_camel(s):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), s)

print(snake_to_camel("sssss_ssssss"))  

# 8. сплит 
print(re.split(r"(?=[A-Z])", "I'm finna pass on this body, I'm JohnStockton"))  

# 9. пробелы
print(re.sub(r"([A-Z])", r" \1", "Beat your ass and hide theBible ifGod watchin'").strip())  

# 10. верблюд на змею
def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower().lstrip('_')

print(camel_to_snake("uuAAUuuuuAAuuAa"))  