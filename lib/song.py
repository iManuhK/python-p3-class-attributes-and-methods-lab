class Song:
    count = 0
    genres = []
    artists = []
    def __init__(self, name, artist, genre):
        Song.add_song_to_count()
        Song.add_artist_to_count()
        Song.add_to_genres()
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, new_genre):
        if(new_genre.count <0):
            cls.genres.append(new_genre)

    @classmethod
    def add_artist_to_count(cls, new_artist):
        if(new_artist.count <0):
            cls.artists.append(new_artist)