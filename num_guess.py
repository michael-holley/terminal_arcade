#!/usr/bin/env python3

import random


print("::::    ::: :::    ::: ::::    ::::  :::::::::  :::::::::: :::::::::        ::::::::  :::    ::: :::::::::: ::::::::   ::::::::  :::::::::: :::::::::")  
print(":+:+:   :+: :+:    :+: +:+:+: :+:+:+ :+:    :+: :+:        :+:    :+:      :+:    :+: :+:    :+: :+:       :+:    :+: :+:    :+: :+:        :+:    :+:")
print(":+:+:+  +:+ +:+    +:+ +:+ +:+:+ +:+ +:+    +:+ +:+        +:+    +:+      +:+        +:+    +:+ +:+       +:+        +:+        +:+        +:+    +:+") 
print("+#+ +:+ +#+ +#+    +:+ +#+  +:+  +#+ +#++:++#+  +#++:++#   +#++:++#:       :#:        +#+    +:+ +#++:++#  +#++:++#++ +#++:++#++ +#++:++#   +#++:++#:")  
print("+#+  +#+#+# +#+    +#+ +#+       +#+ +#+    +#+ +#+        +#+    +#+      +#+   +#+# +#+    +#+ +#+              +#+        +#+ +#+        +#+    +#+")
print("#+#   #+#+# #+#    #+# #+#       #+# #+#    #+# #+#        #+#    #+#      #+#    #+# #+#    #+# #+#       #+#    #+# #+#    #+# #+#        #+#    #+#")
print("###    ####  ########  ###       ### #########  ########## ###    ###       ########   ########  ########## ########   ########  ########## ###    ###\n") 

print("\n")
print("-" * 50)
print("\nI am thinking of a number between 1 and 20.")
print("I bet you can't guess it in 3 tries or less!\n")
print("-" * 50)

random_number = random.randint(1, 20)
guess = input("What is your first guess? ")
tries = 1

while tries < 3:
    if int(guess) > random_number:
        tries = tries + 1
        print("\nYou are too high!")
        guess = input("Try Again: ")
    elif int(guess) < random_number:
        tries = tries + 1
        print("\nYou are too low!")
        guess = input("Try Again: ")
    elif int(guess) == random_number:
        print("YOU GOT IT!")
        break

print(f"\nThe number was {random_number}")
