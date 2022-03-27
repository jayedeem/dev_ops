inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_of_snow):
    total_inches = 0
    for inches in inches_of_snow.values():
        total_inches += inches
    print("Total snowfall inches: ", total_inches)


user_input = int(input("How many inches of snow fell on Thursday? "))

inches_snow["Thursday"] = user_input
print_total_snowfall(inches_snow)
