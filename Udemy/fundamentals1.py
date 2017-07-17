print('Hello %s' %('Harsh'))
print('Floating No %10.2f' %(12.144)) #%n1.n2f = n1 means total character and n2 means after floating points
print('First: {x} Second:{y} Third:{x}'.format(x='Inserted',y='Second'))
print('First: %s, Second: %1.2f, Third: %r' %('hi!',3.14,22))

my_list = [1,2,3]
print(len(my_list))

my_list = ['one','two','three',4,5]
print(my_list[:])
print(my_list[1:])
print(my_list[:3])
print(my_list[::-1])
print(my_list + ['new item']) #note here it is just printing with combined valye, not actually new list added to my_list

#to change it permentatly reassign
my_list =my_list + ['new item']
print(my_list)
print(my_list*2)

# array vs List : no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint (like we've seen above).
l = [1,2,3]
print(l)
print(l.append("Hello"))
print(l)
print(l.pop(0)) #pop usually remove last element if index is not specidied
print(l)
l.append(["Abc","CDE"]) #[2, 3, 'Hello', ['Abc', 'CDE']]
print(l.pop()) #['Abc', 'CDE']
l.extend(["Vishvas","Patel"])
print(l)

#list append vs extend methods
print("index is %s" %l.index("Vishvas"))

l.insert(2,'inserted') #insert the value at given index
l.insert(4,'inserted')
print(l)

l.remove('inserted') #remove first occurance
print(l)

#sorting list.sort() or list.reverse() method is permenant
new_list = ['a','e','x','b','c']
print(new_list)
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
matrix = [lst_1,lst_2,lst_3]
print(matrix[0])
print(matrix[1][0]) #here unlike numpy matrix[:][0] => [1,4,7] but we can use list comprehension
first_col = [row[0] for row in matrix]
print(first_col)
print(lst_1.count(5))


my_file = open('test.txt')
print(my_file.read())
print(my_file.read()) #Blank line bcz no it reached to the last point
my_file.seek(0)
print(my_file.read())
my_file.seek(0)
print(my_file.readlines()) # ['Hello, this is a quick test file']
my_file.close()

my_file = open('test.txt','w+')
my_file.write('This is a new line') #OverWrite the existing file content
my_file.close()

my_file = open('test.txt','r')
print(my_file.read())

for line in open('test.txt'):
    print('--'+line)






