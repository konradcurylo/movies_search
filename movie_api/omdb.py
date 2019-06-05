
from django.template.defaultfilters import slugify
import requests


def collect_movie(title):
    # Zwraca filmy z bazy Omdb, wyszukując po tytule #

    api_key= "fedd02f4"
    s_title = slugify(title).replace('-', '+')
    r = requests.get('http://www.omdbapi.com/?apikey={}&t={}'.format(api_key,s_title))
    data = r.json()
    omdb_data = {key.lower(): data[key] for key in data}
    return omdb_data
