from flask import Flask, render_template, request
import meu_jogo

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        time = request.form['time']
        jogador1 = request.form['jogador1']
        jogador2 = request.form['jogador2']
        jogador3 = request.form['jogador3']
        meu_jogo.criar_time(time, jogador1, jogador2, jogador3)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
