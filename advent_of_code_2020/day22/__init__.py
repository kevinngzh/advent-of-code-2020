import re


PLAYER_PATTERN = re.compile(r"Player (\d+):")


def parse_deck(raw_deck):
    lines = raw_deck.split("\n")

    player = PLAYER_PATTERN.match(lines[0]).group(1)
    cards = [int(line) for line in lines[1:]]

    return int(player), cards


def parse_input(input_):
    return [parse_deck(deck) for deck in input_.split("\n\n")]


class CombatGame:
    def __init__(self, decks):
        self.decks = {player: deck.copy() for player, deck in decks}

        self.round = 0

    def __iter__(self):
        return self

    def __next__(self):
        played_cards = {}

        for player, deck in self.decks.items():
            played_cards[deck.pop(0)] = player

        winning_card = max(played_cards.keys())
        winner = played_cards.pop(winning_card)

        self.decks[winner].append(winning_card)
        self.decks[winner].extend(list(played_cards))

        self.round += 1

        # Cannot `raise` in the earlier `for` loop it could iterate over the
        # winning player's deck first and `pop()` the first card.
        for deck in self.decks.values():
            if not len(deck):
                raise StopIteration

    def get_score(self, player):
        score = 0
        deck = self.decks[player]

        for i in range(1, 1 + len(deck)):
            score += i * deck[-i]

        return score


def part1(decks):
    game = CombatGame(decks)

    try:
        while True:
            next(game)
    except StopIteration:
        scores = []

        for player in game.decks:
            player_score = game.get_score(player)
            scores.append(player_score)

            print(player, player_score)

        return max(scores)


def part2(entries):
    pass
