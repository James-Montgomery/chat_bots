import os
import time
import re
import logging
from slackclient import SlackClient

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.info("Begin Logging.")

slack_client = SlackClient(os.environ['SLACK_TOKEN'])

################################################################################

def find_mentions(message_text):
    MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
    matches = re.search(MENTION_REGEX, message_text)
    if matches:
        return (matches.group(1), matches.group(2).strip())
    return None, None

def parse_messages(slack_events):
    for event in slack_events:
        logger.debug(event)
        # TODO: Fix to respond to all mentions not just the first mention found
        if event["type"] == "message" and not "subtype" in event:
            mention_id, message = find_mentions(event["text"])
            return message, event["user"], mention_id, event["channel"]
    return None, None, None, None

################################################################################

def find_response(message, sender_id, mention_id, bot_id):

    message = message.lower()

    if mention_id == bot_id:
        if "hi" in message:
            return "Hello!"

    else:
        return None

    return "I don't understand. Please try again."

def post_response(response, channel):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response
    )

################################################################################

if __name__ == "__main__":

    allowed_channels = ["CNWNQP678"]

    if slack_client.rtm_connect(with_team_state=False):

        logger.info("Starter Bot connected and running!")
        bot_id = slack_client.api_call("auth.test")["user_id"]

        while True:
            message, sender_id, mention_id, channel = parse_messages(slack_client.rtm_read())

            if message and (channel in allowed_channels):
                response = find_response(message, sender_id, mention_id, bot_id)
                if response:
                    post_response(response, channel)

            # delay to prevent spamming
            time.sleep(1)
    else:
        logger.error("Connection failed. Exception traceback printed above.")
