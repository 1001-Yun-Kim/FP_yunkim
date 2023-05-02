import finalGame


def test_creating_a_deck():
    deck = finalGame.create_deck()
    deck_1 = deck[:]
    shuffled_deck = finalGame.shuffle(deck)
    assert deck_1 != shuffled_deck
    print("'test_creating_a_deck' function passed successfully")


def test_dealing_9_cards():
    deck_1 = finalGame.create_deck()
    shuffled_deck_1 = finalGame.shuffle(deck_1)
    _, shuffled_deck_1 = finalGame.deal(shuffled_deck_1)

    deck_2 = finalGame.create_deck()
    shuffled_deck_2 = finalGame.shuffle(deck_2)

    assert len(shuffled_deck_1) == 23
    assert len(shuffled_deck_2) == 32
    print("'test_dealing_9_cards' function passed successfully")


def test__deal_1_cards():
    deck = finalGame.create_deck()
    shuffled_deck = finalGame.shuffle(deck)
    _, shuffled_deck = finalGame.deal(shuffled_deck)
    shuffled_deck_1 = shuffled_deck[:]
    _, shuffled_deck_2 = finalGame.deal(shuffled_deck)

    assert len(shuffled_deck_1) - 1 == len(shuffled_deck_2)
    print("'test__deal_1_cards' function passed successfully")


def test_updating_card():
    new_card = ['CL', 3]
    deck = finalGame.create_deck()
    shuffled_deck = finalGame.shuffle(deck)
    board, _ = finalGame.deal(shuffled_deck)
    board = finalGame.update_card(board, new_card, [0, 0])

    assert board[0][0] == new_card
    print("'test_updating_card' function passed successfully")


def test_run():
    row_one = ['DM', 1], ['DM', 8], ['HR', 9]
    row_two = ['HR', 2], ['HR', 1], ['SP', 4]
    row_three = ['CL', 2], ['CL', 3], ['CL', 4]
    board = [row_one, row_two, row_three]

    won, score, state = finalGame.verify_matching(board, 0)

    assert won
    assert score == 25
    assert state == 'Run'
    print("'test_run' function passed successfully")


if __name__ == '__main__':
    test_creating_a_deck()
    test_dealing_9_cards()
    test__deal_1_cards()
    test_updating_card()
    test_run()
