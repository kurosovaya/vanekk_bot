import telebot

from flask import Flask, request
import os
import time
import markovify

TOKEN = os.environ["TOKEN"]
bot = telebot.AsyncTeleBot(TOKEN)
server = Flask(__name__)

prohibited_stickers = ("AgADDgADxk5iIA",)
bad_sticker = "CAACAgIAAxkBAANFYVighWF44_O1hkQlo_8QJSnYKJUAAg4AA8ZOYiAVktAJXEArfiEE"
good_sticker = "CAACAgIAAxkBAANXYVi_oJqE_JrrKVh1fol8yID6CUgAAnIBAAI0-xcGv6CkXEKqmUQhBA"

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
with open("vanekkk_sentences.txt") as f:
    vanekk_messages = f.read()
with open("pretentious_phrases.txt") as f:
    fashion_phrases = f.read()
with open("quotes_about_nationalism.txt") as f:
    some_shit = f.read()
with open("Собачье сердце. Михаил Булгаков.txt") as f:
    classic = f.read()

vanekkk_vocabulary = markovify.Text(vanekk_messages)
fashion_vocabulary = markovify.Text(fashion_phrases)
shit_vocabulary = markovify.Text(some_shit)
classic_vocabulary = markovify.Text(classic)

combined_mode = markovify.combine([vanekkk_vocabulary, fashion_vocabulary, shit_vocabulary, classic_vocabulary],
                                  [1, 1, 1.5, 0.7])
combined_mode = combined_mode.compile()


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Я встал в 8 потому что пара")


@bot.message_handler(commands=["what_he_loves_to_suck"])
def reply_suck(message):
    bot.send_sticker(message.chat.id, bad_sticker)


@bot.message_handler(commands=["make_sentence"])
def make_sentence(message):
    txt = None
    while txt is None:
        txt = combined_mode.make_short_sentence(1000, 20, test_output=False)
    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=["timoha_spam"])
def reply_suck(message):
    for i in range(15):
        bot.send_message(message.chat.id, "Жэка гей")
        time.sleep(1)


@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, "Всем привет с вами бендер")
    elif message.text.lower() == "хочу сосать":
        bot.send_sticker(message.chat.id, bad_sticker)
    elif message.text.lower() == "пока":
        bot.send_message(message.chat.id, "Какой же ты еблан")


@bot.message_handler(content_types=["sticker"])
def send_sticker(message):
    if message.sticker.file_unique_id in prohibited_stickers:
        bot.delete_message(message.chat.id, message.message_id)
        sent_msg = bot.send_sticker(message.chat.id, good_sticker)
        time.sleep(8)
        bot.delete_message(sent_msg.result.chat.id, sent_msg.result.message_id)


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "Йух", 200


@server.route("/", methods=["GET"])
def webhook():
    bot.remove_webhook()
    bot.set_webhook("https://vanekk-bot.herokuapp.com/" + TOKEN)
    return "Хуй", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
