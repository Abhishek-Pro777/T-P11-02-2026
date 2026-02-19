def find_first_non_repeating_char(s):
    map={}
    for i in s:
        map[i]=map.get(i,0)+1
    for i in s:
        if map[i]==1:
            return i
    return None

s=input()
print(find_first_non_repeating_char(s))