

def fizzbuzz(min_value, target_num):
    for num in range(min_value, target_num + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        if num % 3 == 0:
            print("Fizz")
        if num % 5 == 0:
            print("Buzz")
        print(num)


fizzbuzz(50, 100)
