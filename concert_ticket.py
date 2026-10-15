def main():
    age = int(input("How old are you?"))
   
    if age >= 65:
        print("You got senior ticket for $10")

    elif age < 13:
        print("You got child ticket for $8")

    else:
        print("You got general admission: $1")

main()