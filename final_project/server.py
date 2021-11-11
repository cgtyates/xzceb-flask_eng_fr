from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.english_to_french(textToTranslate)
    # Write your code here
    return translatedText

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.french_to_english(textToTranslate)
    # Write your code here
    return translatedText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
