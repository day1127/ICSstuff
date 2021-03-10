
"""
create a python program called listFunc.py that contains the following functions
1. shuffleList(list) done
2. bubbleSort(list) done
3. selectSort(list)done
4. insertSort(list)done
5. quickSort(list)done
"""


# listFunc.py
# Day Burke
# March 9, 2021 finshed march 10, 2021
# stored on my github at link
import random as r

def shuffleList(list):
    r.shuffle(list)
    print(list,"\n")

def bubbleSort(list):
    indexLength = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexLength):
            if list[i]> list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]

    return list



def selectSort(list):
    indexLength = range(0, len(list) - 1)


    for i in indexLength:
        maxValue = i

        for j in range(i+1, len(list)):
            if list[j] < list[maxValue]:
                maxValue = j

        if maxValue != i:
            list[i], list[maxValue] = list[maxValue], list[i]
    return list



def insertSort(list):
    indexLength =  range(1,len(list))

    for i in indexLength:
        valToSort = list[i]

        while list[i-1] > valToSort and i > 0:
            list[i-1], list[i]  = list[i], list[i-1]
            i = i-1

    return list



def quickSort(list):
    Len = len(list)
    if Len <=1:
        return list
    else:
        pivot = list.pop()


    iGreater = []
    iSmaller = []

    for i in list:
        if i > pivot:
            iGreater.append(i)

        if i < pivot:
            iSmaller.append(i)


    return quickSort(iSmaller) + [pivot] + quickSort(iGreater)








if __name__ == "__main__":
    shuffleList([1,2,3,4,5,6,7])

    print(bubbleSort([8,6,9,2,1,0,5,3]),"\n")

    print(selectSort([1,4,5,3,6,7,8,9,10]),"\n")

    print(insertSort([3,4,5,6,3,2,3,5,7,8,7,8,9,8,10,11,15,50,49]),"\n")

    print(quickSort([1,4,5,6,4,14,17,7,8,9,4,15,20]))
