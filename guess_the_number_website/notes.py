from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def modify_text(*args):
        return f"<b>{function()}</b>"
    return modify_text

def make_emphasis(function):
    def modify_text(*args):
        return f"<em>{function()}</em>"
    return modify_text

def make_underlined(function):
    def modify_text(*args):
        return f"<u>{function()}</u>"
    return modify_text


@app.route('/')
def hello_world():
    return  '<h1 style="text-align: center">World, hello!</h1>' \
            '<p>This is a paragraph</p>' \
            '<img src="https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif">'

@app.route('/bye')
def bye():
    return "<u><em><b>Bye!</b></em></u>"

@app.route('/goodbye')
@make_bold
@make_emphasis
@make_underlined
def goodbye():  
    return "Goodbye..."

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old."




if __name__ == "__main__":
    app.run(debug=True)