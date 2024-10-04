from flask import Flask
import random

app = Flask(__name__)

guess = random.randint(0,9)

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src = 'https://giphy.com/gifs/muppetwiki-sesame-street-muppets-elmo-fUQ4rhUZJYiQsas6WD'>"



@app.route('/<int:number>')
def Guess(number):
    if number == guess :
        return "<h1 style = 'foreground : green'>Perfect you git it...</h1>" \
            "<img src = 'https://giphy.com/gifs/justin-raccoon-pedro-tHIRLHtNwxpjIFqPdV'>"
    elif number > guess :
        return "<h1 style = 'foreground : red'>Too high, try again </h1>" \
            "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.g'>"
    else :
        return "<h1>Too low ,try again!</h1>" \
            "<img src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)



# def makebold(function):
#     def wrabed():
#         return f"<b>{function()}</b>"
#     return wrabed

# def makeemphasized(function):
#     def wrabed():
#         return f"<em>{function()}</em>"
#     return wrabed

# def makeunderlined(function):
#     def wrabed():
#         return f"<u>{function()}</u>"
#     return wrabed