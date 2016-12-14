import traceback
from sqlite3 import *


def create_music_table():
    db = connect('musicDB.db')


    db.execute(('''
CREATE TABLE IF NOT EXISTS my_music(
artist TEXT NOT NULL,
album TEXT UNIQUE NOT NULL,
genre TEXT NOT NULL);'''))
    db.close()


def get_column_names():
    db = connect('musicDB.db')
    column = db.cursor()
    column.execute('SELECT * FROM my_music')
    columns = [coln[0].upper() for coln in column.description]
    db.close()
    return columns

def search_entries(column, keyword):
    db = connect('musicDB.db')
    search = db.cursor()
    try:
        search.execute('SELECT * FROM my_music WHERE ' +  column + ' LIKE ?', ('%' + keyword + '%',))
        header = get_column_names()
        rows = search.fetchall()
        print(header[0], header[1], header[2])

        for row in rows:
            print(row)

    except Error as e:
        print('Error: ', e, 'occurred')
        traceback.print_exc()

    finally:
        db.close()

def delete_entry(column,todelete):
    db = connect('musicDB.db')
    delete = db.cursor()
    try:
        delete.execute('DELETE FROM my_music WHERE ' +  column + ' LIKE ?', ('%' + todelete + '%',))
        db.commit()

    except IntegrityError:
        print('This album was already deleted')
        db.rollback()

    finally:
        db.close()


def add_entry(album):
    db = connect('musicDB.db')
    add = db.cursor()
    try:
        add.execute('INSERT INTO my_music VALUES (?,?,?)',
                    (album.artist, album.title, album.genre))
        db.commit()

    except IntegrityError:
        print('This album already exists in your music library')
        db.rollback()

    finally:
        db.close()

