import re
import tkinter
import tqdm
from tkinter import filedialog
from pytube import Playlist
from time import sleep
from tqdm import tqdm


class downloader:

    def yt_downloader(self):
        tkinter.Tk().withdraw()
        YOUTUBE_STREAM_AUDIO = input('Input stream ID(140 for mp3): ')  # modify this value to download a different stream
        print('Select download path:')
        DOWNLOAD_DIR = filedialog.askdirectory()
        url = input('Input YT Playlist URL: ')
        playlist = Playlist(url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        print(len(playlist.video_urls), 'videos in playlist:')
        #amount = len(playlist.video_urls)
        #x=1
        #for url in playlist.video_urls:
            #print(url)
        print('')
        print('Download started...')
        for video in tqdm(playlist.videos):
            sleep(1)
            print('')
            print (video.title)
            #print('Download started: downloading',x,'of',amount,'(',video.title,(''),')')
            #x=x + 1

            audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            audioStream.download(output_path=DOWNLOAD_DIR, filename= video.title +".mp3")

Downloader = downloader()
Downloader.yt_downloader()
