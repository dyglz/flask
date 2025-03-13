# Sukurti programą, kuri puslapyje localhost:5000/keliamieji 
# parodytų visus keliamuosius metus nuo 1900 iki 2100 metų.

from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route("/keliamieji")
def leap():
    return render_template("leap.html", calendar = calendar)

if __name__ == "__main__":
    app.run(debug=True)