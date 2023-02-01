# Hashtables
<!-- Short summary or background information -->

Code Challenge 30 - Hashtable Implementation

## Challenge
<!-- Description of the challenge -->

Implement a Hashtable Class with the following methods:

set
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.

get
Arguments: key
Returns: Value associated with that key in the table

has
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.

keys
Returns: Collection of keys

hash
Arguments: key
Returns: Index in the collection for that key

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## API
<!-- Description of each method publicly available in each of your hashtable -->

set: This method will set a key/value pair in the hashtable. Deals with collisons.

get: This method will return the value when a key/value pair based on the key passed in

has: This method will return a boolean(true/false) for whether or not a key already exists in the hastable

keys: This method will return all the keys in the hash table

hash: This method will return the index position for a specific key that is passed in.

## Attributions:

A special thank you to Adam for getting us started in this code challenge and providing the starter code.
