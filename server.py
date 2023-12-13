from flask import Flask
import random

app=Flask(__name__)
random_number=random.randint(0,9)
# random_number=3

@app.route('/')
def home():
    return f'<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/D4HIiJ4LMo3X4uZ0Of/giphy.gif"/>'

@app.route('/<int:number>')
def game(number):
    if random_number == number:
        return f'<h1 style="color: green">{number} is correct!</h1>' \
               '<img src="https://media.giphy.com/media/S9caVuOS5csQvlMscF/giphy.gif"/>'
    elif random_number > number:
        return f'<h1 style="color: red">{number} is too low!</h1>' \
               '<img src="https://media.giphy.com/media/rDcPRxSSDSmuKx1p9G/giphy.gif"/>'
    else:
        return f'<h1 style="color: red">{number} is too high</h1>' \
               '<img src="https://media.giphy.com/media/j5E1K5iOr3TQpu6EDg/giphy.gif"/>'




if __name__=="__main__":
    app.run(debug=True)