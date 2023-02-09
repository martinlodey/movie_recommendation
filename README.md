# Movie Recommendation Program
A program that uses spaCy to recommend a movie based on its description.

## Requirements
- spaCy

## Usage
The program reads the descriptions of movies from a file `movies.txt` and creates movie objects from the data. The program then takes a movie description, compares it to other movie descriptions using spaCy, finds the movie with the closest matching description, and outputs the movie title.

## File Structure
- `movie.py`: Contains the `Movie` class and the `watch_next` function.
- `movies.txt`: A file containing the movie titles and descriptions, separated by a colon and a space (e.g. `"Movie Title: Description of the movie."`).

## How to Run
1. Make sure you have spaCy installed by running `pip install spacy`.
2. Run the program by executing `python movie.py` in the terminal.

## Example
If you have a movie `Planet Hulk` with the description `Will he save their world or destroy it?  When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.`, the program will recommend the closest matching movie.
