init python:
    def list_sort(a):
        a.sort(reverse=True)
        return a
    def find_in_nested_list(list, item):
        for sub_list in list:
            if item in sub_list:
                return (list.index(sub_list), sub_list.index(item))