from datetime import time

def dark_theme_by_time(current_time):
    # переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if time(hour=6) <= current_time < time(hour=22):
        is_dark_theme = False
    else:
        is_dark_theme = True
    return is_dark_theme
def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    is_dark_theme = dark_theme_by_time(current_time)

    assert is_dark_theme is True

def dark_theme_by_time_and_user_choice(current_time, dark_theme_enabled_by_user):
# переключите темную тему в зависимости от времени суток,
#  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user is None:
        if time(hour=6) <= current_time < time(hour=22):
            is_dark_theme = False
        else:
            is_dark_theme = True
    elif dark_theme_enabled_by_user:
        is_dark_theme = True
    else:
        is_dark_theme = False
    return is_dark_theme

def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную
    is_dark_theme = dark_theme_by_time_and_user_choice(current_time, dark_theme_enabled_by_user)
    assert is_dark_theme is True

def find_suitable_user_by_name(users, name):
    for user in users:
        if user['name'] == name:
            suitable_users = user
    return suitable_users

def find_users_younger(users, age):
    suitable_users = []
    # найдите всех пользователей младше 20 лет
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
    return suitable_users

def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # найдите пользователя с именем "Olga"
    suitable_users = find_suitable_user_by_name(users, "Olga" )

    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = find_users_younger(users, 20)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = make_it_readable(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = make_it_readable(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = make_it_readable(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def make_it_readable(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args_formatted = ', '.join([*args])
    print(f'{func_name} [{args_formatted}]')
    return f'{func_name} [{args_formatted}]'
