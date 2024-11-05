import random
import time

class RealEstateAgentNPC:
    def __init__(self, name):
        self.name = name
        self.properties = {
            "Small House": {"price": 100, "renovated": False},
            "Medium House": {"price": 200, "renovated": False},
            "Large House": {"price": 400, "renovated": False}
        }

    def greet(self):
        print(f"{self.name}: Welcome to Kakariko Village's Real Estate! How can I assist you today?")

    def show_properties(self):
        print("\nHere are the properties available:")
        for prop, details in self.properties.items():
            renovated_status = "Yes" if details["renovated"] else "No"
            print(f"{prop} - Price: {details['price']} credits, Renovated: {renovated_status}")

    def buy_property(self, choice, player_credits):
        if choice not in self.properties:
            print("Invalid property choice.")
            return player_credits

        property_price = self.properties[choice]["price"]
        if player_credits >= property_price:
            player_credits -= property_price
            print(f"{self.name}: Congratulations! You are now the owner of {choice}.")
            del self.properties[choice]  # Remove property after purchase
        else:
            print(f"{self.name}: I'm afraid you don't have enough credits to buy {choice}.")
        return player_credits

    def sell_property(self, choice, player_properties, player_credits):
        if choice not in player_properties:
            print("You don't own this property.")
            return player_credits

        sell_price = int(self.properties[choice]["price"] * 0.8)  # 80% return on sell
        player_credits += sell_price
        print(f"{self.name}: You've sold {choice} for {sell_price} credits.")
        return player_credits

    def renovate_property(self, choice, player_credits):
        if choice not in self.properties:
            print("Invalid property choice.")
            return player_credits

        renovation_cost = int(self.properties[choice]["price"] * 0.5)  # 50% of original price
        if player_credits >= renovation_cost:
            player_credits -= renovation_cost
            self.properties[choice]["renovated"] = True
            print(f"{self.name}: {choice} has been successfully renovated!")
        else:
            print(f"{self.name}: You don't have enough credits to renovate {choice}.")
        return player_credits

    def negotiate(self, choice):
        if choice not in self.properties:
            print("Invalid property choice.")
            return

        # Random negotiation outcome
        success = random.choice([True, False])
        if success:
            discount = random.randint(10, 30)  # Discount between 10% and 30%
            self.properties[choice]["price"] -= int(self.properties[choice]["price"] * discount / 100)
            print(f"{self.name}: You've negotiated a {discount}% discount! New price is {self.properties[choice]['price']} credits.")
        else:
            print(f"{self.name}: Sorry, the price remains the same.")

def main():
    agent = RealEstateAgentNPC("Terry the Realtor")
    player_credits = 300
    player_properties = []

    agent.greet()
    time.sleep(1)

    while True:
        print("\nOptions: 1) View Properties 2) Buy Property 3) Sell Property 4) Renovate Property 5) Negotiate 6) Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            agent.show_properties()
        elif choice == "2":
            agent.show_properties()
            prop_choice = input("Enter the property name to buy: ")
            player_credits = agent.buy_property(prop_choice, player_credits)
            if prop_choice in agent.properties:
                player_properties.append(prop_choice)
        elif choice == "3":
            print("Your
