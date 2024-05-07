from aiogram import Bot, Dispatcher, types, executor
from securityone import TOKEN
from TextForBotOne import menu_Project, menu_kb_3
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"]) #вместо command может быть text
async def start_cmd(msg: types.Message):
   await msg.reply(text=START_TEXT) # вместо reply может быть answer или await bot.send_massage(chat_id=)

@dp.message_handler(commands=["start"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="Привет", reply_markup=menu_Project)

@dp.message_handler(commands=["About bot"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="ABOUT_BOT_TEXT")


@dp.message_handler(commands=["random","рандом"])
async def random_cmd(msg: types.Message):
   await msg.answer(text="тыкни!", reply_markup = menu_kb_3)



@dp.callback_query_handler(text="random_num")
async def inline_kb1(call: types.CallbackQuery):
   num = random.randint(1, 10)
   await call.message.answer(text=str(num))
   await call.answer()




"""def S(a: int,b: str):
   print(a*b)"""

@dp.message_handler(commands=["список"])
async def start_cmd(msg: types.Message):
   await msg.answer(text=" ")

@dp.message_handler(text=["Кринж"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="CRINGE")

@dp.message_handler(text=["Сленг"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="SLENG")

@dp.message_handler(text=["Свег"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="SWEG")

@dp.message_handler(text=["Треш"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="TRESH")

@dp.message_handler(text=["Вайб"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="VIBE")

@dp.message_handler(text=["Краш"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="CRASH")

@dp.message_handler(text=["Жиза"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="GIZA")

@dp.message_handler(text=["Лмао"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="LMAO")

@dp.message_handler(text=["Мем"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="MEM")

@dp.message_handler(text=["Пруф"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="PRUF")

@dp.message_handler(text=["Рофл"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="ROFL")

@dp.message_handler(text=["Френдзона"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="FRIENDZONE")

@dp.message_handler(text=["Хайп"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="HYPE")

@dp.message_handler(text=["Шипперить"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="SHIPPERING")

@dp.message_handler(text=["Скам"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="SCAM")

@dp.message_handler(text=["Гг"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="GG")

@dp.message_handler(text=["Имба"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="IMBA")

@dp.message_handler(text=["Нормис"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="NORMIS")

@dp.message_handler(text=["Дед инсайд"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="DED_INSIDE")

@dp.message_handler(text=["Скип"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="SKIP")

@dp.message_handler(text=["Алтын"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="ALTIN")

@dp.message_handler(text=["Аршин"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="ARSHIN")

@dp.message_handler(text=["Безобычный"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="BEZOBOCHNI")

@dp.message_handler(text=["Вёдро"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="VEDRO")

@dp.message_handler(text=["Извадиться"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="IZVADITSA")

@dp.message_handler(text=["Искренок"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="ISKRENOK")

@dp.message_handler(text=["Кузло"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="KUZLO")

@dp.message_handler(text=["Кулижка"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="KYLIGKA")

@dp.message_handler(text=["Ловитва"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="LOVITVA")

@dp.message_handler(text=["Морок"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="MOROK")

@dp.message_handler(text=["Мыльня"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="MILNIA")

@dp.message_handler(text=["Назола"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="NAZOLA")

@dp.message_handler(text=["Нужа"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="NYZA")

@dp.message_handler(text=["Оборы"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="OBORI")

@dp.message_handler(text=["Паленица"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="PALENICA")

@dp.message_handler(text=["Онучи"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="ONYCHI")




if __name__=="__main__":
   executor.start_polling(dp, skip_updates=True)
