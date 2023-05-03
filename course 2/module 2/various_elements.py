list_input = [int(num) for num in input().split()]
output_list = []
for i in list_input:
    if i not in output_list:
        output_list.append(i)
print(len(output_list))
