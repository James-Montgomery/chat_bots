import os
import time
import logging
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.info("Begin Logging.")

ACCESS_TOKEN = os.environ['FACEBOOK_TOKEN']
bot = Bot (ACCESS_TOKEN)

VERIFY_TOKEN = os.environ['FACEBOOK_VERIFY_TOKEN']
logging.info("Verification Token: {}".format(VERIFY_TOKEN))

@app.route("/", methods=['GET', 'POST'])
def receive_message():

    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            logger.info("Verified. Can take up to 15 minutes tom begine posting.")
            return request.args.get("hub.challenge")
        logger.error("Failed Verification.")
        return 'Invalid verification token'

    else:
       for event in request.get_json()['entry']:
          for message in event['messaging']:
            if message.get('message'):

                logger.debug(message)

                sender_id = message['sender']['id']

                message_text, attachment = None, False
                if message['message'].get('text'):
                    message_text = message['message'].get('text')
                if message['message'].get('attachments'):
                    attachment = True

                bot.send_text_message(sender_id, get_response(message_text, attachment))
                logger.info("Response Sent.")
                time.sleep(1)

    logger.info("Message Processed")
    return "Message Processed"

###############################################################################
# Intents
###############################################################################

def get_response(message_text, attachment):
    return "Hi!"

if __name__ == "__main__":
    app.run(debug=True)
