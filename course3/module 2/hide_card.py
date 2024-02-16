def hide_card(card_number):
    card_number = card_number.replace(" ", "")
    hidden_digits = '*' * 12
    hidden_card_number = hidden_digits + card_number[12:]

    return hidden_card_number
