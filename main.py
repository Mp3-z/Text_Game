import config
import logging
import asyncio
import aiogram
from aiogram import Bot, Dispatcher, F
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkugh, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from base import SQL# подключение класса SQLighter из файла base
from aiogram.types import FSInputFile
from aiogram.client.session.aiohttp import AiohttpSession

db = SQL('db.db')  # соединение с БД
session = AiohttpSession(proxy='http://proxy.server:3128') # в proxy указан прокси сервер pythonanywhere, он нужен для подключения
bot = Bot(token=config.TOKEN, session=session)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


buttons = [
        [InlineKeyboardButton(text="Да", callback_data="start")]
    ]
kb_start = InlineKeyboardMarkup(inline_keyboard=buttons)


inspect1 = [
        [InlineKeyboardButton(text="Осмотреться", callback_data="inspect1")]
    ]
kb_inspect1 = InlineKeyboardMarkup(inline_keyboard=inspect1)


room1 = [
        [InlineKeyboardButton(text="Открыть дверь", callback_data="open the dor_room1")],
        [InlineKeyboardButton(text="Осмотреть письменный стол", callback_data="inspect the desk_room1")],
        [InlineKeyboardButton(text="Осмотреть шкаф", callback_data="inspect the bookcase_room1")]
    ]
kb_room1 = InlineKeyboardMarkup(inline_keyboard=room1)


bookcase1 = [
        [InlineKeyboardButton(text="Вернуться обратно", callback_data="get back_room1")],
        [InlineKeyboardButton(text="Толкнуть шкаф", callback_data="push the bookcase_room1")]
    ]

kb_bookcase1 = InlineKeyboardMarkup(inline_keyboard=bookcase1)



Hallway1 = [
        [InlineKeyboardButton(text="Комната номер 1", callback_data="room_number_1")],
        [InlineKeyboardButton(text="Комната номер 2", callback_data="room_number_2")],
        [InlineKeyboardButton(text="Комната номер 3", callback_data="room_number_3")],
        [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
        [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
    ]


ropes = [
        [InlineKeyboardButton(text="Перерезать верёвки", callback_data="knife")],
        [InlineKeyboardButton(text="Перерубить верёвки", callback_data="axe")],
    ]
kb_ropes = InlineKeyboardMarkup(inline_keyboard=ropes)

into = [
        [InlineKeyboardButton(text="Шагнуть внутрь", callback_data="into")]
    ]
kb_into = InlineKeyboardMarkup(inline_keyboard=into)



kb_Hallway1 = InlineKeyboardMarkup(inline_keyboard=Hallway1)



# @dp.message(F.photo)#фотографии
# async def photo(message):
#     global name, price
#     id = message.from_user.id
#     status = db.get_status(id)
#     if status == 7:
#         db.add_item(name, price)
#         id_item = db.get_id_item(name)
#         await message.answer("Товар успешно добавлен!")
#         await bot.download(message.photo[-1], destination=f"images/{id_item}.png")


@dp.message()
async def start(message):
    global axe
    id = message.from_user.id
    if not db.user_exist(id):
        db.add_user(id)
    status = db.get_status(id)
    if status == 0:
        await message.answer("Привет. Хочешь начать игру?", reply_markup=kb_start)
        return
    if status == 1:
        hallway1 = db.get_hallway1(id)
        hallway2 = db.get_hallway2(id)
        hallway3 = db.get_hallway3(id)
        print(hallway1, hallway2, hallway3)



        if hallway1 == 1 and hallway2 == 1 and hallway3 == 1:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 1", callback_data="room_number_1")],
                [InlineKeyboardButton(text="Комната номер 2", callback_data="room_number_2")],
                [InlineKeyboardButton(text="Комната номер 3", callback_data="room_number_3")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 2 and hallway2 == 1 and hallway3 == 1:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 2", callback_data="room_number_2")],
                [InlineKeyboardButton(text="Комната номер 3", callback_data="room_number_3")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 1 and hallway2 == 2 and hallway3 == 1:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 1", callback_data="room_number_1")],
                [InlineKeyboardButton(text="Комната номер 3", callback_data="room_number_3")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 2 and hallway2 == 2 and hallway3 == 1:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 3", callback_data="room_number_3")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 1 and hallway2 == 1 and hallway3 == 2:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 1", callback_data="room_number_1")],
                [InlineKeyboardButton(text="Комната номер 2", callback_data="room number 2")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 1 and hallway2 == 2 and hallway3 == 2:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 1", callback_data="room_number_1")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 2 and hallway2 == 1 and hallway3 == 2:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 2", callback_data="room_number_2")],
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]
        if hallway1 == 2 and hallway2 == 2 and hallway3 == 2:
            Hallway1 = [
                [InlineKeyboardButton(text="Комната номер 4", callback_data="room_number_4")],
                [InlineKeyboardButton(text="Комната без номера", callback_data="room_number_0")],
            ]

        kb_Hallway1 = InlineKeyboardMarkup(inline_keyboard=Hallway1)

        await message.answer("Что дальше?", reply_markup=kb_Hallway1)
        return
    if status == 2:
        await message.answer("Там что-то странное.", reply_markup=kb_into)
        return





@dp.callback_query()
async def start_call(call):
    id = call.from_user.id
    if not db.user_exist(id):
        db.add_user(id)
    status = db.get_status(id)
    if call.data == "start":
        await call.message.answer("Вы с командой направлялись на заказ в виде отпугивания кобольтов, но по пути через лес в ваших глазах резко потемнело и сейчас вы находитесь в какой-то пыльной тусклой комнате, от которой не веет ни граммом симпатии.", reply_markup=kb_inspect1)
        return
    if call.data == "inspect1":
        await call.message.answer("Вы видите металлическую дверь, стены цельные, неровные и каменные, словно выдолбленные в скале. Обернувшись, вы увидели старый письменный стол и рядом стоящий книжный шкаф. Книгами вас обделили. \n Что вы будете делать?", reply_markup=kb_room1)
    if call.data == "open the dor_room1":
        await call.message.answer("Вы тянете металлическую дверь на себя, но безуспешно. Вы пытаетесь её толкать, но это всё так же не приносит результата. Поняв, что эта дверь - неприступный барьер для вас, вы возвращаетесь обратно в центр комнаты.", reply_markup=kb_room1)
    if call.data == "inspect the desk_room1":
        await call.message.answer("На столе ничего нет. Под столом тоже. Пусто. Проведя по нему рукой, вы смахнули большой слой пыли. \n Давно тут никого не было. ", reply_markup=kb_room1)
    if call.data == "inspect the bookcase_room1":
        await call.message.answer("Вы подошли к шкафу. Простой шкаф без единой книги, с закрытыми дверцами нижних отсеков. Но когда вы его осматривали, то заметили, что этот шкаф довольно шаток и качается из стороны в сторону.", reply_markup=kb_bookcase1)
    if call.data == "get back_room1":
        await call.message.answer ("Вы вернулись в центр комнаты и сели на пол.", reply_markup=kb_room1)
    if call.data == "push the bookcase_room1":
        await call.message.answer("Вы толкаете шкаф. Он с грохотом падает, поднимая вверх большое облако пыли. После падения дверцы сломались и упали на пол, а за ними выпала старая медная утварь, в которой скрывался походный топорик.\n За шкафом был мелкий тоннель. Вы не знаете куда он приведёт, но другого выхода, кроме как лезть туда вы не видите. Когда вы закончили ползти, перед вами предстал коридор с пятью комнатами. По две по бокам и одна напротив вас. Старые дверь по бокам от вас были пронумерованы уже потёртыми цифрами от одного, до четырёх, а дверь на против вас была без какого либо номера.", reply_markup=kb_Hallway1)
        db.update_status(id, 1)
        db.update_axe(id, 1)
        return

    if call.data == "room_number_1":
        await call.message.answer("Дверь заперта. Замка нет, а ручку кто-то вовсе открутил.", reply_markup=kb_Hallway1)
        db.update_hallway1(id, 2)
        return
    if call.data == "room_number_2":
        await call.message.answer("Дверь заперта. Замка нет, а ручку кто-то вовсе открутил.", reply_markup=kb_Hallway1)
        db.update_hallway2(id, 2)
        return
    if call.data == "room_number_3":
        await call.message.answer("Вы видите шкафы с какой-то одеждой. Всего три шкафа у трёх разных стен. Обыскав все куртки, плащи и остальную одежду, вы нашли складной нож и набор скрепок. После этого вы вернулись обратно.", reply_markup=kb_Hallway1)
        db.update_hallway3(id, 2)
        db.update_knife(id, 1)
        db.update_paperclip(id, 1)
        return
    if call.data == "room_number_4":
        paperclip = db.get_paperclip(id)
        print(paperclip)
        if paperclip == 0:
            await call.message.answer("Дверь заперта. Вы от безисходности вернулись обратно.")
        elif paperclip == 1:
            print(paperclip)
            await call.message.answer("Вы открываете дверь при помощи пары скрепок из коробки. Вы потратили все скрепки, но с последней попытки открыли замок и дверь со скрипом распахнулась. \nВ пустой комнате вы увидели одиноко стоящий сундук, способный любого заставить захотеть его открыть, благодаря своему красивому виду. Сундук перевязан верёвками. Развязать такое не получится, но можно разрезать или разрубить.",reply_markup=kb_ropes)
            return
    if call.data == "knife":
        await call.message.answer("Вы режете верёвки ножом, но к сожалению он ломается, когда вы пытаетесь сложить его обратно. Ну а что ещё ожидать от ножа, которому не весть сколько лет. Однако у вас есть топорик. Вы уже хотите открыть сундук, но видите что-то, подозрительно похожее на клыки. Отскачив в сторону, вы поняли, что перед вами мимик. Вы не разу с такими не сталкивались и бой с сундуком для вас будет чем-то новым и явно незабываемым. \nДа уж. Сундук не выстоял против топора и проиграл вам бой. \nВсё-таки внутри сундука нашёлся ключ. Вы сразу же, сломя голову побежали проверять, подходит ли он к двери без номера. Дрожащими после боя руками вы вставляете ключ в скважину и открываете тяжёлую, скрипящую дверь.", reply_markup=kb_into)
        db.update_status(id, 2)
        return
    if call.data == "axe":
        await call.message.answer("Вы рубите веревки, во время чего старый топорик ломается. Сундуком оказался мимик и он был очень не доволен ударами топора. У вас остался нож, но он ничем не помог. \n И так, вас съел сундук. Незавидная судьба.")
        db.update_status(id, 0)
        db.update_knife(id, 0)
        db.update_paperclip(id, 0)
        db.update_axe(id, 0)
        db.update_hallway1(id, 1)
        db.update_hallway2(id, 1)
        db.update_hallway3(id, 1)
        await call.message.answer("Напишите: Старт")
        return
    if call.data == "room_number_0":
        await call.message.answer ("Тяжёлая металлическая дверь, поторпевшая ржавчину. Дверь заперта и вы возвращаетесь обратно. Хотя, мысль о том, что бы вернуться и попробовать её открыть нова или хотя бы вновь подёргать за ручку вас не покидает.")
    if call.data == "into":
        await call.message.answer("В туской комнате, обвешанной зеркалами и картинами по центру стоит письменный стол. На этом столе, среди книг и бумаг лежит большой и ржавый ключ. Схватив этот ключ, вы бежите обратно, через дверь, коридор, дыру за шкафом. Добежав до комнаты, где вы очнулись, и вставив ключ в скважину, его получилось провернуть и открыть дверь. Наконец вы открываете тяжёлую дверь и видите перед собой деревянную доску, через щели которой просачиваются лучи солнца. Толкнув доску, вы выходите наружу, после чего вас сильно слепит солнце. Наконец, вы покинули это место. Но остался еще один вопрос. \nГде вы? \n...")
        db.update_status(id, 0)
        db.update_knife(id, 0)
        db.update_paperclip(id,0)
        db.update_axe(id,0)
        db.update_hallway1(id, 1)
        db.update_hallway2(id, 1)
        db.update_hallway3(id, 1)
        await call.message.answer("Напишите: Старт")






async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
