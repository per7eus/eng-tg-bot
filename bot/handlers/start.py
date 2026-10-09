from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import bot.keyboard.start as keyboard

router_start = Router()


@router_start.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привет",reply_markup=keyboard.start_keyboard)