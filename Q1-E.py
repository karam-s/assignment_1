L=["Network" , "Math" , "Programming", "Physics" , "Music"]

length = []
for i in L:
    x =len(i)
    length.append(x)
the_longest_item=max(length)
the_index_for_the_longest_item=length.index(the_longest_item)

print ("the longest item in list is "+str(L[the_index_for_the_longest_item])+"\
And its length "+str(the_longest_item))

