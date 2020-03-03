from tkinter import *
from tkinter import font, messagebox
import random
from PIL import Image, ImageTk
import _sqlite3 as s


# функция регистрации
def reg(event):
    def reg_enter(event):
        reg_login = login_entry.get()  # Считываем желаемый логин
        reg_pass1 = pass1_entry.get()  # Считываем желаемый пароль
        reg_pass2 = pass2_entry.get()  # Считываем повтор желаемого пароля
        reg_s_q = s_q_entry.get()  # Считываем секретный вопрос
        reg_s_a = s_a_entry.get()  # Считываем ответ на секретный вопрос
        reg_birthday = birthday_entry.get()  # Считываем дату рождения
        reg_email = email_entry.get()  # Считываем e-mail
        reg_phone_number = phone_number_entry.get()  # Считываем номер телефона
        cur = users.cursor()  # курсор в базе данных users cur = cursor
        cur.execute('''SELECT login FROM users''')  # считываем в курсор всех пользователей и пароли
        log = cur.fetchone()  # считываем одного из пользователей в БД
        while log is not None and log[
            0] != reg_login:  # пока не найдётся совпадение или пока не закончатся пользователи
            log = cur.fetchone()  # считываем ещё одного пользователя из БД
        if not (log is None):  # если такой логин найден
            s_temp = 'Такое имя пользователя уже существует. \n\nПопробуйте ' + reg_login + str(random.randrange(100))
            messagebox.showinfo('Ошибка', s_temp)
        elif reg_pass1 != reg_pass2:
            messagebox.showinfo('Ошибка', 'Пароли не совпадают!')
        else:
            cur = users.cursor()  # курсор в базе данных users cur = cursor
            cur.execute("""INSERT INTO users (login, password, s_q, s_a, best_score, email, birthday, phone_number)
                              VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                reg_login, reg_pass1, reg_s_q, reg_s_a, '0', reg_email, reg_birthday, reg_phone_number))
            users.commit()
            messagebox.showinfo("Регистрация", "Поздравляем, вы зарегистрировались!")
            window.deiconify()  # переключаемся на окно авторизации
            reg_window.destroy()  # закрываем окно регистрации

    window.withdraw()  # скрываем родительское окно
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
    def check_login(event):
        def s_a_check(event):
            login_global = forget_login_entry.get()
            curs = users.cursor()  # курсор в базе данных users cur = cursor
            curs.execute(
                '''SELECT login, password, s_a FROM users''')  # считываем в курсор всех пользователей, пароли и
            # секретные ответы
            lg = curs.fetchone()  # считываем одного из пользователей в БД
            while lg[0] != login_global:  # пока не найдётся совпадение или пока не закончатся пользователи
                lg = curs.fetchone()  # считываем ещё одного пользователя из БД
            user_s_a = s_a_entry.get()  # считываем пользовательский вариант ответа
            if user_s_a != lg[2]:  # если он не совпадает с ответом из базы данных, сообщаем об этом
                messagebox.showwarning('Ошибка', 'Ваш ответ не совпал с ответом в базе данных!')
            else:  # если ответы совпадают
                temp_string = 'Ваш пароль: ' + lg[1]
                messagebox.showinfo('Поздравляем!', temp_string)  # сообщаем пользователю его пароль
                loginEntry.configure(state=NORMAL)  # включаем
                passEntry.configure(state=NORMAL)  # все поля
                label4.configure(state=NORMAL)  # на форме
                registrationLabel.configure(state=NORMAL)  # авторизации
                window.deiconify()  # переключаемся на окно авторизации
                forget_window.destroy()  # закрываем окно регистрации

        login2check = forget_login_entry.get()  # считываем логин для проверки
        cur = users.cursor()  # курсор в базе данных users cur = cursor
        cur.execute(
            '''SELECT login, password, s_q, s_a FROM users''')  # считываем в курсор всех пользователей, пароли,
        # секретные вопросы и ответы
        log = cur.fetchone()  # считываем одного из пользователей в БД
        while log is not None and log[
            0] != login2check:  # пока не найдётся совпадение или пока не закончатся пользователи
            log = cur.fetchone()  # считываем ещё одного пользователя из БД
        if not (log is None):  # если такой логин найден
            check_log_button.destroy()
            result_label.configure(text='Пользователь найден',
                                   fg='#000')  # выводим сообщение об этом нормальным шрифтом
            instruction_label = Label(forget_window, text='Пожалуйста, ответьте на секретный вопрос:')
            instruction_label.grid(row=3, column=0, columnspan=3)  # надпись с просьбой ответить на секретный вопрос
            s_q_label = Label(forget_window, text=log[2], font=('Arial Black', 8),
                              fg='#55F')  # выделяем секретный вопрос шрифтом и цветом
            s_q_label.grid(row=4, column=0, columnspan=3)
            s_a_label = Label(forget_window,
                              text='Ваш ответ:')  # надпись с предложением пользователю ввести свой вариант ответа
            s_a_label.grid(row=5, column=0)
            s_a_entry = Entry(forget_window, width=35)  # поле для ввода ответа на секретный вопрос
            s_a_entry.grid(row=5, column=1, sticky=W, columnspan=2)
            s_a_button = Button(forget_window, text='Отвечаю!')  # кнопка для отправки варианта ответа на вопрос
            s_a_button.grid(row=6, column=0, columnspan=3)
            s_a_entry.bind('<Return>', s_a_check)  # проверка ответа на секретный вопрос по нажатию Enter
            s_a_button.bind('<Button-1>',
                            s_a_check)  # проверка ответа на секретный вопрос по клику на кнопку "Отвечаю!"
        else:
            result_label.configure(text='Пользователь не найден',
                                   fg='#F00')  # если пользователь не найден - красное сообщение

    window.withdraw()  # скрываем родительское окно
    forget_window = Toplevel(window)  # создаём дочернее окно
    f_ws = forget_window.winfo_screenwidth()  # считываем текущую ширину экрана
    f_hs = forget_window.winfo_screenheight()  # считываем текущую высоту экрана
    forget_window.geometry(
        '%dx%d+%d+%d' % (306, 160, (f_ws / 2) - 153, (f_hs / 2 - 80)))  # расположение по центру экрана
    forget_window.resizable(0, 0)  # запрещаем изменять размер окна
    forget_window.overrideredirect(1)  # отключаем рамку окна (нельзя переместить и закрыть)
    forget_caption = Label(forget_window, text="Восстановление пароля",
                           font=('Arial Black', 10))  # заголовок окна восстановления пароля
    forget_caption.grid(row=0, column=0, columnspan=3)
    forget_login_label = Label(forget_window,
                               text='Введите логин своего аккаунта')  # надпись с просьбой ввести искомый логин
    forget_login_label.grid(row=1, column=0, columnspan=2)
    forget_login_entry = Entry(forget_window, width=20)  # поле для ввода логина с забытого аккаунта
    forget_login_entry.grid(row=1, column=2)
    result_label = Label(forget_window, text="")  # строка с результатами проверки (изначально скрыта)
    result_label.grid(row=2, column=0, columnspan=3)
    check_log_button = Button(forget_window, text="Проверить")  # кнопка для проверки наличия логина в базе
    check_log_button.grid(row=3, column=0, columnspan=3)
    # запускаем функцию по проверке наличия введённого пользователем логина в базе данных
    check_log_button.bind('<Button-1>', check_login)  # по клику на кнопку
    forget_login_entry.bind('<Return>', check_login)  # по нажатию Enter


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
    cur.execute('''SELECT login, password, best_score FROM users''')  # считываем в курсор всех пользователей и пароли
    login = loginEntry.get()  # считываем введённый пользователем логин
    password = passEntry.get()  # считываем введённый пользователем пароль
    log = cur.fetchone()  # считываем одного из пользователей в БД
    while log is not None and log[0] != login:  # пока не найдётся совпадение или пока не закончатся пользователи
        log = cur.fetchone()  # считываем ещё одного пользователя из БД
    if log is None:  # если такой логин не найден
        messagebox.showwarning('Внимание!', 'Пользователь не найден!')  # выводим сообщение что логин не найден
    else:  # если такой логин найден, проверяется пароль
        if log[1] == password:
            intro(log[0], log[2])
        else:
            messagebox.showwarning('Внимание!', 'Пароль неверный!')
            authSuccess += 1
            if authSuccess == 3:  # после трёх неудачных попыток подобрать пароль возможность входа блокируется
                access_denied()


# функция, отвечающая за экран приветствия пользователя (статистика, начало новой игры)
def intro(usr_login, b_score):
    def easy_description(event):
        description_label.configure(
            text='Требуется угадать число от 1 до 10.\nПодсказок нет. Максимум баллов: 100.\nЗа каждую неверную '
                 'попытку снимается 10 баллов.')

    def easy_mode(u_login, b_sc):
        def check_digit(u_l, b_s):
            global soten
            global easy_digit
            global bestOf
            bestOf = b_s
            digit = int(a_entry.get())
            if digit == easy_digit:
                if soten > int(bestOf):
                    messagebox.showinfo('Поздравляю!', 'Ты победил со счетом '+str(soten)+' баллов!\n\nЭто новый рекорд!')
                    bestOf = soten
                    cur = users.cursor()  # курсор в базе данных users cur = cursor
                    sql = "UPDATE users SET best_score = ? WHERE login = ?"
                    cur.execute(sql, (soten, u_l))
                    users.commit()
                else:
                    messagebox.showinfo('Поздравляю!', 'Ты победил со счетом' + str(soten) + ' баллов!')
                game_window.destroy()
                diff_window.deiconify()
                easy_digit = random.randrange(10) + 1  # генерируем новое случайное число
                soten = 100  # очки за лёгкий уровень также обновляются
            else:
                soten -= 10
                q_caption.configure(text='Я загадал число от 1 до 10.\nНе угадал! Осталось '+str(soten)+' баллов!')
        diff_window.withdraw()
        game_window = Toplevel(window)  # создаём окно выбора сложности
        g_ws = game_window.winfo_screenwidth()  # считываем текущую ширину экрана
        g_hs = game_window.winfo_screenheight()  # считываем текущую высоту экрана
        game_window.geometry(
            '%dx%d+%d+%d' % (240, 140, (g_ws / 2) - 120, (g_hs / 2 - 70)))  # расположение по центру экрана
        game_window.resizable(0, 0)  # запрещаем изменять размер окна
        game_window.overrideredirect(1)  # отключаем рамку окна (нельзя переместить и закрыть)
        game_caption = Label(game_window, text="Числорд (easy)", font=('Arial Black', 10))  # заголовок главного окна
        game_caption.grid(row=0, column=0, columnspan=3)
        q_caption = Label(game_window, text="Я загадал число от 1 до 10.\nПопробуй угадай!")  # заголовок главного окна
        q_caption.grid(row=1, column=0, columnspan=3, pady=5)
        a_entry = Entry(game_window, width=39, bd=3)
        a_entry.grid(row=2, column=0, columnspan=3)
        answer_button = Button(game_window, text="Мне повезёт!", padx=5, pady=5, command=lambda: check_digit(u_login, b_sc))
        answer_button.grid(row=3, column=0, columnspan=3, pady=5)

    def normal_description(event):
        description_label.configure(
            text='Требуется угадать число от 1 до 100.\nЕсть подсказки "больше"- "меньше". Максимум баллов: 500.\nЗа '
                 'каждую неверную попытку снимается 50 баллов.')

    def hard_description(event):
        description_label.configure(
            text='Требуется угадать число от 1 до 1000.\nЕсть подсказки "больше"- "меньше". Максимум баллов: '
                 '1000.\nЗа каждую неверную попытку снимается 50 баллов.')

    def nightmare_description(event):
        description_label.configure(
            text='Требуется угадать число от 1 до 1000.\nПодсказок нет. Максимум баллов: 1000.\nЗа каждую неверную '
                 'попытку снимается 10 баллов.')

    def description_off(event):
        description_label.configure(text='Наведите указатель мыши на уровень сложности,\nчтобы прочитать его описание')

    def my_stat(stat_login):
        cur = users.cursor()  # курсор в базе данных users cur = cursor
        cur.execute(
            '''SELECT login, best_score FROM users''')  # считываем в курсор лучший результат данного пользователя
        log = cur.fetchone()  # считываем эту запись в кортеж
        while log[0] != stat_login:
            log = cur.fetchone()
        temp_str = 'Ваш лучший счёт: ' + str(log[1]) + '\n\nВскоре в этом разделе появится больше информации!'
        temp_str1 = 'Статистика игрока ' + log[0]
        messagebox.showinfo(temp_str1, temp_str)

    window.withdraw()  # скрываем окно авторизации
    diff_window = Toplevel(window)  # создаём окно выбора сложности
    d_ws = diff_window.winfo_screenwidth()  # считываем текущую ширину экрана
    d_hs = diff_window.winfo_screenheight()  # считываем текущую высоту экрана
    diff_window.geometry(
        '%dx%d+%d+%d' % (356, 230, (d_ws / 2) - 175, (d_hs / 2 - 115)))  # расположение по центру экрана
    diff_window.resizable(0, 0)  # запрещаем изменять размер окна
    diff_window.overrideredirect(1)  # отключаем рамку окна (нельзя переместить и закрыть)
    diff_caption = Label(diff_window, text="Главное меню", font=('Arial Black', 10))  # заголовок главного окна
    diff_caption.grid(row=0, column=0, columnspan=4)
    # надпись, приветствующая игрока
    welcome_label = Label(diff_window, text="Привет, " + usr_login + "! Давай поиграем?")
    welcome_label.grid(row=1, column=0, columnspan=4, pady=10)
    # кнопка для просмотра личной статистики
    my_stat_button = Button(diff_window, text="Моя статистика", padx=10, pady=5, command=lambda: my_stat(usr_login))
    my_stat_button.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=N + W + S + E)
    # кнопка для просмотра таблицы лидеров
    total_ranks_button = Button(diff_window, text="Таблица рекордов", padx=10, pady=5,
                                command=lambda: top_scores(usr_login))
    total_ranks_button.grid(row=2, column=2, columnspan=2, padx=20, pady=5, sticky=N + W + S + E)
    # надпись, которая предлагает выбрать уровень сложности
    choose_diff_label = Label(diff_window, text="Выбери уровень сложности:")
    choose_diff_label.grid(row=3, column=0, columnspan=4)
    # кнопка легкого уровня сложности

    easy_button = Button(diff_window, text="Лёгкий", padx=5, pady=5, command=lambda: easy_mode(usr_login, b_score))
    easy_button.grid(row=4, column=0, padx=5, pady=5, sticky=N + W + S + E)
    # кнопка нормального уровня сложности
    normal_button = Button(diff_window, text="Нормальный", padx=5, pady=5)
    normal_button.grid(row=4, column=1, padx=5, pady=5, sticky=N + W + S + E)
    # кнопка тяжелого уровня сложности
    hard_button = Button(diff_window, text="Тяжёлый", padx=5, pady=5)
    hard_button.grid(row=4, column=2, padx=5, pady=5, sticky=N + W + S + E)
    # кнопка кошмарного уровня сложности
    nightmare_button = Button(diff_window, text="Кошмарный", padx=5, pady=5)
    nightmare_button.grid(row=4, column=3, padx=5, pady=5, sticky=N + W + S + E)
    # пояснение уровня сложности
    description_label = Label(diff_window,
                              text="Наведите указатель мыши на уровень сложности,\nчтобы прочитать его описание")
    description_label.grid(row=5, column=0, columnspan=4)
    # описание событий с описаниями уровня сложности
    easy_button.bind('<Enter>', easy_description)
    easy_button.bind('<Leave>', description_off)
    normal_button.bind('<Enter>', normal_description)
    normal_button.bind('<Leave>', description_off)
    hard_button.bind('<Enter>', hard_description)
    hard_button.bind('<Leave>', description_off)
    nightmare_button.bind('<Enter>', nightmare_description)
    nightmare_button.bind('<Leave>', description_off)


# функция вывода 10-ти лучших игроков (или всех игроков, если игроков меньше 10)
def top_scores(my_login):
    top_window = Toplevel(window)  # создаём окно выбора сложности
    t_ws = top_window.winfo_screenwidth()  # считываем текущую ширину экрана
    t_hs = top_window.winfo_screenheight()  # считываем текущую высоту экрана
    top_window.geometry('%dx%d+%d+%d' % (300, 350, (t_ws / 2) + 180, (t_hs / 2 - 190)))  # расположение по центру экрана
    top_window.resizable(0, 0)  # запрещаем изменять размер окна
    top_window.title("Таблица рекордов")
    table_header_1 = Label(top_window, text="Игрок", font=('Arial Black', 10))  # заголовок таблицы "Игрок"
    table_header_1.grid(row=0, column=0, padx=40, pady=5, sticky=N + W + S + E)
    table_header_1 = Label(top_window, text="Лучший результат",
                           font=('Arial Black', 10))  # заголовок таблицы "Лучший результат"
    table_header_1.grid(row=0, column=1, padx=5, pady=5, sticky=N + W + S + E)
    # получение данных об игроках и их рекордах
    cur = users.cursor()  # курсор в базе данных users cur = cursor
    cur.execute('''SELECT login, best_score FROM users''')  # считываем в курсор лучший результат данного пользователя
    log = cur.fetchone()  # считываем эту запись в кортеж
    scores = []
    while log is not None:
        scores.append(log)
        log = cur.fetchone()
    scores.sort(reverse=True, key=lambda x: x[1])  # сортировка игроков по убыванию лучшего результата
    # вывод таблицы лидеров на экран
    for i in range(min(10, len(scores))):
        if my_login == scores[i][0]:  # выделяем результаты пользователя
            player_name = Label(top_window, text=scores[i][0], fg="#44F")
            player_name.grid(row=1 + i, column=0, padx=5, pady=5, sticky=N + W + S + E)
            player_score = Label(top_window, text=scores[i][1], fg="#44F")
            player_score.grid(row=i + 1, column=1, padx=5, pady=5, sticky=N + W + S + E)
        else:
            player_name = Label(top_window, text=scores[i][0])
            player_name.grid(row=1 + i, column=0, padx=5, pady=5, sticky=N + W + S + E)
            player_score = Label(top_window, text=scores[i][1])
            player_score.grid(row=i + 1, column=1, padx=5, pady=5, sticky=N + W + S + E)


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
                    cursor='hand2')  # Надпись "Забыли пароль?" неактивна, появляется только при неудачной попытке входа
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
bestOf = 0  # глобальная переменная для лучших счетов
easy_digit = random.randrange(10) + 1  # глобальная переменная для легкого уровня
soten = 100  # глобальная переменная для количества баллов
loginEntry.focus()  # устанавливаем фокус на поле ввода логина
authSuccess = 0  # инициализируем счетчик попыток входа
label4.bind('<Button-1>', enter)  # авторизация по клику на "короле"
loginEntry.bind('<Return>', enter)  # авторизация по нажатию клавиши Enter из поля логина
passEntry.bind('<Return>', enter)  # авторизация по нажатию клавиши Enter из поля пароля
registrationLabel.bind('<Button-1>', reg)  # регистрация по нажатию на соответствующую ссылку
forgetLabel.bind('<Button-1>', forget)  # запуск восстановления пароля по нажатию на надпись "Забыли пароль?"

# запускаем цикл дочернего окна
window.mainloop()
