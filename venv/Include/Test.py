a = [[1,2,3,2,3,2],
     [4,5,6,4,6,4],
     [7,8,9,5,6,4],
     [2,7,3,8,9,5],
     [5,9,0,7,3,8],
     [2,7,3,8,0,7]]

def sprit_marx(maix, m, n):
    lens = m*n
    an = []
    left = 0
    top = 0
    bottom = m
    right = n

    isToR = True #向右
    isToL = False #向左
    isToB = False #向下
    isToT = False #向上
    hang = 0
    lie = 0

    #往左
    for i in range(0,lens):
        print(hang,"-",lie)
        value = maix[hang][lie]
        an.append(value)
        if isToR:
            if lie < right-1:
                #往右
                lie += 1
            else:
                top+=1
                isToR = False
                isToB = True

        if isToB:
            if hang < bottom-1:
                #往下
                hang +=1
            else:
                right -= 1
                isToB = False
                isToL = True
        if isToL:
            if lie > left :
                # 往左
                lie -= 1
            else:
                bottom -=1
                isToL = False
                isToT = True
        if isToT:
            if hang > top:
                # 往上
                hang -= 1
            else:
                left +=1
                lie +=1
                isToT = False
                isToR = True


    return an

print(sprit_marx(a,6,6))


