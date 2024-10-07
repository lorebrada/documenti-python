# esercizio numero 8.6 pagina 141

def city_country(city_name, country_origin):
    """Return a formatted string about cities and countries"""
    full_place = f"{city_name} {country_origin}"
    return full_place.title()

geography = city_country('Chicago,', 'United States')
print(geography)

geography = city_country('New Delhi', 'India')
print(geography)

geography = city_country('Rome', 'Italy')
print(geography)



#esercizio numero 8.7 pagina 142 

def make_album(artist_name, album_title):
    """Return a dictionary containing these two pieces of information."""
    info = {'first': artist_name, 'last': album_title}
    return info

album = make_album('John Lennon', 'Imagine')
print(album)


def make_album(artist_name, album_title, songs=None):
    """Return a dictionary containing these three pieces of information."""
    info = {'first': artist_name, 'last': album_title}
    if songs:
        info['songs'] = songs
    return songs

album = make_album('John Lennon', 'Imagine', songs=61)
print(album)


#esercizio numero 8.8

def get_make_album(artist_name, album_title):
    """Return a dictionary containing these two pieces of information."""
    info = f"{artist_name} {album_title}"
    return info.title()

while True:
    print("\nPlease tell me your favourite artist's name :")
    print("(enter 'q' at any time to quit)")

    f_name = input("artist name: ")
    if f_name == 'q':
        break

    a_title = input("album title: ")
    if a_title == 'q':
        break

    make_album = get_make_album(f_name, a_title)
    print(f"\nThis is the result of your input : {make_album}!")