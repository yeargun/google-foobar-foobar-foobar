# if got hashmap f(number) --> occurence
# insert O(1) average, o(n) to create table
# later on two hashmaps traverse and remove occurences, if !=0, result is that
# o(n) at average
# space complexity shit asf


# n log n sort,

from collections import Counter
def Solution(): 
    counts1 = Counter(li1)
    counts2 = Counter(li2)
    biggerList = counts1 if len(counts1)>len(counts2) else counts2
    for elem in biggerList.elements():
        print(elem, counts2[elem])
        if(counts2[elem]- counts1[elem] !=0):
            return elem

