# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input("Введите сумму загаданных чисел: "))

p = int(input("Введите произведение загаданных чисел: "))

x = (s-int((s**2-4*p)**0.5))//2

y = (s+int((s**2-4*p)**0.5))//2

print(f"Задуманные Петей числа: {x, y}")