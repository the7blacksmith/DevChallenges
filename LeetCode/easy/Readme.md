

# [LeetCode: Problems](https://leetcode.com/problemset/)

# TwoSum 

![Images](/Images/TwoSum.png)

This is my first LeetCode problem, supposedly an 'easy' problem, but I find the problem to be anything but easy.

Initially, the problem is simple: when the sum of two of the numbers equals the target, we will return the indices of those elements in the list.

But here lies the main problem: 👾 we have to sum all the combinations until one gives us the desired result. 

And what thas it mean? Well, you have to do... **a nested loop!!** 🥶

And as you can see in the TwoSum.py file, it was my approach to the excercise. Once you have started doing this "all with all", you just resolve the problem. But...

But when you submit on LeetCode, you discover that your algorithm is the slowest of all those who have attempted the exercise. Yes, you heard that right, the last one. And why? Well, it’s quite simple, because of something called **Big O notation**, and the problem we are encountering: **O(n)²**.

# Big O notation.

Big O notation is a way to describe the efficiency of an algorithm in terms of time or space requirements as the input size grows. In other words, how efficient is your algorithm.

In our exercise, by using a nested loop, we make the algorithm slower in a quadratic manner as the number of data points the problem has to read increases. This is what **O(n)2** means. 

If I have a list of three numbers to sum is ok, but if the algorithm has to manage a big amount of numbers, then becames extremly slow and not effient in terms of space.

So what we do?

Well, I just put a ChatGPT example in the TwoSum.py file, so you can see the difference. In the GPT attempt, the approach is different using a hash-based approach.

Basically it iterates through the list of numbers (nums), calculating the difference between the target and each number (num). It stores the numbers already seen in a dictionary (seen), and if it finds the difference in that dictionary, it returns the indices of the current number and the difference, allowing for efficient **O(n)** time complexity.

If you don´t beleive anything I just told above, I understand. But I imported the time mnodule and I have used it to check the speed of both algorithms, mine and ChatGPT one so you can see the difference, and why consider Big O in your scripts are so important. 

Is this useful for you? I imagine that if you're an expert developer, you're probably not reading this. But if you're still a junior or learning Python basics, these concepts are essential when writing code.

Just in case you're not fully familiar with Python's time library, I'm including some information on it here:

[TimeLibrary](https://docs.python.org/3/library/time.html)





