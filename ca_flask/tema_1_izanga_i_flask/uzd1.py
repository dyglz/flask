# Sukurti programą, kuri turėtų statinį puslapį, 
# pvz. localhost:5000 
# su norimu tekstu (rekomenduojama naudoti šablonus)


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") # This will render the "home.html" file in the templates folder

if __name__ == "__main__":
    app.run(debug=True) # By default, Flask runs on localhost:5000
    