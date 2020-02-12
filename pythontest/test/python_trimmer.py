from prettytable import PrettyTable


def trim_string(string_to_trim:str) -> str :
    split_strings = string_to_trim.split()
    mergedstring = ",".join(split_strings)
    print(mergedstring)



def trim_string_new(file_string:str) -> str:
    if file_string is None:
        return
    file_string=file_string.strip().replace("\"", "")
    if not file_string:
        return
    # print(file_string)
    split_strings=file_string.split()
    merged_string=','.join(split_strings)
    return merged_string


def append_to_csv():
    global strings_to_ignore, fileline, trimmed_string, ignored, trimmed_string_list
    file_write_new = open("output_formatted.csv", 'a+', encoding='UTF-8')
    file_read_new = open("input.csv", "r", encoding="UTF-8")
    strings_to_ignore = ["[", "]"]
    for fileline in file_read_new:
        trimmed_string = trim_string_new(fileline)
        if trimmed_string is None:
            pass
        else:
            ignored = any(string in trimmed_string for string in strings_to_ignore)
            if not ignored:
                # print(trimmed_string)
                trimmed_string_list = trimmed_string.split(",")
                file_write_new.write(','.join(trimmed_string_list) + "\n")
                # prettyTable.add_row(trimmed_string_list)
    file_write_new.close()


if __name__ == '__main__':
    # file = open("file", 'r')
    # file_w=open("filetowrite", 'w')
    # for fileline in file:
    #     csv_string=trim_string(fileline)
    #     file_w.write(csv_string)
    # file.close()
    # file_w.close()
    #
    # trim_string("account  1234  matched")
    file = open('input.csv', 'r', encoding="utf-8")
    file_write=open("output_formatted.csv", 'w', encoding='UTF-8')
    strings_to_ignore = ["[", "]"]
    prettyTable=PrettyTable(['Table','SourceCount','targetCount', 'Status'])
    file_write.write(','.join(['Table','SourceCount','targetCount', 'Status']) + "\n")
    for fileline in file:
        trimmed_string = trim_string_new(fileline)
        if trimmed_string is None:
            pass
        else:
            ignored = any(string in trimmed_string for string in strings_to_ignore)
            if not ignored:
                # print(trimmed_string)
                trimmed_string_list = trimmed_string.split(",")
                file_write.write(','.join(trimmed_string_list) + "\n")
                prettyTable.add_row(trimmed_string_list)

    # Use this if you want HTML table
    table=prettyTable.get_html_string()
    # file_write.write(str(prettyTable))
    file_write.close()
    file.close()

    append_to_csv()

    # trim_string_new("""account  1123  1124 FAIL""")
