from flask import Flask, render_template, request
from cipher import encrypt, decrypt

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    error = ""
    mode = ""
    text = ""
    shift = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        shift = request.form.get("shift", "")
        mode = request.form.get("mode", "encrypt")

        if not text:
            error = "Please enter some text."

        else:
            try:
                shift_value = int(shift)

                if mode == "encrypt":
                    result = encrypt(text, shift_value)
                else:
                    result = decrypt(text, shift_value)

            except ValueError:
                error = "Please enter a valid whole number for the shift."

    return render_template(
        "index.html",
        result=result,
        error=error,
        mode=mode,
        text=text,
        shift=shift
    )


if __name__ == "__main__":
    app.run(debug=True)