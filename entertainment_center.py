import media
import fresh_tomatoes

# Create 6 instances of class 'Movie'.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

oceans_eleven = media.Movie("Ocean's Eleven",
                            "Danny Ocean and his eleven accomplices plan to\
                             rob three Las Vegas casinos simultaneously.",
                            "https://www.movieposter.com/posters/archive/main/186/MPW-93256",  # NOQA
                            "https://www.youtube.com/watch?v=imm6OR605UI")

the_prestige = media.Movie("The Prestige",
                           "Two stage magicians engage in competitive "
                           "one-upmanship in an attempt to create the "
                           "ultimate stage illusion.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDI0MTIxNF5BMl5BanBnXkFtZTYwNTM0MzY2._V1_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=o4gHCmTQDVI")

the_intouchables = media.Movie("The Intouchables",
                               "A quadriplegic aristocrat hires a young man "
                               "from the projects to be his caregiver",
                               "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxNDA3MDQwNl5BMl5BanBnXkFtZTcwNTU4Mzc1Nw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=0RqDiYnFxTk")

inception = media.Movie("Inception",
                        "A thief uses dream-technology to plant an "
                        "idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

# Create a list of the 'Movie' instances
movies = [the_prestige, the_intouchables, inception, toy_story, avatar,
          oceans_eleven]

# Render the movies in an html page
fresh_tomatoes.open_movies_page(movies)
