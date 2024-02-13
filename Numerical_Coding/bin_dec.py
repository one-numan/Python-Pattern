def bin_to_dec(b):
    if b == '':
        return 0
    else:
        # print(b[:-1])

        return int(b[:-1]) + 2 * bin_to_dec(b[:-1])
        # return int(b[:-1])+2*bin_to_dec(b[::-1])


print(bin_to_dec('1010'))
