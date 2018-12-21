import random


def main():
    arr_of_names = ["Arthur", "Merlin", "Lancelot", "Gawain", "Geraint", "Percival", "BorsTheYounger",
                    "Lamorak", "Kay", "Gareth", "Bedivere", "Gaheris", "Galahad", "Tristan", "Palamedes"]
    str_of_nums = "0123456789"
    len_of_arr = len(arr_of_names) - 1
    base_str = arr_of_names[random.randint(0, len_of_arr)]
    rand_nums = "".join(random.sample(str_of_nums, 6))
    password = base_str + rand_nums
    print(password)


main()
