import yt_dlp
import requests

def verify_proxy_and_get_ip(proxy_url):
    """Verify proxy usage and return the IP address if successful."""
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    try:
        response = requests.get("https://api.ipify.org?format=json", proxies=proxies, timeout=10)
        ip = response.json()["ip"]
        print(f"Proxy is working. Public IP via proxy: {ip}")
        return True
    except requests.exceptions.ProxyError:
        print("Proxy Error: Authentication failed or proxy is unreachable.")
        return False
    except requests.exceptions.ConnectTimeout:
        print("Proxy Error: Connection timed out.")
        return False
    except Exception as e:
        print(f"Error verifying proxy: {e}")
        return False

def download_video(link, use_proxy, proxy_url=None):
    """Download video using yt_dlp with or without a proxy server."""
    ydl_opts = {
        'format': 'bestvideo+bestaudio',  # Ensures both video and audio are downloaded
        'outtmpl': 'e:/%(title)s.%(ext)s',  # Save files in Drive E
        'merge_output_format': 'mp4',       # Merges video and audio into MP4 format
        'ffmpeg_location': 'C:/ffmpeg/bin',  # Path to FFmpeg binaries
    }
    
    if use_proxy and proxy_url:
        ydl_opts['proxy'] = proxy_url  # Add proxy to options if enabled

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred during the download: {e}")

# Main Execution
proxy_url = 'socks5://@stockholm.se.socks.nordhold.net:1080'
link = input("Enter YouTube link: ")

# Verify proxy availability
proxy_available = verify_proxy_and_get_ip(proxy_url)

if not proxy_available:
    user_input = input("The proxy server is not available. Do you want to proceed with a normal internet connection? (yes/no): ").strip().lower()
    if user_input == 'yes':
        download_video(link, use_proxy=False)
    else:
        print("Download aborted by the user.")
else:
    download_video(link, use_proxy=True, proxy_url=proxy_url)
