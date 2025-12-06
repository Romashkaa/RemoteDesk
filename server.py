import telekit
import handlers
import config

telekit.Server(config.TOKEN).polling()