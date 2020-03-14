def OnetoOne(s1, s2):
    my_dict = {}
    if(len(s1)!=len(s2)):
        print("False")
        return
    for i in range(len(s1)):
        if s1[i] not in my_dict:
            my_dict.setdefault(s1[i], s2[i])
        else:
            if(my_dict[s1[i]]!=s2[i]):
                print("False")
                return
    print("True")
    return


if __name__ == "__main__":
    str1 = "abc"
    str2 = "bcd"
    OnetoOne(str1, str2)
    str1 = "foo"
    str2 = "bar"
    OnetoOne(str1, str2)
    str1 = "bar"
    str2 = "foo"
    OnetoOne(str1, str2)
    str1 = "123"
    str2 = "321"
    OnetoOne(str1, str2)
