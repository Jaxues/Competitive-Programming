def maxLength(arr):
    len_list = [0]
    for x in arr:
        len_list.append(len(x))
    len_list = sorted(len_list)
    return len_list[-1] + len_list[-2]


print(maxLength(arr=["un","iq","ue"]))
print(maxLength(arr=["cha","r","act","ers"]))
print(maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
