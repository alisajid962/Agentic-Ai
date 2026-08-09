song_count = {}
artists = set()
play_order = []
favorites = []
playlist_limit = int(input("Enter Playlist Limit: "))
favorite_threshold = int(input("Enter Favorite Threshold: "))
no_of_entries = int(input("Enter Number of Songs: "))
for i in range(no_of_entries):
    song = input("Enter Song Name: ")
    artist = input("Enter Artist Name: ")
    entry = (song, artist)
    song = entry[0]
    artist = entry[1]
    if song == "":
        print("Corrupted Entry.")
        continue

    if song in song_count:
        song_count[song] += 1
    else:
        song_count[song] = 1
    artists.add(artist)
    play_order.append(song)

    if song_count[song] >= favorite_threshold:
        if song not in favorites:
            favorites.append(song)

    print("Song Added Successfully.")

    if len(play_order) == playlist_limit:
        print("Playlist is Full.")
        break

print("\nSong Play Counts")

for i in song_count:
    print(i, "=", song_count[i])

print("\nFavorite Songs")

for i in favorites:
    print(i)
print("\nArtists")
for i in artists:
    print(i)
print("Play Order")

for i in play_order:
    print(i)