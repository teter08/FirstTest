def useless(lst):
    print(len(max(lst, key=lambda x:len(x))))

    return lst

print(useless(['111','22222','33sdfdfsd33','44']))