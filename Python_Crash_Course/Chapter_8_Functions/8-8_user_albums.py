def make_album(artist, album, song_num=None):
    """Return a dictionary of information about a music album"""
    album_dic = {
        "artist": artist,
        "album": album,
    }
    if song_num:
        album_dic["number of songs"] = song_num
    return album_dic


while True:
    u_album = input("\n(press q to quit anytime)\nEnter in your favorite album: ")
    if u_album == "q":
        break
    u_artist = input("Artist: ")
    if u_artist == "q":
        break
    print(make_album(u_artist, u_album))
