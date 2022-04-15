from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboard.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Salem!JIHC ga qosh keldin. Biz jaily kobirek aqparat bilu ushin,kerek batyrmany tanda)", reply_markup=menu)

@dp.message_handler(Text(equals=["Director"]))
async def get_fooo(message:Message):
    await message.answer(f"Director of JIHC is Bodaubekov Alisher Rustamovich",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Gruppalar"]))
async def get_fooo(message:Message):
    await message.answer(f"Barlyq gruppa sany-15.     1 kurs:1f1,1f2,1d,1a.     "
                         f"2 kurs:2e, 2d, 2g, 2b1, 2b2.     "
                         f"3 kurs:3h, 3i, 3f, 3c, 3g.     "
                         f"4 kurs:4e",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Mugalimder"]))
async def get_fooo(message:Message):
    await message.answer(f"Kabdushev Erdaulet, "
                         f"Amanzhol Eskendir, "
                         f"Sagyntay Erkebulan, "
                         f"Myktybaev Bakhytzhan",
                         reply_markup=ReplyKeyboardRemove())

@dp.message_handler(Text(equals=["Mamandyqtar"]))
async def get_fooo(message:Message):
    await message.answer(f"IT mamandyqtary, "
                         f"Marketing, "
                         f"Uchet audit, "
                         f"Matematika mugalimderi, "
                         f"Fizika mugalimderi",
                         reply_markup=ReplyKeyboardRemove())