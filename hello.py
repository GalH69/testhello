def dec_to_minusbin(num, amount):
    #to bin
    bin_num = bin(num)
    bin_num = bin_num[2:]
    
    #complete to 2
    lst_bin = ['1' if bit == '0' else '0' for bit in bin_num]
    bin_num = "".join(lst_bin)
    bin_num = int(bin_num, 2)
    
    bin_num_one = bin(1)[2:]
    bin_num = bin_num + int(bin_num_one,2)
    
    print(int(bin_num,2))
dec_to_minusbin(5,8)
        