import asyncio, sys

async def download(torrent_file):
    torrent = read_torrent(torrent_file)
    peer_addresses= await get_peers(torrent)
    file_pieces = asyncio.Queue()
    file_saver = FileSaver(file_pieces_queue)
    peers = [Peer(addr, file_pieces) for addr in peer_addresses]

    await asyncio.gather( *[peers.downlaod() for peer in peers] )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download(sys.argv[1]))
    loop.close()
