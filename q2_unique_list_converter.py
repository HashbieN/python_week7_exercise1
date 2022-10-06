def unique(number_list):
    new_list = []   # create an empty list

    for i in number_list:
        if i not in new_list:
            new_list.append(i)

    return new_list

# Rujuk Whatsapp