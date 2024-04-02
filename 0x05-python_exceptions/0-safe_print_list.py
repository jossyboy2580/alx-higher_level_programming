#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    real_count = 0
    for i in range(x):
        try:
            item = my_list[i]
        except IndexError:
            break
        else:
            real_count += 1
            print("{}".format(item), end="")
    print()
    return (real_count)
