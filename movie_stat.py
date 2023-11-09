REGULAR_PRICE_CODE = 0
NEW_RELEASE_PRICE_CODE = 1
CHILDREN_PRICE_CODE = 2
DUBBED_PRICE_CODE = 3

REGULAR_BASE_PRICE = 2
REGULAR_EXTRA_DAYS_COST = 1.5

NEW_RELEASE_PRICE_PER_DAY = 3

CHILDREN_BASE_PRICE = 1.5
CHILDREN_EXTRA_DAYS_COST = 1.5

DUBBED_BASE_PRICE = 4
DUBBED_EXTRA_DAYS_COST = 1.5

def calculate_regular_amount(days_rented):
    amount = REGULAR_BASE_PRICE
    if days_rented > 2:
        amount += (days_rented - 2) * REGULAR_EXTRA_DAYS_COST
    return amount

def calculate_new_release_amount(days_rented):
    return days_rented * NEW_RELEASE_PRICE_PER_DAY

def calculate_children_amount(days_rented):
    amount = CHILDREN_BASE_PRICE
    if days_rented > 3:
        amount += (days_rented - 3) * CHILDREN_EXTRA_DAYS_COST
    return amount

def calculate_dubbed_amount(days_rented):
    amount = DUBBED_BASE_PRICE
    if days_rented > 1:
        amount += (days_rented - 1) * DUBBED_EXTRA_DAYS_COST
    return amount

def calculate_amount(movie_price_code, days_rented):
    if movie_price_code == REGULAR_PRICE_CODE:
        return calculate_regular_amount(days_rented)
    elif movie_price_code == NEW_RELEASE_PRICE_CODE:
        return calculate_new_release_amount(days_rented)
    elif movie_price_code == CHILDREN_PRICE_CODE:
        return calculate_children_amount(days_rented)
    elif movie_price_code == DUBBED_PRICE_CODE:
        return calculate_dubbed_amount(days_rented)
    else:
        return 0  # Handle unknown price code

def generate_rental_statement(name, rentals):
    total_amount = 0
    frequent_renter_points = 0
    result = f"Rental Record for {name}\n"

    for rental in rentals:
        this_amount = calculate_amount(rental["movie"]["price_code"], rental["days_rented"])
        frequent_renter_points += 1

        if rental["movie"]["price_code"] == NEW_RELEASE_PRICE_CODE and rental["days_rented"] > 1:
            frequent_renter_points += 1

        result += f"\t{rental['movie']['title']}\t{this_amount}\n"
        total_amount += this_amount

    result += f"Amount owed is {total_amount}\n"
    result += f"You earned {frequent_renter_points} frequent renter points"

    return result
