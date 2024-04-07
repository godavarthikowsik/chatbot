import random

def response(input_text):
    responses = {
        "hi": ["hello!!", "hi there!", "hey!", "Hi! How Do You Do?"],
        "how are you": ["Great! What about you?", "Doing good! How do you do?", "Pretty good! Thanks for asking"],
        "i am great": ["Sounds good! How can i help you today?"],
        "good": ["Sounds good! How can i help you today?"],
        "i am good": ["Sounds good! How can i help you today?"],
        "doing good": ["Sounds good! How can i help you today?"],
        "bye": ["Good bye! Have a great day!", "See you next time!"]
    }
    for key in responses:
        if input_text.lower() == key:
            return random.choice(responses[key])
    return "I am sorry.. I couldn't understand!"

print("Bot: Hello! Greetings of the day")
while True:
    user_input = input("You: ")
    res = response(user_input)
    print("Bot:",res)
    if user_input.lower()=="bye":
        break
