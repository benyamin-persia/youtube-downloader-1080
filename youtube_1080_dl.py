import yt_dlp
import requests

def get_public_ip(proxy_url=None):
    """Get the public IP address, optionally using a proxy."""
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    } if proxy_url else None
    
    try:
        response = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        return response.json()["ip"]
    except Exception as e:
        return f"Error retrieving IP: {e}"

def verify_proxy(proxy_url):
    """Verify proxy usage by comparing the IP before and after applying the proxy."""
    print("Checking IP without proxy...")
    ip_without_proxy = get_public_ip()
    print(f"IP without proxy: {ip_without_proxy}")
    
    print("Checking IP with proxy...")
    ip_with_proxy = get_public_ip(proxy_url)
    print(f"IP with proxy: {ip_with_proxy}")
    
    if ip_with_proxy != ip_without_proxy:
        print("Proxy is working correctly.")
    else:
        print("Proxy is not being used or failed to connect.")

def download_video(link):
    """Download video using yt_dlp with a proxy server."""
    proxy_url = 'socks5://username:password@stockholm.se.socks.nordhold.net:1080'
    
    # Verify the proxy before proceeding
    verify_proxy(proxy_url)
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio',  # Ensures both video and audio are downloaded
        'outtmpl': 'e:/%(title)s.%(ext)s',  # Save files in Drive E
        'merge_output_format': 'mp4',       # Merges video and audio into MP4 format
        'ffmpeg_location': 'C:/ffmpeg/bin',  # Path to FFmpeg binaries
        'proxy': proxy_url,                 # Proxy details
    }
    
    # Download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred during the download: {e}")

# Input YouTube link
link = input("Enter YouTube link: ")
download_video(link)
