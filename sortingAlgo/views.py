from django.shortcuts import render,HttpResponse
import random

array_range = (50,650)
array_size = 150

def index(request):
    global arr
    #initialize the array
    arr = generate_array(array_size)
    return render(request, "homepage.html", {'arr': arr})

def generate_array(size:int):
    arr = [random.randint(*array_range) for _ in range(size)]
    return arr

###################################
# Quick Sort
###################################
def quickSort(request):
    animation = []
    auxiliaryArray = arr[:]
    quickSortHelper(auxiliaryArray, 0, len(auxiliaryArray) - 1, animation)
    #return animation
    return HttpResponse([animation])

def quickSortHelper(auxiliaryArray,beg,end,animation):
    #quick sort is to select a random element in given array,put everything smaller or equal to in one side, bigger on the other , recursively til it is all sorted
        if beg < end:
            pivot = partition(auxiliaryArray, beg, end, animation)
            quickSortHelper(auxiliaryArray,beg,pivot-1,animation)
            quickSortHelper(auxiliaryArray,pivot+1,end,animation)


def partition(auxiliaryArray, start, end, animation):
    pivot = auxiliaryArray[end]
    #pointer locate the position of the index to swap and pivot final location
    pointer = start
    for i in range(start, end):
        #first animation color the bar
        animation.append([i, end])
        #second animation to revert it back
        animation.append([i, end])
        if auxiliaryArray[i] <= pivot:
            #move pointer rightward to ith bar location
            animation.append([i, auxiliaryArray[pointer]])
            #put ith bar to pointer location
            animation.append([pointer, auxiliaryArray[i]])
            auxiliaryArray[i], auxiliaryArray[pointer] = auxiliaryArray[pointer], auxiliaryArray[i]
            pointer += 1
        else:
            #no animation needed 
            animation.append([-1, -1])
            animation.append([-1, -1])
        animation.append([-1, -1])
        animation.append([-1, -1])
    #dummy animation add up to 6
    animation.append([-1, -1])
    animation.append([-1, -1])
    animation.append([-1, -1])
    animation.append([-1, -1])
    #put the pivot back at correct position
    animation.append([pointer, pivot])
    animation.append([end, auxiliaryArray[pointer]])
    auxiliaryArray[pointer], auxiliaryArray[end] = auxiliaryArray[end], auxiliaryArray[pointer]
    return pointer


###################################
# Merge Sort
###################################
def mergeSort(request):
    animation =[]
    auxiliaryArray = arr[:]
    mergeSortHelper(arr, 0, len(arr) - 1, auxiliaryArray, animation)
    return HttpResponse([animation])


def mergeSortHelper(mainArray, start, end, auxiliaryArray, animation):
    if start == end: return
    middle = (start + end) // 2
    mergeSortHelper(auxiliaryArray, start, middle, mainArray, animation)
    mergeSortHelper(auxiliaryArray, middle + 1, end, mainArray, animation)
    merge(mainArray, start, middle, end, auxiliaryArray, animation)


def merge(mainArray, start, middle, end, auxiliaryArray, animation):
    #animation cycle = 3
    k = start
    i = start
    j = middle + 1
    while i <= middle and j <= end:
        #first animation color the bar
        animation.append([i, j])
        #second animation revert them back
        animation.append([i, j])
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            #swapping animation for k and i
            animation.append([k, auxiliaryArray[i]])
            mainArray[k] = auxiliaryArray[i]
            k += 1
            i += 1
        else:
            #swapping animation for k and i
            animation.append([k, auxiliaryArray[j]])
            mainArray[k] = auxiliaryArray[j]
            k += 1
            j += 1

    while i <= middle:
        animation.append([k, k])
        animation.append([k, k])
        animation.append([k, auxiliaryArray[i]])
        mainArray[k] = auxiliaryArray[i]
        k += 1
        i += 1

    while j <= end:
        animation.append([k, k])
        animation.append([k, k])
        animation.append([k, auxiliaryArray[j]])
        mainArray[k] = auxiliaryArray[j]
        k += 1
        j += 1

###################################
# Selection Sort
###################################
def selectionSort(reqeust):
    animation = []
    auxiliaryArray = arr[:]
    selectionSortHelper(auxiliaryArray, animation)
    return HttpResponse([animation])

def selectionSortHelper(auxiliaryArray,animation):
    # 0 --> comparison 1
    # 1 --> comparison 2
    # 2 --> swapping animation
    for i in range(0, len(auxiliaryArray)):
        minIndex = i
        for j in range(i+1, len(auxiliaryArray)):
            animation.append([0, j, minIndex])
            animation.append([1, j, minIndex])
            if auxiliaryArray[j] < auxiliaryArray[minIndex]:
                minIndex = j
        #add swapping animation
        animation.append([2, minIndex, auxiliaryArray[i]])
        animation.append([2, i, auxiliaryArray[minIndex]])
        #actual swap
        auxiliaryArray[minIndex], auxiliaryArray[i] = auxiliaryArray[i], auxiliaryArray[minIndex]

###################################
# Bubble Sort
###################################

def bubbleSort(reqeust):
    animation = []
    auxiliaryArray = arr[:]
    bubbleSortHelper(auxiliaryArray, animation)
    return HttpResponse([animation])


def bubbleSortHelper(auxiliaryArray,animation):
    for i in range(len(auxiliaryArray)-1):
        for j in range(len(auxiliaryArray)-1):
            animation.append([j,j+1])
            animation.append([j,j+1])
            if auxiliaryArray[j] > auxiliaryArray[j+1]:
                animation.append([j,auxiliaryArray[j+1]])
                animation.append([j+1,auxiliaryArray[j]])
                auxiliaryArray[j],auxiliaryArray[j+1] = auxiliaryArray[j+1],auxiliaryArray[j]
            else:
                animation.append([-1,-1])
                animation.append([-1,-1])





