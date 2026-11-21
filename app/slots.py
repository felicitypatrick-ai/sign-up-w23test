"""Northside Food Pantry: open pickup slots for the sign-up page (course sample code)."""
 
 
def slots_left(capacity, booked):
    """Return how many pickup slots are still open."""
    return capacity - booked
 
 
def can_book(capacity, booked, party_size=1):
    """Return True when the party fits in the open slots."""
    return party_size <= slots_left(capacity, booked)
