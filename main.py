import random

upper_case = "QWERTZUIOPASDFGHJKLYXCVBNM"
lower_case = upper_case.lower()
number = "0123456789"
symbol = "!§$%&/()=?,.;:-_#+*'~{[]}\\"

upper, lower, numb, sym = True, True, True, True  # Enable/disable the letters symbols or numbers in the password

all = ""

if upper:
    all += upper_case

if lower:
    all += lower_case

if numb:
    all += number

if sym:
    all += symbol

length = 20  # length of the password
amount = 10  # amount of passwords

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)