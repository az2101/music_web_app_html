from lib.database_connection import get_flask_database_connection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.album import Album
from flask import request, render_template, redirect, url_for
from lib.album_parameter_validator import AlbumParametersValidator

def apply_example_routes(app):

    @app.route('/')
    def get_main():
        return render_template("main.html")

    @app.route('/albums', methods=['GET'])
    def get_albums():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        albums = repository.all()
        return render_template('albums/index.html', albums=albums)
    
    @app.route("/albums/<id>")
    def get_album(id):
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        artist_repository = ArtistRepository(connection)
        album = repository.find(id)
        artist = artist_repository.find(album.artist_id)
        return render_template("albums/show.html", album=album, artist=artist)

    @app.route("/artists", methods=['GET'])
    def get_artists():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        artists = repository.all()
        return render_template('artists/index.html', artists=artists)
    
    @app.route("/artists/<id>", methods=['GET'])
    def get_artist(id):
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        artist = repository.find(id)
        return render_template("artists/show.html", artist=artist)
    
    @app.route("/albums/new", methods=['GET'])
    def get_new_album():
        return render_template("albums/new.html")
    
    @app.route("/albums", methods=['POST'])
    def create_album():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        validator = AlbumParametersValidator(request.form['title'], request.form['year'])

        
        if not validator.is_valid():
            errors = validator.generate_errors()
            return render_template('albums/new.html', errors=errors)
        
        album = Album(None, validator.get_valid_title(), validator.get_valid_year(), 1)
        
        repository.create(album)
        return redirect(f"/albums/{album.id}")
    
    @app.route("/artists/new", methods=['GET'])
    def get_new_artist():
        return render_template("artists/new.html")
    
    @app.route("/artists", methods=['POST'])
    def create_artist():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)

        name = request.form['name']
        genre = request.form['genre']
        artist = Artist(None, name, genre)

        if not artist.is_valid():
            return render_template('artists/new.html', errors=artist.generate_errors())
        
        repository.create(artist)
        return redirect(f"/artists/{artist.id}")
    
    
