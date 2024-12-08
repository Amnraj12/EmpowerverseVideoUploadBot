import aiohttp
import aiofiles
import os
from tqdm import tqdm

API_URL = 'https://api.socialverseapp.com'


async def get_upload_url(session, token):
    """Fetch the video upload URL and hash from the API."""
    headers = {"Flic-Token": token, "Content-Type": "application/json"}
    async with session.get(f"{API_URL}/posts/generate-upload-url", headers=headers) as response:
        if response.status == 200:
            response_data = await response.json()
            if 'url' in response_data and 'hash' in response_data:
                return response_data
            else:
                raise KeyError("Response missing 'url' or 'hash' keys")
        else:
            response_text = await response.text()
            raise Exception(f"Failed to fetch upload URL: {response_text}")


async def upload_video(session, upload_url, video_path):
    """Upload the video to the provided upload URL with a progress bar."""
    file_size = os.path.getsize(video_path)
    progress = tqdm(total=file_size, unit="B", unit_scale=True, desc="Uploading Video")

    with open(video_path, 'rb') as file:
        async with session.put(upload_url, data=file) as response:
            if response.status == 200:
                progress.update(file_size)  # Update progress to 100% upon completion
                progress.close()
                print("Video uploaded successfully.")
                return True
            else:
                progress.close()
                response_text = await response.text()
                raise Exception(f"Failed to upload video: {response_text}")


async def create_post(session, token, title, video_hash, category_id=25):
    """Create a post on Empowerverse using the video hash."""
    headers = {"Flic-Token": token, "Content-Type": "application/json"}
    data = {
        "title": title,
        "hash": video_hash,
        "is_available_in_public_feed": True,  # Ensure this is set to true for public feed visibility
        "category_id": category_id  # Replace with actual category ID if needed
    }
    async with session.post(f"{API_URL}/posts", headers=headers, json=data) as response:
        if response.status == 201:
            print("Post created successfully.")
            return await response.json()
        else:
            response_text = await response.text()
            raise Exception(f"Failed to create post: {response_text}")


async def upload_videos(title, token):
    """
    Main function to handle the video upload and post creation.
    Args:
        title: Title of the video.
        token: User-specific Flic Token for authentication.
    """
    video_path = './videos/video.mp4'  # Path to the downloaded video file
    async with aiohttp.ClientSession() as session:
        try:
            # Step 1: Get upload URL and hash
            upload_url_data = await get_upload_url(session, token)
            upload_url = upload_url_data['url']
            video_hash = upload_url_data['hash']

            # Step 2: Upload the video file
            await upload_video(session, upload_url, video_path)

            # Step 3: Create a post with the uploaded video hash
            post_response = await create_post(session, token, title, video_hash)
            print(f"Post created successfully: {post_response}")
        except KeyError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Ensure the video is deleted after processing
            if os.path.exists(video_path):
                try:
                    os.remove(video_path)
                    print(f"Video {video_path} deleted successfully.")
                except Exception as e:
                    print(f"Failed to delete video {video_path}: {e}")
