array = []
while not array:
    try:
        array = list(map(float, input("Введите последовательность чисел через пробел: ").split()))
    except ValueError:
        print("Введены не числовые символы, повторите попытку")

element = None
while not element:
    try:
        element = float(input("Введите число: "))
    except ValueError:
        print("Введены не числовые символы, повторите попытку")

#sorting
import random
def qsort(array, left, right):
    p = random.choice(array[left:right+1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if i < right:
        qsort(array, i, right)

#binary search
def bin_search(array, element, left, right):
    if left > right or element <= array[0] or array[-1]< element:
        return False
    middle = (left + right) // 2
    if array[middle] < element <= array[middle+1]:
        return middle
    elif element <= array[middle]:
        return bin_search(array, element, left, middle-1)
    elif element > array[middle+1]:
        return bin_search(array, element, middle+1, right)

qsort(array, 0, len(array)-1)
print("Отсортированная последовательность: ", array)

result = bin_search(array, element, 0, len(array)-1)

if type(result) == int:
    print(f"Введённое число помещается между элементами № {result+1} и № {result+2}")
else:
    print("Введённое число не удовлетворяет условиям")
