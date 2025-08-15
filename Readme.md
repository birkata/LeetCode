## Part of the Home Lab projects, this one contains solutions for various Leetcode problems 

- [Happy Number](https://leetcode.com/problems/happy-number/submissions/1718060022/) - storing the square results in a 
list caused a delay. Time optimization was achieved by using a Set because search operations in a hash table is with 
O(1) complexity compared to O(n) for a List.
- [Find Tic-Tac-Toe winner](https://leetcode.com/submissions/detail/1517345800/) - I am playing here with the combinations
module of itertools. 
- [HackerRank] Handshake counter - Simple math problem - find the number of unique pair combinations n(n-1)/2
- [valid parentheses](https://leetcode.com/problems/valid-parentheses/submissions/1736489174/) - build a dictionary for 
quick search result, also use a list as a stack - either adding or removing from the top
- [Roman to Integer](https://leetcode.com/submissions/detail/1720657561/) - again a dictionary to get the integer values,
note that roman numbers are sorted except when a number like 90 is represented (XC)
- [Assign Cookies](https://leetcode.com/problems/assign-cookies/submissions/1723508570/) - loop through two lists and 
compare the integer values
- [Max Common Prefix](https://leetcode.com/problems/longest-common-prefix/submissions/1735185253/) - using vertical 
scanning. It's an abstraction as if every string is piled in a column. Then letters for comparison are aligned and can 
be compared easily. Lesson learned - starting from what end will lead faster to an exit or the answer. 