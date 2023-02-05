'''
// To execute Go code, please declare a func main() in a package "main"

// int strstr(string haystack, string needle)
// strstr("hello world", "hello") ==> 0
// strstr("hello world", "elloh") ==> -1
// strstr("hello world", "o world") ==> 4
// strstr("hello world", "dlro w") ==> -1
// strstr("hello world", "asdlfkj") ==> -1


// int strstrp(string haystack, string needle)
// strstrp("hello world", "hello") ==> 0
// strstrp("hello world", "elloh") ==> 0
// strstrp("hello world", "o world") ==> 4
// strstrp("hello world", "dlro w") ==> 5
// strstrp("hello world", "asdlfkj") ==> -1

'''

def needle_to_dict(needle):
    needle_dict = {}
    for c in needle:
        if needle_dict.get(c) is None:
            needle_dict[c] = 1
        else:
            needle_dict[c] = needle_dict[c] + 1
    return needle_dict



def strstrp(haystack, needle):
    for ix in range(len(haystack)):
        needle_dict = needle_to_dict(needle)

        if needle_dict.get(haystack[ix]) is None:
            continue
        if needle_dict.get(haystack[ix]) == 0:
            continue

        for c in haystack[ix:]:
            if needle_dict.get(c) is None:
                break
            needle_dict[c] = needle_dict[c] - 1
            s = set(needle_dict.values())
            if (len(s) == 1) and (s.pop() == 0):
                return ix

    return -1

print(strstrp("hello world", "elloh")) # 0
print(strstrp("hello world", "ello")) # 1
print(strstrp("hello world", "ellow")) # -1
print(strstrp("hello world", "ello w")) # 1

# strstrp("hello world", "o world") ==> 4
print(strstrp("hello world", "o world"))
# strstrp("hello world", "dlro w") ==> 5
print(strstrp("hello world", "dlro w"))
# strstrp("hello world", "asdlfkj") ==> -1
print(strstrp("hello world", "asdlfkj"))

