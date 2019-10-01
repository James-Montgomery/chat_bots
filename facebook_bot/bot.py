import os
import random
import time
from flask import Flask, request
from pymessenger.bot import Bot
import logging

app = Flask(__name__)

logger = logging.getLogger()
#logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)

logging.info("Begin Logging.")

ACCESS_TOKEN = os.environ['FACEBOOK_TOKEN']
VERIFY_TOKEN = os.environ['FACEBOOK_VERIFY_TOKEN']
bot = Bot (ACCESS_TOKEN)

logging.info("Verify Token: {}".format(VERIFY_TOKEN))

##We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():

    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            logger.info("Verified.")
            return request.args.get("hub.challenge")
        logger.error("Failed Verification.")
        return 'Invalid verification token'

    else:
       for event in request.get_json()['entry']:
          for message in event['messaging']:
            if message.get('message'):

                recipient_id = message['sender']['id']

                if message['message'].get('text'):
                    send_message(recipient_id, get_message())

                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    send_message(recipient_id, get_message())

                time.sleep(1)

    return "Message Processed"

def get_message():
    return random.choice(["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"])

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run(debug=True)
