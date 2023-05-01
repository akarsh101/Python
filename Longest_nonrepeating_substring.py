def longest_substring_without_repeating(str):
    chars = set()
    left = right = maxLength = 0
    longest_substring = ''
    
    while right < len(str):
        if str[right] not in chars:
            chars.add(str[right])
            if len(chars) > maxLength:
                maxLength = len(chars)
                longest_substring = str[left:right+1]
            right += 1
        else:
            chars.remove(str[left])
            left += 1
            
    return maxLength, longest_substring

length, substring = longest_substring_without_repeating("abbbcabcdefef")
print("Length of the longest substring without repeating characters:", length)
print("Longest substring without repeating characters:", substring) # Output: "abcdef"
