class hands:
    def __init__(self, name:str):
        self.hand = []
        self.name = name
    def __str__(self):
        return self.name
class PokerTable:

    def __init__(self, players: List[hands]):
        self.deck = pyCardDeck.Deck(cards=deck(),name='Poker deck',reshuffle=False)
        self.players = players
        self.table_cards = []
        print("Created a table with {} players".format(len(self.players)))
