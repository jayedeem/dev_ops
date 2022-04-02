"""Logic for UI Related"""
from dataclasses import dataclass


@dataclass
class DonationMenu:
    def __init__(self, donation_amt: float = 0.0, username: str = "") -> None:
        self.donation_amt = donation_amt
        self.username = username

    def show_homepage() -> None:
        """Display Homepage Prompt"""
        print("       === DonateMe Homepage ===       ")
        print("----------------------------------------")
        print("| 1. Login        | 2. Register        |")
        print("| 3. Donate       | 4. Show Donations  |")
        print("----------------------------------------")
        print("|             5. Exit                  |")
        print("----------------------------------------")

    def donate(self, amount) -> float:
        """Handle Donation Logic"""
        print("Thank you for your donation!")
        self.donation_amt += amount
        return self.donation_amt

    def donation_to_str(self) -> None:
        """Show Donation string"""
        return f"{self.username} donated ${self.donation_amt}!"
