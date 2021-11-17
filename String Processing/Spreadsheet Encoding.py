def spreadsheet_encode_column(col_str):
    num = 0
    for i in range(len(col_str)):
        num += (ord(col_str[-i-1]) - ord("A") + 1)*26**(i)
    return num


print(spreadsheet_encode_column("ZZ"))
