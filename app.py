import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def traduzir(codigoMorse):
    morse = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z", ".----": 1, "..---": 2, "...--": 3, "....-": 4, ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9, "-----": 0}

    codigo = codigoMorse

    aux =[]

    aux = codigo.split(" ")

    mensagem = ""
    for k in range(len(aux)): 
        if aux[k] in morse.keys():
            mensagem = mensagem + morse[aux[k]]

    if mensagem == "":
        return("Não conseguiu traduzir!")
    else:
        return(mensagem)

def get_morse(morse_id):
    conn = get_db_connection()
    morse = conn.execute('SELECT * FROM morseCodes WHERE id = ?',
                        (morse_id,)).fetchone()
    conn.close()
    if morse is None:
        abort(404)
    return morse

app = Flask(__name__)
app.config['SECRET_KEY'] = 'casadeiadriana'

@app.route('/', methods=('GET', 'POST')) 
def home():
    if request.method == 'POST':
        codigoMorse = request.form['morse']

        if not codigoMorse:
            flash('Por favor, digite um Código Morse.')
        else:
            traducao = traduzir(codigoMorse)
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO morseCodes (code, translation) VALUES (?, ?)',
                         (codigoMorse, traducao))
            id = cursor.lastrowid
            conn.commit()
            conn.close()
            morseTraduzido = get_morse(id)
            return render_template('translation.html', morse = morseTraduzido)

    return render_template('home.html')