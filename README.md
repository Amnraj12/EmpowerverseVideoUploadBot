<!-- README STARTS HERE -->

# Empowerverse Video Bot

A Python-based application with a graphical user interface (GUI) that allows users to:
1. Log in to Empowerverse using their credentials.
2. Automatically fetch their API token upon successful login.
3. Provide an Instagram Reel URL for downloading and uploading the video to Empowerverse.
4. Log out securely.

---

## 📋 **Features**
- **Login & Logout**: Users log in with their Empowerverse credentials, and the bot fetches their API token for seamless integration.
- **Video Upload Workflow**:
  - Download Instagram Reel videos.
  - Upload the videos to Empowerverse using APIs.
  - Automatically clean up local files after a successful upload.
- **Async Operations**: High-performance concurrent operations using `asyncio` and `aiohttp`.
- **Progress Tracking**: Visual progress bars for downloading and uploading, powered by `tqdm`.

---

## 🛠️ **Technology Stack**
- **Programming Language**: Python
- **Libraries/Tools**:
  - `tkinter`: GUI creation.
  - `aiohttp`: For asynchronous API communication.
  - `yt_dlp`: For downloading videos from Instagram.
  - `tqdm`: For download/upload progress tracking.

---

## 📂 **Project Structure**
```plaintext
video-bot/
├── main.py                # Entry point for running the bot
├── gui.py                 # GUI implementation
├── video_downloader.py    # Logic for downloading Instagram videos
├── video_uploader.py      # Logic for uploading videos to Empowerverse
├── requirements.txt       # Project dependencies
└── README.md              # Documentation

🚀 Setup Instructions
1. Prerequisites
- Python (>=3.8)
 1. Install `pip`.

2. Clone Repository
