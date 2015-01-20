
import doctest

class Card(object):
    # Rank vals represent values
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
    HIGH_CARD       = (0, "HIGH_CARD")
    ONE_PAIR        = (1, "ONE_PAIR")
    TWO_PAIRS       = (2, "TWO_PAIRS")
    THREE_OF_A_KIND = (3, "THREE_OF_A_KIND")
    STRAIGHT        = (4, "STRAIGHT")
    FLUSH           = (5, "FLUSH")
    FULL_HOUSE      = (6, "FULL_HOUSE")
    FOUR_OF_A_KIND  = (7, "FOUR_OF_A_KIND")
    STRAIGHT_FLUSH  = (8, "STRAIGHT_FLUSH")
    ROYAL_FLUSH     = (9, "ROYAL_FLUSH")

    def __init__(self, cards):
        self.cards = [Card(card) for card in cards]
        self.val = (-1, "WTF")
        self.process_hand()

    def process_hand(self):
        if self.is_royal_flush():
            self.val = Hand.ROYAL_FLUSH
        elif self.is_straight_flush():
            self.val = Hand.STRAIGHT_FLUSH
        elif self.is_four_of_a_kind():
            self.val = Hand.FOUR_OF_A_KIND
        elif self.is_full_house():
            self.val = Hand.FULL_HOUSE
        elif self.is_flush():
            self.val = Hand.FLUSH
        elif self.is_straight():
            self.val = Hand.STRAIGHT
        elif self.is_three_of_a_kind():
            self.val = Hand.THREE_OF_A_KIND
        elif self.is_two_pairs():
            self.val = Hand.TWO_PAIRS
        elif self.is_one_pair():
            self.val = Hand.ONE_PAIR
        else:
            self.val = Hand.HIGH_CARD

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
        return all([Card.TEN in ranks, Card.JACK in ranks, Card.QUEEN in ranks,
            Card.KING in ranks, Card.ACE in ranks])

    def is_straight_flush(self):
        """
        >>> Hand(["2D", "3D", "4D", "5D", "6D"]).is_straight_flush()
        True
        >>> Hand(["2D", "3D", "4D", "5D", "AD"]).is_straight_flush()
        False
        >>> Hand(["2D", "3D", "4D", "5D", "6C"]).is_straight_flush()
        False
        """
        return self.same_suit() and self.have_a_run()

    def have_a_run(self):
        """
        >>> Hand(["8D", "9C", "TH", "JH", "QH"]).have_a_run()
        True
        >>> Hand(["8D", "9C", "TH", "AH", "QH"]).have_a_run()
        False
        """
        r = self.get_ranks()
        r.sort()
        return (r[0]+1 == r[1] and r[1]+1 == r[2] and r[2] + 1 == r[3] and r[3]+1 == r[4])

    is_straight = have_a_run # aliases

    def is_four_of_a_kind(self):
        """
        >>> Hand(["KD","QD","QH","QC","QS"]).is_four_of_a_kind()
        True
        >>> Hand(["KD","QD","QH","KC","QS"]).is_four_of_a_kind()
        False
        """
        ranks = self.get_ranks()
        for c in ranks:
            if ranks.count(c) == 4:
                return True
        return False

    def is_full_house(self):
        """
        >>> Hand(["KD","KH","KS","8S","8C"]).is_full_house()
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_full_house()
        False
        >>> Hand(["KD","KH","JS","JC","KC"]).is_full_house()
        True
        """
        ranks = self.get_ranks()
        counts = [ranks.count(r) for r in ranks]
        return 2 in counts and 3 in counts

    def is_three_of_a_kind(self):
        """
        >>> Hand(["KD","KH","KS","8S","8C"]).is_three_of_a_kind()
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_three_of_a_kind()
        True
        >>> Hand(["KD","8H","JS","JC","KC"]).is_three_of_a_kind()
        False
        """
        ranks = self.get_ranks()
        counts = [ranks.count(r) for r in ranks]
        return 3 in counts

    def is_two_pairs(self):
        """
        >>> Hand(["KD","KH","KS","8S","8C"]).is_two_pairs()
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_two_pairs()
        False
        >>> Hand(["KD","8H","JS","JC","KC"]).is_two_pairs()
        True
        """
        pair_vals = set()
        ranks = self.get_ranks()
        for r in ranks:
            if ranks.count(r) >=2:
                pair_vals.add(r)
        return len(pair_vals) >= 2

    def is_one_pair(self):
        """
        >>> Hand(["KD","KH","JS","8S","5C"]).is_one_pair()
        True
        >>> Hand(["KD","KH","KS","8S","7C"]).is_one_pair()
        True
        >>> Hand(["KD","8H","7S","QC","9C"]).is_one_pair()
        False
        """
        ranks = self.get_ranks()
        for r in ranks:
            if ranks.count(r) >=2:
                return True
        return False

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

doctest.testmod()



with open("p054_poker.txt") as f:
    games = [line.strip("\n").split() for line in f.readlines()]

p1_wins = 0
for game in games:
    p1 = Hand(game[:5])
    p2 = Hand(game[5:])
    print "\n", p1, p1.val[1], "   ", p2, p2.val[1]
    if p1.val > p2.val:
        print "p1 wins"
        p1_wins +=1
    elif p1.val < p2.val:
        print "p2 wins"
        continue
    else: # equal hands
        if p1.val == Hand.HIGH_CARD:
            p1_high = p1.get_high_card_val()
            p2_high = p2.get_high_card_val()
            if p1_high > p2_high:
                p1_wins +=1
                print "p1 wins"
            elif p1_high < p2_high:
                print "p2 wins"
                continue
            else:
                #draw on high cards - MORE WORK NEEDED
                raise UnimplementedException()
        else:
            # hands have drawn - MORE WORK NEEDED
            raise UnimplementedException()

