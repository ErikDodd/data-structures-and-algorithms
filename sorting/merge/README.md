# Blog Notes: Merge Sort

The Merge Sort function is a great way to wrap your head around a classic algorithm. To keep it simple, I will explain what the function is doing on a high-level first. Then I will break it down step-by-step. I will share the solution code at the end of this blog post.

The Merge Sort function takes in a list as an argument and essentially splits the list in half. Given an unsorted list with the values of 8,4,23,42,16,15, it would first split it into two lists, one consisting of 8,4,23 and the other 42,16,15.

The function then calls itself recursively to first split the 8,4,23, list even further. Until eventually it is 3 'mini' lists each containing one value. The function will then go over to the 42,16,15, and use recursion again to split those values into their own mini lists each containing one value.

Once the Merge Sort function has called itself recursively on both the left/right side of the list that was passed in, we now call the merge function. The merge function takes in arguments of left, right, and lst(list). This function simply compares the values in the list two values at a time. Let's use the example of 8 and 4. This function checks to see if 4 is less than or equal to 8, which it is, and then proceeds to move it left side of the list. Next, it will compare 8 to 23, and since 8 is already less than or equal 23, it doesn't move it to the left. Both values maintain their current position.

The Merge function that is invoked inside of Merge Sort will continue to do this first starting at the left side of the list, moving to the right side of the list. It will finish with the whole list and will eventually sort the least completely from lowest to highest values.
