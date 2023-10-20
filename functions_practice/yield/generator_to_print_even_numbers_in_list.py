
def even_funtion(args_list):
    for i in args_list:
        if i%2==0:
            yield i


input_list = [0,1,2,3,5,6,7,8,9,10]

print("Original list=",str(input_list))

print ("Even numbers in the list are",end=" ")

# res:list = even_funtion(input_list)
# for j in res:
    # print(j)
    # print(type(res))
for i in even_funtion(input_list):
    print (i,end=" ")