import asyncio
from gui import VideoBotGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = VideoBotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
