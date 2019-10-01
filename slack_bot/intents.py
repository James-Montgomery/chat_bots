import inspect

greetings_list = [
    "hi",
    "hello",
    "aloha",
    "hola"
]

def toby_intent(message, sender_id, mention_id, bot_id):

    message = message.lower()

    if mention_id == bot_id:

        if any(substring in message for substring in greetings_list):
            return "Hello!"

        if "what can you do" in message:
            return "Whatever I want!"

        # default response
        default_response = inspect.cleandoc("""
        Hmmm...I don't understand. Try asking `@Toby What can you do?`
        """)
        return default_response.strip()

    return None
