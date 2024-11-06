import json
import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def up_cr_label(event):
    global name
    code = combobox.get()
    name = cur_crypt[code]
    c_label.config(text=name)


def exchange():
    code = combobox.get()
    global name #Добавление глобальной переменной Имя для постановки в инфостроку
    if code:
        try:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()
            exchange_rate = data[code]['usd']
            infolabel.config(text=f'Курс: {exchange_rate:.2f} доллар США за 1 {name}')

        except Exception as e: #Проверка на ошибки
            mb.showerror('Error', f'Произошла ошибка: {e}.')
    else: #Окно всплывает, если не выбрана криптовалюта
        mb.showwarning('Attention!', 'Выберите в списке нужную криповалюту')

#Создание списка криптовалют в виде словаря для отображения пользователю
cur_crypt = {
    'bitcoin': 'Биткоин',
    'cardano': 'Кардано',
    'ethereum':'Эфир'
}


name=None

#Создание основного окна
window = Tk()
window.title('Курсы обмена криптовалют')
window.geometry('250x180')
Label(text='Выберите криптовалюту').pack(padx=10, pady=5)

#Создание основных виджетов
combobox = ttk.Combobox(values=list(cur_crypt.keys()))
combobox.pack(padx = 10, pady = 5)
combobox.bind('<<ComboboxSelected>>', up_cr_label)
c_label = ttk.Label(window)
c_label.pack(padx=10, pady=5)
Button(window, text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=5)
infolabel = Label(window, pady=5, font=('Arial', 10))
infolabel.pack(pady=5)


window.mainloop()