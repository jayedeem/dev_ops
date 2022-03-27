# stars = ""
# for i in range(1, 5, 2):
#     for j in range(0, 2, 1):
#         stars += "i"
#         print(j)


def rFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return rFib(n-1) + rFib(n-2)


rFib(4)
