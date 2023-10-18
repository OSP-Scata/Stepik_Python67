def modify_list(l):
    listlen = len(l)
    while listlen > 0:
        listlen -= 1;
        if l[listlen]%2==0:
            l[listlen] = l[listlen]//2;
        else:
            l.remove(l[listlen])