from collections import defaultdict as dd
d_s = {'A1' :5 ,'A2':5,'A3':5,'A4':5,'A5':5}
l_c = []
l_r = []
c_s = dict()
def findstn(n1,n2):
    l = c_s[n1]
    for i in l:
        if i == n2:
            return n1 + ' ' + n2
        else:
            return n1 +" "+ findstn(i,n2)
    return "Route not found"
while(True):
    t =list(map(str,input().split()))
    if len(t) ==3:
        if t[0] == 'ADD':
            if t[1] == 'COMPUTER':
                if t[2] not in l_c:
                    l_c.append(t[2])
                    c_s[t[2]] = []
                    print('Successfully added',t[2])
                else:
                    print('The name already exists')
            elif  t[1] == 'REPEATER':
                if t[2] not in l_r:
                    l_r.append(t[2])
                    c_s[t[2]] = []
                    print('Successfully added',t[2])
                else:
                    print('The name already exists')

            else:
                print('Invalid command syntax')
        elif t[0] == 'SET_DEVICE_STRENGTH':
            if t[2].isdigit():
                d_s[t[1]] = int(t[2]) 
                print('Successfully defined strength')
            else:
                print('Invalid command syntax')
        elif t[0] == 'CONNECT':
            c =l_c
            c.extend(l_r)
            if t[1] in c and t[2] in c:
                l = c_s[t[1]]
                if t[1] == t[2]:
                    print('Cannot connect device to itself')
                elif t[2] not in l :
                    l.append(t[2])
                    c_s[t[1]] = l
                    # print(c_s)
                    print('Successfully connected')
                    print(c_s)
                else:
                    print('Devices are already connected')
            else:
                print('Node not found')
        elif t[0] == "INFO_ROUTE":
            if t[1][0] != t[2][0]:
                print("Route cannot be calculated with a repeater")
            if t[1] == t[2]:
                print(t[1],'->',t[1])
            else:
                if t[1][0] == 'A':
                    if t[1] not in l_c or t[2] not in l_c:
                        print('Node not found')
                    else:
                        a = findstn(t[1],t[2])
                        b = list(map(str,a.split()))
                        if len(b) <= d_s[t[1]]+2:
                            print(*b,sep = '->')
                        else:
                            print('length not enough')
                elif t[1][0] == 'R':
                    if t[1] not in l_r or t[2] not in l_r:
                        print('Node not found')
                    else:
                        a = findstn(t[1],t[2])
                        b = list(map(str,a.split()))
                        if len(b) <= d_s[t[1]]+2:
                            print(*b,sep = '->')
                        else:
                            print('length not enough')
                else:
                    pass

    elif t[0] == "STOP":
        break
    else:
        print('Invalid command syntax')        