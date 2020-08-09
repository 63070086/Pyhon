"""Blackjack"""
def main():
    """intput card"""
    numcard = int(input())
    score = 0
    stop = 0
    testa = 0
    if numcard == 2 or numcard == 3:
        for _ in range(numcard):
            card = input()
            if card.isdecimal() and int(card) >= 2 and int(card) <= 10:
                score += int(card)
            elif card == "J" or card == "Q" or card == "K":
                score += 10
            elif card == "A":
                testa += 1
                score += 11
                if score >= 22:
                    score -= 10
            else:
                stop += 1
        if score != 0 and stop == 0:
            if testa > 0 and score > 21:
                while score > 21:
                    score -= 10
                print(score)
            else:
                print(score)
main()
