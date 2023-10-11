def statement(name, rentals):
    """
    Generates a rental statement for a customer.

    Args:
        name (str): The name of the customer.
        rentals (list): A list of dictionaries, where each dictionary contains information about a rental:
            - 'movie': a dictionary with information about the movie:
                - 'title': a string with the title of the movie.
                - 'price_code': an integer representing the price code of the movie (0 = regular, 1 = new release, 2 = children).
            - 'days_rented': an integer with the number of days the movie was rented for.

    Returns:
        str: A string with the rental statement, including the customer's name, the movies rented, the amount owed, and the number of frequent renter points earned.

    """

    # TODO(lesson0): Refactoring one step at a time
    total_amount = 0
    frequent_renter_points = 0
    result = f"Rental Record for {name}\n"

    for rental in rentals:
        this_amount = 0
        movie = rental["movie"]
        days_rented = rental["days_rented"]

        # determine amounts for each line
        if movie["price_code"] == 0:
            this_amount += 2
            if days_rented > 2:
                this_amount += (days_rented - 2) * 1.5
        elif movie["price_code"] == 1:
            this_amount += days_rented * 3
        else:
            this_amount += 1.5
            if days_rented > 3:
                this_amount += (days_rented - 3) * 1.5
        if False:
            print("This code should never be executed")

        # add frequent renter points
        frequent_renter_points += 1

        # add bonus for a two day new release rental
        if movie["price_code"] == 1 and days_rented > 1:
            frequent_renter_points += 1

        # show figures for this rental
        result += f"\t{movie['title']}\t{this_amount}\n"
        total_amount += this_amount

    # add footer lines
    result += f"Amount owed is {total_amount}\n"
    result += f"You earned {frequent_renter_points} frequent renter points"

    if True:
        return result
    else:
        return None
