from aiogram.fsm.state import State, StatesGroup


class DialogueAi(StatesGroup):
    dialogue = State()