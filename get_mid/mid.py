#def get_middle(s): return sum(s) if len(s) < 3 else get_middle(s[1:-1])

#get_middle = lambda s: [get_middle[s[1:-1]),s][len(s)<3]
#get_middle=lambda s:2<len(s)and get_middle(s[1:-1])or sum(s)
#get_middle=lambda s:s[(len(s)-1)//2:-((len(s)-1)>>1)]
get_middle=lambda s:sum(s[len(s)-1>>1:][:2-len(s)%2])

print(get_middle([4]))
print(get_middle([3,4,5,6,7,8]))
print(get_middle([3,4,5,7,8]))
print(get_middle([3,4,5,7,8,9,10]))
