# given examples
s = "abcba"
k = 2


def find_longest_substring(string:str, num_of_distinct_chars:int) -> str:
    # return empty string if the string is empty
    if not string:
        return ""
    
    # get the length
    length = len(string)
    
    # return the string if the length is less than the number of distinct characters
    if length <= num_of_distinct_chars:
        return string
    
    # a variable to store the current longest substring
    current_longest = ""
    
    # start from number of distinct characters index and loop till the end of string
    for index in range(num_of_distinct_chars, length):
        # start from zero index and loop till you get a gap that is equal to the number of distinct chars
        for inner in range(0, (index - num_of_distinct_chars) + 1):
            # get the substring
            substring = string[inner:index + 1]
            print("index:", index, "inner:", inner, substring)
            # get the number of distinct characters found in the current substring
            current_distinct_chars = len(set(substring))
            
            # check if the current_distinct_chars is less or equal with the num_of_distinct_chars and
            # check if the length of substring is greater than the current_longest string
            if current_distinct_chars <= num_of_distinct_chars and len(substring) > len(current_longest):
                # if yes, update the value
                current_longest = substring

    return current_longest


find_longest_substring(s, k)
find_longest_substring("abcddca", 2)
find_longest_substring("aabbcc", 1)
find_longest_substring("aabbcc", 3)
find_longest_substring("abcbaaab", 2)