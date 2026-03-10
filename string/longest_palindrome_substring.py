def longest_palindrome_substring(s: str) -> str:
    if len(s) <= 1:
        return s
    
    tmp = "-" + "-".join(s) + "-"
    longest_palindrome = ""
    max_len = 0

    for i in range(len(tmp)):
        left = i - 1
        right = i + 1
        radius = 0

        while left >= 0 and right < len(tmp) and tmp[left] == tmp[right]:
            radius += 1
            left -= 1
            right += 1

        if radius > max_len:
            max_len = radius
            longest_palindrome = tmp[left + 1: right].replace("-", "")
    
    return longest_palindrome


print(longest_palindrome_substring("babad"))
print(longest_palindrome_substring("cbbd"))