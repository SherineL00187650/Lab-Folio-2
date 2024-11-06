import tkinter as tk
from tkinter import messagebox

class BadgeStore:
    def __init__(self, root):
        self.root = root
        self.root.title("Badge Storefront")
        self.root.geometry("400x400")

        self.badges = {
            "Warrior Badge": 100,
            "Explorer Badge": 150,
            "Collector Badge": 200,
            "Champion Badge": 250
        }
        self.player_credits = 300
        self.purchased_badges = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Badge Storefront", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.credits_label = tk.Label(self.root, text=f"Available Credits: {self.player_credits}", font=("Helvetica", 12))
        self.credits_label.pack()

        self.badge_list_label = tk.Label(self.root, text="Available Badges:", font=("Helvetica", 12))
        self.badge_list_label.pack(pady=10)

        self.badge_listbox = tk.Listbox(self.root)
        for badge, price in self.badges.items():
            self.badge_listbox.insert(tk.END, f"{badge} - Price: {price} credits")
        self.badge_listbox.pack(pady=5)

        self.purchase_button = tk.Button(self.root, text="Purchase Badge", command=self.purchase_badge)
        self.purchase_button.pack(pady=10)

        self.purchased_badges_button = tk.Button(self.root, text="View Purchased Badges", command=self.view_purchased_badges)
        self.purchased_badges_button.pack(pady=5)

    def purchase_badge(self):
        selected_badge_index = self.badge_listbox.curselection()
        if selected_badge_index:
            badge_info = self.badge_listbox.get(selected_badge_index[0])
            badge_name = badge_info.split(" - ")[0]
            badge_price = self.badges[badge_name]

            if self.player_credits >= badge_price:
                self.player_credits -= badge_price
                self.purchased_badges.append(badge_name)
                self.update_storefront()
                messagebox.showinfo("Purchase Success", f"You have purchased the {badge_name}!")
            else:
                messagebox.showwarning("Insufficient Credits", "You do not have enough credits to purchase this badge.")
        else:
            messagebox.showwarning("No Badge Selected", "Please select a badge to purchase.")

    def view_purchased_badges(self):
        if self.purchased_badges:
            badges = "\n".join(self.purchased_badges)
            messagebox.showinfo("Purchased Badges", f"You own:\n{badges}")
        else:
            messagebox.showinfo("Purchased Badges", "You have not purchased any badges yet.")

    def update_storefront(self):
        self.credits_label.config(text=f"Available Credits: {self.player_credits}")
        self.badge_listbox.delete(0, tk.END)
        for badge, price in self.badges.items():
            self.badge_listbox.insert(tk.END, f"{badge} - Price: {price} credits")

if __name__ == "__main__":
    root = tk.Tk()
    app = BadgeStore(root)
    root.mainloop()
