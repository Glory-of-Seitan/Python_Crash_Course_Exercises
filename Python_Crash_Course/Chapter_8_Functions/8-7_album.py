def make_album(artist, album, song_num = None):
    """Return a dictionary of information about a music album"""
    album_dic = {'artist': artist, 'album': album,}
    if song_num:
        album_dic['number of songs'] = song_num
    return album_dic

print(make_album('linkin park', 'meteora', '12?'))
print(make_album('kelly clarkson', 'breakaway'))
print(make_album('xtina', 'back to basics'))