class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                num_aces += 1
                value += 11
            else:
                value += int(card.rank)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def display(self, hide_first_card=False):
        if hide_first_card:
            print("<Hidden Card>")
            for card in self.cards[1:]:
                print(card)
        else:
            for card in self.cards:
                print(card)
