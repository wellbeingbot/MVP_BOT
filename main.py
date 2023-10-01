from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.keyboards import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database import Database
from data_test1 import DatabaseTest1
from data_test2 import DatabaseTest2
from data_test3 import DatabaseTest3
from states import NewAnket, Test1, Test2, Test3

from texts import *
import test_questions

storage = MemoryStorage()
id_grou = ''
API = '--'
bot = Bot(token=API)
dp = Dispatcher(bot, storage=storage)
dat_anketa = Database('anketa.db')
data_test1 = DatabaseTest1('test_num1.db')
data_test2 = DatabaseTest2('test_num2.db')
data_test3 = DatabaseTest3('test_num3.db')


async def message_time(bot: Bot):
    name = dat_anketa.get_user()
    for i in name:
        if i[-1] == 0:
            await bot.send_message(i[1], 'There is a test pending, please go to Tests to complete it. Thank you!',
                                   reply_markup=ikb_res1)
        elif i[-1] == 'test1':
            await bot.send_message(i[1], 'There is a test pending, please go to Tests to complete it. Thank you!',
                                   reply_markup=ikb_res2)
        elif i[-1] == 'test2':
            await bot.send_message(i[1], 'There is a test pending, please go to Tests to complete it. Thank you!',
                                   reply_markup=ikb_res3)
        else:
            continue


scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
scheduler.add_job(message_time, trigger='cron', hour=10, minute=59,
                  kwargs={'bot': bot})
scheduler.start()


@dp.message_handler(commands='start')
async def start_reg(message: types.Message):
    if not dat_anketa.user_exists(message.from_user.id):
        dat_anketa.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id,
                               text=f"{hi}")
        await bot.send_message(message.from_user.id, text="Please share some information about yourself",
                               reply_markup=ikb_reg)

    else:
        await bot.send_message(message.from_user.id,
                               text="We remember you", reply_markup=ikb_res1)


@dp.callback_query_handler(text='material')
async def material(call: CallbackQuery):
    name = dat_anketa.get_user_one(call.from_user.id)[0][-1]
    if name == '0':
        await call.message.answer(text='Materials', reply_markup=ikb_mat3)
    elif name == 'test1':
        await call.message.answer(text='Materials', reply_markup=ikb_mat2)
    elif name == 'test2':
        await call.message.answer(text='Materials', reply_markup=ikb_mat1)
    else:
        await call.message.answer(text='Materials', reply_markup=ikb_mat0)


@dp.callback_query_handler(text='day1')
async def needtest(call: CallbackQuery):
    await call.message.edit_text(text='<b>Communication difficulties</b>\nhttps://youtu.be/5J5qwdtMHTQ',
                                 parse_mode='html')
    await call.message.answer(text=f'{text1}', parse_mode='html')
    await call.message.answer(text=f'{text11}', parse_mode='html', reply_markup=ikb_res1)


@dp.callback_query_handler(text='day2')
async def needtest(call: CallbackQuery):
    await call.message.edit_text(text='<b>Movements introductions</b>\nhttps://www.youtube.com/watch?v=khuLoAYm_JM',
                                 parse_mode='html')
    await call.message.answer(text='<b>Movements</b>\nhttps://www.youtube.com/watch?v=1faJfjwRg3k',
                              reply_markup=ikb_res2, parse_mode='html')


@dp.callback_query_handler(text='day3')
async def needtest(call: CallbackQuery):
    await call.message.edit_text(
        text='<b>Video - Importance of breaks</b>\nhttps://www.youtube.com/watch?v=0p1xVlZ1IYk', reply_markup=ikb_res3,
        parse_mode='html')


@dp.callback_query_handler(text='day4')
async def needtest(call: CallbackQuery):
    await call.message.edit_text(text='<b>Video - movements</b>\nhttps://www.youtube.com/watch?v=0kKe3IS2xiM',
                                 reply_markup=ikb_fin, parse_mode='html')


@dp.callback_query_handler(text='mini_anketa', state=None)
async def mini_anketa(call: CallbackQuery):
    # await call.message.answer(text='Go!')
    await call.message.answer(text='First name')
    await NewAnket.name.set()


@dp.message_handler(state=NewAnket.name)
async def add_name(message: types.Message, state: FSMContext):
    dat_anketa.set_time_sub(message.from_user.id, message.date.strftime('%H:%M:%S_%d:%m:%Y'))
    dat_anketa.add_name(message.from_user.id, message.text)  # добавляем имя и вводим фамилию
    await message.answer('Last name')
    await NewAnket.lastname.set()


@dp.message_handler(state=NewAnket.lastname)
async def add_lastname(message: types.Message, state: FSMContext):
    dat_anketa.set_lust_name(message.from_user.id, message.text)

    await message.answer('Age')
    await NewAnket.age.set()


@dp.message_handler(state=NewAnket.age)
async def add_age(message: types.Message, state: FSMContext):
    dat_anketa.set_age(message.from_user.id, message.text)

    await message.answer('Weight')
    await NewAnket.weight.set()


@dp.message_handler(state=NewAnket.weight)
async def add_weight(message: types.Message, state: FSMContext):
    dat_anketa.set_weight(message.from_user.id, message.text)

    await message.answer('Height')
    await NewAnket.height.set()


@dp.message_handler(state=NewAnket.height)
async def add_height(message: types.Message, state: FSMContext):
    dat_anketa.set_height(message.from_user.id, message.text)
    st = '0'
    dat_anketa.add_state(message.from_user.id, st)
    await message.answer(f'{registration_behind}', reply_markup=ikb_res1)
    know = dat_anketa.get_user_one(message.from_user.id)[0]
    await bot.send_message(id_grou,
                           text=f"Пользователь @{message.from_user.username} прошел прошел регистрацию в {message.date.strftime('%H:%M:%S %d:%m:%Y')}\nИмя: {know[3]}\nФамилия: {know[4]}\nВозраст: {know[5]}\nВес: {know[6]}\nРост: {know[7]}")

    await state.finish()


ikb_tst1 = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Go', callback_data='test1go1')).add(
    InlineKeyboardButton(text='Back to material', callback_data='material'))


@dp.callback_query_handler(text='test1')
async def go_test1(call: CallbackQuery):
    await call.message.answer(text=f'{burnout_pre_text}', reply_markup=ikb_tst1, parse_mode='html')


@dp.callback_query_handler(text='test1go1')
async def go_test1(call: CallbackQuery):
    data_test1.add_user(call.from_user.id)
    data_test1.set_time_sub(call.from_user.id, call.message.date.strftime('%H:%M:%S_%d:%m:%Y'))
    await call.message.answer(text='Instructions: For each question, click the button that most applies.',
                              parse_mode='html')
    await call.message.answer(text=test_questions.test1.q1, parse_mode='html', reply_markup=ikb_test1)
    await Test1.test1_answ1.set()


@dp.callback_query_handler(state=Test1.test1_answ1)
async def go_answ1(call: CallbackQuery, state: FSMContext):
    print(type(call.data))

    if call.data in '012345678':
        data_test1.add_answ1(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q2, parse_mode='html', reply_markup=ikb_test1)
        await Test1.test1_answ2.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ2)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ2(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q3, parse_mode='html', reply_markup=ikb_test1)
        await Test1.test1_answ3.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ3)
async def go_answ3(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ3(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q4, reply_markup=ikb_test1)
        await Test1.test1_answ4.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ4)
async def go_answ4(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ4(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q5, reply_markup=ikb_test1)
        await Test1.test1_answ5.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ5)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ5(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q6, reply_markup=ikb_test1)
        await Test1.test1_answ6.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ6)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ6(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q7, reply_markup=ikb_test1)
        await Test1.test1_answ7.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ7)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ7(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q8, reply_markup=ikb_test1)
        await Test1.test1_answ8.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ8)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ8(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q9, reply_markup=ikb_test1)
        await Test1.test1_answ9.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ9)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ9(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q10, reply_markup=ikb_test1)
        await Test1.test1_answ10.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ10)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ10(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q11, reply_markup=ikb_test1)
        await Test1.test1_answ11.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ11)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ11(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q12, reply_markup=ikb_test1)
        await Test1.test1_answ12.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ12)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ12(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q13, reply_markup=ikb_test1)
        await Test1.test1_answ13.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ13)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ13(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q14, reply_markup=ikb_test1)
        await Test1.test1_answ14.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ14)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test1.add_answ14(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test1.q15, reply_markup=ikb_test1)
        await Test1.test1_answ15.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test1.test1_answ15)
async def go_answ2(call: CallbackQuery, state: FSMContext):
    if call.data in '012345678':
        data_test1.add_answ15(call.from_user.id, call.data)
        data_test1.add_resalt(call.from_user.id)
        st = 'test1'
        dat_anketa.add_state(call.from_user.id, st)

        res = data_test1.get_resalt(call.from_user.id)[0][0]
        param1 = str()
        if res in range(15, 19):
            param1 += 'No sign of burnout'
        elif res in range(19, 33):
            param1 += 'Little sign of burnout'
        elif res in range(33, 50):
            param1 += 'At risk of burnout'
        elif res in range(50, 59):
            param1 += 'Severe risk of burnout'
        else:
            param1 += 'Very severe risk of burnout'

        await call.message.edit_text(
            text=f'<b>Burnout Self-Test</b>\nScore interpretations (No matter your score, pay attention to areas you ranked a 5)\nYour score: {res}\n{param1}',
            reply_markup=ikb_res2, parse_mode='html')
        await bot.send_message(id_grou,
                               text=f"Пользователь @{call.from_user.username} прошел тест1 набрав: {res}\nзавершил тест в {call.message.date.strftime('%H:%M:%S %d:%m:%Y')}")
        await state.finish()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


"""NEXT TEST"""

ikb_tst2 = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Go', callback_data='test2go2')).add(
    InlineKeyboardButton(text='Back to material', callback_data='material'))


@dp.callback_query_handler(text='test2')
async def go_test2(call: CallbackQuery):
    await call.message.answer(text=f'{stress_pre_text}', reply_markup=ikb_tst2, parse_mode='html')


@dp.callback_query_handler(text='test2go2')
async def go_test2(call: CallbackQuery):
    data_test2.add_user(call.from_user.id)
    data_test2.set_time_sub(call.from_user.id, call.message.date.strftime('%H:%M:%S_%d:%m:%Y'))
    await call.message.answer(text='<b>Instructions:</b> For each question, click the button that most applies',
                              parse_mode='html')
    await call.message.answer(text=test_questions.test2.q1, reply_markup=ikb_test2)
    await Test2.test2_answ1.set()


@dp.callback_query_handler(state=Test2.test2_answ1)
async def go_answ1(call: CallbackQuery):
    if call.data in '012345678':
        data_test2.add_answ1(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test2.q2, reply_markup=ikb_test2)
        await Test2.test2_answ2.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ2)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test2.add_answ2(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test2.q3, reply_markup=ikb_test2)
        await Test2.test2_answ3.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ3)
async def go_answ3(call: CallbackQuery):
    if call.data in '012345678':
        data_test2.add_answ3(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test2.q4, reply_markup=ikb_test2)
        await Test2.test2_answ4.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ4)
async def go_answ4(call: CallbackQuery):
    if call.data in '012345678':
        a = 0
        if call.data == 0:
            a += 4
        elif call.data == 1:
            a += 3
        elif call.data == 2:
            a += 2
        else:
            a += 1

        data_test2.add_answ4(call.from_user.id, a)
        await call.message.edit_text(text=test_questions.test2.q5, reply_markup=ikb_test2)
        await Test2.test2_answ5.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ5)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        a = 0
        if call.data == 0:
            a += 4
        elif call.data == 1:
            a += 3
        elif call.data == 2:
            a += 2
        else:
            a += 1
        data_test2.add_answ5(call.from_user.id, a)
        await call.message.edit_text(text=test_questions.test2.q6, reply_markup=ikb_test2)
        await Test2.test2_answ6.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ6)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test2.add_answ6(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test2.q7, reply_markup=ikb_test2)
        await Test2.test2_answ7.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ7)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        a = 0
        if call.data == 0:
            a += 4
        elif call.data == 1:
            a += 3
        elif call.data == 2:
            a += 2
        else:
            a += 1
        data_test2.add_answ7(call.from_user.id, a)
        await call.message.edit_text(text=test_questions.test2.q8, reply_markup=ikb_test2)
        await Test2.test2_answ8.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ8)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        a = 0
        if call.data == 0:
            a += 4
        elif call.data == 1:
            a += 3
        elif call.data == 2:
            a += 2
        else:
            a += 1
        data_test2.add_answ8(call.from_user.id, a)
        await call.message.edit_text(text=test_questions.test2.q9, reply_markup=ikb_test2)
        await Test2.test2_answ9.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ9)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test2.add_answ9(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test2.q10, reply_markup=ikb_test2)
        await Test2.test2_answ10.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test2.test2_answ10)
async def go_answ2(call: CallbackQuery, state: FSMContext):
    if call.data in '012345678':
        data_test2.add_answ10(call.from_user.id, call.data)
        data_test2.add_resalt(call.from_user.id)
        res = data_test2.get_resalt(call.from_user.id)[0][0]
        st = 'test2'
        dat_anketa.add_state(call.from_user.id, st)
        param1 = str()
        if res in range(0, 14):
            param1 += "Your level of stress is low. You're likely leading a fulfilling and largely stress-free life – good for you! Our practical materials and exersices will help you to keep low level of stress."
        elif res in range(14, 27):
            param1 += "Your level of stress is moderate. While moderate stress can be unpleasant and may cause some discomfort, it is generally manageable. However, if left unmanaged or if it persists over a prolonged period of time, moderate stress can lead to more severe levels of stress and potentially to health problems such as anxiety, depression, and physical illness."
        else:
            param1 += "Your level of stress is high. High levels of stress can have a significant impact on your physical and mental health, and can lead to a range of symptoms and health problems, such as anxiety, depression, high blood pressure, heart disease, sleep disorders, digestive problems, and weakened immune function. It is possible to reduce stress levels and improve overall well-being. We will work on this together!"
        await call.message.answer(text=f'<b>Your score: {res}</b>\n{param1}', reply_markup=ikb_res3, parse_mode='html')
        await bot.send_message(id_grou,
                               text=f"Пользователь @{call.from_user.username} прошел тест2 набрав: {res}\nзавершил тест в {call.message.date.strftime('%H:%M:%S %d:%m:%Y')}")
        await state.finish()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


"""NEXT STEP 3333333"""
ikb_tst3 = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Go', callback_data='test3go3')).add(
    InlineKeyboardButton(text='Back to material', callback_data='material'))


@dp.callback_query_handler(text='test3')
async def go_test3(call: CallbackQuery):
    await call.message.answer(text=f"{pain_test}", reply_markup=ikb_tst3, parse_mode='html')


@dp.callback_query_handler(text='test3go3')
async def go_test3(call: CallbackQuery):
    data_test3.add_user(call.from_user.id)
    data_test3.set_time_sub(call.from_user.id, call.message.date.strftime('%H:%M:%S_%d:%m:%Y'))
    await call.message.answer(text='Instructions: For each question, click the button that most applies.',
                              parse_mode='html')
    await call.message.answer(text=test_questions.test3.q1, reply_markup=ikb_test3)
    await Test3.test3_answ1.set()


@dp.callback_query_handler(state=Test3.test3_answ1)
async def go_answ1(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ1(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q2, reply_markup=ikb_test3)
        await Test3.test3_answ2.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ2)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ2(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q3, reply_markup=ikb_test3)
        await Test3.test3_answ3.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ3)
async def go_answ3(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ3(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q4, reply_markup=ikb_test3)
        await Test3.test3_answ4.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ4)
async def go_answ4(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ4(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q5, reply_markup=ikb_test3)
        await Test3.test3_answ5.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ5)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ5(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q6, reply_markup=ikb_test3)
        await Test3.test3_answ6.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ6)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ6(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q7, reply_markup=ikb_test3)
        await Test3.test3_answ7.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ7)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ7(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q8, reply_markup=ikb_test3)
        await Test3.test3_answ8.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ8)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ8(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q9, reply_markup=ikb_test3)
        await Test3.test3_answ9.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ9)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ9(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q10, reply_markup=ikb_test3)
        await Test3.test3_answ10.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ10)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ10(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q11, reply_markup=ikb_test3)
        await Test3.test3_answ11.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ11)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ11(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q12, reply_markup=ikb_test3)
        await Test3.test3_answ12.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ12)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ12(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q13, reply_markup=ikb_test3)
        await Test3.test3_answ13.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ13)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ13(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q14, reply_markup=ikb_test3)
        await Test3.test3_answ14.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ14)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ14(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q15, reply_markup=ikb_test3)
        await Test3.test3_answ15.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ15)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ15(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q16, reply_markup=ikb_test3)
        await Test3.test3_answ16.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ16)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ16(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q17, reply_markup=ikb_test3)
        await Test3.test3_answ17.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ17)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ17(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q18, reply_markup=ikb_test3)
        await Test3.test3_answ18.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ18)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ18(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q19, reply_markup=ikb_test3)
        await Test3.test3_answ19.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ19)
async def go_answ2(call: CallbackQuery):
    if call.data in '012345678':
        data_test3.add_answ19(call.from_user.id, call.data)
        await call.message.edit_text(text=test_questions.test3.q20, reply_markup=ikb_test3)
        await Test3.test3_answ20.set()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(state=Test3.test3_answ20)
async def go_answ2(call: CallbackQuery, state: FSMContext):
    if call.data in '012345678':
        data_test3.add_answ20(call.from_user.id, call.data)
        data_test3.add_resalt(call.from_user.id)
        st = 'test3'
        dat_anketa.add_state(call.from_user.id, st)
        res = data_test3.get_resalt(call.from_user.id)[0][0]
        await call.message.edit_text(
            text=f'<b>THE QUEBEC BACK PAIN DISABILITY SCALE (QBPDS)</b>\nYour score is {res}.\nSitting in the office for prolonged periods of time can have negative effects on back pain. We will offer simple exercises which you can do just at your desk. Try to do at least some of them every day. In a month we will ask you to take this test again and we hope you will see changes.',
            reply_markup=ikb_material, parse_mode='html')
        await bot.send_message(id_grou,
                               text=f"Пользователь @{call.from_user.username} прошел тест3 набрав: {res}\nзавершил тест в {call.message.date.strftime('%H:%M:%S %d:%m:%Y')}")
        await state.finish()
    else:
        await call.answer(text='Need to finish the test', show_alert=True)


@dp.callback_query_handler(text='finish')
async def get_finish(call: CallbackQuery):
    res = data_test1.get_resalt(call.from_user.id)[0][0]
    param1 = str()
    if res in range(15, 19):
        param1 += 'No sign of burnout'
    elif res in range(19, 33):
        param1 += 'Little sign of burnout'
    elif res in range(33, 50):
        param1 += 'At risk of burnout'
    elif res in range(50, 59):
        param1 += 'Severe risk of burnout'
    else:
        param1 += 'Very severe risk of burnout'

    await call.message.answer(
        text=f'<b>Burnout Self-Test</b>\nScore interpretations (No matter your score, pay attention to areas you ranked a 5)\nYour score: {res}\n{param1}',
        parse_mode='html')

    res = data_test2.get_resalt(call.from_user.id)[0][0]
    param1 = str()
    if res in range(0, 14):
        param1 += "Your level of stress is low. You're likely leading a fulfilling and largely stress-free life – good for you! Our practical materials and exersices will help you to keep low level of stress."
    elif res in range(14, 27):
        param1 += "Your level of stress is moderate. While moderate stress can be unpleasant and may cause some discomfort, it is generally manageable. However, if left unmanaged or if it persists over a prolonged period of time, moderate stress can lead to more severe levels of stress and potentially to health problems such as anxiety, depression, and physical illness."
    else:
        param1 += "Your level of stress is high. High levels of stress can have a significant impact on your physical and mental health, and can lead to a range of symptoms and health problems, such as anxiety, depression, high blood pressure, heart disease, sleep disorders, digestive problems, and weakened immune function. It is possible to reduce stress levels and improve overall well-being. We will work on this together!"
    await call.message.answer(
        text=f'<b>PERCEIVED STRESS SCALE</b>\nOffice work can be demanding and stressful, and many office workers may experience stress as a result of their job. We will ask you to take a short test to find out your current level of stress. The questions in this scale ask you about your feelings and thoughts during the last month. In each case, you will be asked to indicate how often you felt or thought a certain way.\nYour score: {res}\n{param1}',
        parse_mode='html')

    res = data_test3.get_resalt(call.from_user.id)[0][0]
    await call.message.answer(
        text=f'<b>THE QUEBEC BACK PAIN DISABILITY SCALE (QBPDS)</b>\nYour score is {res}.\nSitting in the office for prolonged periods of time can have negative effects on back pain. We will offer simple exercises which you can do just at your desk. Try to do at least some of them every day. In a month we will ask you to take this test again and we hope you will see changes.',
        reply_markup=ikb_material, parse_mode='html')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
