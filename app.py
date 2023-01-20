from flask import Flask, render_template, request
import json
import spacy
from ner_client import NamedEntityClient

app = Flask(__name__)

model = spacy.load("en_core_web_sm")
ner = NamedEntityClient(model)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ner", methods=["POST"])
def get_named_entities():
    data = request.get_json()
    result = ner.get_ents(data["sentence"])
    print(result)
    return json.dumps({"entities": result.get("ents"), "html": result.get("html")})


if __name__ == "__main__":
    app.run(debug=True)
