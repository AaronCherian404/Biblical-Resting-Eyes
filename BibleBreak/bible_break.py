import tkinter as tk
from tkinter import messagebox
import time
import random
from threading import Timer
import os
from datetime import datetime

class BibleBreakApp:
    def __init__(self):
        # Create main window but keep it hidden
        self.root = tk.Tk()
        self.root.withdraw()
        
        # Dictionary of Bible verses (reference: text)
        self.bible_verses = {
            "1 Thessalonians 5:16": "Rejoice always",
            "John 11:35": "Jesus wept",
            "1 John 4:8": "God is love",
            "1 Thessalonians 5:19": "Do not quench",
            "1 Thessalonians 5:20": "Do not despise",
            "1 Thessalonians 5:21": "Test all things",
            "1 Thessalonians 5:22": "Abstain from evil",
            "Romans 12:12": "Rejoicing in hope",
            "1 Thessalonians 5:18": "Give thanks always",
            "1 Thessalonians 5:17": "Pray without ceasing"
        }
        
        self.break_interval = 40 * 60  # 20 minutes in seconds
        self.current_verse = None
        self.timer = None
        self.break_window = None
        
        # Start the monitoring
        self.start_monitoring()
        
        # Start the main event loop
        self.root.mainloop()

    def start_monitoring(self):
        """Start the timer for the next break"""
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(self.break_interval, self.show_break_window)
        self.timer.start()

    def show_break_window(self):
        """Display the break window with a random Bible verse"""
        self.break_window = tk.Toplevel(self.root)
        self.break_window.title("Bible Break")
        self.break_window.attributes('-fullscreen', True)
        self.break_window.attributes('-topmost', True)
        self.break_window.configure(bg='black')
        
        # Randomly select a verse
        self.current_verse = random.choice(list(self.bible_verses.items()))
        reference, verse = self.current_verse
        
        # Create and pack widgets
        verse_label = tk.Label(
            self.break_window,
            text=f"Type the following verse to continue:\n{reference}",
            fg='white',
            bg='black',
            font=('Arial', 16)
        )
        verse_label.pack(pady=50)
        
        self.entry = tk.Entry(self.break_window, width=100)
        self.entry.pack(pady=20)
        
        submit_button = tk.Button(
            self.break_window,
            text="Submit",
            command=self.check_verse
        )
        submit_button.pack()
        
        # Bind Enter key to submit
        self.break_window.bind('<Return>', lambda e: self.check_verse())
        
        # Disable the close button
        self.break_window.protocol("WM_DELETE_WINDOW", lambda: None)

    def check_verse(self):
        """Check if the entered text matches the Bible verse"""
        user_input = self.entry.get().strip().lower()
        correct_verse = self.current_verse[1].strip().lower()
        
        if user_input == correct_verse:
            self.break_window.destroy()
            self.break_window = None
            self.start_monitoring()
        else:
            messagebox.showwarning("Incorrect", "Please try again with the exact verse text.")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = BibleBreakApp()