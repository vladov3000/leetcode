def Solution(s):
    if len(s)==0:
        return 0
    if len(s)==1:
        return 1
    p1=0
    p2=1
    sub={s[0]:p1}
    out=-1
    while p2<len(s) and p1<=p2:
        if s[p2] in sub.keys():
            #rint(sub)
            if len(sub)>out:
                out=len(sub)
            del sub[s[p1]]
            p1+=1
        else:
            sub[s[p2]]=p2
            p2+=1
    if len(sub)>out:
        out=len(sub)
    return out

#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#Given a string, find the length of the longest substring without repeating characters.
