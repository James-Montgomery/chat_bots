
sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]

def get_message():
    return random.choice(sample_responses)

def send_response(bot, recipient_id):
    # send response to message
    bot.send_text_message(recipient_id, "Hi!")
    return "success"
