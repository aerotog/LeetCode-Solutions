# https://leetcode.com/problems/corporate-flight-bookings/
# Runtime: 1000 ms, faster than 58.14% of Python3 online submissions for Corporate Flight Bookings.
# Memory Usage: 26.5 MB, less than 100.00% of Python3 online submissions for Corporate Flight Bookings.

from typing import List


def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    seat_diffs = [0] * n

    for booking in bookings:
        seat_inc_index = booking[0]
        seat_dec_index = booking[1] + 1
        seats = booking[2]

        # Flights are 1-based indexed, so need to offset by -1 for the 0-based array
        seat_inc_index -= 1
        seat_dec_index -= 1

        seat_diffs[seat_inc_index] += seats

        if seat_dec_index < n:
            seat_diffs[seat_dec_index] -= seats

    seats = 0
    for seat_diff in seat_diffs:
        seats += seat_diff
        yield seats


bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
n = 5

for i in corpFlightBookings(bookings, n):
    print(i)
