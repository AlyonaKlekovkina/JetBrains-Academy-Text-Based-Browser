import os
import os.path
import sys

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
# write your code here
args = sys.argv
dir_name = args[1]
tabs_list = []


def save_file(name):
    n = name.split('.')
    n = n[0]
    the_name = os.path.join(dir_name, "{}".format(n))
    with open(the_name, "w") as f:
        if n == 'bloomberg':
            f.write(bloomberg_com)
            options.append(n)
        else:
            f.write(nytimes_com)
            options.append(n)


def read_file(name):
    the_name = os.path.join(dir_name, name)
    with open(the_name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())


def create_directory():
    try:
        os.mkdir(dir_name)
        tabs_list.append(dir_name)
    except FileExistsError:
        tabs_list.append(dir_name)


if len(args) > 1:
    create_directory()


options = ['bloomberg.com', 'nytimes.com', 'exit']
while True:
    inp = input()
    if inp not in options:
        print("Error: Incorrect URL")
    elif inp == 'bloomberg.com':
        save_file('bloomberg.com')
        print(bloomberg_com)
    elif inp == 'nytimes.com':
        save_file('nytimes.com')
        print(nytimes_com)
    elif inp == 'bloomberg' and inp in options and len(tabs_list) >= 1:
        read_file('bloomberg')
    elif inp == 'nytimes' and inp in options and len(tabs_list) >= 1:
        read_file('nytimes')
    elif inp == 'exit':
        break
