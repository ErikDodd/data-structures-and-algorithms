# Singly Linked List
<!-- Short summary or background information -->

## Challenge
<!-- Description of the challenge -->

### Node
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.

### Linked List
- Create a Linked List class
- Within your Linked List class, include a head property.
- Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods

insert
Arguments: value
Returns: nothing
Adds a new node with that value to the head of the list with an O(1) Time performance.

includes
Arguments: value
Returns: Boolean
Indicates whether that value exists as a Node’s value somewhere within the list.

to string
Arguments: none
Returns: a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

- The Big O Time is Linear Time O(n). As the amount of values in the list increases, it will take longer to traverse the linked list
- The Big O Space is O(n). As the amount of values in the list increases, it will take up more space.

## API
<!-- Description of each method publicly available to your Linked List -->

- N / A

## Attributions

I used the following websites to help me with this code challenge:

https://www.educative.io/answers/how-to-create-a-linked-list-in-python

https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
