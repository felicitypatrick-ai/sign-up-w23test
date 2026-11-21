import unittest
 
from app.slots import can_book, slots_left
 
 
class SlotTests(unittest.TestCase):
    def test_slots_left_counts_open_slots(self):
        self.assertEqual(slots_left(20, 15), 5)
 
    def test_slots_left_never_below_zero(self):
        self.assertEqual(slots_left(20, 25), 0)
 
    def test_small_party_fits(self):
        self.assertTrue(can_book(20, 18, party_size=2))
 
    def test_full_day_refuses_booking(self):
        self.assertFalse(can_book(20, 20))
