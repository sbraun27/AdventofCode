import time


class Deck():
    def __init__(self, starting_cards, name):
        self.deck = starting_cards
        self.no_cards = len(starting_cards)
        self.card_history = []
        self.name = name

    def play_card(self):
        self.no_cards -= 1
        return self.deck.pop(0)

    def add_to_deck(self, card1, card2):
        self.deck.append(card1)
        self.deck.append(card2)
        self.no_cards += 2

    def calculate_score(self):
        self.score = 0
        for i, card in enumerate(reversed(self.deck)):
            self.score += card * (i+1)

        return self.score

    def check_history(self):
        if self.deck in self.card_history:
            return True
        else:
            self.card_history.append(self.deck.copy())
            return False


def load(file_path):
    with open(file_path) as f:
        file_input = f.read().split("\n\n")

    player1_cards = file_input[0].split("\n")
    player2_cards = file_input[1].split("\n")
    player1 = Deck([int(i) for i in player1_cards if i.isdigit()], "player1")
    player2 = Deck([int(i) for i in player2_cards if i.isdigit()], "player2")

    return player1, player2


def play_combat(player1, player2):
    while player1.no_cards > 0 and player2.no_cards > 0:
        player1_deals = player1.play_card()
        player2_deals = player2.play_card()
        if player1_deals > player2_deals:
            player1.add_to_deck(player1_deals, player2_deals)
        else:
            player2.add_to_deck(player2_deals, player1_deals)

    return player1 if player1.no_cards > 0 else player2


def play_recursive_combat(player1, player2):
    # If there was a previous round that had the same cards in the same order, in the same players deck, player 1 wins
    # If the current deck wasn't used before, play as normal
    # If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner is determined by playing another round of recursive combat
    # Else the player doesn't have enough cards to recurse, the winner is the player with the highest card value dealt

    while player1.no_cards > 0 and player2.no_cards > 0:
        player1_repeat = player1.check_history()
        player2_repeat = player2.check_history()
        if player1_repeat and player2_repeat:
            # Player 1 wins automatically
            return player1
        else:
            player1_deals = player1.play_card()
            player2_deals = player2.play_card()
            if player1_deals <= player1.no_cards and player2_deals <= player2.no_cards:
                sub_player1 = Deck(player1.deck[:player1_deals], "player1")
                sub_player2 = Deck(player2.deck[:player2_deals], "player2")
                sub_winner = play_recursive_combat(sub_player1, sub_player2)
                if "1" in sub_winner.name:
                    player1.add_to_deck(player1_deals, player2_deals)
                else:
                    player2.add_to_deck(player2_deals, player1_deals)
            else:
                if player1_deals > player2_deals:
                    player1.add_to_deck(player1_deals, player2_deals)
                else:
                    player2.add_to_deck(player2_deals, player1_deals)

    return player1 if player1.no_cards > 0 else player2


if __name__ == "__main__":
    player1, player2 = load("../input/day22.txt")
    start = time.time()
    winner = play_combat(player1, player2)
    part1 = winner.calculate_score()
    elapsed = round(time.time() - start, 3)
    print(
        f"Part 1: The winner was: {winner.name} with a score of: {part1}. Took: {elapsed} seconds.")

    player1, player2 = load("../input/day22.txt")  # Create a new set of decks
    start = time.time()
    winner = play_recursive_combat(player1, player2)
    part2 = winner.calculate_score()
    elapsed = round(time.time() - start, 3)
    print(
        f"Part 2: the winner was: {winner.name} with a score of {part2}. Took: {elapsed} seconds.")
