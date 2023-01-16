[My Leetcode page](https://leetcode.com/ganpoweird/)

### **Solved Problems:**
* [**202. Happy Number**](#202-happy-number)
* [**54. Spiral Matrix**](#54-spiral-matrix)
* [**14. Longest Common Prefix**](#14-longest-common-prefix)
* [**43. Multiply Strings**](#43-multiply-strings)
* [**19. Remove Nth Node From End of List**](#19-remove-nth-node-from-end-of-list)
* [**234. Palindrome Linked List**](#234-palindrome-linked-list)
* [**977. Squares of a Sorted Array**](#977-squares-of-a-sorted-array)
* [**189. Rotate Array**](#189-rotate-array)
* [**175. Combine Two Tables**](#175-combine-two-tables)
* [**66. Plus One**](#66-plus-one)
* [**658. Find K Closest Elements**](#658-find-k-closest-elements)
* [**459. Repeated Substring Pattern**](#459-repeated-substring-pattern)
* [**896. Monotonic Array**](#896-monotonic-array)
* [**28. Find the Index of the First Occurrence in a String**](#28-find-the-index-of-the-first-occurrence-in-a-string)


#### 202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:
* Input: `n = 19`
* Output: `true`
* Explanation:
  * `12 + 92 = 82`
  * `82 + 22 = 68`
  * `62 + 82 = 100`
  * `12 + 02 + 02 = 1`

Example 2:
* Input: `n = 2`
* Output: `false`
 

Constraints:

`1 <= n <= 231 - 1`

---- 

#### 54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" alt=""/>


* Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]` 
* Output: `[1,2,3,6,9,8,7,4,5]`

Example 2:

<img src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" alt=""/>

* Input: `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
* Output: `[1,2,3,4,8,12,11,10,9,5,6,7]`
 

Constraints:

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 10`
* `-100 <= matrix[i][j] <= 100`
----

#### 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

* Input: `strs = ["flower","flow","flight"]`
* Output: `"fl"`

Example 2:

* Input: `strs = ["dog","racecar","car"]`
* Output: `""`
* Explanation: There is no common prefix among the input strings.
 

Constraints:

* `1 <= strs.length <= 200`
* `0 <= strs[i].length <= 200`
* `strs[i]` consists of only lowercase English letters.
----

#### 43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
 

Example 1:
* Input: `num1 = "2", num2 = "3"`
* Output: `"6"`

Example 2:
* Input: `num1 = "123", num2 = "456"`
* Output: `"56088"`
 

Constraints:
* `1 <= num1.length, num2.length <= 200`
* `num1` and `num2` consist of digits only.
* Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.

----

#### 19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
<img src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" alt=""/>
* Input: `head = [1,2,3,4,5], n = 2`
* Output: `[1,2,3,5]`

Example 2:
* Input: `head = [1], n = 1`
* Output: `[]`

Example 3:
* Input: `head = [1,2], n = 1`
* Output: `[1]`
 

Constraints:
* The number of nodes in the list is `sz`.
* `1 <= sz <= 30`
* `0 <= Node.val <= 100`
* `1 <= n <= sz`
 

Follow up: Could you do this in one pass?

----

#### 234. Palindrome Linked List

Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

 

Example 1:

<img src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" alt=""/>

* Input: `head = [1,2,2,1]`
* Output: `true`

Example 2:

<img src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" alt=""/>

* Input: `head = [1,2]`
* Output: `false`
 

Constraints:
* The number of nodes in the list is in the range `[1, 105]`.
* `0 <= Node.val <= 9`
 

Follow up: Could you do it in O(n) time and O(1) space?

----

#### 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
Example 1:
* Input: `nums = [-4,-1,0,3,10]`
* Output: `[0,1,9,16,100]`
* Explanation: 
  * After squaring, the array becomes `[16,1,0,9,100]`. 
  * After sorting, it becomes `[0,1,9,16,100]`.

Example 2:
* Input: `nums = [-7,-3,2,3,11]`
* Output: `[4,9,9,49,121]`
 

Constraints:
* `1 <= nums.length <= 104`
* `-104 <= nums[i] <= 104`
* `nums` is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

----
#### 189. Rotate Array 

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
* Input: `nums = [1,2,3,4,5,6,7], k = 3`
* Output: `[5,6,7,1,2,3,4]`

* Explanation:
  * rotate 1 steps to the right: `[7,1,2,3,4,5,6]`
  * rotate 2 steps to the right: `[6,7,1,2,3,4,5]`
  * rotate 3 steps to the right: `[5,6,7,1,2,3,4]`
  
Example 2:
* Input: `nums = [-1,-100,3,99], k = 2`
* Output: `[3,99,-1,-100]`
* Explanation: 
  * rotate 1 steps to the right: `[99,-1,-100,3]`
  * rotate 2 steps to the right: `[3,99,-1,-100]`
 
Constraints:
* `1 <= nums.length <= 105`
* `-231 <= nums[i] <= 231 - 1`
* `0 <= k <= 105`
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

----

#### 175. Combine Two Tables

Table: Person

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| personId    | int     |
| lastName    | varchar |
| firstName   | varchar |
+-------------+---------+
```

`personId` is the primary key column for this table.
This table contains information about the ID of some persons and their first and last names.
 

Table: Address
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| addressId   | int     |
| personId    | int     |
| city        | varchar |
| state       | varchar |
+-------------+---------+
```
`addressId` is the primary key column for this table.
Each row of this table contains information about the city and state of one person with `ID = PersonId`.
 

Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

Return the result table in any order.

The query result format is in the following example.

Example 1:

* Input: 

  Person table:
  ```
  +----------+----------+-----------+
  | personId | lastName | firstName |
  +----------+----------+-----------+
  | 1        | Wang     | Allen     |
  | 2        | Alice    | Bob       |
  +----------+----------+-----------+
  ```
  Address table:
  ```
  +-----------+----------+---------------+------------+
  | addressId | personId | city          | state      |
  +-----------+----------+---------------+------------+
  | 1         | 2        | New York City | New York   |
  | 2         | 3        | Leetcode      | California |
  +-----------+----------+---------------+------------+
  ```
* Output:
  ```
  +-----------+----------+---------------+----------+
  | firstName | lastName | city          | state    |
  +-----------+----------+---------------+----------+
  | Allen     | Wang     | Null          | Null     |
  | Bob       | Alice    | New York City | New York |
  +-----------+----------+---------------+----------+
  ```
* Explanation:
  * There is no address in the address table for the `personId = 1` so we return null in their city and state.
  * `addressId = 1` contains information about the address of `personId = 2`.

----

#### 66. Plus One

You are given a large integer represented as an integer array digits, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to the least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
* Input: `digits = [1,2,3]`
* Output: `[1,2,4]`
* Explanation: 
  * The array represents the integer `123`.
  * Incrementing by one gives `123 + 1 = 124`.
  * Thus, the result should be `[1,2,4]`.

Example 2:
* Input: `digits = [4,3,2,1]`
* Output: `[4,3,2,2]`
* Explanation: 
  * The array represents the integer `4321`.
  * Incrementing by one gives `4321 + 1 = 4322`.
  * Thus, the result should be `[4,3,2,2]`. 

Example 3:
* Input: `digits = [9]`
* Output: `[1,0]`
* Explanation: 
  * The array represents the integer `9`.
  * Incrementing by one gives `9 + 1 = 10`.
  * Thus, the result should be `[1,0]`.
 

Constraints:

* `1 <= digits.length <= 100`
* `0 <= digits[i] <= 9`
* digits do not contain any leading 0's.

----

#### 658. Find K Closest Elements

Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:

`|a - x| < |b - x|`, or
`|a - x| == |b - x| and a < b`
 

Example 1:
* Input: `arr = [1,2,3,4,5], k = 4, x = 3`
* Output: `[1,2,3,4]`

Example 2:
* Input: `arr = [1,2,3,4,5], k = 4, x = -1`
* Output: `[1,2,3,4]`
 
Constraints:
* `1 <= k <= arr.length`
* `1 <= arr.length <= 104`
* `arr` is sorted in ascending order.
* `-104 <= arr[i], x <= 104`

----

#### 459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
* Input: `s = "abab"`
* Output: `true`
* Explanation: It is the substring `"ab"` twice.

Example 2:
* Input: `s = "aba"`
* Output: `false`

Example 3:
* Input: `s = "abcabcabcabc"`
* Output: `true`
* Explanation: It is the substring `"abc"` four times or the substring `"abcabc"` twice.
 

Constraints:

* `1 <= s.length <= 104`
* `s` consists of lowercase English letters.

----

#### 896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array nums is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
* Input: `nums = [1,2,2,3]`
* Output: `true`

Example 2:
* Input: `nums = [6,5,4,4]`
* Output: `true`

Example 3:
* Input: `nums = [1,3,2]`
* Output: `false` 

Constraints:
* `1 <= nums.length <= 105`
* `-105 <= nums[i] <= 105`

----

#### 28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

* Input: `haystack = "sadbutsad", needle = "sad"`
* Output: `0`
* Explanation: 
  * `"sad"` occurs at index `0` and `6`.
  * The first occurrence is at index `0`, so we return `0`.

Example 2:

* Input: `haystack = "leetcode", needle = "leeto"`
* Output: `-1`
* Explanation: `"leeto"` did not occur in `"leetcode"`, so we return `-1`.
 
Constraints:
* `1 <= haystack.length, needle.length <= 104`
* `haystack` and `needle` consist of only lowercase English characters.