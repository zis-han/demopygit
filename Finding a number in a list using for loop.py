def search(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            pos = i
            print("Found at", pos+1)
            break
    else:
        print("Not found")


nums = [45, 25, 21, 5, 22, 56]
x = 66

search(nums, x)

