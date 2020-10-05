inp = input(">")


def replace_in_brackets(input_string):
    greeks = "αβγδεζηθικλμνξοπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    count = 0
    list_with_numbers = []
    list_of_start_brackets = [i for i in range(len(input_string)) if input_string.startswith("(", i)]
    list_of_end_brackets = [i for i in range(len(input_string)) if input_string.startswith(")", i)]
    for _ in range(len(list_of_start_brackets)):
        e1 = list_of_start_brackets[_]
        e2 = list_of_end_brackets[_]
        y = input_string[e1:e2 + 2]
        list_with_numbers.append(y)
    for i in range(1, len(list_with_numbers) + 1):
        input_string = input_string.replace(list_with_numbers[i - 1], greeks[i - 1])
    for elements in list_with_numbers:
        zzz = ""
        number = elements[-1]
        elements = elements[:-1]
        get_caps = get_caps_indices(elements)
        elements_separated = split_by_indices(elements, get_caps)
        for element in elements_separated:
            element = element.replace("(", "").replace(")", "")
            if element[-1].isnumeric():
                zzz += element[:-1] + str(int(element[-1]) * int(number))
            else:
                zzz += element + str(number)
        input_string = input_string.replace(greeks[count], zzz)
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
