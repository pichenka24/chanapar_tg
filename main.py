from aiogram import executor, types
from all_users import control_word

from config import bot, dp, app


@dp.message_handler(commands=['id'])
async def send_welcome(message: types.Message):

    await app.start()
    async for member in app.get_chat_members(int('-1001616867686')):
        print(member.user)
    await app.stop()


@dp.message_handler(content_types=['text'])
async def all_members(message: types.Message):
    msg = message.text
    print(msg)

    result = control_word(msg)
    if result == 1:
        await bot.send_message(chat_id=-1001616867686, text='Еще раз увижу мат, Бан')


    if msg == '@all':
        tag = ''
        try:
            await app.start()

            async for member in app.get_chat_members(int('-1001616867686')):
                if member.user.username == message.from_user.username or member.user.username == 'chanapar_bot':
                    continue
                else:
                    if member.user.username:
                        tag += f'@{member.user.username}\n'
                    else:
                        tag += f'@{member.user.first_name}\n'
            await bot.send_message(chat_id=-1001616867686, text=tag)

        except Exception as ex:
            print(ex)

        finally:
            await app.stop()

    if message.from_user.username == 'Liliya_a_a':
        await bot.send_sticker(chat_id=-1001616867686, stiker='CAACAgIAAxkBAAEJq8dkrr391q0irOpyN_7MxLlqNXmzZQACBgADkTmcHK0SVrvESXOeLwQ')
        await bot.send_sticker(chat_id=-1001616867686,
                               stiker='CAACAgIAAxkBAAEJq89krsBjHCmeFWEbQyYpL9rSvmOpPAACnQMAAn60IAVLi7tSg5Arqi8E')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
