import asyncio
from openai import AsyncOpenAI

from config import API_AGENT


client = AsyncOpenAI(
    api_key=API_AGENT,
    base_url="https://ai.api.cloud.yandex.net/v1",
    project="b1ggqesp8dhj1hrgce7c",
)


async def dialogue(previous_response_id, message):
    '''

    :param previous_response_id:
    :param message:
    :return:{
            "errors": [
            {"wrong": "неправильный фрагмент", "correct": "правильный вариант", "explanation": "краткое пояснение на русском"}
          ],
          "reply_en": "Твой ответ собеседнику на английском языке",
          "reply_ru": "Расшифровка твоего ответа на русском языке"
        }
    '''
    response = await client.responses.create(
        prompt={
            "id": "fvtb33o8qvpefsif64hq",
        },
        previous_response_id=previous_response_id,
        input=message,
    )

    return response.id, response.output_text




async def agentai():
    message = input("Диалог с агентом начат!\n> ")

    response_id, message_result = await dialogue(None, message)

    while True:
        message = input(f"{message_result}\n> ")

        message_result = await dialogue(
            response_id,
            message,
        )


if __name__ == "__main__":
    asyncio.run(agentai())