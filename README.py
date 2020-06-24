try:
    from random import randint

    a = randint(0, 10)
    b = 0
    print("You have 3 chance")

    while b <= 3:
        if b == 3:
            print("*********   START AGAIN   *********")
        else:
            c = int(input(f"Try again{b+1}: "))
            if c == a:
                print("Good Work Play Again")
                break
            elif c > a:
                print("too high try again")
            elif c < a:
                print("too low try again ")
            else:
                print("not good try again")
        b = b + 1


except ValueError:
    print("Enter integer value")
