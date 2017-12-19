#a = [1,2,3,4,2,1,5,6,2]
#a=[1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
a = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
n = len(a)
m = 3
#Optimal Page Replacement Algorithm
def __optimal():
    global a,n,m
    x = 0
    page_faults = 0
    page = []
    FREE = -1
    for i in range(m):
        page.append(FREE)
 
    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == a[i]):
                flag = 1
                break
             
        if flag == 0:
            # look for an empty one
            faulted = False
            new_slot = FREE
            for q in range(m):
                if page[q] == FREE:
                    faulted = True
                    new_slot = q
             
            if not faulted:
                # find next use farthest in future
                max_future = 0
                max_future_q = FREE
                for q in range(m):
                    if page[q] != FREE:
                        found = False
                        for ii in range(i, n):
                            if a[ii] == page[q]:
                                found = True
                                if ii > max_future:
                                    print("\n\tFound what will be used last: a[%d] = %d" % (ii, a[ii]))
                                    max_future = ii
                                    max_future_q = q
 
                                break
                         
                        if not found:
                            print("\n\t%d isn't used again." % (page[q]))
                            max_future_q = q
                            break
 
                faulted = True
                new_slot = max_future_q
             
            page_faults += 1
            page[new_slot] = a[i]
            print("\n%d ->" % (a[i]),end='  ')
            for j in range(m):
                if page[j] != FREE:
                    print(page[j],end='  ')
                else:
                    print("-",end='  ')
        else:
            print("\n%d -> No Page Fault" % (a[i]))
             
    print("\n Total page faults : %d." % (page_faults))
#main
__optimal()
