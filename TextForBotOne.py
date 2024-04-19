from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,

menu_Project = ReplyKeyboardMarkup(resize_keyboard=True)

b_1 = KeyboardButton("Запуск")
b_2 = KeyboardButton("Автор")

menu_Project.add(b_1,b_2)


inline_Project = InlineKeyboardMarkup(row_width=2)

b_3 = InlineKeyboardButton(text="тут что нап. на кнопке", url="ghbioiu")
b_4 = InlineKeyboardButton(text="Ссылка на автора", url="hhjljknkj")

inline_Project = (b_3, b_4)

START_TEXT = """Добро пожаловать!
Это бот, который поможет узнать
значение неизвестных вам слов,
а также более распространенные синонимы к ним."""

