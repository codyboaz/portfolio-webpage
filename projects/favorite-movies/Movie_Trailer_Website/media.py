import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    #All valid movie rating options
    VAILID_RATINGS = ["G", "PG", "PG-13", "R"]

    #constructor to initialize movie object
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Function plays trailer in web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
