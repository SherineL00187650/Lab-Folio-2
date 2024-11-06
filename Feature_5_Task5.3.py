import tkinter as tk
from tkinter import messagebox

class BadgeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Badge Tracker")
        self.root.geometry("400x400")

        self.badges = {
            "Warrior Badge": {"acquired": False, "achievement": "Proven strength in battle."},
            "Explorer Badge": {"acquired": False, "achievement": "Traveled across the land."},
            "Collector Badge": {"acquired": False, "achievement": "Collected all rare items."},
            "Champion Badge": {"acquired": False, "achievement": "Won the ultimate challenge."}
        }

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Your Badge Collection", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.badge_listbox = tk.Listbox(self.root, width=50)
        self.badge_listbox.pack(pady=5)

        self.view_badge_button = tk.Button(self.root, text="View Badge Details", command=self.view_badge_details)
        self.view_badge_button.pack(pady=5)

        self.update_badge_list()

    def update_badge_list(self):
        self.badge_listbox.delete(0, tk.END)
        for badge, details in self.badges.items():
            status = "Acquired" if details["acquired"] else "Not Acquired"
            self.badge_listbox.insert(tk.END, f"{badge} - {status}")

    def view_badge_details(self):
        selected_badge_index = self.badge_listbox.curselection()
        if selected_badge_index:
            badge_name = self.badge_listbox.get(selected_badge_index[0]).split(" - ")[0]
            badge_info = self.badges[badge_name]
            acquired_status = "Acquired" if badge_info["acquired"] else "Not Acquired"
            messagebox.showinfo(badge_name, f"Status: {acquired_status}\nAchievement: {badge_info['achievement']}")
        else:
            messagebox.showwarning("No Badge Selected", "Please select a badge to view details.")

    def acquire_badge(self, badge_name):
        if badge_name in self.badges:
            self.badges[badge_name]["acquired"] = True
            self.update_badge_list()
            messagebox.showinfo("Badge Acquired", f"You have acquired the {badge_name}!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BadgeTracker(root)

    # Simulating badge acquisition for demonstration
    app.acquire_badge("Warrior Badge")
    app.acquire_badge("Explorer Badge")

    root.mainloop()
