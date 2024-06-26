#!/usr/bin/env python3

from random import randrange
import boto3
import json
import sys

FILES_DIRECTORY = '../wikipedia-movie-data/' #'/Users/rjimeno/JPMC/jpmc-percc-2024/wikipedia-movie-data/'
FILES = (
     'movies-1900s.json',
     'movies-1910s.json',
     'movies-1920s.json',
     'movies-1930s.json',
     'movies-1940s.json',
     'movies-1950s.json',
     'movies-1960s.json',
     'movies-1970s.json',
     'movies-1980s.json',
     'movies-1990s.json',
     'movies-2000s.json',
     'movies-2010s.json',
     'movies-2020s.json'
     )

class MovieStoreLoader:
    counter = 0
    records = []

    def __init__(self):
        pass

    def load_json_file(self, *file_names):
        """
        >>> msl = MovieStoreLoader()
        >>> msl.load_json_file()
        Number of files: 0.
        >>> msl.load_json_file('movies-1900s.json')
        Number of files: 1.
        File: ../wikipedia-movie-data/movies-1900s.json.
        Loaded 354 records.
        >>> msl.load_json_file('movies-1900s.json', 'movies-1910s.json')
        Number of files: 2.
        File: ../wikipedia-movie-data/movies-1900s.json.
        Loaded 354 records.
        File: ../wikipedia-movie-data/movies-1910s.json.
        Loaded 3869 records.
        """
        number_of_files = len(file_names)
        print(f'Number of files: {number_of_files}.')
        for f in file_names:
            file_path = f'{FILES_DIRECTORY}{f}'
            with open(file_path, 'r', encoding='UTF-8') as input_file:
                print(f'File: {file_path}.')
                self.records = json.load(input_file)
            size = len(self.records)
            print(f'Loaded {size} records on memory.')

    def save_in_db(self, table_name):
        """
        This function should be improved to enhance indexing and reduce
        duplication. We are starting with a very simple approach.
        >>> msl = MovieStoreLoader()
        >>> msl.load_json_file('movies-1900s.json') # doctest: +ELLIPSIS
        Number ...
        >>> msl.save_in_db('movies') # doctest: +ELLIPSIS
        1: {'title': 'After Dark in Central Park', 'year': 1900, 'cast': [], 'genres': [], 'href': None}
        2: ...
        """
        dynamodbclient=boto3.resource('dynamodb', region_name='us-east-1')
        movies_table = dynamodbclient.Table(table_name)
        for record in self.records:
            self.counter += 1
            record['id'] = randrange(0, 1_000_000_000_000)
            # print(f'{self.counter}: {record}') # Maybe comment-out for debugging.
            _ = movies_table.put_item(Item=record)  # Ignoring return value for simplicity.
        print(f"Stored {self.counter} memory records persistently.")

if __name__ == '__main__':
    # Disable unit tests until I can create good ones.
    # import doctest
    # doctest.testmod()
    for f in FILES:
        msl = MovieStoreLoader()
        msl.load_json_file(f)
        msl.save_in_db('movies')
