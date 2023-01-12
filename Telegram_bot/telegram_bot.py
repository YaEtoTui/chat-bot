import telebot
from telebot import types

bot = telebot.TeleBot('5595730514:AAECAp96E6C4coliWcMRmy6qx5BhSMokNH4')
states = {}

@bot.message_handler(commands=['go', 'start'])
def startGame(message):
    user = message.chat.id
    states[user] = 0
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(text="Начать путешествие", callback_data="0"))
    user_name = {message.from_user.first_name}

    bot.send_photo(user, "https://i.imgur.com/pNcGNMR.jpg")

    bot.send_message(message.chat.id, f'Приветствую вас {message.from_user.first_name}, это текстовая игра(квест), '
                                     'все действия выполняются с помощью кнопок под окном чата, '
                                     'а результаты приходят в виде сообщений и картинок. Исследуйте мир вашего компьютера, '
                                     'узнавайте что-то новое о вирусах и программах, способных навредить вашему устройству, получайте подсказки,'
                                     ' уничтожайте врагов(вирусы) и сражайтесь с основными врагами-боссами (главными вирусами).'
                     , reply_markup=kb)
    process_state(user, states[user])

@bot.callback_query_handler(func=lambda call: True)
def user_answer(call):
    user = call.message.chat.id
    process_answer(user, call.data)

def process_state(user, state):
    kb = types.InlineKeyboardMarkup()
    if state == 1:
        kb.add(types.InlineKeyboardButton(text="Перезапущу компьютер, и всё будет хорошо", callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Ой, а что же теперь делать? ", callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Да не может такого быть, приколы какие-то :)", callback_data="3"))

        bot.send_photo(user, "https://i.imgur.com/gBmow4i.jpeg")

        bot.send_message(user, "Вернувшись домой после тяжелого дня, вы замечаете, что на вашу электронную "
                               "почту пришло письмо с незнакомого адреса. Заинтересованные, вы открываете его.")
        bot.send_message(user, "В тот же миг на ваш компьютер загружается вредоносная программа, которая находилась "
                               "в письме и только и ждала того, чтобы вы его открыли. ", reply_markup=kb)

    if state == 2:
        kb.add(types.InlineKeyboardButton(text="Нажать «Enter» и погрузиться в мир устройства", callback_data="1"))

        bot.send_photo(user, "https://i.imgur.com/rZAfigl.png")

        bot.send_message(user, "Вы не сразу заметили сообщение в командной строке, но сейчас обратили внимание. "
                               "Там следующий текст: «Привет, пользователь! У нас плохие времена, компьютеру и так "
                               "требовалась "
                               "чистка, а сейчас его захватило большое количество вирусов. Мы очень нуждаемся в тебе, "
                               "поэтому я, твой cmd, обращаюсь к тебе за помощью, и если ты готов отправиться в недры "
                               "своего компьютера и разобраться со всеми проблемами, то нажми Enter»", reply_markup=kb)

    if state == 3:
        kb.add(types.InlineKeyboardButton(text="Начать исследование устройства", callback_data="1"))
        bot.send_message(user, f"Вы сами не заметили как, но уже через пару секунд оказались внутри вашего компьютера. "
                               f"Оглядевшись вы поняли, что вокруг запутанный лабиринт из различных папок, плат и "
                               f"сети проводов. Для начала следует изучить окрестности получше", reply_markup=kb)

    if state == 4:
        kb.add(types.InlineKeyboardButton(text="Опознать незнакомца",
                                          callback_data="1"))
        bot.send_message(user, "После 10 минут блуждания вы обнаружили достаточно широкую тропинку, "
                               "по которой и приняли решение идти. Но пройдя всего пару шагов и завернув за угол, "
                               "вы в первый раз в этом мире встречаете живое существо. К счастью, оно пока вас не видит",
                         reply_markup=kb)

    if state == 5:
        bot.send_photo(user, "https://i.imgur.com/SsAjRKv.png")

        kb.add(types.InlineKeyboardButton(text="Напасть ",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Попытаться незаметно ускользнуть",
                                          callback_data="1"))
        bot.send_message(user, "Вы явно не самый везучий, ведь путь вам преградил никто иной, как деструктивный "
                               "троянский конь. В школе на занятиях по информатике вам рассказывали о самых "
                               "распространённых компьютерных вирусах, поэтому ты легко опознал в существе врага",
                         reply_markup=kb)

    if state == 6:
        kb.add(types.InlineKeyboardButton(text="Выполнить полную проверку системы и удалить вредоносное ПО",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Удалить корневую папку где находился вирус, подождать "
                                               "некоторое время, вдруг вирус сам испариться",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Остановить программу через диспетчер задач",
                                          callback_data="3"))

        bot.send_message(user, "На вид кажущаяся безобидной программой, Деструктивный троянский конь несет в "
                               "себе немало вреда. Чтобы попасть в ваше устройство он использовал маскировку, "
                               "но с недавнего времени он начал свою беспощадную атаку.",
                         reply_markup=kb)

    if state == 7:
        kb.add(types.InlineKeyboardButton(text="Снова включить компьютер ",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Закончить игру",
                                          callback_data="2"))

        bot.send_message(user, "Вы оказались снова у себя в комнате, а компьютер перед вами выключен.", reply_markup=kb)

    if state == 7.1:
        bot.send_photo(user, "https://i.imgur.com/5j7tOob.png")

        kb.add(types.InlineKeyboardButton(text="Буду использую двухфакторную аутентификацию",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Дам доступ к личной информации другим ",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Буду использовать спам-фильтр",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Везде буду использовать один и тот же пароль",
                                          callback_data="4"))

        bot.send_message(user, "Как только вы нажали кнопку включения, компьютер сразу затянул вас внутрь. "
                               "Но ввести пароль для входа вам мешает ещё один вирус, спуфер. "
                               "Чтобы обратно вернуться в цифровой мир вам следует избавиться от него. Что предпримите?",
                         reply_markup=kb)

    if state == 8:
        kb.add(types.InlineKeyboardButton(text="Продолжить путь",
                                          callback_data="2"))
        bot.send_message(user, "Поздравляем вы уничтожили своего первого противника, но впереди еще долгое путешествие, "
                               "наберитесь сил и отправляйтесь дальше.",
                         reply_markup=kb)

    if state == 9:
        kb.add(types.InlineKeyboardButton(text="Oпознать врага",
                                          callback_data="1"))

        bot.send_message(user, "Вы не успели отдышаться, как на вашем пути появилась новая неизвестная программа.",
                         reply_markup=kb)

    if state == 10:
        kb.add(types.InlineKeyboardButton(text="Попытаться проникнуть внутрь коня изнутри его уничтожить.",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Отключить питание устройства и запустить его снова.",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Установить утилиту для удаления троянских коней.",
                                          callback_data="3"))

        bot.send_photo(user, "https://i.imgur.com/p3WoJ2f.png")

        bot.send_message(user, "Программа кажется идентичной предыдущей, но стоит вам приглядеться, как вы понимаете, "
                               "что этот соперник гораздо больше, из это неудивительно, ведь перед вами Главный "
                               "троянский вирус.")
        bot.send_message(user, "Он наносит первый удар настолько неожиданно, что вы не успели среагировать. К счастью "
                               "нанести вам большой урон у врага не получилось, и уже вы предпринимаете "
                               "попытку атаковать.")
        bot.send_message(user, "Так как вы уже встречались с трояном вы решили попробовать сделать то же самое, "
                               "выполнить полную проверку системы и удалить вредоносное ПО, но босс не так прост, "
                               "чтобы убрать его с устройства нужно больше усилий.", reply_markup=kb)

    if state == 10.1:
        bot.send_photo(user, "https://i.imgur.com/5j7tOob.png")

        kb.add(types.InlineKeyboardButton(text="Буду использую двухфакторную аутентификацию",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Дам доступ к личной информации другим ",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Буду использовать спам-фильтр",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Везде буду использовать один и тот же пароль",
                                          callback_data="4"))

        bot.send_message(user, "Компьютер вновь выключился, как только вы нажали кнопку включения, "
                               "компьютер сразу затянул вас внутрь. "
                               "Но ввести пароль для входа вам мешает ещё один вирус, спуфер. "
                               "Чтобы обратно вернуться в цифровой мир вам следует избавиться от него. Что предпримите?",
                         reply_markup=kb)

    if state == 11:
        kb.add(types.InlineKeyboardButton(text="Запуск антивируса для удаления остатков коня",
                                          callback_data="1"))

        bot.send_message(user, "Ого! Ваши действия нанесли сильный вред противнику, троян почти уничтожен, "
                               "но остался последний удар, чтобы его добить.", reply_markup=kb)

    if state == 12:
        kb.add(types.InlineKeyboardButton(text="Oстановиться и подождать ",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Зачем нам ещё один бой? Попробовать убежать",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Этот мир не очень дружелюбный, не помешает подготовиться к битве",
                                          callback_data="3"))

        bot.send_message(user, "Немного передохнув, вы двинулись дальше, но пройдя совсем немного заметили, "
                               "как на встречу вам бежит ещё один совершенно незнакомый вам человечек",
                         reply_markup=kb)

    if state == 13:
        bot.send_photo(user, "https://i.imgur.com/7nrfxwx.png")

        kb.add(types.InlineKeyboardButton(text="«А что здесь произошло, почему в моём компьютере одновременно "
                                               "оказалось столько вредоносных программ?» ",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="«И как нам справиться со всеми врагами?»",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="«Рад знакомству, какие будут предложения, что делать дальше?»",
                                          callback_data="3"))

        bot.send_message(user, "«Человек, я очень рад, что ты принял моё приглашение и "
                               "пришёл помочь освободить наш мир от непрошенных гостей. "
                               "Судя по твоему виду, ты уже встретил кого-то из наших недоброжелателей. "
                               "Хорошо, что ты не пострадал! Ой, я совсем забыл представиться, меня зовут "
                               "Cmd, надеюсь, мы быстро подружимся и вместе одолеем все вирусы.»",
                         reply_markup=kb)

    if state == 14:
        kb.add(types.InlineKeyboardButton(text="Что для этого нужно?",
                                          callback_data="1"))

        bot.send_message(user,"«Ты сидишь но многих незащищённых сайтах, скачиваешь с них различные файлы, а вместе с "
                              "ними и вирусы разных видов. С каждым днём они становятся всё хитрее и изворотливее, "
                              "иногда могут долгое время оставаться незаметными, усыпляя бдительность систем ПО и "
                              "поджидая удобного случая напасть. Даже современные антивирусы не всегда успевают за их "
                              "эволюцией. Таким образом на твоём компьютере появлялось всё больше и больше вредоносных "
                              "программ, что привело к тому, что сейчас необходимо провести экстренную зачистку.»",
                         reply_markup=kb)

    if state == 15:
        kb.add(types.InlineKeyboardButton(text="И где находится эта папка?",
                                          callback_data="1"))

        bot.send_message(user,
                         "В первую очередь тебе надо пробраться в корневую папку и найти там архив с фалами паролей. "
                         "Их нужно изменить, чтобы вирусы больше не могли иметь доступ к любым фалам и операциям. "
                         "Сейчас корневая папка находится под контролем зомби, поэтому будь готов к сражению. Также "
                         "тебе стоит знать, что в нашем мире вирусы разделились на боссов и их помощников. Так что для "
                         "того, чтобы разобраться со всеми вредителями, надо уничтожить их главаря.»", reply_markup=kb)

    if state == 16:
        kb.add(types.InlineKeyboardButton(text="Опознать программу",
                                          callback_data="1"))

        bot.send_message(user,
                         "«Чтобы добраться до неё тебе следует идти по этой дороге через несколько других папок, если "
                         "будешь быстро идти, то потребуется совсем немного времени, но будь осторожен, нельзя "
                         "предсказать, что тебя ждёт на этом пути. У меня самого ещё есть дела, поэтому не могу пойти с"
                         " тобой, но я верю, что ты со всем справишься! Встретимся позже.»")
        bot.send_message(user,
                         "После этих слов ваш новый приятель сделал молниеносный рывок и скрылся за ближайшим "
                         "поворотом.")
        bot.send_message(user,
                         "Вы же постояли некоторое время на месте, обдумывая всё только что услышанное, и только после "
                         "пары минут активной мозговой деятельности пришли к выводу, что нужно попытаться освободить "
                         "свой компьютер от этих нежелательных гостей, и двинулись в указанном направлении.")
        bot.send_message(user,
                         "Поначалу всё было спокойно, неподвижную тишину нарушал только звук ваших шагов. "
                         "Направление вашего движения подсказывали указатели, расставленные на какой развилке. "
                         "Вы уже даже успели подумать, что всё не так страшно, как показалось изначально, как вдруг "
                         "прямо перед вами материализовалась какая-то программа.", reply_markup=kb)

    if state == 17:
        bot.send_photo(user, "https://i.imgur.com/Ms8E81e.png")

        kb.add(types.InlineKeyboardButton(text="Удалить все файлы руткита которые сразу заметны",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Позволить антивирусу разобраться",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Провести полный анализ системы и очистить все "
                                               "глубокие источники руткита",
                                          callback_data="3"))
        kb.add(types.InlineKeyboardButton(text="Переустановить операционную систему",
                                          callback_data="4"))
        kb.add(types.InlineKeyboardButton(text="сбросить настройки системы",
                                          callback_data="5"))

        bot.send_message(user,
                         "Похоже, что руткит серьёзно настроен устранить вас, поэтому избежать сражения не "
                         "представляется возможным. Стоит попробовать ответить обидчику.",
                         reply_markup=kb)

    if state == 17.1:
        bot.send_photo(user, "https://i.imgur.com/5j7tOob.png")

        kb.add(types.InlineKeyboardButton(text="Буду использую двухфакторную аутентификацию",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Дам доступ к личной информации другим ",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Буду использовать спам-фильтр",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Везде буду использовать один и тот же пароль",
                                          callback_data="4"))

        bot.send_message(user, "Компьютер вновь выключился, как только вы нажали кнопку включения, "
                               "компьютер сразу затянул вас внутрь. "
                               "Но ввести пароль для входа вам мешает ещё один вирус, спуфер. "
                               "Чтобы обратно вернуться в цифровой мир вам следует избавиться от него. Что предпримите?",
                         reply_markup=kb)

    if state == 18:
        kb.add(types.InlineKeyboardButton(text="Пройду мимо, незачем отвлекаться от намеченной цели, "
                                               "сейчас есть дела поважнее",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Нельзя позволять вирусам так безнаказанно "
                                               "воровать информацию у меня под носом! ",
                                          callback_data="2"))

        bot.send_message(user,
                         "Дальнейший ваш путь прошёл без происшествий. Вы уже видите указатель на корневую папку, "
                         "но тут ваш взгляд привлек к себе небольшой странный комок, состоящий из проводов.")
        bot.send_message(user,
                         "Подойдя чуть ближе, вы смогли разглядеть, что узел проводов подключён к самому компьютеру и "
                         "перекачивает ваши данные. Скорее всего, это клавиатурный шпион. Как поступите?",
                         reply_markup=kb)

    if state == 18.1:
        bot.send_photo(user, "https://i.imgur.com/PKJAN6a.png")

        kb.add(types.InlineKeyboardButton(text="Установлю антишпионский продукт",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Буду всегда вводить пароли вручную",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Буду сохранять пароли и вводить их на "
                                               "любых сайтах, даже не очень защищённых",
                                          callback_data="3"))
        kb.add(types.InlineKeyboardButton(text="Обновлю систему и программные продукты и "
                                               "в будущем буду делать так регулярно ",
                                          callback_data="4"))

        bot.send_message(user,
                         "Что предпримите?",
                         reply_markup=kb)

    if state == 19:
        kb.add(types.InlineKeyboardButton(text="Бой",
                                          callback_data="1"))

        bot.send_message(user,
                         "Наткнувшись на иконку браузера вы заметили возле него "
                         "Рекламную программу считывающую полную информацию о вас",
                         reply_markup=kb)

    if state == 20:
        bot.send_photo(user, "https://i.imgur.com/f5fHhOi.png")

        kb.add(types.InlineKeyboardButton(text="Удалить браузер",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Использовать панель управления для "
                                               "удаления вредоносного ПО",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Сбросить все настройки браузера",
                                          callback_data="3"))
        kb.add(types.InlineKeyboardButton(text="Обнулить операционную систему",
                                          callback_data="4"))

        bot.send_message(user, "Недолго думая вы решили настоятельно уничтожить программу",
                         reply_markup=kb)

    if state == 20.1:
        kb.add(types.InlineKeyboardButton(text="Отомстить самозванцу!",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Блин блинский тяжко... Дайте подсказочку, плиииз.",
                                          callback_data="2"))
        bot.send_message(user, "Вы потерпели поражение. Вас убили. Измотали. "
                               "Дали по морде. Сломали рёбра. Пнули в живот",
                         reply_markup=kb)

    if state == 21:
        kb.add(types.InlineKeyboardButton(text="Опознать врага",
                                          callback_data="1"))
        bot.send_message(user, "Рекламная программа была удалена, вы решили следовать дальше")
        bot.send_message(user, "Ваши поиски прерывает новый враг", reply_markup=kb)

    if state == 22:
        kb.add(types.InlineKeyboardButton(text="Бой",
                                          callback_data="1"))
        bot.send_message(user, "Перед вами появляется программа Кликер который занимается "
                               "рассылкой спама, содержащий потенциально опасные приложения",
                         reply_markup=kb)

    if state == 23:
        bot.send_photo(user, "https://i.imgur.com/SNQzRZI.png")

        kb.add(types.InlineKeyboardButton(text="Удалить весь спам собственноручно",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Установить утилиту против кликера.",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Написать товарищам что ваши сообщения спам",
                                          callback_data="3"))

        bot.send_message(user, "Кликер не особо рад вашему присутствию.",
                         reply_markup=kb)

    if state == 23.1:
        kb.add(types.InlineKeyboardButton(text="Вновь в бой, щас этот вирусняк у меня получит!!!",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Это треш товарищи, мне нужна помощь. Чет вообще не могу"
                                               "избавиться от этого кликера...",
                                          callback_data="2"))

        bot.send_message(user, "Вы пытались, но ничего не произошло. Капец че делать то?",
                         reply_markup=kb)

    if state == 24:
        kb.add(types.InlineKeyboardButton(text="Сброс настроек и удаление вредоностного ПО",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Удалить вирусы по одному.",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Установить новый браузер.",
                                          callback_data="3"))

        bot.send_message(user, "После сражений перед вами появляются все рекламные вирусы. "
                               "Вы решили использовать полученные знания, но ваши попытки были тщетны, "
                               "этот босс оказался не так прост.",
                         reply_markup=kb)

    if state == 24.1:
        kb.add(types.InlineKeyboardButton(text="Реклама не нужна! В БОООООЙ!",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Чет непонятки какие то... Помогите?",
                                          callback_data="2"))

        bot.send_message(user, "Группой на одного? Результат ожидаем... У вас ничего не вышло, что же делать?",
                         reply_markup=kb)

    if state == 25:
        bot.send_photo(user, "https://i.imgur.com/XCFGqbl.png")

        kb.add(types.InlineKeyboardButton(text="Удалить браузер",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Удалить в браузере все ненужных и "
                                               "подозрительных инструментов и расширений",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Поменять основной браузер на другой",
                                          callback_data="3"))
        kb.add(types.InlineKeyboardButton(text="Сбросить настройки поисковой системы",
                                          callback_data="4"))

        bot.send_message(user, "До вашей цели осталось всего лишь повернуть за угол. И вот вы уже воодушевлены и "
                               "готовы к встрече с новыми противниками, как вдруг что-то хватает вас за ногу и резко "
                               "тянет назад. Вы падаете, и нечто утягивает вас в расщелину, не замеченную вами ранее.")

        bot.send_message(user, "Как оказалось, вы слишком рано переключились на мысли о своих дальнейших действиях и не"
                               " обратили внимание на осторожно ползущие за вами щупальца хиджакера. ")

        bot.send_message(user, "Ваша легкомысленность приводит к тому, что, находясь в нескольких шагах от заветной "
                               "папки, вы оказались затянуты очередным вирусом в недра компьютера, внешне "
                               " чащу леса. Оглядев своё новое местоположение, чуть поодаль вы увидели иконку браузера,"
                               " из чего вами был сделан вывод, что вирус пришёл из Интернета.")

        bot.send_message(user, "Сам же монстр наконец предстал перед вами во всей красе, и вы снова оказались перед "
                               "непростым выбором: каким же образом вступить с противником в бой",
                         reply_markup=kb)

    if state == 25.1:
        kb.add(types.InlineKeyboardButton(text="Я бравый малый, сейчас устрою взбучку!!!",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Эхх... подсказочку бы...",
                                          callback_data="2"))

        bot.send_message(user, "После проигрыша от Хиджакера вы лежите измотанный на полу, как поступите?",
                         reply_markup=kb)

    if state == 26:
        kb.add(types.InlineKeyboardButton(text="Бой",
                                          callback_data="1"))

        bot.send_message(user, "Заинтересовавшись замеченной ранее иконкой, вы подошли туда. Конечно же, с вашей "
                               "сегодняшней удачей около браузера вы заметили Рекламную программу считывающую "
                               "полную информацию о вас, не спросив у вас разрешения. Так не годится!",
                         reply_markup=kb)

    if state == 27:
        kb.add(types.InlineKeyboardButton(text="Удалить браузер",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Использовать панель управления для удаления вредоносного ПО",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Сбросить все настройки браузера, обнулить операционную систему",
                                          callback_data="3"))

        bot.send_message(user, "Недолго думая, вы решили настоятельно уничтожить программу",
                             reply_markup=kb)

    if state == 27.1:
        kb.add(types.InlineKeyboardButton(text="Нападай!!!",
                                        callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Подсказка бы не помешала...",
                                        callback_data="2"))

        bot.send_message(user, "Ещё одна рекламная программа??? Не повезло тебе друг, будешь дальше биться? "
                               "Может тебе помочь?",
                         reply_markup=kb)

    if state == 28:
        kb.add(types.InlineKeyboardButton(text="Изменить расширение файла",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Отправить файл проверенному знакомому для проверки",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Считать файл в другом приложении для чтения",
                                          callback_data="3"))
        kb.add(types.InlineKeyboardButton(text="Проверить файл на наличие вируса",
                                          callback_data="4"))

        bot.send_message(user, "Оказывается, что в компьютерах путаются и теряются не только бабушки, так как вы "
                                "сами уже битый час плутаете в лабиринте различных проводов, матриц и непонятных "
                                "деталей и складывается ощущение, что бродите вы по кругу.")
        bot.send_message(user, "И вот, когда вы в очередной раз заметили знакомый узел проводов, прямо из воздуха "
                                "появилось всплывающее окно с сообщением от вашего друга:")
        bot.send_message(user, "«Привет, вышла новая игра, и у меня есть доступ к бесплатной версии. Скачивай "
                                "быстрее, иначе этот файл быстро почистят. Надо просто открыть файл, и загрузка "
                                "пойдёт сама. Я вот уже несколько часов играю, это бомба!»")
        bot.send_message(user, "К сообщению был прикреплён файл, а так как вы никогда не отказывались от халявных "
                                "игр, то ваш первый порыв был просто запустить файл. ")

        bot.send_message(user, "Но уже в следующую секунду вы остановили себя и решили немного подумать. За "
                                   "последние пару часов вы столкнулись с таким количеством вредоносных программ, "
                                   "что подумали о том, что сразу же открывать незнакомый файл не стоит, а лучше",
                             reply_markup=kb)

    if state == 28.1:
        kb.add(types.InlineKeyboardButton(text="Вот блин, щас я этому приколисту дам!",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="А в чем прикол то? Помогите плиз...",
                                          callback_data="2"))

        bot.send_message(user, "Шутканули так шутканули, поиграл в игрушки так сказать. Че делать будем то?",
                         reply_markup=kb)

    if state == 29:
        bot.send_photo(user, "https://i.imgur.com/PXIcIvk.png")
        kb.add(types.InlineKeyboardButton(text="Зайду на сайты, где требуется ввод логина и пароля",
                                          callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Уберу удалённый доступ из процессов устройства",
                                          callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Запрещу подключения удалённого помощника к этому устройству",
                                          callback_data="3"))

        bot.send_message(user, "Похоже, что мы всё-таки вышли на правильный путь, и буквально через 10 минут "
                                "вы уже стоите у входа в корневую папку."
                                ""
                                "Только зайдя внутрь, вы сразу встречаете двух зомби. Судя по всему, это "
                                "программы удалённого администрирования, и настроены они явно недружелюбно."
                                ""
                                "Вы, может, и хотели разойтись мирно, но вирусы ваше желание не разделили, "
                                "так что возникает необходимость атаковать. Что предпримите?",
                         reply_markup=kb)

    if state == 30:
        bot.send_photo(user, "https://i.imgur.com/eML2gRt.png")
        kb.add(types.InlineKeyboardButton(text="Полная переустановка системы",
                                                callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Полное сканирование устройства с "
                                                "помощью антивируса и удаления временных файлов ",
                                                callback_data="2"))
        kb.add(types.InlineKeyboardButton(text="Считывание информации об утечке личных данных",
                                                callback_data="3"))

        bot.send_message(user, "Вы уже успели подумать, что всё закончено и вы справились со всеми трудностями "
                                "и преодолели все препятствия, как вдруг, раздался громкий нечеловеческий рёв.")
        bot.send_message(user, "Разворачиваетесь на звук и только сейчас замечаете большое чудище, чем-то "
                                "напоминающее двух предыдущих. Но размерами он превышал их вместе взятых.")
        bot.send_message(user, "Вы вспомнили о том, что cmd предупреждал вас о наличии боссов, и решили, "
                                "что это именно он. ")
        bot.send_message(user, "Сейчас вы понимаете, что до победы остался один шаг, и перед вами встаёт "
                                "последний выбор, который повлияет на то, избавитесь ли вы окончательно от всех "
                                "вредоносных программ или нет.")
        bot.send_message(user, "Как будете бороться с врагом?",
                                 reply_markup=kb)

    if state == 30.1:
        kb.add(types.InlineKeyboardButton(text="Попытка не пытка, сейчас я ему точно дам!",
                                                callback_data="1"))
        kb.add(types.InlineKeyboardButton(text="Что сказал? Не побеждал он меня, я "
                                               "просто за подсказочкой отступил",
                                                callback_data="2"))

        bot.send_message(user, "Тебя победил мертвец, он и так уже мертвый, как ты смог проиграть?",
                         reply_markup=kb)

    if state == 31:
        bot.send_photo(user, "https://i.imgur.com/7nrfxwx.png")
        kb.add(types.InlineKeyboardButton(text="Выбраться из устройства",
                                                  callback_data="1"))
        bot.send_message(user, "После вашей победы открывается командная строка:")
        bot.send_message(user, "«Ты большой молодец! Тебе удалось уничтожить главного врага. Доступ к твоим "
                                "данным снова восстановлен, вирусы и их помощники исчезли. Ты можешь вернуться в"
                                " свой мир, чтобы и дальше жить своей жизнью, но помни про ошибки, которые ты "
                                "сделал. Думай, прежде чем устанавливать и скачивать неизвестные файлы на своё "
                                "устройство. Полагаю нам пора прощаться.»")
        bot.send_message(user, "После такой трогательной речи от вашего друга можно было проронить слезу, но"
                                " вы сдерживаетесь и решаетесь на последний шаг в своем путешествии.",
                                reply_markup=kb)

    if state == 32:
        bot.send_photo(user, "https://i.imgur.com/K12otzW.jpg")

        bot.send_message(user, "Очнувшись в своей комнате, вы понимаете, что ваше приключение "
                                "окончено и пора возвращаться к повседневной жизни, снова…")
        bot.send_message(user, "Поздравляем, вы смогли справиться со всеми трудностями, уничтожили все вирусы,"
                                " теперь на вашем устройстве воцарятся мир и процветание, а уровень ваших"
                                " знаний значительно вырос!")
        bot.send_message(user, "Вы способны избавиться от вирусов самостоятельно. Главное, не стоит забывать,"
                                " что самый простой выбор не всегда самый правильный. Также не бойтесь прибегать"
                                " к уже  существующим устройствам для удаления вредоносных программ и защиты"
                                " вашего компьютера, ведь не всегда у вас будет возможность самим залезть в"
                                " устройство и победить всех врагов.")
        bot.send_message(user, "Все истории подходят к концу, и, к сожалению, эта не исключение, но, если у вас"
                                " будут вопросы, вы всегда можете обратиться к другим источникам для получения"
                                " новых знаний.")
        bot.send_message(user, "На этом моменте пора прощаться.")
        bot.send_message(user, "Над квестом работала команда codEater.")

def process_answer(user, answer):
    kb = types.InlineKeyboardMarkup()
    if states[user] == 0:
        if answer == "0":
            states[user] = 1

    elif states[user] == 1:

        if answer == "1":
            bot.send_message(user, "После перезапуска ничего не изменилось, и"
                                   " вирусы всё так же находятся в компьютере")
            states[user] = 2
        if answer == "3":
            bot.send_message(user, "К сожалению это не чья-то глупая шутка, и "
                                   "вирусы действительно заполонили ваш компьютер")
            states[user] = 2

    elif states[user] == 2:
        states[user] = 3

    elif states[user] == 3:
            states[user] = 4

    elif states[user] == 4:
            states[user] = 5

    elif states[user] == 5:
        if answer == "1":
            states[user] = 6
        else:
            bot.send_message(user, "Упс, Но кажется, вам не удалось остаться "
                                   "незамеченным, так что убежать уже не представляется возможным")
            states[user] = 6

    elif states[user] == 6:
        if answer == "1":
            states[user] = 8
        if answer == "2":
            bot.send_message(user, "Похоже, что удаление папки только разозлило "
                                   "деструктивного троянского коня. "
                                   "Разъярённый, он бросился на вас.")
            states[user] = 7
        if answer == "3":
            bot.send_message(user, "Вы остановили программу, но не самого вируса.")
            states[user] = 7

    elif states[user] == 7:
        if answer == "1":
            states[user] = 7.1
        else:
            bot.send_message(user, "Спасибо за игру, что бы начать заново напишите /go или /start")

    elif states[user] == 7.1:
        if answer == "1":
            bot.send_message(user, "Прекрасно! Вы справились с шпионом на вашем "
                                   "компьютере и можете продолжить свой путь.")
            states[user] = 6
        else:
            bot.send_message(user, "Похоже, что ваши действия не "
                                   "возымели действия, стоит попробовать сделать что-то другое.")
            bot.send_message(user, "Подсказка: Никогда не следует давать свою личную информацию, "
                                   "использовать один пароль, отвечать на звонки незнакомым людям ")
            states[user] = 7.1

    elif states[user] == 8:
        if answer == "2":
            states[user] = 9

    elif states[user] == 9:
        if answer == "1":
            states[user] = 10

    elif states[user] == 10:
        if answer == "1":
            bot.send_message(user, "Вы оказались очень ловким и смогли проникнуть внутрь, "
                                   "но там вам не удалось нанести врагу значительный урон, "
                                   "несмотря на все ваши удары")
            states[user] = 10
        if answer == "2":
            bot.send_message(user, "Похоже это было бесполезным действием, так как после того как "
                                   "вы перезапустили компьютер, монстр остался на том же месте")
            states[user] = 10
        if answer == "3":
            states[user] = 11

    elif states[user] == 10.1:
        if answer == "1":
            bot.send_message(user, "Прекрасно! Вы справились с шпионом на вашем "
                                   "компьютере и можете продолжить свой путь.")
            states[user] = 10
        else:
            bot.send_message(user, "Похоже, что ваши действия не "
                                   "возымели действия, стоит попробовать сделать что-то другое.")
            bot.send_message(user, "Подсказка: Никогда не следует давать свою личную информацию, "
                                   "использовать один пароль, отвечать на звонки незнакомым людям ")
            states[user] = 10.1

    elif states[user] == 11:
        if answer == "1":
            states[user] = 12

    elif states[user] == 12:
        if answer == "1":
            bot.send_message(user, "Через пару секунд существо нагнало вас, запыхавшись он начал говорить:")
            states[user] = 13
        if answer == "2":
            bot.send_message(user, "Вы развернулись и даже успели сделать несколько шагов, после чего услышали как "
                                   "вас окликнули по имени и остановились. Вам стало любопытно, откуда этому лицу "
                                   "известно ваше имя. Решив разобраться в этой ситуации, вы развернулись и "
                                   "настороженно стали ждать, когда человечек подойдёт ближе.")
            bot.send_message(user, "Долго ждать не пришлось, и уже через несколько секунд он был около "
                                   "вас. Остановившись, он оглядел вас и начал говорить:")
            states[user] = 13
        if answer == "3":
            bot.send_message(user, "Морально настроившись на ещё один бой, вы встали в оборонительную позицию. "
                                   "Приблизившись к вам на расстояние нескольких шагов, человечек остановился, "
                                   "оглядел вас и, примирительно подняв руки, сказал:")
            states[user] = 13

    elif states[user] == 13:
            states[user] = 14

    elif states[user] == 14:
            states[user] = 15

    elif states[user] == 15:
            states[user] = 16

    elif states[user] == 16:
        states[user] = 17

    elif states[user] == 17:
        if answer == "1":
            bot.send_message(user, "Вирус проник намного глубже и удаление только "
                                   "заметных файлов не помогли окончательно избавиться от руткита")
            states[user] = 17.1
        if answer == "2":
            bot.send_message(user, "(Антивирус оказался не самым быстрым вашим другом, а "
                                   "следующий удар руткита всё же достиг задуманной цели и попал в вас")
            states[user] = 17.1
        if answer == "3":
            bot.send_message(user, "Только руткит собрался ударить ещё раз, как начал "
                                   "распадаться на мелкие частички и через пару секунд совсем исчез")
            states[user] = 18
        if answer == "4":
            bot.send_message(user, "К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас")
            states[user] = 17.1
        if answer == "5":
            bot.send_message(user, "Попытка была неплохой, но не самой действенной, ведь после сброса настроек "
                                   "вирус так и остался перед вами, да ещё и с очередным ударом, "
                                   "увернуться от которого уже не представляется возможным")
            states[user] = 17.1

    elif states[user] == 17.1:
        if answer == "1":
            bot.send_message(user, "Прекрасно! Вы справились с шпионом на вашем "
                                   "компьютере и можете продолжить свой путь.")
            states[user] = 17
        else:
            bot.send_message(user, "Похоже, что ваши действия не "
                                   "возымели действия, стоит попробовать сделать что-то другое.")
            bot.send_message(user, "Подсказка: Никогда не следует давать свою личную информацию, "
                                   "использовать один пароль, отвечать на звонки незнакомым людям ")
            states[user] = 17.1

    elif states[user] == 18:
        if answer == "1":
            states[user] = 19
        else:
            states[user] = 18.1

    elif states[user] == 18.1:
        if answer == "2":
            bot.send_message(user, "Данные действия только упростили вирусу задачу, стоит попробовать что-то другое ")
            bot.send_message(user, "Клавиатурный шпион(кейлоггер)- это отслеживание нажатий каждой клавиши клавиатуры, "
                                   "поэтому ввод паролей на незащищенных сайтах и ввод его в ручную является "
                                   "грубой ошибкой при пользовании устройством")
            states[user] = 18
        if answer == "3":
            bot.send_message(user, "Кажется, что перекачка пошла ещё быстрее, давайте попытаемся ещё раз ")
            bot.send_message(user, "Клавиатурный шпион(кейлоггер)- это отслеживание нажатий каждой клавиши клавиатуры, "
                                   "поэтому ввод паролей на незащищенных сайтах и ввод его в ручную является "
                                   "грубой ошибкой при пользовании устройством")
            states[user] = 18
        else:
            states[user] = 19

    elif states[user] == 19:
            states[user] = 20

    elif states[user] == 20:
        if answer == "2":
            states[user] = 21
        else:
            states[user] = 20.1

    elif states[user] == 20.1:
        if answer == "1":
            states[user] = 20
        if answer == "2":
            bot.send_message(user, "Чтобы избавиться от рекламной программы, "
                                   "не обязательно что-то удалять или сбрасывать")
            states[user] = 20

    elif states[user] == 21:
        states[user] = 22

    elif states[user] == 22:
        states[user] = 23

    elif states[user] == 23:
        if answer == "2":
            states[user] = 24
        else:
            states[user] = 23.1

    elif states[user] == 23.1:
        if answer == "1":
            states[user] = 23
        if answer == "2":
            bot.send_message(user, "Кликер можно уничтожить, используя специальную программу(утилиту)")
            states[user] = 23

    elif states[user] == 24:
        if answer == "1":
            states[user] = 25
        else:
            states[user] = 24.1

    elif states[user] == 24.1:
        if answer == "1":
            states[user] = 24
        if answer == "2":
            bot.send_message(user, "Рекламные вирусы можно уничтожить, "
                                   "средством удаления их всех одновременно (удалением ПО)")
            states[user] = 24

    elif states[user] == 25:
        if answer == "2":
            states[user] = 26
        else:
            if answer == "1":
                bot.send_message(user, "Простое удаление не всегда решает проблему, а особенно, если эта проблема "
                                       "способна наносить такие удары, как те, что полетели в вас")
            if answer == "3":
                bot.send_message(user, "Похоже, что дело не в простой смене браузера, ведь монстр уже "
                                       "успел уложить вас на лопатки")
            if answer == "4":
                bot.send_message(user, "Принятое вами решение не возимело успеха, а время было утрачено, и удар "
                                       "хиджакеры вам отразить не удалось")
            states[user] = 25.1

    elif states[user] == 25.1:
        if answer == "1":
            states[user] = 25
        if answer == "2":
            bot.send_message(user, "Хиджакер может изменить поисковую систему по умолчанию и домашнюю страницу, "
                                   "замедлить загрузку веб-страниц, установить несколько панелей инструментов без "
                                   "разрешения пользователя и создать несколько контекстных предупреждений для рекламы")
            states[user] = 25

    elif states[user] == 26:
        if answer == "1":
            states[user] = 27
        else:
            states[user] = 26

    elif states[user] == 27:
        if answer == "2":
            bot.send_message(user, "Да! Вы решили совершенно верно, и уже через секунду "
                                   "вирус пропал, будто его никогда и не было")
            states[user] = 28
        else:
            if answer == "1":
                bot.send_message(user, "Самый простой способ — не всегда самый верный")
            if answer == "3":
                bot.send_message(user, "Можно и компьютер сразу разбить, тогда проблем точно не будет")
            states[user] = 27.1

    elif states[user] == 27.1:
        if answer == "1":
            states[user] = 27
        if answer == "2":
            bot.send_message(user, "Удаление браузера не спасёт тебя от рекламы. А сброс настроек черезчур сильная мера"
                                   "для такого вируса.")
            states[user] = 27

    elif states[user] == 28:
        if answer == "4":
            bot.send_message(user, "Действительно, самый логичный выбор. Ну и теперь мы видим, что сообщение нам писал "
                                   "никакой не друг, а вирус «шутка», и открывающего точно не стоит. "
                                   "Так что двигаемся дальше.")
            states[user] = 29
        else:
            if answer == "1":
                bot.send_message(user, "Другое расширение файла никаким образом не гарантирует его безопасность. "
                                       "В эту ловушку то вы и попались, запустив файл")
            if answer == "2":
                bot.send_message(user, "Мы что, хотим подставить знакомого?")
            if answer == "3":
                bot.send_message(user, "Слабая надежда на то, что другое приложение для чтения испугает вирус, "
                                       "что и произошло. +1 новый вирус на вашем компьютере")
            states[user] = 28.1

    elif states[user] == 28.1:
        if answer == "1":
            states[user] = 28
        if answer == "2":
            bot.send_message(user, "Не стоит доверять в интернете всем и каждому, даже своему другу,"
                                   " мало ли его взломали? Советую проверить программу.")
            states[user] = 28

    elif states[user] == 29:
        if answer == "3":
            bot.send_message(user, "Поздравляем! Запрет подключения, действительно, "
                                   "избавил вас от этих вредоносных программ.")
            states[user] = 30
        else:
            if answer == "1":
                bot.send_message(user, "Такими действиями вы дали вирусам доступ к "
                                       "ещё большему количеству своих данных")
            if answer == "2":
                bot.send_message(user, "Вирусы всё равно остались на вашем устройстве, "
                                       "так что это был неэффективный вариант решения проблемы ")
            states[user] = 29

    elif states[user] == 30:
        if answer == "2":
            bot.send_message(user, "Вау! После сканирования и удаления в сторону босса от вас пошла волна, "
                                   "которая своей мощью снесла зомби, сбила его с ног, после чего он просто исчез. ")
            states[user] = 31
        else:
            if answer == "1":
                bot.send_message(user, "Боюсь, это не возымело действия, а вот зомби, в свою очередь, "
                                       "нанёс вам очень сильный удар ")
            if answer == "3":
                bot.send_message(user, "Вряд ли эта информация будет сейчас вам полезна. Но вот время, "
                                       "потраченное на считывание, позволило монстру наброситься на вас "
                                       "и в мгновение ока одолеть ")
            states[user] = 30.1

    elif states[user] == 30.1:
        if answer == "1":
            states[user] = 30
        if answer == "2":
            bot.send_message(user, "Найти вирус зомби не вооруженным глазом практически невозможно, но современные "
                                   "антивирусы способны избавиться от него")
            states[user] = 30

    elif states[user] == 31:
        if answer == "1":
            states[user] = 32

    process_state(user, states[user])

bot.polling(none_stop=True)