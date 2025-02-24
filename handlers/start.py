from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from create_bot import duty_admins, save_duty_admins

router = Router()


def get_duty_buttons():
    buttons = [
        [KeyboardButton(text="✅ Пост принял")],
        [KeyboardButton(text="📤 Пост сдал")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False,
    )


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Это бот для дежурства в мониторинге, выберите действие кнопками ниже.", reply_markup=get_duty_buttons())


@router.message(F.text == "✅ Пост принял")
async def accept_duty(message: Message):
    if message.from_user.id not in duty_admins:
        duty_admins.add(message.from_user.id)
        save_duty_admins(duty_admins)
        await message.answer("Пост принят. Теперь вы в списке дежурных.")
    else:
        await message.answer("Вы уже являетесь дежурным.")


@router.message(F.text == "📤 Пост сдал")
async def release_duty(message: Message):
    if message.from_user.id in duty_admins:
        duty_admins.remove(message.from_user.id)
        save_duty_admins(duty_admins)
        await message.answer("Пост сдан. Вы больше не являетесь дежурным.")
    else:
        await message.answer("Вы не являетесь дежурным.")


@router.message()
async def respond_to_keyword(message: Message) -> None:
    user_message = message.text.lower()

    if not '📤 Пост сдал' or not '✅ Пост принял' in user_message:
        await message.answer('Пожалуйста, используйте кнопки ниже.')
