def dvoichnaya(x):
    y = ''
    while x>0:
        y = str(x%2) + y
        x = x//2
    return y
def vosmerichnaya(x):
    y = ''
    while x>0:
        y = str(x%8) + y
        x = x//8
    return y
print ('введите число:')
try:
    a = int(input())
except ValueError:
    print ('ошибка: не работаю с введенным типом данных')
else:
    if a<=0:
        print('ошибка: работаю только с положительными значениями чисел')
    else:
        print ('введите целевую систему счисления:')
        try:
            systema = int(input())
        except ValueError:
            print('ошибка ввода данных')
        else:
            if systema==2:
                print('введенное число в двоичной системе счисления:',dvoichnaya(a))
            if systema==8:
                print('введенное число в восьмеричной системе счисления:',vosmerichnaya(a))
            else:
                print('ошибка ввода данных')
           
            
