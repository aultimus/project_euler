# https://projecteuler.net/problem=54
#
# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:
#
#     High Card: Highest value card.
#     One Pair: Two cards of the same value.
#     Two Pairs: Two different pairs.
#     Three of a Kind: Three cards of the same value.
#     Straight: All cards are consecutive values.
#     Flush: All cards of the same suit.
#     Full House: Three of a kind and a pair.
#     Four of a Kind: Four cards of the same value.
#     Straight Flush: All cards are consecutive values of same suit.
#     Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the
# highest value wins; for example, a pair of eights beats a pair of fives
# (see example 1 below). But if two ranks tie, for example, both players have
# a pair of queens, then highest cards in each hand are compared (see example
# 4 below); if the highest cards tie then the next highest cards are compared,
# and so on.
#
# Consider the following five hands dealt to two players:
# Hand        Player 1        Player 2        Winner
# 1       5H 5C 6S 7S KD
# Pair of Fives
#         2C 3S 8S 8D TD
# Pair of Eights
#         Player 2
# 2       5D 8C 9S JS AC
# Highest card Ace
#         2C 5C 7D 8S QH
# Highest card Queen
#         Player 1
# 3       2D 9C AS AH AC
# Three Aces
#         3D 6D 7D TD QD
# Flush with Diamonds
#         Player 2
# 4       4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
#         3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
#         Player 1
# 5       2H 2D 4C 4D 4S
# Full House
# With Three Fours
#         3C 3D 3S 9S 9D
# Full House
# with Three Threes
#         Player 1
#
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
# first five are Player 1's cards and the last five are Player 2's cards. You
# can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear
# winner.
#
# How many hands does Player 1 win?




import doctest

class Card(object):
    # Rank vals represent actual card rank values
    TWO         = 2
    THREE       = 3
    FOUR        = 4
    FIVE        = 5
    SIX         = 6
    SEVEN       = 7
    EIGHT       = 8
    NINE        = 9
    TEN         = 10
    JACK        = 11
    QUEEN       = 12
    KING        = 13
    ACE         = 14

    # arbitrary enum vals
    SPADES      = 20
    CLUBS       = 21
    HEARTS      = 22
    DIAMONDS    = 23

    def __init__(self, card):
        self.rank = rank_map[card[0]]
        self.suit = suit_map[card[1]]

    def __str__(self):
        return rank_repr[self.rank] + suit_repr[self.suit]

    def __cmp__(self, other):
        return self.__dict__ == other.__dict__

def is_royal_flush(hand):
    pass

class Hand(object):
    # Ordered enum
    HIGH_CARD       = [0, "HIGH_CARD"]
    ONE_PAIR        = [1, "ONE_PAIR"]
    TWO_PAIRS       = [2, "TWO_PAIRS"]
    THREE_OF_A_KIND = [3, "THREE_OF_A_KIND"]
    STRAIGHT        = [4, "STRAIGHT"]
    FLUSH           = [5, "FLUSH"]
    FULL_HOUSE      = [6, "FULL_HOUSE"]
    FOUR_OF_A_KIND  = [7, "FOUR_OF_A_KIND"]
    STRAIGHT_FLUSH  = [8, "STRAIGHT_FLUSH"]
    ROYAL_FLUSH     = [9, "ROYAL_FLUSH"]

    def __init__(self, cards):
        self.cards = [Card(card) for card in cards]
        self.val = (-1, "WTF")
        self.val = self.process_hand()

    def process_hand(self):
        if self.is_royal_flush():
            return Hand.ROYAL_FLUSH

        v = self.is_straight_flush()
        if v:
            return Hand.STRAIGHT_FLUSH, v

        v = self.is_four_of_a_kind()
        if v:
            return Hand.FOUR_OF_A_KIND, v

        v  = self.is_full_house()
        if v:
            return Hand.FULL_HOUSE, v

        v = self.is_flush()
        if v:
            return Hand.FLUSH, v

        v = self.is_straight()
        if v:
            return Hand.STRAIGHT, v

        v =  self.is_three_of_a_kind()
        if v:
            return Hand.THREE_OF_A_KIND, v

        v = self.is_two_pairs()
        if v:
            return Hand.TWO_PAIRS, v

        v = self.is_one_pair()
        if v:
            return Hand.ONE_PAIR, v

        return Hand.HIGH_CARD, self.get_high_card_val()

    def __str__(self):
        return str([card.__str__() for card in self.cards])

    def get_ranks(self):
        return [card.rank for card in self.cards]

    def same_suit(self):
        """
        >>> Hand(["TH", "3C", "4D", "5S", "TS"]).same_suit()
        False
        >>> Hand(["2D", "3C", "4C", "5C", "6C"]).same_suit()
        False
        >>> Hand(["2C", "3C", "4C", "5C", "6C"]).same_suit()
        True
        """
        first_suit = self.cards[0].suit
        return all([card.suit == first_suit for card in self.cards])

    def is_flush(self):
        """
        >>> Hand(["TH", "3C", "4D", "5S", "TS"]).is_flush()
        0
        >>> Hand(["2D", "3C", "4C", "5C", "6C"]).same_suit()
        0
        >>> Hand(["2C", "3C", "4C", "5C", "6C"]).same_suit() == Card.SIX
        True
        """
        if self.same_suit():
            return self.get_ranks().sorted()[-1]
        else:
            return 0

    is_flush = same_suit # Aliases

    def is_royal_flush(self):
        """
        >>> Hand(["TH", "JH", "QH", "KH", "AH"]).is_royal_flush()
        True
        >>> Hand(["TH", "JH", "QD", "KH", "AH"]).is_royal_flush()
        False
        """
        if not self.same_suit():
            return False
        ranks = self.get_ranks()
        if all([Card.TEN in ranks, Card.JACK in ranks, Card.QUEEN in ranks,
            Card.KING in ranks, Card.ACE in ranks]):
            return Card.ACE # for consistency

    def is_straight_flush(self):
        """
        >>> Hand(["2D", "3D", "4D", "5D", "6D"]).is_straight_flush() == Card.SIX
        True
        >>> Hand(["2D", "3D", "4D", "5D", "AD"]).is_straight_flush()
        0
        >>> Hand(["2D", "3D", "4D", "5D", "6C"]).is_straight_flush()
        0
        """
        if self.same_suit():
            return self.have_a_run()
        return 0

    def have_a_run(self):
        """
        Returns highest ranked card value if there's a run present, if not
        returns falsey value.
        >>> Hand(["8D", "9C", "TH", "JH", "QH"]).have_a_run() == Card.QUEEN
        True
        >>> Hand(["8D", "9C", "TH", "AH", "QH"]).have_a_run()
        0
        """
        r = self.get_ranks()
        r.sort()
        if (r[0]+1 == r[1] and r[1]+1 == r[2] and r[2] + 1 == r[3] and r[3]+1 == r[4]):
            return r[-1]
        else:
            return 0

    is_straight = have_a_run # aliases

    def is_four_of_a_kind(self):
        """
        >>> Hand(["KD","QD","QH","QC","QS"]).is_four_of_a_kind() == Card.QUEEN
        True
        >>> Hand(["KD","QD","QH","KC","QS"]).is_four_of_a_kind()
        0
        """
        ranks = self.get_ranks()
        for c in ranks:
            if ranks.count(c) == 4:
                return c
        return 0

    def is_full_house(self):
        """
        >>> Hand(["KD","KH","KS","8S","8C"]).is_full_house() == [Card.KING, Card.EIGHT]
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_full_house()
        []
        >>> Hand(["KD","KH","JS","JC","KC"]).is_full_house() == [Card.KING, Card.JACK]
        True
        """
        vals = [0,0]
        ranks = self.get_ranks()
        for r in ranks:
            if ranks.count(r) >= 3:
                vals[0] = r
            elif ranks.count(r) >= 2:
                vals[1] = r
        if 0 not in vals:
            return vals
        else:
            return []

    def is_three_of_a_kind(self):
        """
        >>> Hand(["KD","KH","KS","8S","8C"]).is_three_of_a_kind() == Card.KING
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_three_of_a_kind() == Card.KING
        True
        >>> Hand(["KD","8H","JS","JC","KC"]).is_three_of_a_kind()
        0
        """
        ranks = self.get_ranks()
        for r in ranks:
            if ranks.count(r) >=3:
                return r
        return 0

    def is_two_pairs(self):
        """
        >>> Hand(["KD","KH","KS","8S","8C"]).is_two_pairs() == set([Card.KING, Card.EIGHT])
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_two_pairs()
        set([])
        >>> Hand(["KD","8H","JS","JC","KC"]).is_two_pairs() == set([Card.JACK, Card.KING])
        True
        """
        pair_vals = set()
        ranks = self.get_ranks()
        for r in ranks:
            if ranks.count(r) >=2:
                pair_vals.add(r)
        if len(pair_vals) >= 2:
            return pair_vals
        else:
            return set()

    def is_one_pair(self):
        """
        >>> Hand(["KD","KH","JS","8S","5C"]).is_one_pair() == Card.KING
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_one_pair() == Card.KING
        True
        >>> Hand(["KD","8H","7S","QC","9C"]).is_one_pair()
        0
        """
        ranks = self.get_ranks()
        for r in ranks:
            if ranks.count(r) >=2:
                return r
        return 0

    def get_high_card_val(self):
        """
        >>> Hand(["KD","KH","JS","8S","5C"]).get_high_card_val() == Card.KING
        True
        >>> Hand(["7DD","2S","AS","8S","7C"]).get_high_card_val() == Card.ACE
        True
        >>> Hand(["2D","8H","7S","QC","9C"]).get_high_card_val() == Card.QUEEN
        True
        """
        return max(self.get_ranks())


suits = (("H", Card.HEARTS), ("C", Card.CLUBS), ("D", Card.DIAMONDS), ("S", Card.SPADES))
ranks = (("2", Card.TWO), ( "3", Card.THREE), ( "4", Card.FOUR), ( "5", Card.FIVE), (
"6", Card.SIX), ( "7", Card.SEVEN), ( "8", Card.EIGHT), ( "9", Card.NINE), ( "T", Card.TEN), (
"J", Card.JACK), ( "Q", Card.QUEEN), ( "K", Card.KING), ("A", Card.ACE))

suit_map    = dict(suits)
suit_repr   = dict((y,x) for x,y in suits)

rank_map    = dict(ranks)
rank_repr   = dict((y, x) for x, y in ranks)

class UnimplementedException(Exception):
    pass

def p1_wins(i):
    print "p1 wins"
    return i+1

doctest.testmod()

with open("p054_poker.txt") as f:
    games = [line.strip("\n").split() for line in f.readlines()]

p1_win_count = 0
for game in games:
    p1 = Hand(game[:5])
    p2 = Hand(game[5:])
    # Unpack our ugly data structure - TODO - streamline this
    (p1_hand_value, p1_hand_name), p1_aux_val = p1.val
    (p2_hand_value, p2_hand_name), p2_aux_val = p2.val
    print "\n", p1, p1_hand_name, "   ", p2, p2_hand_name
    if p1_hand_value > p2_hand_value:
        p1_win_count = p1_wins(p1_win_count)
    elif p1_hand_value < p2_hand_value:
        print "p2 wins"
    else:
        # we have equal hand types, check our aux info for more info on hand value
        # This tells us if we have a pair of eights or a pair of aces for example
        if p1_aux_val > p2_aux_val:
            p1_win_count = p1_wins(p1_win_count)
        elif p1_aux_val < p2_aux_val:
            print "p2 wins"
        else:
            # OK, hands are a draw e.g. both have pairs of eights,
            # compare highest cards in hand
            p1_hi = p1.get_high_card_val()
            p2_hi = p2.get_high_card_val()
            if p1_hi > p2_hi:
                p1_win_count = p1_wins(p1_win_count)
            elif p1_hi < p2_hi:
                print "p2 wins"
            else:
                print "Stalemate"
                raise UnimplementedException()

print "player one won", p1_win_count
