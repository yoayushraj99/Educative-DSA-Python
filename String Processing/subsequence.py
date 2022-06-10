def get_all_subsequence(input, output, i):
    if i==len(input):
        print(output)
    else:
        # Exclude the first character
        get_all_subsequence(input, output, i+1)

        #Include the first character
        output+=input[i]
        get_all_subsequence(input, output, i+1)
    return

get_all_subsequence("abc","",0)
