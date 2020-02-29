from tkinter import *
from tkinter import font, messagebox
import random
from PIL import Image, ImageTk
import _sqlite3 as s


def reg(event):
    def reg_enter(event):
        global s_reg
        reg_login = login_entry.get()
        reg_pass1 = pass1_entry.get()
        reg_pass2 = pass2_entry.get()
        cur = users.cursor()  # курсор в базе данных users cur = cursor
        cur.execute('''SELECT login FROM users''')  # считываем в курсор всех пользователей и пароли
        log = cur.fetchone()  # считываем одного из пользователей в БД
        while log is not None and log[0] != reg_login:  # пока не найдётся совпадение или пока не закончатся пользователи
            log = cur.fetchone()  # считываем ещё одного пользователя из БД
        if not(log is None):  # если такой логин не найден
            s_temp = 'Такое имя пользователя уже существует. \n\nПопробуйте ' + reg_login + str(random.randrange(100))
            messagebox.showinfo('Ошибка', s_temp)
        elif reg_pass1 != reg_pass2:
            messagebox.showinfo('Ошибка', 'Пароли не совпадают!')
        else:
            cur = users.cursor()  # курсор в базе данных users cur = cursor
            cur.execute("""INSERT INTO users (login, password, s_q, s_a, best_score, email, birthday, phone_number)
                              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(reg_login, reg_pass1, 'dump', 'dump', '0', 'a', 'b', 'c' ))
            users.commit()
            messagebox.showinfo("Регистрация", "Поздравляем, вы зарегистрировались!")
            s_reg = True

    window.withdraw()
    reg_window = Toplevel(window)  # создаём дочернее окно
    r_ws = reg_window.winfo_screenwidth()  # считываем текущую ширину экрана
    r_hs = reg_window.winfo_screenheight()  # считываем текущую высоту экрана
    reg_window.geometry('%dx%d+%d+%d' % (266, 90, (r_ws / 2) - 133, (r_hs / 2 - 45)))  # расположение по центру экрана
    reg_window.resizable(0, 0)  # запрещаем изменять размер окна
    reg_window.overrideredirect(1)  # отключаем рамку окна (нельзя переместить и закрыть)
    reg_caption = Label(reg_window, text="Регистрация", font=('Arial Black', 10))  # заголовок окна регистрации
    reg_caption.grid(row=0, column=0, columnspan=2)
    login_reg = Label(reg_window, text='Введите желаемое имя: ')  # заголовок поля для логина
    login_reg.grid(row=1, column=0, sticky=E)
    pass1_reg = Label(reg_window, text='Введите пароль: ')  # заголовок поля для пароля
    pass1_reg.grid(row=2, column=0, sticky=E)
    pass2_reg = Label(reg_window, text='Повторите пароль: ')  # заголовок поля для повторения пароля
    pass2_reg.grid(row=3, column=0, sticky=E)
    login_entry = Entry(reg_window, width=20)  # поле для ввода желаемого логина
    login_entry.grid(row=1, column=1)
    pass1_entry = Entry(reg_window, width=20)  # поле для ввода желаемого пароля
    pass1_entry.grid(row=2, column=1)
    pass2_entry = Entry(reg_window, width=20)  # поле для повтора желаемого пароля
    pass2_entry.grid(row=3, column=1)
# создаём рабочую часть
    login_entry.focus()  # устанавливаем фокус на поле ввода логина
    login_entry.bind('<Return>', reg_enter)  # регистрация по нажатию клавиши Enter из поля логина
    pass1_entry.bind('<Return>', reg_enter)  # регистрация по нажатию клавиши Enter из поля пароля
    pass2_entry.bind('<Return>', reg_enter)  # регистрация по нажатию клавиши Enter из поля пароля 2
# закрываем окно регистрации, переключаемся на окно авторизации
    if s_reg:
        window.deiconify()
        reg_window.quit()
    else:
        reg_window.mainloop()


def access_denied():  # функция запрета доступа
    access_denied_message = 'Вы совершили слишком большое количество попыток входа (' + str(authSuccess) + ').\n\nВ ' \
                                                                                                           'доступе ' \
                                                                                                           'отказано! '
    messagebox.showerror('Критическая ошибка!', access_denied_message)
    loginEntry.configure(state=DISABLED)
    passEntry.configure(state=DISABLED)
    label4.configure(state=DISABLED)
    registrationLabel.configure(state=DISABLED)
    forgetLabel.configure(text='Забыли пароль?')  # отключается возможность входа и появляется надпись "Забыли пароль?"


def enter(event):  # функция авторизации
    global authSuccess  # глобальная переменная для подсчета попыток неудачного входа
    cur = users.cursor()  # курсор в базе данных users cur = cursor
    cur.execute('''SELECT login, password FROM users''')  # считываем в курсор всех пользователей и пароли
    login = loginEntry.get()  # считываем введённый пользователем логин
    password = passEntry.get()  # считываем введённый пользователем пароль
    log = cur.fetchone()  # считываем одного из пользователей в БД
    while log is not None and log[0] != login:  # пока не найдётся совпадение или пока не закончатся пользователи
        log = cur.fetchone()  # считываем ещё одного пользователя из БД
    if log is None:  # если такой логин не найден
        messagebox.showwarning('Внимание!', 'Пользователь не найден!')  # выводим сообщение что логин не найден
    else:  # если такой логин найден, проверяется пароль
        if log[1] == password:
            print('Пароль верный! Добро пожаловать!')
        else:
            messagebox.showwarning('Внимание!', 'Пароль неверный!')
            authSuccess += 1
            if authSuccess == 3:  # после трёх неудачных попыток подобрать пароль возможность входа блокируется
                access_denied()


# ====== инициализация базы данных ======
users = s.connect('Top_secret.db')  # объект в базах данных
c = users.cursor()  # курсор в базе данных users c = cursor
c.execute('''CREATE TABLE IF NOT EXISTS users(login, password, s_q, s_a, best_score, email, birthday,
phone_number)''')  # s_q - контрольный вопрос, s_a - контрольный ответ

#  ====== задание основных параметров окна ======
window = Tk()  # создаём новую форму
ws = window.winfo_screenwidth()  # считываем текущую ширину экрана
hs = window.winfo_screenheight()  # считываем текущую высоту экрана
window.geometry('%dx%d+%d+%d' % (270, 160, (ws / 2) - 135, (hs / 2 - 80)))  # расположение по центру экрана
window.resizable(0, 0)  # запрещаем изменять размер окна
window.overrideredirect(1)  # отключаем рамку окна (нельзя переместить и закрыть)

#  ====== заполнение формы содержимым ======
authCaption = Label(window, text='Авторизация', font=('Arial Black', 12))  # Заголовок формы авторизации
authCaption.grid(row=0, column=0, columnspan=3)
loginLabel = Label(window, text='Логин')  # надпись "Логин"
loginLabel.grid(row=1, column=0)
passLabel = Label(window, text='Пароль')  # надпись "Пароль"
passLabel.grid(row=2, column=0)
loginEntry = Entry(window, width=20, bd=3)  # поле для ввода логина
loginEntry.grid(row=1, column=1)
passEntry = Entry(window, width=20, bd=3, show='*')  # поле для ввода пароля
passEntry.grid(row=2, column=1)
img = Image.open("king.png")  # добавляем на форму изображения Короля!
logo = ImageTk.PhotoImage(img)
label4 = Label(window, image=logo, cursor='heart')
label4.grid(row=1, column=2, rowspan=2)
forgetLabel = Label(window, text='',
                    cursor='hand2')  # Надпись "Забыли пароль?" неактивна и появляется только при неудачной попытке
# входа
forgetLabel.grid(row=3, column=0, columnspan=2, sticky=E)
f = font.Font(forgetLabel, forgetLabel.cget('font'))  # делаем текст в виде ссылки, с подчеркиванием
f.configure(underline=True)
forgetLabel.configure(font=f)
registrationLabel = Label(window, text='Регистрация', cursor='hand2')  # ссылка ведущая в форму регистрации
registrationLabel.grid(row=3, column=2)
f = font.Font(registrationLabel, registrationLabel.cget('font'))
f.configure(underline=True)
registrationLabel.configure(font=f)

#  ====== рабочая часть программы ======
loginEntry.focus()  # устанавливаем фокус на поле ввода логина
authSuccess = 0  # инициализируем счетчик попыток входа
s_reg = False  # статус процесса регистрации
label4.bind('<Button-1>', enter)  # авторизация по клику на "короле"
loginEntry.bind('<Return>', enter)  # авторизация по нажатию клавиши Enter из поля логина
passEntry.bind('<Return>', enter)  # авторизация по нажатию клавиши Enter из поля пароля
registrationLabel.bind('<Button-1>', reg)  # регистрация по нажатию на соответствующую ссылку

window.mainloop()
