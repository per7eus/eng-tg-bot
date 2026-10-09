from aiogram import Router
from bot.handlers.start import router_start
from bot.handlers.dialogueai import router_dialogue


router = Router()

router.include_router(router_start)
router.include_router(router_dialogue)
