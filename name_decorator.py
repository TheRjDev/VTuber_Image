from curses import wrapper
from os import link
from typing import Counter
from numpy import inner
import pandas as pd


def decorator(func):
    df = pd.read_csv('names.csv')
    file = None

    with open('test.md', mode='r', encoding='utf-8') as f:
        file = f.read()

    file.replace('\n', ' ')

    words = file.split(' ')
    first_names = df['first_name'].tolist()
    last_names = df['last_name'].tolist()
    links = df['link'].tolist()

    def wrapper():
        new_file = ''

        for i in range(len(words)):
            if words[i] in first_names:
                name_index = first_names.index(words[i])
                try:
                    if words[i + 1] in last_names:
                        new_file += f'<img src="{links[name_index]}" alt="{words[i]} {words[i + 1]}"> {words[i]} {words[i + 1]} '
                    elif words[i - 1] in last_names:
                        break
                    else:
                        new_file += f'<img src="{links[name_index]}" alt="{words[i]}"> {words[i]} {words[i]} '
                except IndexError:
                    new_file += f'<img src="{links[name_index]}" alt="{words[i]}"> {words[i]} '

            elif words[i] in last_names:
                name_index = last_names.index(words[i])
                try:
                    if words[i - 1] in first_names:
                        break
                    elif words[i + 1] in first_names:
                        new_file += f'<img src="{links[name_index]}" alt="{words[i]} {words[i + 1]}"> {words[i]} {words[i + 1]} '
                except IndexError:
                    new_file += f'<img src="{links[name_index]}" alt="{words[i]}"> {words[i]} '
            else:
                new_file += words[i] + ' '

        with open('new_file.md', mode='w', encoding='utf-8') as f:
            f.write(new_file)
        func()
    return wrapper

@decorator
def main():
    print('works')


if __name__ == '__main__':
    main()
