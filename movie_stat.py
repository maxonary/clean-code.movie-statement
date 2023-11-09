REGULAR_PRICE_CODE = 0
NEW_RELEASE_PRICE_CODE = 1
CHILDREN_PRICE_CODE = 2

REGULAR_BASE_PRICE = 2
REGULAR_EXTRA_DAYS_COST = 1.5

NEW_RELEASE_PRICE_PER_DAY = 3

CHILDREN_BASE_PRICE = 1.5
CHILDREN_EXTRA_DAYS_COST = 1.5

def generate_rental_statement(name, rentals):
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

    total_amount = 0
    frequent_renter_points = 0
    result = f"Rental Record for {name}\n"

    for rental in rentals:
        this_amount = 0
        movie = rental["movie"]
        days_rented = rental["days_rented"]

        if movie["price_code"] == REGULAR_PRICE_CODE:
            this_amount += REGULAR_BASE_PRICE
            if days_rented > 2:
                this_amount += (days_rented - 2) * REGULAR_EXTRA_DAYS_COST
        elif movie["price_code"] == NEW_RELEASE_PRICE_CODE:
            this_amount += days_rented * NEW_RELEASE_PRICE_PER_DAY
        else:
            this_amount += CHILDREN_BASE_PRICE
            if days_rented > 3:
                this_amount += (days_rented - 3) * CHILDREN_EXTRA_DAYS_COST

        frequent_renter_points += 1

        if movie["price_code"] == NEW_RELEASE_PRICE_CODE and days_rented > 1:
            frequent_renter_points += 1

        result += f"\t{movie['title']}\t{this_amount}\n"
        total_amount += this_amount

    result += f"Amount owed is {total_amount}\n"
    result += f"You earned {frequent_renter_points} frequent renter points"

    return result
