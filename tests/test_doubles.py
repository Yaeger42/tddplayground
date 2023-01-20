class NerModelTestDouble:
    """
    Test double for spaCy NLP model
    """

    def __init__(self, model):
        self.model = model

    def returns_doc_entities(self, ents):
        self.ents = ents

    def __call__(self, sentence: str):
        return DocTestDouble(sentence, self.ents)


class DocTestDouble:
    """
    Test double for spacy doc
    """

    def __init__(self, sentence: str, ents):
        self.ents = [SpanTestDouble(ent["text"], ent["label_"]) for ent in ents]

    def patch_method(self, attr, return_value):
        def patched():
            return return_value

        setattr(self, attr, patched)
        return self


class SpanTestDouble:
    def __init__(self, text: str, label: str):
        self.text = text
        self.label_ = label
