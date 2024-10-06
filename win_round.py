# Numbered Cards

# You have a pack of 5 randomly numbered cards, which can range from 0-9. You can win if you can produce a higher two-digit number from your cards, than your opponent. Return True if your cards win that round.
# Worked Example

# win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True
# # Your cards can make the number 96
# # Your opponent can make the number 73
# # You win the round since 96 > 73

# Examples

# win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]) ➞ True

# win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]) ➞ False

# win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]) ➞ False



def win_round(you, opp):
    x = sorted(you)
    y = sorted(opp)
    if x[-2:]> y[-2:]:
        return True
    else:
        return False
print(win_round([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]))
print(win_round([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]))
print(win_round([4, 3, 4, 4, 5], [3, 2, 5, 4, 1]))



def win_round(your_cards, opponent_cards):
    # Sort the cards in descending order to form the highest possible two-digit number
    your_best = sorted(your_cards, reverse=True)[:2]
    opponent_best = sorted(opponent_cards, reverse=True)[:2]
    
    # Convert the two highest numbers to two-digit numbers
    your_number = int(f"{your_best[0]}{your_best[1]}")
    opponent_number = int(f"{opponent_best[0]}{opponent_best[1]}")
    
    # Return True if your number is higher than the opponent's number
    return your_number > opponent_number

# Test cases
test_cases = [
    ([2, 5, 2, 6, 9], [3, 7, 3, 1, 2]),  # True
    ([1, 2, 3, 4, 5], [9, 8, 7, 6, 5]),  # False
    ([4, 3, 4, 4, 5], [3, 2, 5, 4, 1])   # False
]

results = {str(test): win_round(*test) for test in test_cases}
results
