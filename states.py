from aiogram.dispatcher.filters.state import StatesGroup, State


class NewAnket(StatesGroup):
    step_reg = State()
    name = State()    # задаем first name
    lastname = State()     # задаем last name
    age = State()    # age
    weight = State()     # задаем weight
    height = State()     # задаем height
    confirm = State()    # подтверждаем, что всё верно
    finish = State()


class Test1(StatesGroup):
    test1_answ1 = State()  # вопрос 1
    test1_answ2 = State()  # задаем last name
    test1_answ3 = State()  # age
    test1_answ4 = State()  # задаем weight
    test1_answ5 = State()  # вопрос 5
    test1_answ6 = State()
    test1_answ7 = State()
    test1_answ8 = State()
    test1_answ9 = State()
    test1_answ10 = State()
    test1_answ11 = State()
    test1_answ12 = State()
    test1_answ13 = State()
    test1_answ14 = State()
    test1_answ15 = State()


class Test2(StatesGroup):
    test2_answ1 = State()  # вопрос 1
    test2_answ2 = State()  # задаем last name
    test2_answ3 = State()  # age
    test2_answ4 = State()  # задаем weight
    test2_answ5 = State()  # вопрос 5
    test2_answ6 = State()  # вопрос 1
    test2_answ7 = State()  # задаем last name
    test2_answ8 = State()  # age
    test2_answ9 = State()  # задаем weight
    test2_answ10 = State()  # вопрос 5


class Test3(StatesGroup):
    test3_answ1 = State()  # вопрос 1
    test3_answ2 = State()  # задаем last name
    test3_answ3 = State()  # age
    test3_answ4 = State()  # задаем weight
    test3_answ5 = State()  # вопрос 5
    test3_answ6 = State()  # вопрос 6
    test3_answ7 = State()
    test3_answ8 = State()
    test3_answ9 = State()
    test3_answ10 = State()
    test3_answ11 = State()
    test3_answ12 = State()
    test3_answ13 = State()
    test3_answ14 = State()
    test3_answ15 = State()
    test3_answ16 = State()
    test3_answ17 = State()
    test3_answ18 = State()
    test3_answ19 = State()
    test3_answ20 = State()
