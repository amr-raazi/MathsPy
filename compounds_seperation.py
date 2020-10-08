inp = input(">")


def num_of_digits(index, input_str):
    for i in range(len(input_str[index + 1:])):
        e = input_str[index + i + 1]
        if not e.isnumeric():
            return i + 1
    return len(input_str)


def replace_in_brackets(input_string):
    greeks = "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    count = 0
    list_with_numbers = []
    list_of_start_brackets_index = [i for i in range(len(input_string)) if input_string.startswith("(", i)]
    list_of_end_brackets_index = [i for i in range(len(input_string)) if input_string.startswith(")", i)]
    # get list of all elements in brackets + numbers
    for _ in range(len(list_of_start_brackets_index)):
        bracket_start_index = list_of_start_brackets_index[_]
        bracket_end_index = list_of_end_brackets_index[_]
        number_of_digits = num_of_digits(bracket_end_index, input_string)
        in_brackets_with_number = input_string[bracket_start_index:bracket_end_index + number_of_digits]
        list_with_numbers.append(in_brackets_with_number)
    # replace in string(bracket compounds + numbers) with greek pointer
    for i in range(1, len(list_with_numbers) + 1):
        input_string = input_string.replace(list_with_numbers[i - 1], greeks[i - 1])
    for groups in list_with_numbers:
        replacement = ""
        import re
        # find number outside bracket and elements inside
        elements = re.findall(r"\(([A-Za-z0-9_]+)\)", groups)
        elements = ''.join([str(e) for e in elements])
        number = groups.replace(elements, "").replace("()", "")
        # split into separated elements
        elements_separated = split_by_indices(elements, get_caps_indices(elements))
        # add number or multiply and add to string
        for element in elements_separated:
            if element[-1].isnumeric():
                letters = re.findall("[A-Za-z]", element)
                letters = ''.join([str(e) for e in letters])
                inside_number = re.findall(r'[0-9]', element)
                inside_number = ''.join([str(e) for e in inside_number])
                replacement += str(letters) + str(int(inside_number) * int(number))
            else:
                replacement += element + str(number)
        # replace greek pointers with substring
        input_string = input_string.replace(greeks[count], replacement)
        count += 1
    return input_string


def get_caps_indices(input_string):
    out = []
    for i in range(len(input_string)):
        char = input_string[i]
        if char.isupper():
            out.append(i)
    return out


def split_by_indices(input_string, indexes):
    out = []
    indexes.append(len(input_string))
    for _ in range(1, len(indexes)):
        out.append(input_string[indexes[_ - 1]:indexes[_]])
    return out


inp = replace_in_brackets(inp)
indices = get_caps_indices(inp)
print(split_by_indices(inp, indices))
