from flask import Flask, render_template

app = Flask(__name__)

# Set the template folder
app.template_folder = 'D:/Final project report/final project/project code/1_Language Translator/templates'

@app.route('/')
def homepage():
    return render_template('Homepage.html')

@app.route('/page1')
def page1():
    return render_template('Language_Translator.html')

@app.route('/page2')
def page2():
    return render_template('Drag_Drop.html')

@app.route('/page3')
def page3():
    return render_template('upload.html')

@app.route('/page4')
def page4():
    return render_template('Text_To_Speech.html')

@app.route('/page5')
def page5():
    return render_template('Dictionary.html')

@app.route('/page6')
def page6():
    return render_template('File_Foramat.html')

@app.route('/page7')
def page7():
    return render_template('Palindrome.html')

@app.route('/page8')
def page8():
    return render_template('Notes.html')

@app.route('/page9')
def page9():
    return render_template('Quote_Generator.html')
#    GAMES SECTION STARTS FROM HERE
@app.route('/page10')
def page10():
    return render_template('Word_Guessing_Game.html')

@app.route('/page11')
def page11():
    return render_template('Word_Scramble_Game.html')

@app.route('/page12')
def page12():
    return render_template('Typing_Speed.html')

@app.route('/page13')
def page13():
    return render_template('Hangman_game.html')

@app.route('/page14')
def page14():
    return render_template('Quiz.html')

@app.route('/page15')
def page15():
    return render_template('Drawing.html')


if __name__ == '__main__':
    app.run(debug=True)
