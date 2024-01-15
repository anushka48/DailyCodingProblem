# DailyCodingProblem + My Notes
## A Collection of Technical Questions

This is my effort to continuously practive technical questions and further my understanding of data structures and algorithms.

## Ordered Dict
#### import
from collections import OrderedDict

d = OrderedDict()
#### popitem: pops item from end in LIFO fashion if last is True, from begin in FIFO fashion of last is False
popped = d.popitem(last = True | False)
#### move_to_end: moves item with key to the end if last = True; begin if last = False
d.move_to_end(key, last = True | False)

## defaultdict
#### import
from collections import defaultdict

d = defaultdict()
#### to set:
d['x'] = 'y'
#### Get: to get make SURE to use get function in case it's not in dict
d.get('z')
#### AND make sure to compare return to None in if statement; in case key does exist and return is 0. Ex:
if (d.get('z') == None) and not if (d.get('z')) # in case (key, val) = ('z',0)

## sort vs sorted
#### sorted: is NOT in-place, works for iterables like list, dict, and set
l_sorted = sorted(l, key = lambda <fxn>, reverse = True | False)
<fxn> could be: x : (x[0], x[1]), len, other built-in functions...

#### sort: IS in-place from list class, only works on lists
l.sort(reverse = True | False, key = lambda x: <fxn>)

## heapq
#### Import
import heapq
#### Build
list1 = list() #populate it

heapq.heapify(list1)
#### Common Functions
heapq.heappush(list1, elem)

heapq.heappop(list1)

heapq.nsmallest(n, list1) # returns list; NOTE: this will be sorted but indexing list1[0:n] will not

heapq.nlargest(n, list1) 

list(heapq.merge(list1, list2) # will merge two sorted lists and return them as a list

## unpack

*list or *str will unpack the iterable into individual elements.

ex) l = [1,2,3] so *l will yield 1,2,3

s = "app", so [*s] = ["a","p","p"]

**dict will unpack the dictionary into its keys

ex) d = {1:a, 2:b, 3:c} so **d will yield a,b,c

