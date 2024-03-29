#!/usr/bin/env python3

import json

FILES_DIRECTORY = '/Users/rjimeno/JPMC/jpmc-percc-2024/wikipedia-movie-data/'
FILES = ('movies-1900s.json', 'movies-1910s.json')

def load_json_file(*file_names):
    """
    >>> load_json_file()
    Number of files: 0.
    >>> load_json_file('movies-1900s.json')
    Number of files: 1.
    File: /Users/rjimeno/JPMC/jpmc-percc-2024/wikipedia-movie-data/movies-1900s.json.
    Loaded 354 records.
    >>> load_json_file('movies-1900s.json', 'movies-1910s.json')
    Number of files: 2.
    File: /Users/rjimeno/JPMC/jpmc-percc-2024/wikipedia-movie-data/movies-1900s.json.
    Loaded 354 records.
    File: /Users/rjimeno/JPMC/jpmc-percc-2024/wikipedia-movie-data/movies-1910s.json.
    Loaded 3869 records.
    """
    number_of_files = len(file_names)
    print(f'Number of files: {number_of_files}.')
    for f in file_names:
        file_path = f'{FILES_DIRECTORY}{f}'
        with open(file_path, 'r') as input_file:
            print(f'File: {file_path}.')
            records = json.load(input_file)
        size = len(records)
        counter = 0
        print(f'Loaded {size} records.')
        # for record in records:
        #     counter += 1
        #     print(f'{counter}: {record}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()