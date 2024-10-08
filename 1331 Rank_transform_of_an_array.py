"""Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.


Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest."""
# import copy
# class Solution(object):
#     def arrayRankTransform(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: List[int]
#         """
#         # соблюдаем условия длинны списка
#         if len(arr) < 0 or len(arr) > 100000:
#             return False
#         arr_new = []
#
#         # соблюдаем условие на размер элемента списка
#         for i in arr:
#             if i >= -1000000000 and i <= 1000000000:
#                 arr_new.append(i)
#
#         print(arr_new)
#
#         arr2 = copy.deepcopy(arr_new)
#         # print('arr ', arr_new)
#         arr3 = sorted(set(arr_new))
#         # print('sort_arr ', arr3)
#         # print()
#         solution = []
#
#         for i in arr2:
#             # print(i, arr3.index(i))
#             solution.append(arr3.index(i)+1)
#
#         print(solution)
#         return solution


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        num_of_rank = {}
        sorted_arr = sorted(arr)
        rank = 1

        for i in range(len(sorted_arr)):
            if i > 0 and  sorted_arr[i] > sorted_arr[i - 1]:
                rank += 1
            num_of_rank[sorted_arr[i]] = rank

        for i in range(len(arr)):
            arr[i] = num_of_rank[arr[i]]

        return arr

arr = [37,12,28,9,100,56,80,5,12]


print(Solution.arrayRankTransform(arr, arr))