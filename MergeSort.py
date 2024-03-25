import random
import time
from playsound import playsound

arraySize = input("Please type the array size\n> ")
array = []
playsound('confirm.wav')


def MergeSort(mainArray):
    time.sleep(1)
    if len(mainArray) > 1:
        print(mainArray)
        playsound('confirm.wav')

        midpoint = len(mainArray) // 2
        leftArray = mainArray[:midpoint]
        rightArray = mainArray[midpoint:]

        MergeSort(leftArray)
        MergeSort(rightArray)

        time.sleep(1)

        i = 0
        j = 0
        k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] <= rightArray[j]:
                mainArray[k] = leftArray[i]
                i += 1
            else:
                mainArray[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            mainArray[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            mainArray[k] = rightArray[j]
            j += 1
            k += 1

    print(mainArray)
    playsound('confirm.wav')

    return mainArray


for i in range(int(arraySize)):
    array.append(random.randint(0, int(arraySize) * 3))

originalArray = array.copy()

time.sleep(1)

array = MergeSort(array)

print("\nOriginal list:\n" + str(originalArray))
