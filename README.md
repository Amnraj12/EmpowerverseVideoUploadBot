# Empowerverse Video Upload Bot

A Python-based application with a graphical user interface (GUI) that simplifies video management. The bot allows users to log in, download Instagram Reels, and upload them to Empowerverse seamlessly.

---

## 📋 Features

- **Login & Logout**: 
  - Secure login with Empowerverse credentials.
  - Automatically fetch API tokens for a smooth workflow.
- **Video Upload Workflow**:
  - Download Instagram Reels videos.
  - Upload videos to Empowerverse using APIs.
  - Automatically clean up local files post-upload.
- **Async Operations**: 
  - High-performance tasks using `asyncio` and `aiohttp`.
- **Progress Tracking**: 
  - Visual progress bars for downloads/uploads powered by `tqdm`.

---

## 🛠️ Technology Stack

- **Programming Language**: Python
- **Libraries/Tools**:
  - `tkinter` - GUI creation.
  - `aiohttp` - Asynchronous API calls.
  - `yt_dlp` - Download videos from Instagram.
  - `tqdm` - Progress tracking for tasks.

---

## 📂 Project Structure

```plaintext
EmpowerverseVideoUploadBot/
├── main.py                # Entry point for running the bot
├── gui.py                 # GUI implementation
├── video_downloader.py    # Logic for downloading Instagram videos
├── video_uploader.py      # Logic for uploading videos to Empowerverse
├── requirements.txt       # Project dependencies
└── README.md              # Documentation
```

---

## 🚀 Setup Instructions

### Prerequisites

- Python (>= 3.8)
- Pip (Python package manager)

### Clone Repository
```
git clone <repository-url> 
cd video-bot
```

### Install Dependencies
```
pip install -r requirements.txt
```


### Run the Application

Launch the bot using the following command:
```
python main.py
```

---

## 📝 Usage Guide

### Login:

1. Enter your Empowerverse username and password.
2. Click **"Login"**. Upon success, the API token is fetched automatically, and you'll be redirected to the main screen.

### Provide Video URL:

1. Paste the Instagram Reel URL into the provided input field.
2. Optionally, provide a title for the video post.

### Upload Video:

1. Click **"Upload to Empowerverse"**.
2. The bot:
   - Downloads the video.
   - Uploads it to Empowerverse.
   - Cleans up local files after a successful upload.

### Logout:

Click **"Logout"** to return to the login screen and clear your session.

---

## 🔄 Workflow Explanation

### Step 1: User Authentication

- User logs in with Empowerverse credentials.
- Bot fetches the Flic-Token via `/user/token` API.

### Step 2: Video Download

- `yt_dlp` fetches the video from the provided URL.
- Progress tracked using `tqdm`.

### Step 3: Video Upload

- Pre-signed upload URL retrieved via API.
- Video uploaded using `aiohttp`.
- Progress displayed with `tqdm`.

### Step 4: Post Creation

- Video post created on Empowerverse using video hash and title.

### Step 5: Cleanup

- Local files are deleted after successful upload.

---

## 🌟 Key Libraries Used

1. **`asyncio`**: 
   - Manages asynchronous operations like API calls and file uploads.

2. **`aiohttp`**:
   - Makes asynchronous HTTP requests for login, uploading videos, and creating posts.

3. **`yt_dlp`**:
   - Downloads Instagram Reels efficiently.

4. **`tqdm`**:
   - Provides progress bars for user-friendly tracking.

---

## 🌐 API Reference

### 1. User Login
- **Endpoint**: `/user/token`
- **Method**: GET
- **Query Parameters**:
```
username=<your_username>
password=<your_password>
```

- **Response**:
```
{ "token": "<Flic-Token>" }
```

### 2. Get Upload URL
- **Endpoint**: `/posts/generate-upload-url`
- **Method**: GET
- **Headers**:
  ```
  { "Flic-Token": "<your_flic_token>",
    "Content-Type": "application/json" }
  ```

### 3. Upload Video
- **Endpoint**: `<upload_url>` (provided by the previous API)
- **Method**: PUT
- **Body**: Binary video file.

### 4. Create Post
- **Endpoint**: `/posts`
- **Method**: POST
- **Headers**:
  ```
  { "Flic-Token": "<your_flic_token>",
    "Content-Type": "application/json" }
  ```

- **Body**:
  ```
  { "title": "<video_title>",
    "hash": "<video_hash>",
    "is_available_in_public_feed": true,
    "category_id": 25 }
  ```


---

## ❓ FAQ

1. **How do I fetch my Flic-Token?**
 - You do not need to manually fetch the token. The bot fetches it automatically upon successful login.

2. **What happens to my videos after upload?**
 - They are deleted from your local system after a successful upload.

3. **Why is my upload failing?**
 - Check:
   - Ensure the video URL is correct and publicly accessible.
   - Check your internet connection.
   - Verify your Empowerverse credentials.

---

## 🙏 Acknowledgments

This project was built using the following tools and resources:

- Python and its vibrant open-source community.
- Libraries like `yt_dlp`, `aiohttp`, and `tqdm`.
- The Empowerverse platform for providing the API and inspiration.

## 📜 License

This repository is protected under copyright law.  
- You may view and clone this repository for personal, non-commercial use only.  
- Modification, distribution, or commercial use is strictly prohibited.  

For additional permissions, please contact `amnraj125@example.com`.


## ⚠️ Disclaimer

This project is intended for personal or educational use. Please respect the terms of service of Empowerverse and Instagram.
