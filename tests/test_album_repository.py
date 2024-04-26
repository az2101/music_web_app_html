
from lib.album import *
from lib.album_repository import *

"""
When i call #all on the AlbumRepository
I get all the albums back in a list
"""

def test_list_all_albums(db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    repository = AlbumRepository(db_connection)
    result = repository.all()
    assert result == [ 
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
        ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_album(db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3, "Waterloo", 1974, 2)

"""
When we call AlbumRepo #create
We can add an album to the database
"""

def test_create_album(db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    repository = AlbumRepository(db_connection)
    
    repository.create(Album(None, 'Arrival', 1976, 2))
    result = repository.all()
    assert result == [ 
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(3, "Waterloo", 1974, 2),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2),
        Album(13, "Arrival", 1976, 2)
        ]

"""
When we call AlbumRepo #delete
We can delete an album from the database
"""

def test_delete_album(db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    repository = AlbumRepository(db_connection)
    
    repository.delete(3)
    result = repository.all()
    assert result == [ 
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(4, "Super Trouper", 1980, 2),
        Album(5, "Bossanova", 1990, 1),
        Album(6, "Lover", 2019, 3),
        Album(7, "Folklore", 2020, 3),
        Album(8, "I Put a Spell on You", 1965, 4),
        Album(9, "Baltimore", 1978, 4),
        Album(10, "Here Comes the Sun", 1971, 4),
        Album(11, "Fodder on My Wings", 1982, 4),
        Album(12, "Ring Ring", 1973, 2)
    ]