import inspect

greetings_list = [
    "hi",
    "hello",
    "aloha",
    "hola"
]

def toby_intent(message, sender_id, mention_id, bot_id):

    response, user_name, icon_url = None, None, None
    message = message.lower()

    if mention_id == bot_id:

        if any(substring in message for substring in greetings_list):
            response = "Hello!"

        elif "what can you do" in message:
            response = "Whatever I want!"

        else:
            # default response
            default_response = inspect.cleandoc("""
            Hmmm...I don't understand. Try asking `@Toby What can you do?`
            """)
            response = default_response.strip()

    elif "Toby" in message:
        response = "...did someone mention my name?"

    return response, user_name, icon_url
