#__metaclass__ = type

from microsoftbotframework import MsBot
from tasks import *
import os

#bot = MsBot(port=int(os.environ['PORT']))
bot = MsBot(port=5000)
#bot = MsBot()
bot.add_process(echo_response)

if __name__ == '__main__':
    bot.run()