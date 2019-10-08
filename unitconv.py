print("Hello, this unit converter will allow You to convert kilometers into miles.")


while True:
    print("Please, enter the kilometers that You would like to convert.")

    km = input("kilometers: ")

    km = float(km.replace(",", "."))

    miles = km * 0.621

    print("{0} km is {1} miles".format(km, miles))

    repeat = input("Would you like another convesrsion (yes/no)? ")

    if repeat != "yes":
        break
