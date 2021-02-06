def longestPalindrome(String, i, j, table):
    if i > j:
        return 0
        
    if i == j:
        return 1
 
    key = (i, j)
    if key not in table:
        if String[i] == String[j]:
            table[key] = longestPalindrome(String, i + 1, j - 1, table) + 2
        else:
            table[key] = max(longestPalindrome(String, i, j - 1, table),
                              longestPalindrome(String, i + 1, j, table))

    return table[key]
	
String = "ABDDDDEEEFFFCBCDBDCBBCDDEEEFFF"

print("The Longest palindrome length = ", longestPalindrome(String, 0, len(String) - 1, table = {}))