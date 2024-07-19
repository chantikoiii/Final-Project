import time


# Ascending quick sort
def quickSort(list):
    less = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less)+equal+quickSort(greater)
    else:
        return list


# Ascending selection sort    
def selectSort(list):
    if len(list) > 1:
        for i in range(0, len(list)-1):
            index_min=i
            for j in range(i+1, len(list)):
                if list[j] < list[index_min]:
                    index_min=j

            list[i], list[index_min] = list[index_min], list[i]
    else:
        return list


# Timers for each algorithm    
def quickTimer(x):
    start=time.time()
    quickSort(x)
    end=time.time()
    print(end-start)

def selectTimer(x):
    start=time.time()
    selectSort(x)
    end=time.time()
    print(end-start)
