
def trim_string(string_to_trim:str) -> str :
    split_strings = string_to_trim.split()
    mergedstring = ",".join(split_strings)
    print(mergedstring)




if __name__ == '__main__':
    # file = open("file", 'r')
    # file_w=open("filetowrite", 'w')
    # for fileline in file:
    #     csv_string=trim_string(fileline)
    #     file_w.write(csv_string)
    # file.close()
    # file_w.close()

    trim_string("account  1234  matched")
