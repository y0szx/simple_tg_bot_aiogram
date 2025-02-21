from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from create_bot import bot, ADMIN_ID

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, <b>{message.from_user.first_name}</b>! Я бот для ответа по ключевым словам.")


@router.message()
async def respond_to_keyword(message: Message) -> None:
    user_message = message.text.lower()

    first_name = message.from_user.first_name

    if 'эцп' in user_message:
        await message.answer(f'Здравствуйте, {first_name}! Вам позвонят сисадмины.')
    elif 'уволился' in user_message:
        await message.answer(f'Здравствуйте, {first_name}! Вам позвонят с отдела зарплат.')
    else:
        await message.answer(f'Здравствуйте, {first_name}! Извините, я не понял ваше сообщение.')

    await bot.send_message(chat_id=message.from_user.id, text=f"Здравствуйте, {first_name}! С вами свяжется администратор.")

    await bot.forward_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)
