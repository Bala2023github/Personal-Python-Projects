

def concatenate(**kwargs):
    result = ""

    for x in kwargs.values():
        result+=x
    return result

print(concatenate(a='Testing',b='Python',c='Kwargs'))