#Author: JTI 9/26/21 
free_throw_scored = input ("How many free throws did you score? ")
regular_basket_scored = input ("How many regular baskets did you score?")
three_pointers_scored = input ("How many three pointers did you score? ")

total = int(free_throw_scored) + int(regular_basket_scored) * 2 + int(three_pointers_scored) * 3

print(total)

