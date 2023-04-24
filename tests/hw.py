from datetime import time


def test_dark_theme_by_time():
	"""
	Протестируйте правильность переключения темной темы на сайте в зависимости от времени
	"""
	current_time = time(hour=23)
	is_dark_theme = current_time.hour >= 22 or current_time.hour < 6
	assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
	"""
	Проверка корректности переключения темной темы на сайте
	в зависимости от времени суток и выбора пользователя
	dark_theme_enabled_by_user = True - темная тема включена
	dark_theme_enabled_by_user = False - темная тема выключена
	dark_theme_enabled_by_user = None - пользователь не сделал выбора (используется автоматическое переключение по времени системы)
	"""
	current_time = time(hour=16)
	dark_theme_enabled_by_user = True
	if dark_theme_enabled_by_user is not None:
		is_dark_theme = dark_theme_enabled_by_user
	else:
		is_dark_theme = current_time.hour >= 22 or current_time.hour < 6
	assert is_dark_theme is True


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
	# Найдите пользователя с именем "Olga"
	suitable_user = [user for user in users if user["name"] == "Olga"]
	assert suitable_user == [{"name": "Olga", "age": 45}]
	# Найдите всех пользователей младше 20 лет
	suitable_users = [user for user in users if user["age"] < 20]
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
	open_browser("Chrome")
	go_to_companyname_homepage("https://companyname.com")
	find_registration_button_on_login_page("https://companyname.com/login", "Register")


def print_name_function(func, *args):
	result = func.__name__.replace("_", " ").title() + f" [{', '.join(args)}]"
	print(result)
	return result


def open_browser(browser_name):
	actual_result = print_name_function(open_browser, browser_name)
	assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
	actual_result = print_name_function(go_to_companyname_homepage, page_url)
	assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
	actual_result = print_name_function(find_registration_button_on_login_page, page_url, button_text)
	assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
