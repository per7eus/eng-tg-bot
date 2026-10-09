from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.states.dialogueai import DialogueAi
import bot.keyboard.dialogueai as keyboard

from bot.utils.agentai import dialogue
from bot.utils.message import creat_message


router_dialogue = Router()


@router_dialogue.message(F.text == "Начать общение с AI")
async def start(message: Message):
    await message.answer("Напиши первое сообщение боту",reply_markup=keyboard.remove_button)

@router_dialogue.message(F.text)
async def start(message: Message,state: FSMContext):
    sent_message = await message.answer("Сообщение обрабатывается ⏳")
    previous_response_id,text = await dialogue(None, message.text)

    message_error, message_reply_en, message_reply_ru = await creat_message(text)
    await state.update_data(message_reply_ru=message_reply_ru, message_reply_en=message_reply_en)
    await sent_message.delete()
    if message_error:
        await message.answer(message_error)

    await message.answer(message_reply_en, reply_markup=keyboard.show_ru_message)

    await state.set_state(DialogueAi.dialogue)
    await state.update_data(previous_response_id=previous_response_id)

@router_dialogue.message(DialogueAi.dialogue)
async def start(message: Message,state: FSMContext):
    sent_message = await message.answer("Сообщение обрабатывается ⏳")
    data = await state.get_data()
    previous_response_id = data['previous_response_id']
    previous_response_id, text = await dialogue(previous_response_id, message.text)
    message_error, message_reply_en, message_reply_ru = await creat_message(text)
    await state.update_data(message_reply_ru=message_reply_ru, message_reply_en=message_reply_en)
    await sent_message.delete()
    if message_error:
        await message.answer(message_error)

    await message.answer(message_reply_en, reply_markup=keyboard.show_ru_message)

    await state.update_data(previous_response_id=previous_response_id)


@router_dialogue.callback_query( F.data == "show_ru_message")
async def show_ru_message(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    message_reply_ru = data['message_reply_ru']
    await call.message.edit_text(message_reply_ru, reply_markup=keyboard.show_en_message)


@router_dialogue.callback_query( F.data == "show_en_message")
async def show_ru_message(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    message_reply_en = data['message_reply_en']
    await call.message.edit_text(message_reply_en, reply_markup=keyboard.show_ru_message)

