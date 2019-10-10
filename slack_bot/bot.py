import os
import time
import re
import logging
from slackclient import SlackClient
from intents import toby_intent
from reminders import check_reminders

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logging.info("Begin Logging.")

class SlackBot(object):

    def __init__(self, slack_token=None, allowed_channels=None):
        if not slack_token:
            slack_token = os.environ['SLACK_TOKEN']
        self.slack_client = SlackClient(slack_token)
        self.allowed_channels = allowed_channels
        self._intent_defined = False

    def define_intent_ontology(self, find_response):
        self._find_response = find_response
        self._intent_defined = True

    def start(self):
        assert self._intent_defined, "Please define intent ontology before starting."

        if self.slack_client.rtm_connect(auto_reconnect=True):

            logger.info("Starter Bot connected and running!")
            bot_id = self.slack_client.api_call("auth.test")["user_id"]

            start = time.time()
            while True:
                message, sender_id, mention_id, channel = self._parse_messages(self.slack_client.rtm_read())

                if message:
                    if (self.allowed_channels is None) or (channel in self.allowed_channels):
                        response, user_name, icon_url = self._find_response(message, sender_id, mention_id, bot_id)
                        if response:
                            self.post_response(response, channel, user_name, icon_url)

                # check reminders
                reminder, channel = check_reminders(self.allowed_channels)
                if reminder:
                    self.post_response(reminder, channel)

                # check run times for debugging
                elapsed_time = time.time() - start
                logger.debug(elapsed_time)

                # delay to prevent spamming
                time.sleep(0.5)
        else:
            logger.error("Connection failed. Exception traceback printed above.")

    @staticmethod
    def _find_mentions(message_text):
        # Note
        # A static method does not have access to self
        # A property only has access to self and outputs a class attribute
        MENTION_REGEX = "^<@(|[WU].+?)>(.*)"
        matches = re.search(MENTION_REGEX, message_text)
        if matches:
            return matches.group(1), matches.group(2).strip()
        return None, None

    def _parse_messages(self, slack_events):
        # Note
        # A static method does not have access to self
        # A property only has access to self and outputs a class attribute
        for event in slack_events:
            logger.debug(event)
            # TODO: Fix to respond to all mentions not just the first mention found
            if event["type"] == "message" and not "subtype" in event:
                mention_id, message = self._find_mentions(event["text"])
                return message, event["user"], mention_id, event["channel"]
        return None, None, None, None

    def post_response(self, response, channel, username=None, icon_url=None):
        if icon_url and username:
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=response,
                username=username,
                icon_url=icon_url
            )
        else:
            self.slack_client.api_call(
                "chat.postMessage",
                channel=channel,
                text=response
            )
        logger.info("Message Sent.")

if __name__ == "__main__":
    bot = SlackBot(slack_token=None, allowed_channels=["CNWNQP678"])
    bot.define_intent_ontology(toby_intent)
    bot.start()
