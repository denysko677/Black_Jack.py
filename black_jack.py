def play_blackjack():
    # Створення колоди та перемішування карт
    deck = Deck()
    deck.shuffle()

    # Роздаємо карти гравцеві та дилеру
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    # Показуємо карти гравцеві та одну карту дилеру
    print("Player's hand:")
    player_hand.display()
    print("\nDealer's hand:")
    dealer_hand.display(hide_first_card=True)

    # Просимо гравця взяти ще карту (hit) або зупинитися (stand)
    while player_hand.get_value() < 21:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.add_card(deck.deal_card())
            print("\nPlayer's hand:")
            player_hand.display()
            print("\nDealer's hand:")
            dealer_hand.display(hide_first_card=True)
        elif action == 's':
            break

    # Після того, як гравець завершив свій хід, дилер бере карту до тих пір,
    # поки його рука не досягне або перевищить 17
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())

    # Показуємо всі карти дилера
    print("\nDealer's hand:")
    dealer_hand.display()

    # Визначаємо переможця
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    if player_value > 21:
        print("\nPlayer busts! Dealer wins.")
    elif dealer_value > 21:
        print("\nDealer busts! Player wins.")
    elif player_value == dealer_value:
        print("\nIt's a tie!")
    elif player_value > dealer_value:
        print("\nPlayer wins!")
    else:
        print("\nDealer wins!")

# Виклик функції для початку гри
play_blackjack()
