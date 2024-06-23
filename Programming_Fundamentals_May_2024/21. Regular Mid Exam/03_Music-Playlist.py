songs_list = input().split()
n = int(input())

for i in range(n):
    command_list = input().split(' * ')
    command = command_list[0]

    if command == 'Add Song':
        song = command_list[1]
        if song not in songs_list:
            songs_list.append(song)
            print(f'{song} successfully added')

    if command == 'Delete Song':
        number_songs = int(command_list[1])
        if len(songs_list) >= number_songs:
            deleted_songs = songs_list[:number_songs]
            songs_list = songs_list[number_songs:]
            print(f'{", ".join(map(str, deleted_songs))} deleted')

    if command == 'Shuffle Songs':
        start = int(command_list[1])
        end = int(command_list[2])
        if len(songs_list) > start and len(songs_list) > end:
            temp_song = songs_list[start]
            songs_list[start] = songs_list[end]
            songs_list[end] = temp_song
            print(f'{songs_list[start]} is swapped with {songs_list[end]}')

    if command == 'Insert':
        song_name = command_list[1]
        index = int(command_list[2])
        if len(songs_list) > index:
            if song_name not in songs_list:
                songs_list.insert(index, song_name)
                print(f'{song_name} successfully inserted')
            else:
                print('Song is already in the playlist')
        else:
            print('Index out of range')

    if command == 'Sort':
        songs_list = sorted(songs_list, reverse=True)

    if command == 'Play':
        print('Songs to Play:')
        for elm in songs_list:
            print(elm)
