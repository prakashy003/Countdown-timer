import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.root = tk.Tk()
        self.root.title("Countdown Timer")
        self.label = tk.Label(self.root, font=("Arial", 24), text="")
        self.label.pack(pady=20)
        self.root.geometry('250x250')
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_timer, state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

        self.remaining = 0
        self.timer_running = False
        self.paused_time = 0

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.run_timer()

    def run_timer(self):
        if self.remaining <= 0:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.DISABLED)
            self.label.config(text="Time's up!")
        else:
            mins, secs = divmod(self.remaining, 60)
            timer = f"{mins:02d}:{secs:02d}"
            self.label.config(text=timer)
            self.remaining -= 1
            if self.timer_running:
                self.root.after(1000, self.run_timer)

    def pause_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.paused_time = self.remaining
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(text="Resume")
        else:
            self.timer_running = True
            self.remaining = self.paused_time
            self.run_timer()
            self.start_button.config(state=tk.DISABLED)
            self.pause_button.config(text="Pause")
            self.reset_button.config(state=tk.NORMAL)

    def reset_timer(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
        self.label.config(text="")
        self.remaining = self.duration
        self.paused_time = 0

    def start(self):
        self.remaining = self.duration
        self.root.mainloop()

# Example usage: countdown for 5 minutes (300 seconds)
timer = CountdownTimer(300)
timer.start()
