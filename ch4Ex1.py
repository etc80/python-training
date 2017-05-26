import os


def main():
    filename = select_file()
    print("selected file: {0}".format(filename))
    file_data = read_file_to_list(filename)
    print("lines in file: {0}; type of object: {1}".format(len(file_data), type(file_data)))
    work_with_list(file_data, filename)



def select_file():
    list_of_all_files = os.listdir()
    list_of_lst = []
    for file in list_of_all_files:
        if file.endswith('.lst'):
            list_of_lst.append(file)

    if len(list_of_lst) == 0:
        return input_filename()

    print_list(list_of_lst, "List of  LST files in directory:")
    while True:
        filenum = input("Select file from list by inputing number or press 0 to create new: ")
        filenum = int(filenum) if filenum is not None else -1
        if filenum in range(0, len(list_of_lst)+1):
            break
    if filenum == 0:
        return input_filename()
    else:
        return list_of_lst[filenum-1]


def print_list(list_to_print, message):
    print(message)
    list_to_print.sort()
    for i in range(0, len(list_to_print)):
        print("{0}: {1}".format(i+1, list_to_print[i]))


def input_filename():
    while True:
        filename = input("Input file name >> ")
        if filename:
            break
    return filename if filename.endswith(".lst") else filename+'.lst'


def read_file_to_list(filename):
    file_content = []
    try:
        f = open(filename, 'r')
        for line in f:
            file_content.append(line.replace('\n', ''))
    except FileNotFoundError:
        f = open(filename, 'a')
    finally:
        f.close()

    return file_content


def work_with_list(listname, filename):
    saved = True
    last_action = ""
    while True:
        if len(listname) == 0:
            print("-- no items are in the list --")
            print(show_dialog(delete="", save="" if saved else "[S]ave ", last_action=last_action), end='')
        else:
            print_list(listname, "")
            print(show_dialog(save="" if saved else "[S]ave ", last_action=last_action), end='')
        action = input()
        if action not in "AaDdSsQq":
            print("Error: invalid choice--enter one of 'AaDdSsQq'")
        elif action in "Aa":
            listname = add_item_to_list(listname)
            saved = False
            last_action = '[a]'
        elif action in "Dd":
            listname = delete_item_from_list(listname)
            saved = False
            last_action = "[d]"
        elif action in "Ss":
            save_results_in_file(listname, filename)
            saved = True
            last_action = "[s]"
        elif action in "Qq":
            if not saved:
                while True:
                    answer = input("Save unsaved changes (y/n) [y]:")
                    if (answer in "Yy") or (answer == ""):
                        save_results_in_file(listname, filename)
                        break
                    elif answer in "Nn":
                        break
                return
            else:
                return


def save_results_in_file(listname, fname):
    try:
        f = open(fname, 'w')
        for item in listname:
            f.write(item + '\n')
    except FileNotFoundError:
        print("Error in file reading/writing")
    finally:
        f.close()

    print("Saved {0} item{1} to {3}".format(len(listname), "" if len(listname) == 0 else "s", "", fname))


def add_item_to_list(listname):
    while True:
        item = input("Add item: ")
        if item:
            break
    listname.append(item)
    return listname


def delete_item_from_list(list):
    while True:
        item = int(input("Delete item number (or 0 to cancel): "))
        if item == 0:
            break
        elif item in range(1, len(list)+1):
            list.pop(item-1)
            break
    return list


def show_dialog(add="[A]dd ", delete="[D]elete ", save="[S]ave ", quite="[Q]uit ", last_action=""):
    dialog_string = "{0}{1}{2}{3} {4}: ".format(add, delete, save, quite, last_action)
    return dialog_string


main()
