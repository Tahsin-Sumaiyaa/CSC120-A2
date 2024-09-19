class Computer:


    # What attributes will it need?
    desc: str
    processor: str
    hdd: int
    memory: int
    os: str
    year: int
    price: int


    # How will you set up your constructor?

    def __init__(self,description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int) -> None:
        
        self.desc=description
        self.processor=processor_type
        self.hdd=hard_drive_capacity
        self.memory=memory
        self.os=operating_system
        self.year=year_made
        self.price=price

    
    # What methods will you need?

def main():
    desc= "Mac Pro (Late 2013)"
    processor= "3.5 GHc 6-Crore Intel Xeon E5"
    hdd= 1024
    memory= 64
    os= "macOS Big Sur"
    year= 2013
    price= 1500

    #Now, we will make our first computer
    computer= Computer(desc, processor, hdd, memory, os, year, price)

    print("\n")
    print("Description of the computer is:", desc)
    print("Processor type is:", processor)
    print("Hard-drive capacity is:", hdd)
    print("Memory of the computer is:", memory)
    print("Operating System is:", os)
    print("Year made is:", year)
    print("Price of the computer is:", price)
    print("\n")

if __name__ == "__main__":
    main()



        