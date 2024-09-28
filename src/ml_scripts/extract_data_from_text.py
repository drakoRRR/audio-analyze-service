import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')


def extract_name_and_location(text: str):
    name = None
    location = None

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
