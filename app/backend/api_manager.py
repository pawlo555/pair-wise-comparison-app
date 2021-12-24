from typing import Dict

from imdb import IMDb

VALUES = ['title', 'year', 'kind', 'plot outline', 'directors', 'rating', 'languages', 'full-size cover url', 'cast']


class APIManager:
    def __init__(self):
        self.imdb = IMDb()

    def fetch_movie(self, title: str):
        #print(self.imdb.get_movie_infoset())
        try:
            result = self.imdb.search_movie(title)
            movie_dictionary = self.compose_dictionary(result[0].getID())
        except Exception:
            return {"error": "error during parsing"}
        return movie_dictionary

    def compose_dictionary(self, movieID: int) -> Dict[str, str]:
        movie = self.imdb.get_movie(movieID)
        movie_dictionary = {}
        for value in VALUES:
            movie_dictionary[value] = movie[value]
        cast = movie_dictionary['cast']
        names = cast[0]['name'] + ", " + cast[1]['name'] + ", " + cast[2]['name']
        movie_dictionary['cast'] = names
        movie_dictionary['directors'] = movie_dictionary['directors'][0]['name']

        return movie_dictionary


if __name__ == '__main__':
    print(APIManager().fetch_movie("Star Wars"))
