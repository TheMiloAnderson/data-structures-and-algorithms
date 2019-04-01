hand = [12, 7, 11, 5, 13, 6]

end = len(hand) - 1
while end > 1:
    for i in range(end):
        if hand[i] > hand[i + 1]:
            hand[i], hand[i + 1] = hand[i + 1], hand[i]
    end -= 1

print('hand')
