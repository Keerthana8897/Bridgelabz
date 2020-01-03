def anagram(s1,s2):
    k=0
    h=[]
    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            if s1[i]==s2[j]:
                k=k+1
        h.append(k)
        k=0
    if max(h)>1:
        print "false"
    else:
        print"true"


s1=raw_input("Enter the first string")
s2=raw_input("Enter the second string ")
anagram(s1,s2)
