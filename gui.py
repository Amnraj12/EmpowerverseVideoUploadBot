import tkinter as tk
from tkinter import ttk
import asyncio
import aiohttp
from video_downloader import download_videos
from video_uploader import upload_videos


class VideoBotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Empowerverse Video Bot")
        self.root.geometry("400x420")  # Adjusted vertical rectangle
        self.root.resizable(False, False)
        self.flic_token = None  # Store the login token

        self.create_login_page()  # Start with the login page

    def create_login_page(self):
        """Creates the login page."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Login Frame
        login_frame = tk.Frame(self.root, bg="white")
        login_frame.pack(fill="both", expand=True)

        # Login Title
        tk.Label(
            login_frame,
            text="Login to Empowerverse",
            font=("Helvetica", 16, "bold"),
            fg="#E1306C",
            bg="white",
        ).pack(pady=(20, 10))

        # Username Entry
        tk.Label(login_frame, text="Username:", font=("Helvetica", 12), bg="white").pack(pady=(10, 5))
        self.username_entry = tk.Entry(login_frame, width=30, font=("Helvetica", 12))
        self.username_entry.pack(pady=5, ipady=5)

        # Password Entry
        tk.Label(login_frame, text="Password:", font=("Helvetica", 12), bg="white").pack(pady=(10, 5))
        self.password_entry = tk.Entry(login_frame, width=30, font=("Helvetica", 12), show="*")
        self.password_entry.pack(pady=5, ipady=5)

        # Login Button
        login_button = tk.Button(
            login_frame,
            text="Login",
            font=("Helvetica", 12, "bold"),
            bg="#E1306C",
            fg="white",
            command=self.login_user,
        )
        login_button.pack(pady=(20, 5))

        # Login Status
        self.login_status_label = tk.Label(login_frame, text="", font=("Helvetica", 10), bg="white", fg="red")
        self.login_status_label.pack(pady=(10, 5))

    async def fetch_token(self, username, password):
        """Fetch the Flic token using the API."""
        url = f"https://api.socialverseapp.com/user/token?username={username}&password={password}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    response_data = await response.json()
                    return response_data.get("token")
                else:
                    return None

    def login_user(self):
        """Handles user login."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username and password:
            asyncio.run(self.process_login(username, password))
        else:
            self.login_status_label.config(text="Please enter both username and password.")

    async def process_login(self, username, password):
        """Processes the login credentials."""
        self.login_status_label.config(text="Logging in...", fg="blue")
        self.root.update_idletasks()  # Immediately update the UI to show the status
        token = await self.fetch_token(username, password)
        if token:
            self.flic_token = token
            self.create_main_page()  # Proceed to the main page
        else:
            self.login_status_label.config(text="Invalid username or password.", fg="red")


    def create_main_page(self):
        """Creates the main video bot page."""
        for widget in self.root.winfo_children():
            widget.destroy()

        # Main Content Frame
        main_frame = tk.Frame(self.root, bg="white")
        main_frame.pack(fill="both", expand=True)

        # Title Label
        tk.Label(
            main_frame,
            text="Empowerverse Video Bot",
            font=("Helvetica", 16, "bold"),
            fg="#E1306C",
            bg="white",
        ).pack(pady=(20, 10))

        # URL Entry
        tk.Label(main_frame, text="Enter Video URL:", font=("Helvetica", 12), bg="white").pack(pady=(10, 5))
        self.url_entry = tk.Entry(main_frame, width=40, font=("Helvetica", 12))
        self.url_entry.pack(pady=5, ipady=6)

        # Title Entry
        tk.Label(main_frame, text="Enter Video Title (optional):", font=("Helvetica", 12), bg="white").pack(pady=(10, 5))
        self.title_entry = tk.Entry(main_frame, width=40, font=("Helvetica", 12))
        self.title_entry.pack(pady=5, ipady=6)

        # Download and Upload Button
        tk.Button(
            main_frame,
            text="Upload to Empowerverse",
            command=self.download_and_upload,
            bg="#E1306C",
            fg="white",
            font=("Helvetica", 12, "bold"),
            relief="flat",
        ).pack(pady=(20, 5))

        # Status Label
        self.status_label = tk.Label(
            main_frame,
            text="",
            font=("Helvetica", 10),
            fg="black",
            bg="white",
            wraplength=300,
            justify="center",
        )
        self.status_label.pack(pady=5)

        # Logout Button
        tk.Button(
            main_frame,
            text="Logout",
            command=self.logout_user,
            font=("Helvetica", 10, "bold"),
            bg="#555",
            fg="white",
        ).pack(pady=(10, 5))

    def update_status(self, message, color="black"):
        """Updates the status label with a message and color."""
        self.status_label.config(text=message, fg=color)
        self.status_label.update_idletasks()

    def download_and_upload(self):
        """Handles downloading and uploading the video."""
        url = self.url_entry.get()
        title = self.title_entry.get() or "Untitled Video"
        if url:
            self.update_status("Processing video...", color="#3498DB")
            self.root.after(0, asyncio.run, self.process_video(url, title))
        else:
            self.update_status("Please enter a video URL.", color="#E74C3C")

    async def process_video(self, url, title):
        """Processes the video download and upload."""
        try:
            self.update_status("Processing video...", color="#3498DB")
            await download_videos(url)

            self.update_status("Uploading video...", color="#3498DB")
            await upload_videos(title, self.flic_token)  # Pass the token here

            # Clear URL and Title fields, and show success message
            self.url_entry.delete(0, tk.END)
            self.title_entry.delete(0, tk.END)
            self.update_status("Uploaded successfully!", color="#27AE60")
        except Exception as e:
            self.update_status(f"An error occurred: {e}", color="#E74C3C")

    def logout_user(self):
        """Logs the user out and redirects to the login page."""
        self.flic_token = None
        self.create_login_page()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoBotGUI(root)
    root.mainloop()
