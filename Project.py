from aiogram import Bot, Dispatcher, types, executor
from security import TOKEN
from text import (START_TEXT, CRINGE, SLENG, SWEG, TRESH, VIBE, CRASH, GIZA, LMAO, MEM, PRUF, ROFL,
                  FRIENDZONE, HYPE, SHIPPING, SCAM, GG, IMBA, NORMIS, DED_INSIDE, SKIP, ALTIN, ARSHIN,BEZOBICHNI,
                  VEDRO, IZVADITSA, ISKRENOK, KUZLO, KYLIGKA, LOVITVA, MOROK,MILNIA, NAZOLA, NYZA,
                  OBORI, PALENICA, ONYCHI, INSTRUCTION, NEW_WORDS, OBOSLETE_WORDS)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(text=["/start"])
async def cmd_start(msg: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   button = ["Инструкция"]
   keyboard.add(*button)
   await msg.answer(text=START_TEXT, reply_markup=keyboard)

@dp.message_handler(text=["Инструкция"])
async def greet_text(msg: types.Message):
    await msg.reply(text=INSTRUCTION, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(text=["Список", "список"])
async def cmd_start(msg: types.Message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
   buttons = ["Новые слова", "Устаревшие слова"]
   keyboard.add(*buttons)
   await msg.answer(text="Выберите одну из кнопок", reply_markup=keyboard)

@dp.message_handler(text=["Новые слова"])
async def greet_text(msg: types.Message):
   await msg.answer(text=NEW_WORDS, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(text=["Устаревшие слова"])
async def greet_text(msg: types.Message):
   await msg.answer(text=OBOSLETE_WORDS, reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(text=["Кринж", "кринж"])
async def greet_text(msg: types.Message):
   await msg.answer(text=CRINGE)

@dp.message_handler(text=["Сленг", "сленг"])
async def greet_text(msg: types.Message):
   await msg.answer(text=SLENG)

@dp.message_handler(text=["Свег", "свег"])
async def greet_text(msg: types.Message):
   await msg.answer(text=SWEG)

@dp.message_handler(text=["Треш", "треш"])
async def greet_text(msg: types.Message):
   await msg.answer(text=TRESH)

@dp.message_handler(text=["Вайб", "вайб"])
async def greet_text(msg: types.Message):
   await msg.answer(text=VIBE)

@dp.message_handler(text=["Краш", "краш"])
async def greet_text(msg: types.Message):
   await msg.answer(text=CRASH)

@dp.message_handler(text=["Жиза","жиза"])
async def greet_text(msg: types.Message):
   await msg.answer(text=GIZA)

@dp.message_handler(text=["Лмао","лмао"])
async def greet_text(msg: types.Message):
   await msg.answer(text=LMAO)

@dp.message_handler(text=["Мем","мем"])
async def greet_text(msg: types.Message):
   await msg.answer(text=MEM)

@dp.message_handler(text=["Пруф", "пруф"])
async def greet_text(msg: types.Message):
   await msg.answer(text=PRUF)

@dp.message_handler(text=["Рофл", "рофл"])
async def greet_text(msg: types.Message):
   await msg.answer(text=ROFL)

@dp.message_handler(text=["Френдзона", "френдзона"])
async def greet_text(msg: types.Message):
   await msg.answer(text=FRIENDZONE)

@dp.message_handler(text=["Хайп", "хайп"])
async def greet_text(msg: types.Message):
   await msg.answer(text=HYPE)

@dp.message_handler(text=["Шипперить","шипперить"])
async def greet_text(msg: types.Message):
   await msg.answer(text=SHIPPING)

@dp.message_handler(text=["Скам", "скам"])
async def greet_text(msg: types.Message):
   await msg.answer(text=SCAM)

@dp.message_handler(text=["Гг", "гг"])
async def greet_text(msg: types.Message):
   await msg.answer(text=GG)

@dp.message_handler(text=["Имба", "имба"])
async def greet_text(msg: types.Message):
   await msg.answer(text=IMBA)

@dp.message_handler(text=["Нормис", "нормис"])
async def greet_text(msg: types.Message):
   await msg.answer(text=NORMIS)

@dp.message_handler(text=["Дед инсайд", "дед инсайд"])
async def greet_text(msg: types.Message):
   await msg.answer(text=DED_INSIDE)

@dp.message_handler(text=["Скип", "скип"])
async def greet_text(msg: types.Message):
   await msg.answer(text=SKIP)

@dp.message_handler(text=["Алтын", "алтын"])
async def greet_text(msg: types.Message):
   await msg.answer(text=ALTIN)

@dp.message_handler(text=["Аршин", "аршин"])
async def greet_text(msg: types.Message):
   await msg.answer(text=ARSHIN)

@dp.message_handler(text=["Безобычный", "безобычный"])
async def greet_text(msg: types.Message):
   await msg.answer(text=BEZOBICHNI)

@dp.message_handler(text=["Вёдро", "вёдро"])
async def greet_text(msg: types.Message):
   await msg.answer(text=VEDRO)

@dp.message_handler(text=["Извадиться", "извадиться"])
async def greet_text(msg: types.Message):
   await msg.answer(text=IZVADITSA)

@dp.message_handler(text=["Искренок", "искренок"])
async def greet_text(msg: types.Message):
   await msg.answer(text=ISKRENOK)

@dp.message_handler(text=["Кузло", "кузло"])
async def greet_text(msg: types.Message):
   await msg.answer(text=KUZLO)

@dp.message_handler(text=["Кулижка", "кулижка"])
async def greet_text(msg: types.Message):
   await msg.answer(text=KYLIGKA)

@dp.message_handler(text=["Ловитва", "ловитва"])
async def greet_text(msg: types.Message):
   await msg.answer(text=LOVITVA)

@dp.message_handler(text=["Морок", "морок"])
async def greet_text(msg: types.Message):
   await msg.answer(text=MOROK)

@dp.message_handler(text=["Мыльня", "мыльня"])
async def greet_text(msg: types.Message):
   await msg.answer(text=MILNIA)

@dp.message_handler(text=["Назола", "назола"])
async def greet_text(msg: types.Message):
   await msg.answer(text=NAZOLA)

@dp.message_handler(text=["Нужа", "нужа"])
async def greet_text(msg: types.Message):
   await msg.answer(text=NYZA)

@dp.message_handler(text=["Оборы", "оборы"])
async def greet_text(msg: types.Message):
   await msg.answer(text=OBORI)

@dp.message_handler(text=["Паленица", "паленица"])
async def greet_text(msg: types.Message):
   await msg.answer(text=PALENICA)

@dp.message_handler(text=["Онучи", "онучи"])
async def greet_text(msg: types.Message):
   await msg.answer(text=ONYCHI)

@dp.message_handler()
async def all_text(msg: types.Message):
    await msg.answer(text="Простите, я Вас не понимаю")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
