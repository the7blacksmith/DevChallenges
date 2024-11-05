class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        r_string = string[::-1]
        if string == r_string:
            print("Input: x =", x)
            print("Explanation: ",x, "reads as ",x, "from left to right and from right to left")
            return True
        else:
            print("Input: x =", x)
            print("From left to right, it reads", x,". From right to left, it becomes", r_string, ". Therefore it is not a palindrome")
            return False

   
class Solution_v2:
    def isPalindrome_v2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]