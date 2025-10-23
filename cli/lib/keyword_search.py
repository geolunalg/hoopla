import string
from .search_utils import (
    DEFAULT_SEARCH_LIMIT,
    load_movies,
    load_stop_word
)


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    for movie in movies:
        query_vals = set(tokenized_text(remove_punctuation(query.lower())))
        title_vals = tokenized_text(remove_punctuation(movie["title"].lower()))
        if any(value in " ".join(title_vals) for value in query_vals):
            results.append(movie)

        if len(results) >= limit:
            break
    return results


def remove_punctuation(text) -> str:
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def tokenized_text(text) -> list[str]:
    tokens = []
    stop_words = load_stop_word()
    for val in text.split():
        if val != "" and val not in stop_words:
            tokens.append(val)
    return tokens
