from bank import Account

def main():
    user = Account("Alice")
    print(user)

    try:
        user.deposit(200)
        print("After deposit:", user)

        user.withdraw(300)
        print("After withdrawal:", user)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
