from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Russian": "ru",
    "Arabic": "ar",
    "Korean": "ko"
}

@app.route("/")
def home():
    return render_template("index.html", languages=languages.keys())

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data["text"]
    source = languages[data["source"]]
    target = languages[data["target"]]

    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    return jsonify({
        "translated": translated
    })

if __name__ == "__main__":
    app.run(debug=True)