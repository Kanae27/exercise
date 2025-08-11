from datetime import datetime

name = input("Enter your name: ")
age = input("Enter your age: ")

current_date_time = datetime.now()

current_year = current_date_time.year

age1 = 100 - int(age)

date = current_date_time.year + age1 
print (f"{name}, you will turn 100 years old in the year {date}.")

