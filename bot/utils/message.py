import json

async def creat_message(text):
    text_json = json.loads(text)
    message_error = ""
    if text_json.get("errors"):
        message_error = "В вашем сообщении есть ошибки: \n"

        for error in text_json["errors"]:
            message_error += f"\tФрагмент: {error["wrong"]}\n"
            message_error += f"\tПравильное написание: {error["correct"]}\n"
            message_error += f"\tПояснение: {error["explanation"]}\n\n"

    message_reply_en = text_json["reply_en"]
    message_reply_ru = text_json["reply_ru"]

    return message_error, message_reply_en, message_reply_ru