#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.HELP_USER,
            parse_mode="html",
            disable_web_page_preview=True,
            reply_to_message_id=update.message_id
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
        # logger.info(update)
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.START_TEXT.format(update.from_user.first_name),
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤴My Master", url="https://t.me/The_Ghost_Hunter",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Group", url="https://t.me/helpcenterbot1"
                    ),
                    InlineKeyboardButton(
                        "📺 Star Wolrd Entertainment", url="https://t.me/fire_world_entertainment"
                    ),
                    InlineKeyboardButton(
                    text="💾 Source Code", url="https://github.com/HuntingBots/CloudPlus_URLUploader/")], 
                    ] 
               ),
            
            reply_to_message_id=update.message_id
        )
