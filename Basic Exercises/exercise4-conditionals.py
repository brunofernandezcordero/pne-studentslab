def letter_score(score):
    if 0 <= score < 3:
        letter = "F"
    elif 3 <= score < 5:
        letter = "D"
    elif 5 <= score < 7:
        letter = "C"
    elif 7 <= score < 9:
        letter = "B"
    else:
        letter = "A"
    return letter

print("Score 9.5",letter_score(9.5))
print("Score 7.0",letter_score(7.0))
print("Score 5.5",letter_score(5.5))
print("Score 3.2",letter_score(3.2))
print("Score 1.0",letter_score(1))