# Display Credit Card number

card_Num = input('Enter your card number\n')

last_digits_ofCard = card_Num[12::]

four_star = '*' * 4 + ' '

display_Number = four_star * 3 + last_digits_ofCard

print(display_Number) 