from transacation_mngr import add_transaction, view_transactions

def main():
    print("\nRod's Personal $$$ Manager")

    #Create command line/menu
    while True:
        print("\nMenu:")
        print("1- Add a transaction")
        print("2- View transaction")
        print("3- Exit")

        choice = input("Enter your choices: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            print("Exiting...\n")
            break
        else:
            print("Invalid input. Try Again!")

if __name__ == "__main__":
    main()