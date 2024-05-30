def BDecode(file):
    with open(file, 'rb') as torrent:
        torrent_data = torrent.readlines()[:1]
        print(torrent_data)
    return 0

BDecode('./test_files/test.torrent')
