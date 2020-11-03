import os
import os.path
import sys
import requests

from bs4 import BeautifulSoup

# write your code here
args = sys.argv
dir_name = args[1]
tabs_list = []


def request_content(users_input):
    if users_input.startswith("https://"):
        url = users_input
    else:
        url = "https://" + users_input
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except requests.exceptions.ConnectionError:
        return "Connection refused"


def create_directory():
    try:
        os.mkdir(dir_name)
        tabs_list.append(dir_name)
    except FileExistsError:
        tabs_list.append(dir_name)


def get_name(users_input):
    a = users_input.split('.')
    if len(a) <= 2:
        name = a[0]
        return name
    else:
        name = ''
        for i in range(len(a) - 1):
            name += a[i] + '.'
        return name[:-1]


def save_file(name, text):
    the_name = os.path.join(dir_name, "{}".format(name))
    with open(the_name, "w") as f:
        f.write(text)


def read_file(name):
    the_name = os.path.join(dir_name, name)
    with open(the_name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


if len(args) > 1:
    create_directory()
saved_files = []

while True:
    inp = input()

    if inp in saved_files:
        read_file(inp)
    elif inp == 'back':
        if len(saved_files) >= 2:
            current = saved_files.pop()
            previous = saved_files.pop()
            read_file(previous)
        elif len(saved_files) < 2:
            continue
    elif inp == 'exit':
        break
    elif ('.' not in inp) and (inp not in saved_files):
        print("Error: Incorrect URL")
    else:
        file_name = get_name(inp)
        text_to_fill = request_content(inp)
        print(text_to_fill)
        save_file(file_name, text_to_fill)
        saved_files.append(file_name)
