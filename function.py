
def my_function(most_frequent):
    print(most_frequent)
most_frequent = input("Please enter a string: ")

len = str(most_frequent)
dict= {}
for i in len:
    dict[i]= dict.get(i, 0)+1
   
my_function(dict)
