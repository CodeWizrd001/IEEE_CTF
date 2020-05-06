from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
import logging
import os
import sys
from telegram.ext.dispatcher import run_async
updater=Updater(token='1186964408:AAFk8YGpDGQdhXPdQ9mygft8jrvHNWQB4Ls',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def start(update,context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text="Huraken's Personal KickAss bot")
@run_async
def dl(update, context):
    p=update.message.text
    if(p=='HTB{v3rsi0n_c0ntr0l_am_I_right?}')  :
        ans=str('SlU1VDFOUjAxTDRORA==')
        print("Solving:RicknMorty question")  
        context.bot.send_message(chat_id=update.effective_chat.id, text="*nervous laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ahh FINE! Here you go ...\n Part 2 of Rick and Morty")
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    elif (p=='HTB{B33P5_4R3_4_T3L3GR4M_B0T}'):
        ans=str('anU1dDFucjAxbDRuZA==')
        print("Solving:RicknMorty question")  
        context.bot.send_message(chat_id=update.effective_chat.id, text="*nervous laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ahh FINE! Here you go ...\nPart 1 of Rick and Morty")
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    elif (p=='HTB{ju5t1nr01l4ndJU5T1NR01L4ND}'):
        ans=str('aWVlZXtuM3YzcnIxY2sxbmdtMHJ0eX0=')
        print("Solved:RicknMorty question")  
        context.bot.send_message(chat_id=update.effective_chat.id, text="*nervous laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ahh FINE! Here you go ...\nThe final flag of Rick and Morty")
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
        
    elif (p=='HTB{B4BY_R3V_TH4TS_EZ}'):
        ans=str('VV8wVUdIVF9UMF9LTjBXXzFUX1VfUzRXX1RIM19NMFYxMw==')
        print("Solved:SUBARU WRX question")  
        context.bot.send_message(chat_id=update.effective_chat.id, text="*nervous laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ahh FINE! Here you go ...\nPart 2 of Red Subaru WRX")
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    elif (p=='HTB{QR_!snt_d34d}'):
        ans=str('V0gxQ0hfMTVfQjRCWTVfRjRWX1MwTkc=')
        print("Solved:SUBARU WRX question")  
        context.bot.send_message(chat_id=update.effective_chat.id, text="*nervous laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ahh FINE! Here you go ...\nPart 1 of Red Subaru WRX")
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    elif (p=='HTB{WH1CH_15_B4BY5_F4V_S0NGU_0UGHT_T0_KN0W_1T_U_S4W_TH3_M0V13}'):
        ans=str('aWVlZXtCUjFHSFQzTl9SMENLXzE1X1RIM19CMzVUfQ==')
        print("Solved:Subaru wrx question")  
        context.bot.send_message(chat_id=update.effective_chat.id, text="*nervous laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ahh FINE! Here you go ...\nThe final flag of Red Subaru WRX")
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)    
    else :
        context.bot.send_message(chat_id=update.effective_chat.id, text="*sarcastic laughter*")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Whoopsie Daisy ?!!")
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, dl)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()