import random as r

symbols = '=+#@*&^%~qwertyuiopasdfghjklzxcvbnm,.1234567890QWERTYUIOPASDFGHJKLZXCVBNM<>:;"!?/{}[]`'


kol = int(input('Введите количество паролей: '))
dlina = int(input('Введите длину паролей: '))
for n in range(kol):
    password =''
    for i in range(dlina):
        password += r.choice(symbols)
    print(password)
