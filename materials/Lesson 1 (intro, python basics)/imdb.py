import webbrowser
import random
import string

movie_id = 'tt0' + ''.join(random.choice(string.digits) for _ in range(6))

imdb_url = f"https://www.imdb.com/title/{movie_id}/"

webbrowser.open(imdb_url)