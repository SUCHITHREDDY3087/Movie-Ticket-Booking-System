# Movie Ticket Booking System (CLI Based)

movies = {
    "1": {"name": "Interstellar", "price": 200},
    "2": {"name": "Inception", "price": 180},
    "3": {"name": "Avengers", "price": 220}
}

shows = {
    "1": "10:00 AM",
    "2": "2:00 PM",
    "3": "7:00 PM"
}

snacks = {
    "1": {"name": "Popcorn", "price": 120},
    "2": {"name": "Coke", "price": 80},
    "3": {"name": "Nachos", "price": 150}
}


def choose_movie():
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie['name']} - ₹{movie['price']}")

    choice = input("Select movie (1-3): ")
    return movies.get(choice)


def choose_show():
    print("\nShow Timings:")
    for key, time in shows.items():
        print(f"{key}. {time}")

    choice = input("Select show time (1-3): ")
    return shows.get(choice)


def choose_seats():
    seats = int(input("\nEnter number of seats: "))
    return seats


def choose_snacks():
    total_snack_cost = 0
    selected_snacks = []

    print("\nAvailable Snacks:")
    for key, snack in snacks.items():
        print(f"{key}. {snack['name']} - ₹{snack['price']}")

    while True:
        choice = input("Select snack (1-3) or '0' to stop: ")
        if choice == "0":
            break
        if choice in snacks:
            qty = int(input("Enter quantity: "))
            cost = snacks[choice]["price"] * qty
            total_snack_cost += cost
            selected_snacks.append(
                f"{snacks[choice]['name']} x {qty} = ₹{cost}"
            )

    return selected_snacks, total_snack_cost


def payment_summary(movie, show, seats, snack_list, snack_cost):
    ticket_cost = movie["price"] * seats
    total_cost = ticket_cost + snack_cost

    print("\n========== PAYMENT SUMMARY ==========")
    print(f"Movie       : {movie['name']}")
    print(f"Show Time   : {show}")
    print(f"Seats       : {seats}")
    print(f"Ticket Cost : ₹{ticket_cost}")

    if snack_list:
        print("\nSnacks:")
        for snack in snack_list:
            print(" -", snack)
        print(f"Snack Cost  : ₹{snack_cost}")
    else:
        print("\nNo snacks selected")

    print("-----------------------------------")
    print(f"TOTAL AMOUNT: ₹{total_cost}")
    print("===================================")

    return total_cost


def main():
    print("🎬 Welcome to Movie Ticket Booking System 🎬")

    movie = choose_movie()
    if not movie:
        print("Invalid movie selection!")
        return

    show = choose_show()
    if not show:
        print("Invalid show selection!")
        return

    seats = choose_seats()
    snack_list, snack_cost = choose_snacks()

    total_amount = payment_summary(movie, show, seats, snack_list, snack_cost)

    payment = input("\nConfirm payment? (yes/no): ")
    if payment.lower() == "yes":
        print("\n✅ Booking Confirmed!")
        print("🎟 Enjoy your movie!")
    else:
        print("\n❌ Booking Cancelled")


if __name__ == "__main__":
    main()

