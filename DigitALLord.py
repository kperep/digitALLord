from tkinter import *
from tkinter import font, messagebox
import random
from PIL import Image, ImageTk
import _sqlite3 as s


# функция регистрации
def reg(event):
    def reg_enter(event):
        reg_login = login_entry.get()            # Считываем желаемый логин
        reg_pass1 = pass1_entry.get()            # Считываем желаемый пароль
        reg_pass2 = pass2_entry.get()            # Считываем повтор желаемого пароля
        reg_s_q = s_q_entry.get()                    # Считываем секретный вопрос
        reg_s_a = s_a_entry.get()                    # Считываем ответ на секретный вопрос
        reg_birthday = birthday_entry.get()          # Считываем дату рождения
        reg_email = email_entry.get()                # Считываем e-mail
        reg_phone_number = phone_number_entry.get()  # Считываем номер телефона
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
                              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(reg_login, reg_pass1, reg_s_q, reg_s_a, '0', reg_email, reg_birthday, reg_phone_number))
            users.commit()
            messagebox.showinfo("Регистрация", "Поздравляем, вы зарегистрировались!")
            window.deiconify()  # переключаемся на окно авторизации
            reg_window.destroy()  # закрываем окно регистрации

    window.withdraw()              # скрываем родительское окно
    reg_window = Toplevel(window)  # создаём дочернее окно
    r_ws = reg_window.winfo_screenwidth()  # считываем текущую ширину экрана
    r_hs = reg_window.winfo_screenheight()  # считываем текущую высоту экрана
    reg_window.geometry('%dx%d+%d+%d' % (292, 220, (r_ws / 2) - 144, (r_hs / 2 - 110)))  # расположение по центру экрана
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
    s_q_reg = Label(reg_window, text='Секретный вопрос: ')  # заголовок поля для секретного вопроса
    s_q_reg.grid(row=4, column=0, sticky=E)
    s_a_reg = Label(reg_window, text='Ответ на секретный вопрос: ')  # заголовок поля для секретного ответа
    s_a_reg.grid(row=5, column=0, sticky=E)
    birthday_reg = Label(reg_window, text='Дата рождения: ')  # заголовок поля для даты рождения
    birthday_reg.grid(row=6, column=0, sticky=E)
    email_reg = Label(reg_window, text='E-mail: ')  # заголовок поля для e-mail
    email_reg.grid(row=7, column=0, sticky=E)
    phone_number_reg = Label(reg_window, text='Номер телефона: ')  # заголовок поля для номера телефона
    phone_number_reg.grid(row=8, column=0, sticky=E)
    login_entry = Entry(reg_window, width=20)  # поле для ввода желаемого логина
    login_entry.grid(row=1, column=1)
    pass1_entry = Entry(reg_window, width=20)  # поле для ввода желаемого пароля
    pass1_entry.grid(row=2, column=1)
    pass2_entry = Entry(reg_window, width=20)  # поле для повтора желаемого пароля
    pass2_entry.grid(row=3, column=1)
    s_q_entry = Entry(reg_window, width=20)  # поле для ввода секретного вопроса
    s_q_entry.grid(row=4, column=1)
    s_a_entry = Entry(reg_window, width=20)  # поле для ввода ответа на секретный вопрос
    s_a_entry.grid(row=5, column=1)
    birthday_entry = Entry(reg_window, width=20)  # поле для ввода даты рождения
    birthday_entry.grid(row=6, column=1)
    email_entry = Entry(reg_window, width=20)  # поле для ввода e-mail
    email_entry.grid(row=7, column=1)
    phone_number_entry = Entry(reg_window, width=20)  # поле для ввода даты рождения
    phone_number_entry.grid(row=8, column=1)
    submit_reg_button = Button(reg_window, text="Зарегистрироваться")
    submit_reg_button.grid(row=9, column=0, columnspan=2)
# создаём рабочую часть
    login_entry.focus()  # устанавливаем фокус на поле ввода логина
    login_entry.bind('<Return>', reg_enter)  # регистрация по нажатию клавиши Enter из поля логина
    pass1_entry.bind('<Return>', reg_enter)  # регистрация по нажатию клавиши Enter из поля пароля
    pass2_entry.bind('<Return>', reg_enter)  # регистрация по нажатию клавиши Enter из поля пароля 2
    submit_reg_button.bind('<Button-1>', reg_enter)  # регистрация по нажатию на кнопку "Зарегистрироваться"
# запускаем цикл дочернего окна
    reg_window.mainloop()


# функция восстановления пароля
def forget(event):
    window.withdraw()  # скрываем родительское окно
    forget_window = Toplevel(window)  # создаём дочернее окно
    f_ws = forget_window.winfo_screenwidth()  # считываем текущую ширину экрана
    f_hs = forget_window.winfo_screenheight()  # считываем текущую высоту экрана
    forget_window.geometry('%dx%d+%d+%d' % (306, 120, (f_ws / 2) - 153, (f_hs / 2 - 60)))  # расположение по центру экрана
    forget_window.resizable(0, 0)  # запрещаем изменять размер окна
    forget_window.overrideredirect(1)  # отключаем рамку окна (нельзя переместить и закрыть)
    forget_caption = Label(forget_window, text="Восстановление пароля", font=('Arial Black', 10))  # заголовок окна регистрации
    forget_caption.grid(row=0, column=0, columnspan=2)
    forget_login_label = Label(forget_window, text='Введите логин своего аккаунта')
    forget_login_label.grid(row=1, column=0)
    forget_login_entry = Entry(forget_window, width=20)  # поле для ввода логина с забытого аккаунта
    forget_login_entry.grid(row=1, column=1)


# функция запрета доступа
def access_denied():
    access_denied_message = 'Вы совершили слишком большое количество попыток входа (' + str(authSuccess) + ').\n\nВ ' \
                                                                                                           'доступе ' \
                                                                                                           'отказано! '
    messagebox.showerror('Критическая ошибка!', access_denied_message)
    loginEntry.configure(state=DISABLED)
    passEntry.configure(state=DISABLED)
    label4.configure(state=DISABLED)
    registrationLabel.configure(state=DISABLED)
    forgetLabel.configure(text='Забыли пароль?')  # отключается возможность входа и появляется надпись "Забыли пароль?"


# функция авторизации
def enter(event):
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
window.geometry('%dx%d+%d+%d' % (280, 150, (ws / 2) - 140, (hs / 2 - 75)))  # расположение по центру экрана
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
                    cursor='hand2')  # Надпись "Забыли пароль?" неактивна и появляется только при неудачной попытке входа
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
label4.bind('<Button-1>', enter)  # авторизация по клику на "короле"
loginEntry.bind('<Return>', enter)  # авторизация по нажатию клавиши Enter из поля логина
passEntry.bind('<Return>', enter)  # авторизация по нажатию клавиши Enter из поля пароля
registrationLabel.bind('<Button-1>', reg)  # регистрация по нажатию на соответствующую ссылку
forgetLabel.bind('<Button-1>', forget)  # запуск восстановления пароля по нажатию на надпись "Забыли пароль?"

# запускаем цикл дочернего окна
window.mainloop()
