def dec_to_minusbin(num):
    #to bin
    bin_num = bin(num)
    bin_num = bin_num[2:]
    
    #complete to 2
    for n in bin_num:
        