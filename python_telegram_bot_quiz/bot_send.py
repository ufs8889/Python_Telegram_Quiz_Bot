from make_quiz import *
from telegram import Bot, Poll
from telegram.ext import Updater, CommandHandler
import threading
import time
import schedule

# Replace 'YOUR_TOKEN_HERE' with your bot's token
TOKEN = '6201292411:AAER7Y4UlCHVFKx1Fuh6KMasWjYUtM8wYhg'

# Replace 'YOUR_CHANNEL_ID' with your channel's ID (including the '-' sign if it's a supergroup)
CHANNEL_ID = '-1002018568907'

def send_quiz(bot: Bot) -> None:
    i = 0
    while i < 5:
        random_question = get_random_question()
        question = random_question[1]
        right_answer = random_question[2]
        options = shuffle_answers(random_question[1:])
        
        # Calculate the total length of options
        total_length = sum(len(option) for option in options)
        
        if total_length <= 100:
            index_of_correct = options.index(right_answer)
            bot.send_poll(chat_id=CHANNEL_ID,
                          question=question,
                          options=options,
                          type=Poll.QUIZ,
                          correct_option_id=int(index_of_correct))
            i += 1  # Exit the loop if options are valid
        else:
            #print(f"Options length exceeds 100 characters. Choosing a new random question:{random_question}")
            continue

def start(update, context) -> None:
    send_quiz(context.bot)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Handler for the start command
    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    # Send the quiz immediately when the bot starts
    send_quiz(updater.bot)

    # Schedule sending quiz every morning at 10 AM in Tashkent time (GMT+5)
    schedule.every().day.at("10:00").do(send_quiz, updater.bot)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute for scheduled tasks

if __name__ == '__main__':
    main()
