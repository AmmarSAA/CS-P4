# b.
def InsertionSort(list):
    flag = False
    size = len(list)

    # Nothing needs sorting
    if size <= 1:
        return list


# c.
def OutputArray(arr):
    for i in arr:
        print(i, end=" ")


# e.
def Search(DataArray, ItemToFind):
    found = -1
    


# d.i.
def main():
    DataArray = [0, 3, 4, 56, 67, 44, 43, 32, 31, 345, 45, 6, 54, 1]
    OutputArray(DataArray)
    SortedArray = InsertionSort(DataArray)
    OutputArray(SortedArray)


main()
