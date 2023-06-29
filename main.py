from typing import Literal

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello() -> Literal["Hello World!"]:
    return "Hello World!"
