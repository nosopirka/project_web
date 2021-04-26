# - *- coding: utf- 8 - *-
from glob import glob
import logging
from random import choice
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

import settings
import functions

TOKEN = settings.API_KEY

# PROXY = {
#     'proxy_url': settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {
#         'username': settings.PROXY_USERNAME,
#         'password': settings.PROXY_PASSWORD
#     }
# }

commands = [
    "/start - начать диалог с ботом",
    "/help - подсказка по пользованию ботом, в которой содержатся все функции",
    "/count_sistem - функция для того, что переводить числа из одной системы счисления в другую",
    "/sequences - фунукция для того, чтобы расчитать сумму n первых членов арифметической или геометрической "
    "прогрессии",
    "/equation - функция для того, чтобы бот решил вам уравнение, которое может быть до 2ой степени",
    "/meme - функция после вызова которой бот скинет вам смешную картиночку",
    "/site - функция отправляет вам ссылку на наш вебсайт с дополнительной теорией по алгебре и геометрии"
]

for_cnt_sis = {
    "num": 0,
    "sis1": 0,
    "sis2": 0
}

for_seq = {
    "a1/b1": 0,
    "d/q": 0,
    "n": 0,
    "f": 0
}

sis_keys = [["арифметическая", "геометрическая"]]
markup_sis = ReplyKeyboardMarkup(sis_keys, one_time_keyboard=True)

mem_but = [["мем", "закрыть"]]
markup_mem = ReplyKeyboardMarkup(mem_but, one_time_keyboard=False)

logging.basicConfig(filename="bot.log", level=logging.INFO)


def cnt_sis(update, context):
    update.message.reply_text("Я умею переводить целые положительные числа из одной системы счисления в другую легко "
                              "и просто! (я могу перевести любое целое положительное число в (2ой - 10ой) "
                              "системе счисления в любую другую (так же от 2ой до 10ой))")
    update.message.reply_text("Вам нужная моя помощь в этом?")
    return 4


def cnt_sis1(update, context):
    if not update.message.text.isdigit():
        update.message.reply_text("Введите, пожалйста, в правильном формате: любое целое положительное число")
        return 1
    if int(update.message.text) != float(update.message.text):
        update.message.reply_text("Введите, пожалйста, в правильном формате: любое целое положительное число")
        return 1
    if int(update.message.text) < 0:
        update.message.reply_text("Введите, пожалйста, в правильном формате: любое целое положительное число")
        return 1
    for_cnt_sis["num"] = int(update.message.text)
    update.message.reply_text("Теперь введите в какой системе считсления оно находится(целое число от 2 до 10)")
    return 2


def cnt_sis2(update, context):
    if not update.message.text.isdigit():
        update.message.reply_text("Введите, пожалйста, систему счисления в правильном формате: целое число от 2 до 10")
        return 2
    if int(update.message.text) != float(update.message.text):
        update.message.reply_text("Введите, пожалйста, систему счисления в правильном формате: целое число от 2 до 10")
        return 2
    if not (1 < int(update.message.text) < 11):
        update.message.reply_text("Введите, пожалйста, систему счисления в правильном формате: целое число от 2 до 10")
        return 2
    for_cnt_sis["sis1"] = int(update.message.text)
    update.message.reply_text("А теперь введите в какую систему счисления вы хотите его перевести")
    return 3


def cnt_sis3(update, context):
    if not update.message.text.isdigit():
        update.message.reply_text("Введите, пожалйста систему счисления в правильном формате: целое число от 2 до 10")
        return 3
    if int(update.message.text) != float(update.message.text):
        update.message.reply_text("Введите, пожалйста систему счисления в правильном формате: целое число от 2 до 10")
        return 3
    if not (1 < int(update.message.text) < 11):
        update.message.reply_text("Введите, пожалйста систему счисления в правильном формате: целое число от 2 до 10")
        return 3
    for_cnt_sis["sis2"] = int(update.message.text)
    update.message.reply_text(str(for_cnt_sis["num"]) + " в " + str(for_cnt_sis["sis1"]) +
                              "ой системе счисления равно " + functions.perevod(for_cnt_sis) + " в " +
                              str(for_cnt_sis["sis2"]) + "ой системе счисления")
    return ConversationHandler.END


def cnt_sis4(update, context):
    if ("да" in update.message.text.lower() or "yes" in update.message.text.lower() or
        "of course" in update.message.text.lower() or "конечно" in update.message.text.lower()) \
            and ("не" not in update.message.text.lower() or "no" not in update.message.text.lower()):
        update.message.reply_text("Введите целое положительное число, которое хотите перевести:")
        return 1
    else:
        update.message.reply_text("Ну ладно, как пожелаете...")
        return ConversationHandler.END


def seq(update, context):
    update.message.reply_text("Могу посчитать сумму первых n членов геометрической прогрессии по её первому члену и"
                              " знаменателю прогрессии! Вам нужна моя помощь?")
    return 4


def seq1(update, context):
    if not update.message.text.isdigit():
        update.message.reply_text("Пожалуйста, введите первый член в правильном формате: число")
        return 1
    for_seq["a1/b1"] = float(update.message.text)
    if for_seq["f"]:
        update.message.reply_text("А теперь введите разность вашей арифметической прогрессии(число)")
    else:
        update.message.reply_text("А теперь введите знаменатель вашей геометрической прогрессии(число)")
    return 2


def seq2(update, context):
    if not update.message.text.isdigit():
        if for_seq["f"]:
            update.message.reply_text("Пожалуйста, введите разность вашей арифметической прогрессии "
                                      "в правильном формате: число")
        else:
            update.message.reply_text("Пожалуйста, введите знаменатель вашей геометрической прогрессии "
                                      "в правильном формате: число")
        return 2
    for_seq["d/q"] = float(update.message.text)
    if for_seq["f"]:
        update.message.reply_text("Ну и осталось ввести количесво членов в вашей фриметической прогрессии. "
                                  "Введите его(это должно быть целое неотрицательное число)")
    else:
        update.message.reply_text("Ну и осталось ввести количество членов в вашей геометрической прогрессии."
                                  "Введите его(это должно быть целое неотрицательное число)")
    return 3


def seq3(update, context):
    if not update.message.text.isdigit():
        update.message.reply_text("Пожалуйста, введите количество членов в правильном формате: "
                                  "целое неотрицательное ЧИСЛО")
    if int(update.message.text) != float(update.message.text):
        update.message.reply_text("Пожалуйста, введите количество членов в правильном формате: "
                                  "ЦЕЛОЕ неотрицательное число")
    if int(update.message.text) < 0:
        update.message.reply_text("Пожалуйста, введите количество членов в правильном формате: "
                                  "целое НЕОТРИЦАТЕЛЬНОЕ число")
    for_seq["n"] = int(update.message.text)
    if for_seq["f"]:
        update.message.reply_text("Сумма первых " + str(for_seq["n"]) + " членов вашей арифметической прогресии равна "
                                  + str(functions.sequences(for_seq)))
    else:
        update.message.reply_text("Сумма первых " + str(for_seq["n"]) + " членов вашей геометрической прогресии равна "
                                  + str(functions.sequences(for_seq)))
    return ConversationHandler.END


def seq4(update, context):
    if ("да" in update.message.text.lower() or "yes" in update.message.text.lower() or
        "of course" in update.message.text.lower() or "конечно" in update.message.text.lower()) \
            and ("не" not in update.message.text.lower() or "no" not in update.message.text.lower()):
        update.message.reply_text("А теперь выберите для какой прогрессии вы хотите посчитать сумму первых n членов",
                                  reply_markup=markup_sis)
        return 5
    else:
        update.message.reply_text("Ну ладно, как пожелаете...")
        return ConversationHandler.END


def seq5(update, context):
    if update.message.text.lower() == "арифметическая":
        update.message.reply_text("Теперь введите первый член вашей арифметической прогрессии (число)",
                                  reply_markup=ReplyKeyboardRemove())
        for_seq["f"] = 1
        return 1
    elif update.message.text.lower() == "геометрическая":
        update.message.reply_text("Теперь введите первый член вашей геометрической прогрессии (число)",
                                  reply_markup=ReplyKeyboardRemove())
        for_seq["f"] = 0
        return 1
    else:
        update.message.reply_text("Я не понял, какую прогрессию вы выбрали, пожалуйста выберите ещё раз",
                                  reply_markup= markup_sis)
        return 5


def eq(update, context):
    update.message.reply_text("О, вы хочешь чтобы я решил для тебя уравнение? Не так ли?")
    return 1


def eq1(update, context):
    if ("да" in update.message.text.lower() or "yes" in update.message.text.lower() or
        "of course" in update.message.text.lower() or "конечно" in update.message.text.lower()) \
            and ("не" not in update.message.text.lower() or "no" not in update.message.text.lower()):
        update.message.reply_text("Ну тогда введите уравнение, которое вы хотите, чтобы я решил. Но учтите,"
                                  " я могу понять уравние, только по шаблону, который выглядит так:\n"
                                  "ax^2 + bx + c, где:\n"
                                  "a и b - коэфиценты\n"
                                  "c - свободный член\n"
                                  "Уравнения степени выше 2ой я ещё не умею корректно решать. Поэтому если вы "
                                  "будете вводить уравнение не так, как я попросил, то я либо скажу вам об этом, "
                                  "либо решу его неправильно, поэтому заранее, извиняюсь.")
        return 2
    else:
        update.message.reply_text("Ну ладно, как пожелаете...")
        return ConversationHandler.END


def eq2(update, context):
    urav = update.message.text
    ot = functions.solving(urav)
    if "%" not in ot:
        if ot[0] == "F":
            update.message.reply_text("Уравнение верно для любого x")
        elif ot[0] == "N":
            update.message.reply_text("У вашего уравнения нет решений")
        else:
            update.message.reply_text("Вы ввели уравнение в неправильном формате")
    else:
        if ot.split("%")[0] == ot.split("%")[1]:
            update.message.reply_text("Ваше уравнение имеет один корень: " + ot.split("%")[0])
        else:
            update.message.reply_text("Корни вашего уравнение это:" + ot.split("%")[0] + " и " + ot.split("%")[1])
    return ConversationHandler.END


def send_meme(update, context):
    meme_list = glob("images/mem*.jp*g")
    meme_pic = choice(meme_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(meme_pic, "rb"))


def cmd(update, context):
    cmds = commands[0]
    for x in commands[1:]:
        cmds += "\n"
        cmds += x
    update.message.reply_text(cmds)


def stop(update, context):
    update.message.reply_text("ОК")
    return ConversationHandler.END


def close_but(update, context):
    update.message.reply_text("Закрываю", reply_markup = ReplyKeyboardRemove())


def send_website(update, context):
    update.message.reply_text("А вот наш сайт, на котором вы можете найти теорию по алгебре и геометрии, котора вам "
                              "обязательно поможет. Так же вы можете ознакомиться с его функционалом и получить "
                              "удовольствие от пользования им. \n"
                              "НАДО БУДЕТ СЮДЫ ССЫЛКУ ВСТАВИТЬ")


def start(update, context):
    update.message.reply_text(
        "Привет! Я колобот. Я не малое умею. Также я бот-математик. Я умею переводить числа из одной системы счисления "
        "в другую. Ещё я умею считать суммы первых скольки-то членов арифметической или геометрической прогрессий. "
        "А самое интересное, что я умею, это решение уравнений до 2ой степени включительно!")
    update.message.reply_text("Хоть я и умный математик, но у меня так же есть чувство юмора и у меня есть немного "
                              "мемов для вас. \n Для большей информации используйте функцию /help",
                              reply_markup=markup_mem)


def help(update, context):
    update.message.reply_text(
        "Если вам интересно узнать мои способности и функции, то напишите /commands, чтобы увидеть список моих команд")


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    count_sis = ConversationHandler(
        entry_points=[CommandHandler('count_sistem', cnt_sis)],

        states={

            1: [MessageHandler(Filters.text, cnt_sis1, pass_user_data=True)],

            2: [MessageHandler(Filters.text, cnt_sis2, pass_user_data=True)],

            3: [MessageHandler(Filters.text, cnt_sis3, pass_user_data=True)],

            4: [MessageHandler(Filters.text, cnt_sis4, pass_user_data=True)]
        },

        fallbacks=[CommandHandler("stop", stop)]
    )

    sequences = ConversationHandler(
        entry_points=[CommandHandler('sequences', seq)],

        states={

            1: [MessageHandler(Filters.text, seq1, pass_user_data=True)],

            2: [MessageHandler(Filters.text, seq2, pass_user_data=True)],

            3: [MessageHandler(Filters.text, seq3, pass_user_data=True)],

            4: [MessageHandler(Filters.text, seq4, pass_user_data=True)],

            5: [MessageHandler(Filters.text, seq5, pass_user_data=True)]
        },

        fallbacks=[CommandHandler("stop", stop)]
    )

    equation = ConversationHandler(
        entry_points=[CommandHandler('equation', eq)],

        states= {
            1: [MessageHandler(Filters.text, eq1, pass_user_data=True)],

            2: [MessageHandler(Filters.text, eq2, pass_user_data=True)]
        },

        fallbacks=[CommandHandler("stop", stop)]
    )

    dp.add_handler(count_sis)
    dp.add_handler(sequences)
    dp.add_handler(equation)

    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("commands", cmd))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("meme", send_meme))
    dp.add_handler(CommandHandler("site", send_website))
    dp.add_handler(MessageHandler(Filters.regex("^закрыть$"), close_but))
    dp.add_handler(MessageHandler(Filters.regex("^мем$"), send_meme))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()