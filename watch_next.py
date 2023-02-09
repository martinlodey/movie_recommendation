import spacy
nlp = spacy.load('en_core_web_md')


class Movie:
    """Class to represent movies."""

    def __init__(self, title, description):
        """Constructs the attributes of the movie object.   

        Args:
            title (str): Title of the movie.
            description (str): Description of the movie.
        """
        self.title = title
        self.description = description

    def get_title(self):
        """Method to return the movie title.

        Returns:
            str: Title of the movie.
        """
        return self.title

    def get_description(self):
        """Method to return description of a movie.

        Returns:
            str: Description of the movie.
        """
        return self.description


movie_list = []


def watch_next(description):
    """Function that takes in a movie description, compares it to other movie descriptions using spaCy, finds
    the movie with the closest matching description and outputs the movie title.

    Args:
        description (str): Description of a movie.
    """
    temp_comparitive_score = 0
    description = nlp(description)

    # Loops through movie objects in a list.
    for movie in movie_list:

        # Compares the descriptions and produces a similarity score.
        comparitive_score = nlp(movie.get_description()
                                ).similarity(description)

        # Conditional if the similarity score is greater than the previously stored score.
        if comparitive_score > temp_comparitive_score:

            temp_comparitive_score = comparitive_score
            
            # Gets movie title.
            movie_to_watch = movie.get_title()

    # Outputs movie with most similar description.
    print(movie_to_watch)
    return


movies = ""

try:
    # Opens file and reads lines.
    with open("movies.txt", "r") as f:

        for line in f:
            movies += line

# If file not found, outputs error and exits program.
except FileNotFoundError:
    print("\nThe movies.txt file not found, please upload the movies.txt file and try again.")
    exit()


# Replaces space, colon and new line with a pipe.
movies = movies.replace(" :", "|")
movies = movies.replace("\n", "|")

# Splits data in to a list.
movies = list(movies.split("|"))

# Loop through list.
for i in range(0, len(movies), 2):

    # Creates movie object from data.
    movie = Movie(movies[i], movies[i+1])

    # Adds the movie object to the movie list.
    movie_list.append(movie)

watched = Movie("Planet Hulk", "Will he save their world or destroy it?  When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.")

# Calls the watch_next function and passes the movie description that is retrieved using the get.description method of the class.
watch_next(watched.get_description())
