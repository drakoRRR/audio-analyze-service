# import spacy
#
# nlp = spacy.load("en_core_web_sm")
#
#
# def extract_name_and_location(text: str):
#     doc = nlp(text)
#
#     name = None
#     location = None
#
#     for entity in doc.ents:
#         if entity.label_ == "PERSON" and name is None:
#             name = entity.text
#         elif entity.label_ == "GPE" and location is None:
#             location = entity.text
#
#         if name and location:
#             break
#
#     return name, location

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Ensure that required NLTK data files are downloaded
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

def extract_name_and_location(text: str):
    name = None
    location = None

    # Tokenize and perform NER
    chunks = ne_chunk(pos_tag(word_tokenize(text)))

    for chunk in chunks:
        if hasattr(chunk, 'label'):
            if chunk.label() == 'PERSON' and name is None:
                name = ' '.join(c[0] for c in chunk)
            elif chunk.label() == 'GPE' and location is None:
                location = ' '.join(c[0] for c in chunk)

            if name and location:
                break

    return name, location
