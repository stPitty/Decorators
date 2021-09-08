import requests


def wiki_api(s_obj):
    url = "https://ru.wikipedia.org/w/api.php"
    params = {
        "action": 'opensearch',
        "search": s_obj,
        "limit": 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response
