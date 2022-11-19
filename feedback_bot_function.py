import asyncio

from aiogram import Bot, Dispatcher, executor

admin_tg_id =
token = ""

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
