from os import link
from typing import Counter
import pandas as pd

def decorator():
    def wrapper(func):
        pass
    return wrapper

def main():
    df=pd.read_csv('names.csv')
    file=None
    with open('test.md', mode='r', encoding='utf-8') as f:
        file = f.read()
    
    first_names = df['first_name'].tolist()
    last_names = df['last_name'].tolist()
    links = df['link'].tolist()
    new_file=''

    for words in file:
        if words in first_names:
            index = first_names.index(words)
            try:
                if words[index+1] == last_names[index+1]:

            
            new_file += f'<img src="{links[index]}" alt="{words}">'

if __name__ == '__main__':
    main()