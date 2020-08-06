

def rate_stack(stack):
    """
    the lower the better
    :param stack:
    :return:
    """
    rate = 0
    stack.cards.reverse()
    for i, card in enumerate(stack.cards, start=2):
        rate += min(abs(i - card.number), abs(101 - i - card.number))
    return rate