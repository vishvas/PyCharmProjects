my_list = []

def permute(s):

    if len(s) ==0:
        return '\n--'

    for i in s:
        print(i)
        new_string = s.replace(i,'',1)
        print(new_string)
        permute(new_string)


    #return my_list


print(permute('abc'))
#print("Hello".replace('l','',1))