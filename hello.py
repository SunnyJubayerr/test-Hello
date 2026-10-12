import datetime

def main():
    print("=========================================")
    print(" 🎉 Welcome to my first GitHub Repo! 🎉 ")
    print("=========================================")
    
    name = input("\nWhat is your name? ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nHello, {name}! Thanks for checking out test-Hello.")
    print(f"Program executed at: {current_time}")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()