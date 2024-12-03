import yt_dlp 
def download_video(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'ffmpeg_location': 'C:/ffmpeg/bin',  # Replace with the actual path
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

link = input("Enter YouTube link: ")
download_video(link)
