def split_half(x):
    length_x=len(x)
    half_x=length_x // 2
    add =0
    if length_x %2:
        add = 1
    left= x[:half_x + add]
    right= x[half_x+add:]
    return right+ left
odd= "aaabccc"
even="aaabbb"
print(split_half(even))
print(split_half(odd))

def unq_char(uq):
    len_str=len(uq)
    x= set(uq)
    len_set=len(x)
    return len_str == len_set
result_true= "abcde"
result_false="abccddee"
print(unq_char(result_true))
print(unq_char(result_false))










