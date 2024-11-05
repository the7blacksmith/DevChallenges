# [LeetCode: Problems](https://leetcode.com/problemset/)

![RomantoInteger](/Images/Roman%20to%20integer.png)

A real-life problem you can actually use in your everyday life. 

Or are you going to say you don’t use Roman numerals all the time?

Ok, whatever... 😒

So, even if it looks a hard problem, you just need to think which are the main challenges you are facing when you convert Roman numerals to integers.

- Every letter has a value: So you can create a dictionary; the **key** can be the Roman and the **value** the integer related as below:

 romans = {
    "I": 1, 
    "V": 5, 
    "X": 10, 
    "L": 50, 
    "C":100, 
    "D": 500, 
    "M": 1000
    }

- You normally add the values, so VI = 6 and XIII = 13.

- Except when a lower value comes first, in which case you subtract: IV = 4 or IX = 9.

In my algorithm, I first reverse the number you want to convert, just like with the palindrome problem, using slicing with a negative step [::-1]. Then, I append the corresponding values to a list; so 'XIV' would turn into [5, 1, 10].

But if I just add up the values in the list, it won’t give me the desired result. We need to consider that if a smaller value comes after a larger one, we should subtract instead of add. So, whenever a number is lower than the previous one, I convert it to a negative number and subtract it that from the total result at the end of the function.

if i == 0: 
    addition.append(y)
elif y < list_numbers[i-1]: 
    y = -y
    addition.append(y)
else:
    addition.append(y)

You use sum(), a function that adds up all the elements in any iterable, such as a list or a tuple, and then you return the integer value.

# And this is how the Romans used to count, my dear friend, using Python!






