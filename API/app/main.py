"""
API for querying movies data. It can be queried by year, movie name
(i.e. title), cast member, or genre.

Or at lest that's what it should do.
"""
#import json
#import sys
from random import randrange
#from typing import Optional, Union
from fastapi import FastAPI  #, HTTPException, status, Query, Response
from pydantic import BaseModel


import boto3
from boto3.dynamodb.conditions import Key

# {'title': 'After Dark in Central Park', 'year': 1900, 'cast': [], 'genres': [], 'href': None}
class Movie(BaseModel):
    title: str = ""
    cast: list = []
    extract: str | None = None
    genres: list = []
    href: str | None = None
    id: int | None = None
    thumbnail: str | None = None
    thumbnail_height: int | None = None
    thumbnail_width: int | None = None
    year: int = 0

TABLE_NAME = 'movies'
app = FastAPI()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Should not need keys.
table = dynamodb.Table(TABLE_NAME)
m = Movie()

@app.get("/hello_world")
def read_root():
    """Hello World endpoint and function are useful for testing."""
    return {"Hello": "World"}

# # READ a lot! Comment out as this may send 36K rows to explode on your face.
# @app.get("/getAllMovies")
# def getall():
#     items = table.scan()
#     print(items)
#     return items

# CREATE (works well)
@app.post("/create_movie")
def create_movie(movie: Movie = m):
    """ Create movie entry in persistent storage. """
    movie.id = randrange(0, 1_000_000_000_000)
    try:
        response = table.put_item(
            Item=movie.__dict__
        )
        #return response
        return response["HTTPStatusCode"]
    except Exception as e: # I know .. too broad (tech debt?).
        print(f"Couldn't add movie {movie} to table {TABLE_NAME}. Here's why:{e}.")
        raise

# READ (works great)
@app.get("/movie_id/{id_n}")
def movie_id(id_n: int):
    """Fetches all the information for one movie using its ID"""
    try:
        response = table.get_item(
            Key={
                "id": id_n
            }
        )
        # get_item() is fater than query() and is guaranteed to return one item.
        movie = response['Item']
        return movie
    except Exception as e: # I know .. too broad (tech debt?).
        print(f"Could not read movie with id '{id}' on table '{TABLE_NAME}'. Here's why:{e}.")
        raise

# READ (works well)
@app.get("/movie_year/{year}")
def movie_year(year: int):
    """Retrieves the IDs of all records for movies released on the given year."""
    try:
        response = table.query(
            IndexName = "year_i",
            KeyConditionExpression=Key("year").eq(year),
            ProjectionExpression="id",
        )
        movies = response['Items']
        return movies
    except Exception as e: # I know .. too broad (tech debt?).
        print(f"Could not read movie from year '{year}' on table '{TABLE_NAME}'. Here's why:{e}.")
        raise

# READ (works well)
@app.get("/movie_title/{title}")
def movie_title(title: str):
    """Retrieves the IDs of all records for movies with the given title."""
    try:
        response = table.query(
            IndexName = "title_i",
            KeyConditionExpression = Key("title").eq(title),
            ProjectionExpression="id",
        )
        movies = response['Items']
        return movies
    except Exception as e: # I know .. too broad (tech debt?).
        print(f"Couldn't read movie title '{title}' from table '{TABLE_NAME}'. Here's why:{e}.")
        raise

# UPDATE (works well)
@app.put("/update_movie")
def update_movie(movie: Movie = m):
    """ Update movie entry in persistent storage. """
    # Obs.: movie.id should match an existing record. Otherwise, one is created.
    try:
        response = table.put_item(
            Item=movie.__dict__
        )
        #return response
        return response["HTTPStatusCode"]
    except Exception as e: # I know .. too broad (tech debt?).
        print(f"Couldn't update movie with id '{id}' on table '{TABLE_NAME}'. Here's why:{e}.")
        raise


# DELETE from DynamoDB using id
@app.delete("/delete_movie/{id_n}")
def delete_movie(id_n: int):
    try:
        response = table.delete_item(
            TableName="movies",
            Key={
                'id': id_n
            }
        )
        #return response
        return response["HTTPStatusCode"]
    except Exception as e: # I know .. too broad (tech debt?).
        print(f"Couldn't delete movie with '{id_n}' from table '{TABLE_NAME}'. Here's why:{e}.")
        raise