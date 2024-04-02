#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_count = 0
    for i in range(x):
        try:
            n = my_list[i]
            print("{:d}".format(n), end="")
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise
        else:
            real_count += 1
    print()
    return (real_count)
