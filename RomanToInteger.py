# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        # dictionary for values 
        values = { 
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5, 
            "I": 1
        }
        # start at the end 
        sum = values.get(s[-1])
        # work backwards
        # we don't need to know the next number to 
        # know what to do with the current one 
        for i in reversed(range(len(s)-1)):
            if values[s[i]] < values[s[i+1]]:
                sum -= values[s[i]]
            else: 
                sum += values[s[i]]
        return sum