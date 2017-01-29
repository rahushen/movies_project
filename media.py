import webbrowser


class Movie():
    """This is a class that holds information about movies

        Attributes:
            title (str): Release title of the Movie
            storyline (str): Brief description of the movie's plot
            poster_img_url (str): link to the movie's poster image
            trailer_youtube_url (str): youtube link to the movie trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """The constructor for class Movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Plays the movie's youtube trailer in a webbrowser."""
        webbrowser.open(self.trailer_youtube_url)
