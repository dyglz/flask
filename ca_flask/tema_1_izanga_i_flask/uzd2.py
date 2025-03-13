# Sukurti programą, kuri įvedus norimą žodį adreso eilutėje 
# (po / simbolio) ir paspaudus ENTER, 
# atspausdintų jį penkis kartus.


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<word>")
def word(word):
    return render_template("word.html", word = word)

if __name__ == "__main__":
    app.run(debug=True)