import json
import pprint
import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def up_c_label(event):
    global name
    code = combobox.get()
    print(code)
    name = cur_crypt[code]
    print(name)
    c_label.config(text=name)
    print(c_label)

def exchange():
    code = combobox.get()
    global name
    if code:
        try:
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,cardano&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()
            print(data)
            exchange_rate = data[code]['usd']
            infolabel.config(text=f'Курс:  {exchange_rate:.2f} доллар за 1 {name}')

        except Exception as e:
            mb.showerror('Error', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Attention!', 'Введите код валюты')

cur_crypt = {
    'bitcoin': 'Биткоин',
    'cardano': 'Кардано',
    'ethereum':'Эфир'
}

name=None

window = Tk()
window.title('Курсы обмена криптовалют')
window.geometry('250x180')
Label(text='Выберите код валюты').pack(padx=10, pady=5)

combobox = ttk.Combobox(values=list(cur_crypt.keys()))
combobox.pack(padx = 10, pady = 5)
combobox.bind('<<ComboboxSelected>>', up_c_label)
c_label = ttk.Label(window)
c_label.pack(padx=10, pady=5)
Button(window, text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=5)
infolabel = Label(window, pady=5)
infolabel.pack(pady=5)
window.mainloop()