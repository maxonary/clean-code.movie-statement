import unittest
from movie_stat import generate_rental_statement


class TestRental(unittest.TestCase):
    def test_regular_movie_rental_for_1_day(self):
        rentals = [
            {"movie": {"title": "The Godfather", "price_code": 0}, "days_rented": 1}
        ]
        expected_result = "Rental Record for John\n\tThe Godfather\t2\nAmount owed is 2\nYou earned 1 frequent renter points"
        self.assertEqual(generate_rental_statement("John", rentals), expected_result)

    def test_regular_movie_rental_for_3_days(self):
        rentals = [
            {"movie": {"title": "The Godfather", "price_code": 0}, "days_rented": 3}
        ]
        expected_result = "Rental Record for John\n\tThe Godfather\t3.5\nAmount owed is 3.5\nYou earned 1 frequent renter points"
        self.assertEqual(generate_rental_statement("John", rentals), expected_result)

    def test_new_release_movie_rental_for_1_day(self):
        rentals = [
            {"movie": {"title": "Avengers: Endgame", "price_code": 1}, "days_rented": 1}
        ]
        expected_result = "Rental Record for John\n\tAvengers: Endgame\t3\nAmount owed is 3\nYou earned 1 frequent renter points"
        self.assertEqual(generate_rental_statement("John", rentals), expected_result)

    def test_new_release_movie_rental_for_2_days(self):
        rentals = [
            {"movie": {"title": "Avengers: Endgame", "price_code": 1}, "days_rented": 2}
        ]
        expected_result = "Rental Record for John\n\tAvengers: Endgame\t6\nAmount owed is 6\nYou earned 2 frequent renter points"
        self.assertEqual(generate_rental_statement("John", rentals), expected_result)

    def test_children_movie_rental_for_1_day(self):
        rentals = [
            {"movie": {"title": "The Lion King", "price_code": 2}, "days_rented": 1}
        ]
        expected_result = "Rental Record for John\n\tThe Lion King\t1.5\nAmount owed is 1.5\nYou earned 1 frequent renter points"
        self.assertEqual(generate_rental_statement("John", rentals), expected_result)

    def test_children_movie_rental_for_4_days(self):
        rentals = [
            {"movie": {"title": "The Lion King", "price_code": 2}, "days_rented": 4}
        ]
        expected_result = "Rental Record for John\n\tThe Lion King\t3.0\nAmount owed is 3.0\nYou earned 1 frequent renter points"
        self.assertEqual(generate_rental_statement("John", rentals), expected_result)


if __name__ == "__main__":
    unittest.main()
