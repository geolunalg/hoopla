import string
from .search_utils import (
    DEFAULT_SEARCH_LIMIT,
    load_movies,
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


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def tokenized_text(text):
    return [val for val in text.split() if val != ""]
