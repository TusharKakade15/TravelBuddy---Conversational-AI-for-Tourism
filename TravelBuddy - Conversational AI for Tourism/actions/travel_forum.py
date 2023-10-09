import openai



def chatbot(input):
    openai.api_key = "API KEY"

    messages = [
        {"role": "system", "content": "You are TravelBuddy, A helpful and kind AI Assistant for only indian tourism and you give short answers and you don't ask any questions, users default location is smt indira gandhi college of engineering ghansoli, And always give google maps location after places name"},
    ]

    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply
print(chatbot("good restaurants in bangluru"))