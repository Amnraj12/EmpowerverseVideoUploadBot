# Empowerverse Video Bot

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

plaintext video-bot/ ├── main.py # Entry point for running the bot ├── gui.py # GUI implementation ├── video_downloader.py # Logic for downloading Instagram videos ├── video_uploader.py # Logic for uploading videos to Empowerverse ├── requirements.txt # Project dependencies └── README.md # Documentation

yaml
Copy code

---

## 🚀 Setup Instructions

### Prerequisites

- Python (>= 3.8)
- Pip (Python package manager)

### Clone Repository

bash git clone <repository-url> cd video-bot

shell
Copy code

### Install Dependencies

bash pip install -r requirements.txt

mathematica
Copy code

### Run the Application

Launch the bot using the following command:

bash python main.py

yaml
Copy code

---

## 📝 Usage Guide

### Login:

1. Enter your Empowerverse username and password.
2. Click **"Login"**. Upon success, the API token is fetched automatically.

### Provide Video URL:

1. Paste the Instagram Reel URL into the input field.
2. Optionally, provide a title for the video.

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
plaintext username=<your_username> password=<your_password>

markdown
Copy code
- **Response**:
json { "token": "<Flic-Token>" }

markdown
Copy code

### 2. Get Upload URL
- **Endpoint**: `/posts/generate-upload-url`
- **Method**: GET
- **Headers**:
json { "Flic-Token": "<your_flic_token>", "Content-Type": "application/json" }

markdown
Copy code

### 3. Upload Video
- **Endpoint**: `<upload_url>` (from Step 2)
- **Method**: PUT
- **Body**: Binary video file.

### 4. Create Post
- **Endpoint**: `/posts`
- **Method**: POST
- **Headers**:
json { "Flic-Token": "<your_flic_token>", "Content-Type": "application/json" }

markdown
Copy code
- **Body**:
json { "title": "<video_title>", "hash": "<video_hash>", "is_available_in_public_feed": true, "category_id": 25 }

yaml
Copy code

---

## ❓ FAQ

1. **How do I fetch my Flic-Token?**
 - The bot automatically fetches your token upon login.

2. **What happens to my videos after upload?**
 - They are deleted from your local system after a successful upload.

3. **Why is my upload failing?**
 - Check:
   - URL validity.
   - Internet connection.
   - Empowerverse credentials.

---

## 🧑‍💻 Contributors

- **Your Name**
- Email: `your-email@example.com`

---

## ⚠️ Disclaimer

This project is intended for personal or educational use. Respect the terms of service of Empowerverse an
