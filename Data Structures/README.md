# Data Structures and Algorithms
### Linked List

One disadvantage of using arrays to store data is that arrays are static structures and therefore cannot be easily extended or reduced to fit the data set. A linked list is a linear data structure where each element is a separate object.
A linked list is a dynamic data structure. The number of nodes in a list is not fixed and can grow and shrink on demand. Any application which has to deal with an unknown number of objects will need to use a linked list.
One disadvantage of a linked list against an array is that it does not allow direct access to the individual elements. If you want to access a particular item then you have to start at the head and follow the references until you get to that item.
Another disadvantage is that a linked list uses more memory compared to an array.

The average time complexity for linked list operations such as insertion and deletion is __O(1)__ and accessing and searching takes up __O(n)__ time. 
The space complexity is __o(n)__

### Stack

A stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. In the pushdown stacks only two operations are allowed: push the item into the stack, and pop the item out of the stack. A stack is a limited access data structure - elements can be added and removed from the stack only at the top. push adds an item to the top of the stack, pop removes the item from the top. A helpful analogy is to think of a stack of books; you can remove only the top book, also you can add a new book on the top.

The average time complexity for stack operations such as insertion and deletion is __O(1)__ and accessing and searching takes up __O(n)__ time. 
The space complexity is __o(n)__

### Queue

A queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.  In the queue only two operations are allowed enqueue and dequeue. Enqueue means to insert an item into the back of the queue, dequeue means removing the front item.

The time complexity for insertion is __O(1)__ while deletion is __O(n)__ (in the worst case) for a single operation.
### Binary Tree

A tree in which every node can have a maximum of two children is called Binary Tree. Since each element has at most two children, we name them as the left child and right child. When a node is inserted in Binary Tree, the new node always checks with its parent node. If the new node is less than the value of parent node, the new node will be placed on the left side of the parent otherwise the new node will be placed on the right side of the tree.

The average time complexity is __Θ(log(n))___ and worst case space complexity is __Θ(n)__. 

### Trie

The name trie come from its use for re<b>trie</b>val. A trie is, like other tree-based data structures, made up of a set of nodes connected by pointers. These pointers indicate a parent-child relationship between the nodes. Parents are above their children in the tree. 

The tries can insert and find strings in o(L) time(where L represent the length of a single word) which is much faster than hash tables and binary search trees. Contrary to Binary trees, Trie holds a single character and has a maximum fan-out equal to the length of the alphabet which says that the operations (insert, search, remove) would take time __O(WL)__ (W = alphabet size  and L = length of the string involved in the operation) and the space complexity can be stated as O(W) W = total size of the string S.

#### For more details:
* https://www.cs.bu.edu/teaching/c/tree/trie/
* https://brilliant.org/wiki/tries/#
* [Applications of trie](http://blog.xebia.in/index.php/2015/09/28/applications-of-trie-data-structure/)
* https://www.youtube.com/watch?v=AXjmTQ8LEoI

### Hash Table

We use search algorithms for example, Binary Search, to search an item in an ordered list in logarithmic time. By using Hash Tables, we go a step further by building a data structure that can search in __O(1)__ time. Hash Table also known as Hashmap is a data structure that can map keys to values.
A hash table uses a hash function to compute the index of the position or slot where an item is stored. The slots can range from 0 to n. 
The main advantage of Hash Table is that it allows direct access to its items. Hash Tables can be very useful when the number of element we're dealing with is very huge or unknown. The hash function returns an integer or an hash value in a finite range of slots.

#### For more details:
* https://stackoverflow.com/questions/2179965/whats-the-point-of-a-hash-table
* http://blog.chapagain.com.np/hash-table-implementation-in-python-data-structures-algorithms/
* https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm
### Merge Sort

Merge sort arranges the elements by using devide and conquer strategy. It recursively splits the list into halves then the algorithm sorts the elements and performs, the fundamental operation, called merge. Merging takes two smaller sorted list and combines the into a single, sorted list. Merge sort is an efficient sorting algorithm with an overall time complexity of __O(n log n)__ and space complexity of __O(n)__ .
<hr></hr>

## Additional links 

* [Big O cheatsheet](https://www.bigocheatsheet.com/)
* [UC Berkeley 61B (Fall 2006): Data Structures (39 videos)](https://archive.org/details/ucberkeley-webcast-PL4BBB74C7D2A1049C)
* [https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
* [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
* [Understanding Hash Functions (video)](https://archive.org/details/0102WhatYouShouldKnow/06_02-understandingHashFunctions.mp4)
* [Using Hash Tables (video)](https://archive.org/details/0102WhatYouShouldKnow/06_03-usingHashTables.mp4)
* [Data Structures (Video)](https://www.coursera.org/learn/data-structures/home/week/3)


