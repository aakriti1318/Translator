from multiprocessing.connection import answer_challenge
from flask import Flask, render_template, request
from openaix import getLanguageTranslation

app = Flask(__name__)
app.config['SECRET_KEY'] = '3eaee030-6ce4-4eac-b4a6-2fb9d6999dfd'

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        prompt = request.form['aiPrompt']
        language = request.form['language']
        answer = getLanguageTranslation(prompt, language)

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)