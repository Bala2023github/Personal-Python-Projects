

def sum_of_args(*numbers):
    result = 0

    for x in numbers:
        result+=x
    return result

print(sum_of_args(1,2,3,4,5))