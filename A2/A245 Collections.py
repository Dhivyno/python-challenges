def cmp(self, other):
    # Check the suits
    if self.suit > other.suit: return 1
    if self.suit < other.suit: return -1
    # Suits are the same... check ranks
    if self.rank == 1: return 1
    if other.rank == 1: return -1
    if self.rank > other.rank: return 1
    if self.rank < other.rank: return -1
    # Ranks are the same... it's a tie
    return 0
