from flask import Flask, request, Response
from threading import Thread
import time

app = Flask('')


@app.route('/')
def home():
    return "Codebuilder is Immortal!"

def run():
    app.run(host='0.0.0.0', port=5190)


def keep_alive():
    t = Thread(target=run)
    t.start()
