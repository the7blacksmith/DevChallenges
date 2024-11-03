import time

start = time.time()
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        List = []
        for i, x in enumerate(nums):
            for i_2, y in enumerate(nums):
                if i == i_2:
                    continue
                if x + y == target:
                    List.append(i)
                    List.append(i_2)
            if len(List) == 2:
                break
        print("Input: nums =", nums, ", target =", target)
        return List



solucion = Solution()
print(solucion.twoSum([2, 5, 4, 5, 7], 9))

end = time.time()
my_version = end - start  



#ChatGPT solution:
start_GPT_v = time.time()
class Solution_GPT_v:
    def twoSum_GPT_v(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
            print(seen)
        return []
    
solucion_2 = Solution_GPT_v()
print(solucion_2.twoSum_GPT_v([2, 5, 4, 5, 7], 9))
end_GPT_v = time.time()
GPT_v = end_GPT_v - start_GPT_v

print("Time_version =", my_version)
print("Time_version_GPT =", GPT_v)