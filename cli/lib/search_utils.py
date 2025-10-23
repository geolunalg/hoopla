import json
import os

DEFAULT_SEARCH_LIMIT = 5

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data")


def load_movies() -> list[dict]:
    with open(os.path.join(DATA_PATH, "movies.json"), "r") as f:
        data = json.load(f)
    return data["movies"]


def load_stop_word() -> set:
    with open(os.path.join(DATA_PATH, "stopwords.txt"), "r") as f:
        data = f.read().splitlines()
    return set(data)
