from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    generated_password = ""
    if request.method == "POST":
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                   'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                   'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                   'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = int(request.form.get("letters"))
        nr_symbols = int(request.form.get("symbols"))
        nr_numbers = int(request.form.get("numbers"))

        password = []

        for char in range(0, nr_letters):
            password += random.choice(letters)
        for char in range(0, nr_symbols):
            password += random.choice(symbols)
        for char in range(0, nr_numbers):
            password += random.choice(numbers)

        random.shuffle(password)
        pa = ""
        for char in password:
            pa += char

        generated_password = pa

    return render_template("index.html", password=generated_password)

if __name__ == "__main__":
    app.run(debug=True)
