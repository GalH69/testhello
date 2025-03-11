def dec_to_minusbin(num, amount):
    #to bin
    bin_num = bin(num)
    bin_num = bin_num[2:]
    text_bin_num = f"{bin_num}"
    
    missing_zeros = amount - len(bin_num)
    text_bin_num = ('0' * missing_zeros) + text_bin_num
    
    #complete to 2
    lst_bin = ['1' if bit == '0' else '0' for bit in text_bin_num]
    text_bin_num = "".join(lst_bin)
    bin_num = int(text_bin_num, 2)
    
    
    bin_num = bin(bin_num)[2:]
    bin_num_one = bin(1)[2:]
    bin_num = bin_num + bin_num_one
    
    print(bin_num)
dec_to_minusbin(5,8)



# def dec_to_minusbin(num, amount):
#     # שלב 1: המרת המספר לעשרוני לבינארי
#     bin_num = bin(num)[2:]  # מסיר את '0b'
    
#     # שלב 2: השלמת הביטים החסרים
#     missing_zeros = amount - len(bin_num)
#     bin_num = ('0' * missing_zeros) + bin_num  # הוספת אפסים משמאל

#     # שלב 3: היפוך כל הביטים (משלים ל-1)
#     inverted_bin = ''.join('1' if bit == '0' else '0' for bit in bin_num)

#     # שלב 4: הוספת 1 למשלים ל-2
#     inverted_dec = int(inverted_bin, 2)  # המרה לעשרוני
#     twos_complement_dec = inverted_dec + 1  # הוספת 1
#     twos_complement_bin = bin(twos_complement_dec)[2:]  # חזרה לבינארי

#     # שלב 5: הבטחת מספר ביטים נכון (בלי `zfill()`)
#     missing_zeros = amount - len(twos_complement_bin)  # כמה אפסים חסרים אחרי החיבור
#     twos_complement_bin = ('0' * missing_zeros) + twos_complement_bin  # השלמה ידנית

#     print(twos_complement_bin)  # הדפסת התוצאה

# # בדיקה
# dec_to_minusbin(5, 8)