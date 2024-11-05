import tkinter as tk
from tkinter import messagebox
import random

class RealEstateDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Kakariko Village Real Estate Dashboard")
        self.root.geometry("500x400")

        self.properties = {
            "Small House": {"price": 100, "renovated": False},
            "Medium House": {"price": 200, "renovated": False},
            "Large House": {"price": 400, "renovated": False}
        }
        self.transaction_history = []
        self.player_credits = 300

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Real Estate Dashboard", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.credits_label = tk.Label(self.root, text=f"Credits: {self.player_credits}", font=("Helvetica", 12))
        self.credits_label.pack()

        self.property_list_label = tk.Label(self.root, text="Available Properties:", font=("Helvetica", 12))
        self.property_list_label.pack(pady=10)

        self.property_listbox = tk.Listbox(self.root)
        for prop in self.properties:
            self.property_listbox.insert(tk.END, f"{prop} - Price: {self.properties[prop]['price']} credits")
        self.property_listbox.pack(pady=5)

        self.buy_button = tk.Button(self.root, text="Buy Property", command=self.buy_property)
        self.buy_button.pack(pady=5)

        self.transaction_button = tk.Button(self.root, text="View Transaction History", command=self.view_transactions)
        self.transaction_button.pack(pady=5)

        self.notifications_button = tk.Button(self.root, text="View Notifications", command=self.show_notifications)
        self.notifications_button.pack(pady=5)

        self.new_property_button = tk.Button(self.root, text="New Property Listing", command=self.add_new_property)
        self.new_property_button.pack(pady=5)

    def buy_property(self):
        selected_property = self.property_listbox.curselection()
        if selected_property:
            property_name = self.property_listbox.get(selected_property[0]).split(" - ")[0]
            property_price = self.properties[property_name]["price"]
            if self.player_credits >= property_price:
                self.player_credits -= property_price
                self.transaction_history.append(f"Bought {property_name} for {property_price} credits.")
                self.update_dashboard()
                messagebox.showinfo("Transaction Success", f"Successfully bought {property_name}!")
            else:
                messagebox.showwarning("Insufficient Credits", "You do not have enough credits.")
        else:
            messagebox.showwarning("No Property Selected", "Please select a property to buy.")

    def view_transactions(self):
        transactions = "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."
        messagebox.showinfo("Transaction History", transactions)

    def show_notifications(self):
        notifications = [
            "New property listings available!",
            "Property prices have changed!"
        ]
        notifications_message = "\n".join(notifications)
        messagebox.showinfo("Notifications", notifications_message)

    def add_new_property(self):
        new_property = f"Large House {random.randint(1, 100)}"
        self.properties[new_property] = {"price": random.randint(150, 500), "renovated": False}
        self.property_listbox.insert(tk.END, f"{new_property} - Price: {self.properties[new_property]['price']} credits")
        self.transaction_history.append(f"New property {new_property} listed!")
        self.show_notifications()

    def update_dashboard(self):
        self.credits_label.config(text=f"Credits: {self.player_credits}")
        self.property_listbox.delete(0, tk.END)
        for prop in self.properties:
            self.property_listbox.insert(tk.END, f"{prop} - Price: {self.properties[prop]['price']} credits")


if __name__ == "__main__":
    root = tk.Tk()
    app = RealEstateDashboard(root)
    root.mainloop()
