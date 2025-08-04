## Part of the Home Lab projects, this one contains solutions for various Leetcode problems 

- [Happy Number](https://leetcode.com/problems/happy-number/submissions/1718060022/) - storing the square results in a 
list caused a delay. Time optimization was achieved by using a Set because search operations in a hash table is with 
O(1) complexity compared to O(n) for a List.
- [Find Tic-Tac-Toe winner](https://leetcode.com/submissions/detail/1517345800/) - I am playing here with the combinations
module of itertools. 
- [HackerRank] Handshake counter - Simple math problem - find the number of unique pair combinations n(n-1)/2
- Valid Parentheses - build a dictionary for quick search result, alo suse a list as a stack - either adding or 
removing from the top
- [Roman to Integer](https://leetcode.com/submissions/detail/1720657561/) - again a dictionary to get the integer values,
note that roman numbers are sorted except when a number like 90 is represented (XC)
- [Assign Cookies](https://leetcode.com/problems/assign-cookies/submissions/1723508570/) - loop through two lists and 
compare the integer values