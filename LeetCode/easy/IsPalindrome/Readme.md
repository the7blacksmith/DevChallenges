# [LeetCode: Problems](https://leetcode.com/problemset/)

![Palindrome_image](/Images/Palindrome%20number.png)


A **palindrome number** is a number that reads the same forward and backward. In other words, if you reverse its digits, the resulting number remains identical.

So, basically, they provide us with a number, and if it is a palindrome, our algorithm should return True; otherwise, it should return False.

We just need here:

1. Reverse the number
2. Check if the reversed number is the same to the initial number they have provided us. 

Easy Peasy! 🍋

So I create a string and reverse it by using slicing with a negative step.

string = str(x)
r_string = string[::-1]

# Slicing with negative step [::-1]

Is a technique to reverse a string or a list. Simple and useful. 

So I did those steps however ChatGPT did it simpler and you can learn from it here. 

class Solution_v2:
    def isPalindrome_v2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

Just three lines, two if you consider you don´t really need a class to resolve this problem. 

In Spanish we say: "¿Cómo te quedas?"







