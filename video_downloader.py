import yt_dlp
import os
from tqdm import tqdm

async def download_videos(reel_url, folder_name="videos", output_file="video.mp4"):
    """
    Downloads an Instagram reel from the given URL with progress display.
    
    Args:
        reel_url (str): The URL of the Instagram reel.
        folder_name (str): The folder to save the video.
        output_file (str): The name of the output file.
    """
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Set the full path for the output file
    output_path = os.path.join(folder_name, output_file)

    # Progress bar hook
    def tqdm_hook(d):
        """Hook for yt_dlp to integrate with tqdm progress bar."""
        if d['status'] == 'downloading':
            if not hasattr(tqdm_hook, "pbar"):
                tqdm_hook.pbar = tqdm(total=float(d.get("total_bytes", 0)), unit="B", unit_scale=True)
            tqdm_hook.pbar.n = float(d.get("downloaded_bytes", 0))
            tqdm_hook.pbar.refresh()
        elif d['status'] == 'finished':
            if hasattr(tqdm_hook, "pbar"):
                tqdm_hook.pbar.close()
                del tqdm_hook.pbar

    # yt_dlp options
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': output_path,  # Save file in the specified folder
        'progress_hooks': [tqdm_hook],  # Attach the progress bar
        'quiet': True,  # Suppress standard yt-dlp output
    }

    try:
        # Download the reel
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([reel_url])
        print(f"Download complete! Saved as {output_path}")
    except Exception as e:
        print(f"An error occurred during download: {e}")
        raise
