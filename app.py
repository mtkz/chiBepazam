'''
description : for mom's with love . hope to enjoy :)
author : mohammad tahourian from mtkz.ir
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    data = open('data.txt', 'r' , encoding='utf-8')
    datas = data.readlines()

    return render_template('index.html', datas=datas)


if __name__ == '__main__':
    app.run(debug=True)
