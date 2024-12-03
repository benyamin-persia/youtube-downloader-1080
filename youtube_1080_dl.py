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
    except requests.exceptions.ProxyError:
        return "Proxy Error: Authentication failed or proxy is unreachable"
    except requests.exceptions.ConnectTimeout:
        return "Proxy Error: Connection timed out"
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
    
    if "Proxy Error" not in ip_with_proxy and ip_with_proxy != ip_without_proxy:
        print("Proxy is working correctly.")
        return True
    else:
        print("Proxy is not being used or failed to connect.")
        return False

def download_video(link, use_proxy):
    """Download video using yt_dlp with or without a proxy server."""
    proxy_url = 'socks5://uUqMyyy199BW37rANvgQk8xH:P6Vcwex2UpHz65eFBTrcH1Py@stockholm.se.socks.nordhold.net:1080'
    
    ydl_opts = {
        'format': 'bestvideo+bestaudio',  # Ensures both video and audio are downloaded
        'outtmpl': 'e:/%(title)s.%(ext)s',  # Save files in Drive E
        'merge_output_format': 'mp4',       # Merges video and audio into MP4 format
        'ffmpeg_location': 'C:/ffmpeg/bin',  # Path to FFmpeg binaries
    }
    
    if use_proxy:
        ydl_opts['proxy'] = proxy_url  # Add proxy to options if enabled

    # Download the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred during the download: {e}")

# Main Execution
link = input("Enter YouTube link: ")

# Verify proxy availability
proxy_url = 'socks5://username:password@stockholm.se.socks.nordhold.net:1080' # Put your NordVpn username password here
proxy_available = verify_proxy(proxy_url)

if not proxy_available:
    user_input = input("The proxy server is not available. Do you want to proceed with a normal internet connection? (yes/no): ").strip().lower()
    if user_input == 'yes':
        download_video(link, use_proxy=False)
    else:
        print("Download aborted by the user.")
else:
    download_video(link, use_proxy=True)
