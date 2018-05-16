def map(n, arr1, arr2):
    result_list = []
    result = ""

    for x in range(0, n):
        result = bin(arr1[x] | arr2[x])
        result = result.replace("0b", "")
        result_list.append(result.zfill(n))

    for x in result_list:
        x = str(x).translate({ord('0') : ' ', ord('1') : '#'})
        print(x)
print(map(5, arr1 = [9,20,28,18,11], arr2 = [30,1,21,17,28]))