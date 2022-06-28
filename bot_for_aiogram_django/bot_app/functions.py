from typing import Dict, List

from aiogram.types import InputMediaPhoto, Message

from bot_app.keyboards import main_keyboard


async def create_message(data: List[Dict], images: List[Dict], message: Message) -> None:
    """
    This function collects the message itself
    and sends it based on the data sent to it
    """
    global send_photo, message_answer, media_group

    await message.answer("Результаты: ", reply_markup=main_keyboard)  # This answer is required to replace the keyboard
    # because method answer_media_group does not support reply_markup

    for i in data:
        media_group = []
        field_id = i.get("id")
        message_answer = f"""
Название - {i.get('name')}
Адрес - {i.get("address")}
Размеры поля - {i.get("size")}
Количество ворот - {i.get("gate")}
Условия - {i.get("conditions")}
Локация - {i.get("location")}
Номер телефона - {i.get("phone_number")}"""
        for j in images:
            if j.get("football_field") == field_id:
                send_photo = open(j.get("image").replace("/", "\\", 99)[1:], 'rb')
                media_group.append(InputMediaPhoto(send_photo))
        try:
            media_group[0].caption = message_answer
        except IndexError:
            await message.answer(text=message_answer)
            # Send info of football field without photo
        else:
            await message.answer_media_group(media=media_group)
            # Send info with photo 1 or more
        finally:
            send_photo.close()
