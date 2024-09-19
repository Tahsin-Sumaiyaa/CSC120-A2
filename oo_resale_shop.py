from typing import Optional

class ResaleShop:


    # What attributes will it need?
    inventory: list


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)

    def __init__(self):
        self.inventory=[]
        self.item_id_counter = 0


    # What methods will you need?

    '''def buy(self,c):
        print("Trying to add", c, "to inventory...")
        self.inventory.append(c)
        print("Success!")'''

    def buy(self, c):
        print("Trying to add", c, "to inventory...")
        self.item_id_counter += 1
        self.inventory.append({"id": self.item_id_counter, "computer": c})
        print("Success!")    

    def sell(self, c):
        print("Trying to remove", c, "from inventory...")
        if c in self.inventory:
            self.inventory.remove(c)
            print("Success!")
        else:
            print(f"{c} not found in inventory.")

    def update_price(self, item_id, new_price):
        print("Trying to update price...")
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print(f"Item {item_id} not found. Cannot update price.")          

    def print_inventory(self):
        print("Trying to display inventory...")
        if self.inventory:
            for item in self.inventory:
                print(f'Item ID: {item["id"]} : {item["computer"]}')
        else:
            print("No inventory to display.") 


    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        for item in self.inventory:
            if item["id"] == item_id:
                computer = item["computer"]
                if computer.year_made < 2000:
                    computer.price = 0  # too old to sell, donation only
                elif computer.year_made < 2012:
                    computer.price = 250  # heavily-discounted price
                elif computer.year_made < 2018:
                    computer.price = 550  # discounted price
                else:
                    computer.price = 1000  # recent stuff
                
                if new_os:
                    computer.update_os(new_os)
                print(f"Item ID {item_id} refurbished with new price {computer.price} and OS {computer.operating_system}.")
                return
        print(f"Item ID {item_id} not found.")   


def main():

    myShop: ResaleShop = ResaleShop()
    print("\nThere are", len(myShop.inventory), "items in stock.")

    c= "MY AWESOME COMPUTER!"
    d= "MY CARDBOARD COMPUTER"

    myShop.buy(c)
    print("There are now", len(myShop.inventory), "items in stock.")
    #print(myShop.inventory)
    myShop.sell(d)
    print("There are now", len(myShop.inventory), "items in stock.")

    myShop.print_inventory()
    '''myShop.refurbish(1, "macOS Monterey")
    myShop.print_inventory()

    myShop.sell(1)
    myShop.print_inventory()


    print("\n")'''


if __name__ == "__main__":
    main()            
