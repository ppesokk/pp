from aiogram import Bot, Dispatcher, types, executor
from securityone import TOKEN
from TextForBotOne import menu_Project

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"]) #вместо command может быть text
async def start_cmd(msg: types.Message):
   await msg.reply(text=START_TEXT) # вместо reply может быть answer или await bot.send_massage(chat_id=)


@dp.message_handler(commands=["start"])
async def start_cmd(msg: types.Message):
   await msg.answer(text="Привет", reply_markup=menu_Project)


if __name__=="__main__":
   executor.start_polling(dp, skip_updates=True)
