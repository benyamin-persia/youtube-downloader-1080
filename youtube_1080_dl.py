import yt_dlp # pip install yt-dlp

def download_video(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'ffmpeg_location': 'C:/ffmpeg-master-latest-win64-gpl-shared/bin',  # unzip this "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl-shared.zip"  in c:
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

link = input("Enter YouTube link: ")
download_video(link)
