import asyncio

from aiogram import Bot, Dispatcher, executor

input_test = input()

admin_tg_id = 1055839574
token = "5881481818:AAHTTKN6swk4wgaCBIwY-8bvZdDxoZP3YWU"

bot = Bot(token=token)
dp = Dispatcher(bot)


def go(message):
    async def send_msg(sleep_for):
        await asyncio.sleep(sleep_for)
        await bot.send_message(admin_tg_id, message)

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.create_task(send_msg(1))
        executor.start_polling(dp, skip_updates=True)


go(input_test)
