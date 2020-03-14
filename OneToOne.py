#! python
def OnetoOne(s1, s2):
    my_dict = {} #empty dictionary to hold one to one mapping
    if(len(s1)!=len(s2)): #check if lengths of string are unequal
        print("false")
        return
    for i in range(len(s1)): #for every character in s1 do:
        if s1[i] not in my_dict: #if character hasn't been seen before
            my_dict.setdefault(s1[i], s2[i])
        else: #if character already exists in dictionary
            if(my_dict[s1[i]]!=s2[i]): #check if key is mapping to two different values
                print("false")
                return
    print("true") #reach to end of code means one to one character mapping is possible


