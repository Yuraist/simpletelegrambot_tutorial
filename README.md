# Простой echo-бот на Python

__Внимание__: Мы работаем на операционных системах macOS и Linux. 
Не все, описанное ниже, может корректно работать с ОС Windows. Поэтому, 
если вы хотите повторить все действия и получить такой же результат, советуем
вам использовать Linux или macOS. Вы можете установить одну из этих систем на свой 
персональный компьютер или использовать виртуальную машину. Если же вы решите
использовать Windows, то при возникновении проблем, обращайтесь за помощью в наш 
[Telegram-чат](https://t.me/therealtalkchat) или 
старайтесь найти решения ваших вопросов в интернете. 
 

### Настройка окружения
Перед тем как приступить непосредственно к написанию кода, 
вам понадобится установить некоторые инструменты, с которыми
мы будем работать далее. Если вы уже работали с Python, pip, 
virtualenv, git и Heroku, то вы можете перейти сразу к просмотру видео. 
Если же на вашем компьютере еще не установлены эти инструменты, то давайте
настроим их.

1. Для начала скачаем интерпретатор языка Python. Делается это довольно просто: 
перейдите на [официальный сайт языка Python](https://www.python.org/downloads/), 
скачайте версию языка Python 3.6.x для своей операционной системы 
и установите его, как обычную программу. 
2. Теперь нужно установить пакетный менеджер pip (он позволит быстро устанавливать нужные библиотеки).
Если вы установили Python версии 3.6, то pip должен быть установлен автоматически. Проверьте, есть ли он
на вашем компьютере, открыв Terminal и написав `pip -V`. Если pip установлен, то
вы увидите сообщение с номером его версии, и вы сможете перейти к следующему шагу. В противном случае, 
вам нужно продолжить установку. Для этого откройте приложение Terminal на вашем компьютере и введите команду:
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`.
Эта команда скачает установщик pip. Далее введите 
`python get-pip.py`. Поизойдет установка пакетного менеджера. 
3. Установка виртуального окружения, позволяющего изолировать установленные библиотеки разных проектов. 
Для быстрой установки данного инструмента, мы воспользуемся установленным ранее pip. Введите в Terminale 
`pip install virtualenv` и наш пакетный менеджер скачает все нужные файлы. Теперь виртуальное окружение установлено.
4. На этом минимальная настройка окружения для Python разработки закончена. Но нам еще нужно установить некоторые 
инструменты для дальнейшей публикации нашего бота (а также других приложений, если вы продолжите разрабатывать на 
Python). Начнем с установки системы контроля версий - git. Git позволяет управлять вашими изменениями в коде, а также 
удобно переносить код из окружения разработки на рабочие машины. Кстати, он также может быть уже установлен на вашем 
компьютере, поэтому проверьте его наличие перед установкой: `git --version`. Если вы не увидели версию, то продолжайте 
этот пункт. Так как в установке git есть отличия в разных ОС, мы 
не будем повторять сотни других гайдов по его установки, а просто поделимся самым популярным русскоязычным руководством:
[Установка git](https://git-scm.com/book/ru/v2/%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%A3%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0-Git).
5. Итак, мы установили Python на наш компьютер, поставили pip и virtualenv. Даже скачали git! Остался последний 
инструмент - Heroku  (который, кстати, вы можете не настраивать, если не хотите запускать своего бота на сервере. В таком случае вы сможете 
 запустить и попробовать его на своем компьютере, а даже показать своему другу. Но бот будет работать только пока ваша 
 программа запущена, поэтому для его постоянной работы потребуется либо сервер, либо постоянно включеный компьютер). 
 Зайдите на сайт нашего будущего хостинга [heroku.com](https://heroku.com) и создайте на нем аккаунт. После того, как 
 зарегистрируйтесь, перейдите на 
 [страницу установки heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up). 
 Установите пакет для своей системы и авторизуйтесь через Terminal с помощью команды `heroku login`. 

Если вы выполнили предыдущие 5 действий, то на вашем компьютере должны быть установлены все инструменты для разработки и 
публикации чатбота для Telegram. Но для продолжения работы, нужно выполнить еще одно простое действие - получить токен у 
крестного отца всех Telegram-ботов – [BotFather](https://t.me/BotFather). Для этого вам нужно просто начать диалог с 
"главным ботом" и ввести команду __/newbot__. После этого введите название вашего бота (это будет заголовок, который
видят пользователи вверху диалога), а следующим шагом введите username вашего бота, который должен заканчиваться на 
*bot*. Заметьте, что username должен быть уникальным, поэтому при вводе желаемого имени, BotFather может попросить 
ввести другое, если введенный вами вариант уже занят. Далее, как только вы ввели корректный username, бот напишет вам: 
"Done! Congratulations on your new bot..." и отправит сообщение с токеном: "Use this token to access the HTTP API:
__123414:qwertyasdfg__". У вас будет свой личный токен для управления вашим ботом, поэтому не стоит им делиться с 
кем-либо.  
 
После того, как вы наконец-то выполните все действия, которые описаны выше, можете смело приступать к разработке своего 
первого проекта на Python. 

Если у вас остались какие-то вопросы или возникли сложности в установке, то смело спрашивайте в 
нашем чате [@therealtalkchat](https://t.me/therealtalkchat)! 