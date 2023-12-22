from argparse import ArgumentParser
from operator import itemgetter
import pandas as pd
import sys


def best_movies(path_movie, path_rating):
    """ Function that takes in two paths to
    csv files, reads them, performs a merge 
    of the data in those files based on the 
    item id and movie id columns. Then an 
    average rating for each movie is found
    and a series of movies ordered based 
    on average rating is returned. 

    Args:
        path_movie - a path to the csv file containing movies 
        path_rating - a path to the csv file containing ratings for movies

    Returns:
        ser.sort_values(ascending=False) - series of movies ordered 
        based on average rating and presented in a movie:rating format
    """
    movies = pd.read_csv(path_movie)
    ratings = pd.read_csv(path_rating)

    inner_merge = ratings.merge(movies, left_on="item id", right_on="movie id", how="inner")

    ser = inner_merge.groupby("movie title")["rating"].mean()

    return ser.sort_values(ascending=False)


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())
