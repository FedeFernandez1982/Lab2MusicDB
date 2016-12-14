import database
import sys
from album import *
from menus import *

search_options = ('Artist', 'Album', 'Genre')

def main_menu():
    display_initial_message()
    while True:
        display_options_menu()

        menu_choice = input('Please select an option\n')
        if menu_choice == '1':
            search_database()

        elif menu_choice == '2':
            add_to_table()

        elif menu_choice == '3':
            delete_entry()

        elif menu_choice == '4':
            sys.exit()

        else:
            print('Please select a valid option\n')


def search_database():
    display_search_menu()

    while True:
        try:
            value = int(input('Enter an option \n'))

        except ValueError:
            display_error()
            continue

        else:
            break
    if value == 1:
        art = (str(input('Introduce the name of the artist to search:\n')))
        database.search_entries('artist', art)
    elif value == 2:
        alb = (str(input('Introduce the name of the album to search:\n')))
        database.search_entries('album', alb)
    elif value == 3:
        gen = (str(input('Introduce the genre of music to search:\n')))
        database.search_entries('genre', gen)


def add_to_table():

    newAlbum = Album('','','')
    artist = input('Introduce the name of the Artist \n')

    newAlbum.setartist(artist)
    title = input('Introduce the name of the Album \n')

    newAlbum.settitle(title)
    genre = input('Introduce the genre of the Album \n')

    newAlbum.settitle(genre)

    database.add_entry(newAlbum)

def delete_entry():

    todelete = input('Introduce the name of the Album you want to delete')
    database.delete_entry('Album',todelete)

def main():
    database.create_music_table()
    main_menu()


main()
