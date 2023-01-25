import spacy

nlp = spacy.load('en_core_web_md')
movies_file = r".\movies.txt"

def read_movies(movies_file: str) -> list:
    '''Reads movies.txt and returns a list with movie and description'''

    movies_list = []
    with open(movies_file, "r") as f:
        for movie in f.readlines():
            movie = movie.split(":")
            movies_list.append([movie[0].strip(" "), movie[1].strip("\n")])
    return movies_list

def get_watched_movie(movies: list) -> int:
    '''Gets input from user of which movie they watched'''

    print("Which movie did you watch out of the following ?")
    for nr, movie in enumerate(movies, start=1):
        print(f"{nr}. ".center(3) + f"{movie[0]}.")
    while True:
        watched_movie = int(input(f"Your Choice 1 to {len(movies)}: "))
        if watched_movie > 0 and watched_movie <= len(movies):
            break
    return watched_movie-1

def recommend_movie(watched_movie: int, movies: list) -> int:
    '''Recommends movie based on previous user input'''

    watched_movie_description = nlp(movies[watched_movie][1])
    best_match = 0
    next_movie = watched_movie

    for nr, movie in enumerate(movies):
        similarity_rating = nlp(movie[1]).similarity(watched_movie_description)
        #print(movie[0], similarity_rating) #un-comment line to print similarty rating
        if similarity_rating > best_match and similarity_rating < 1:
            best_match = similarity_rating
            next_movie = nr
    return next_movie

def main():
    '''Main function calls other functions and prints out recommended movie and description'''

    movies = read_movies(movies_file)
    watched_movie = get_watched_movie(movies)
    recommended_movie = recommend_movie(watched_movie, movies)

    print(f"\nYour next recommended movie to watch is: \n\n{movies[recommended_movie][0]}\n")
    print(f"Description of movie:\n\t{movies[recommended_movie][1]}")

if __name__ == "__main__":
    main()

