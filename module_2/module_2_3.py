my_list = int(input())
my_list = list(my_list)
i = -1
while i <= len(my_list):
    i = i + 1
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i] == 0:
        continue
    elif my_list[i] < 0:
        break
