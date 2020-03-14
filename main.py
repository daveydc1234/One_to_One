#! python
import sys

from OneToOne import OnetoOne

if __name__ == "__main__":
    #print("IT IS WORKING")
    if len(sys.argv)==3: #check if there are only 2 args
        OnetoOne(sys.argv[0], sys.argv[1])
    else: #error because there are too little or more than 2 str
        print("Error with arguments")
        
    """""
    s1 = input()
    s2 = input()
    OnetoOne(s1, s2)
    
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
    """""