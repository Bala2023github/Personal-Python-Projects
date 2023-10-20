# initializing string


def count_of_geeks(test_string):
     for i in test_string:
          if i=='geeks':
            yield i

test_string = " There are many geeks around you, \
              geeks are known for teaching other geeks"

test_string = test_string.split()

print("Original string is : ", test_string)

count = 0

for j in count_of_geeks(test_string):

     count+=1
print(count)    


