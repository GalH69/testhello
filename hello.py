def dec_to_minusbin(num):
    #to bin
    bin_num = bin(num)
    bin_num = bin_num[2:]
    
    #complete to 2
    lst_bin = ['1' if bit == '0' else '0' for bit in bin_num]
        