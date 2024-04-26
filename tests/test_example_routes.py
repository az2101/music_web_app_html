from playwright.sync_api import Page, expect

def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_web_app.sql")

    page.goto(f"http://{test_web_address}/albums")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Doolittle",
        "Surfer Rosa",
        "Waterloo",
        "Super Trouper",
        "Bossanova",
        "Lover",
        "Folklore",
        "I Put a Spell on You",
        "Baltimore",
        "Here Comes the Sun",
        "Fodder on My Wings",
        "Ring Ring"
    ])
    # expect(paragraph_tags).to_have_text([
    #     "Released: 1989",
    #     "Released: 1988",
    #     "Released: 1974",
    #     "Released: 1980",
    #     "Released: 1990",
    #     "Released: 2019",
    #     "Released: 2020",
    #     "Released: 1965",
    #     "Released: 1978",
    #     "Released: 1971",
    #     "Released: 1982",
    #     "Released: 1973"
    # ])

"""
The page returned by GET/albums should contain a link for each album listed.
It should link to '/albums/<id>', where <id> is the corresponding album's id.
That page should then show info about the album
"""   

def test_visit_album_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")

    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Doolittle'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Doolittle")
    year_tag = page.locator(".t-year")
    expect(year_tag).to_have_text("Released: 1989")

def test_visit_album_show_page_and_go_back(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")

    page.goto(f"http://{test_web_address}/albums") 
    page.click("text='Doolittle'")
    page.click("text='Go back to album list'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

def test_get_artists(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_web_app.sql")

    page.goto(f"http://{test_web_address}/artists")
    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])

def test_visit_artist_show_page(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")

    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Pixies")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Rock")

def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.fill("input[name='title']", "Test Album")
    page.fill("input[name='year']", "2024")
    page.click("text=Create Album")
    
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Test Album")
    year_tag = page.locator(".t-year")
    expect(year_tag).to_have_text("Released: 2024")

def test_validate_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add new album")
    page.click("text=Create Album")

    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Year can't be blank")

def test_create_artists(page, test_web_address, db_connection):
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add new artist")
    page.fill("input[name='name']", "Test Artist")
    page.fill("input[name='genre']", "Test Genre")
    page.click("text=Create Artist")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Test Artist")
    genre_tag = page.locator(".t-genre")
    expect(genre_tag).to_have_text("Genre: Test Genre")

def test_validate_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_web_app.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add new artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Artist can't be blank, Genre can't be blank")

