from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ikb_reg = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Go!", callback_data="mini_anketa"))    #кнопка анкетирования
ikb_res1 = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Assessment 1', callback_data='test1')).add(InlineKeyboardButton(text='Learning Materials',callback_data='material'))
ikb_res2 = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Assessment 2', callback_data='test2')).add(InlineKeyboardButton(text='Learning Materials',callback_data='material'))
ikb_res3 = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Assessment 3', callback_data='test3')).add(InlineKeyboardButton(text='Learning Materials',callback_data='material'))
ikb_material = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Learning Materials',callback_data='material'))


ikb_test1 = InlineKeyboardMarkup()
ikb_test1_answ1 = InlineKeyboardButton(text='Not At All', callback_data='1')
ikb_test1_answ2 = InlineKeyboardButton(text='Rarely', callback_data='2')
ikb_test1_answ3 = InlineKeyboardButton(text='Sometimes', callback_data='3')
ikb_test1_answ4 = InlineKeyboardButton(text='Often', callback_data='4')
ikb_test1_answ5 = InlineKeyboardButton(text='Very Often', callback_data='5')
ikb_test1.add(ikb_test1_answ1, ikb_test1_answ2, ikb_test1_answ3).add(ikb_test1_answ4, ikb_test1_answ5)


ikb_test2 = InlineKeyboardMarkup()
ikb_test2_answ1 = InlineKeyboardButton(text='Never', callback_data='0')
ikb_test2_answ2 = InlineKeyboardButton(text='Almost Never', callback_data='1')
ikb_test2_answ3 = InlineKeyboardButton(text='Sometimes', callback_data='2')
ikb_test2_answ4 = InlineKeyboardButton(text='Fairly Often', callback_data='3')
ikb_test2_answ5 = InlineKeyboardButton(text='Very Often', callback_data='4')
ikb_test2.add(ikb_test2_answ1, ikb_test2_answ2, ikb_test2_answ3).add(ikb_test2_answ4, ikb_test2_answ5)


ikb_test3 = InlineKeyboardMarkup()
ikb_test3_answ1 = InlineKeyboardButton(text='Not difficult at all', callback_data='0')
ikb_test3_answ2 = InlineKeyboardButton(text='Minimally difficult', callback_data='1')
ikb_test3_answ3 = InlineKeyboardButton(text='Somewhat difficult', callback_data='2')
ikb_test3_answ4 = InlineKeyboardButton(text='Fairly difficult', callback_data='3')
ikb_test3_answ5 = InlineKeyboardButton(text='Very difficult', callback_data='4')
ikb_test3_answ6 = InlineKeyboardButton(text='Unable to do', callback_data='5')
ikb_test3.add(ikb_test3_answ1, ikb_test3_answ2).add(ikb_test3_answ3, ikb_test3_answ4).add(ikb_test3_answ5, ikb_test3_answ6)

ikb_mat0 = InlineKeyboardMarkup()           # ПОЛНОЕ ПРОХОЖДЕНИЕ
ikb_mat01 = InlineKeyboardButton(text='DAY 1', callback_data='day1')
ikb_mat02 = InlineKeyboardButton(text='DAY 2', callback_data='day2')
ikb_mat03 = InlineKeyboardButton(text='DAY 3', callback_data='day3')
ikb_mat04 = InlineKeyboardButton(text='DAY 4', callback_data='day4')
ikb_mat0.add(ikb_mat01).add(ikb_mat02).add(ikb_mat03).add(ikb_mat04)

ikb_mat1 = InlineKeyboardMarkup()           # БЕЗ ОДНОГО ТЕСТА
ikb_mat11 = InlineKeyboardButton(text='DAY 1', callback_data='day1')
ikb_mat12 = InlineKeyboardButton(text='DAY 2', callback_data='day2')
ikb_mat13 = InlineKeyboardButton(text='DAY 3', callback_data='day3')
ikb_mat14 = InlineKeyboardButton(text='🔒DAY 4🔒', callback_data='need_test')
ikb_mat1t = InlineKeyboardButton(text='Tests', callback_data='test3')
ikb_mat1.add(ikb_mat11).add(ikb_mat12).add(ikb_mat13).add(ikb_mat14).add(ikb_mat1t)

ikb_mat2 = InlineKeyboardMarkup()           # БЕЗ ДВУХ ТЕСТОВ
ikb_mat21 = InlineKeyboardButton(text='DAY 1', callback_data='day1')
ikb_mat22 = InlineKeyboardButton(text='DAY 2', callback_data='day2')
ikb_mat23 = InlineKeyboardButton(text='🔒DAY 3🔒', callback_data='need_test')
ikb_mat24 = InlineKeyboardButton(text='🔒DAY 4🔒', callback_data='need_test')
ikb_mat2t = InlineKeyboardButton(text='Tests', callback_data='test2')
ikb_mat2.add(ikb_mat21).add(ikb_mat22).add(ikb_mat23).add(ikb_mat24).add(ikb_mat2t)

ikb_mat3 = InlineKeyboardMarkup()           # БЕЗ ТРЕХ ТЕСТОВ
ikb_mat31 = InlineKeyboardButton(text='DAY 1', callback_data='day1')
ikb_mat32 = InlineKeyboardButton(text='🔒DAY 2🔒', callback_data='need_test')
ikb_mat33 = InlineKeyboardButton(text='🔒DAY 3🔒', callback_data='need_test')
ikb_mat34 = InlineKeyboardButton(text='🔒DAY 4🔒', callback_data='need_test')
ikb_mat3t = InlineKeyboardButton(text='Test', callback_data='test1')
ikb_mat3.add(ikb_mat31).add(ikb_mat32).add(ikb_mat33).add(ikb_mat34).add(ikb_mat3t)

ikb_fin = InlineKeyboardMarkup().add(InlineKeyboardButton(text='Test results', callback_data='finish')).add(InlineKeyboardButton(text='Learning Materials',callback_data='material'))

