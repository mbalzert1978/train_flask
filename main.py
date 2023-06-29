from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def hello() -> str:
    portfolio = "Portfolio"
    return render_template(
        "index.html",
        greeting="Welcome to my portfolio",
        author="Markus Iorio",
        title=portfolio,
        nav_brand=portfolio,
    )
