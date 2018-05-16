def map(n, arr1, arr2):
    invert1 = []
    invert2 = []
    result = []
    str_invert = []
    length_check = 0

    for x in range(0, n):       # invert에 입력받은 숫자를 2진수로 변환해서 대입
        invert1.append(int(bin(arr1[x]).replace("0b", "")))
        invert2.append(int(bin(arr2[x]).replace("0b", "")))

    for x in range(0, n):
        length_check = len(str(invert1[x]))
        str_invert = str(invert1[x])

        if length_check < n:
            for k in range(0, n - length_check):
                str_invert = "0" + str_invert
        invert1[x] = int(str_invert)

        length_check = len(str(invert2[x]))
        str_invert = str(invert2[x])

        if length_check < n:
            for k in range(0, n - length_check):
                str_invert = "0" + str_invert
        invert2[x] = int(str_invert)


    for x in range(0, n):
        result.append(invert1[x] | invert2[x])

    for x in range(0, n):
        print(result[x])
        print("\n")

num = int(input("몇 줄 입력? "))

arr1 = []
arr2 = []

for x in range(0, num):
    arr1.append(int(input()))
for x in range(0, num):
    arr2.append(int(input()))

map(num, arr1, arr2)