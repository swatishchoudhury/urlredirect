import os
from flask import Flask, redirect

app = Flask(__name__)

redirects = {}
if os.path.exists("redirects"):
    with open("redirects") as f:
        for line in f:
            short, long = line.strip().split()
            redirects[short] = long

@app.route("/")
def home():
    return redirect("http://github.com/swatishchoudhury")

@app.route("/<short>")
def redirect_url(short):
    long = redirects.get(short)
    if long:
        if not long.startswith("https://"):
            long = "https://" + long
        return redirect(long)
    else:
        return "404"

if __name__ == "__main__":
    app.run()