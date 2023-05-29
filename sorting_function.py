#open file
def open_file(file):
    f = open(file,"r")
    data = f.read().split(",")
    new_data = []
    for i in range(len(data)):
        try:
            new_data.append(int(data[i]))
        except:
            new_data.append(float(data[i]))
    f.close()
    return new_data

def store_file(data,sorting_algorithm):
    #store in the new file
    f = open(f"sorted_data/sorted_data_using_{sorting_algorithm}.txt","w")
    f.write("\n".join(str(mynum) for mynum in data))
    f.close()

#### SORT Algorithm !!!!!!
def bubble_sort(file):
    #opening file
    data = open_file(file)
    # Sorting argument
    for i in range(len(data)):
        for j in range(len(data)-(i+1)):
            if data[j] > data[j+1]:
                swap = data[j]
                data[j] = data[j+1]
                data[j+1] = swap

    #storing file
    store_file(data,"bubble_sort")

def insertion_sort(file):
    #opening file
    data = open_file(file)
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1     
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key
    #storing file
    store_file(data,"insertion_sort")

def selection_sort(file):
        arr = open_file(file)
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index],arr[i]
        
        store_file(arr,"selection_sort")

# Native sort
def native_sort(file):
    data = open_file(file)
    data.sort()
    store_file(data,"native_sort")