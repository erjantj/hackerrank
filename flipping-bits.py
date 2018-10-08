def flippingBits(n):
    n_bin = "{0:b}".format(n)
    n_bin_len = len(n_bin)

    n_bin_32 = ''
    inverted = ''
    
    for i in range(32):
        if i < n_bin_len:
            n_bin_32 += n_bin[i]
        else:
            n_bin_32 = '0'+n_bin_32
    
    for i in range(32):
        if n_bin_32[i] == '1':
            inverted += '0'
        else:
            inverted += '1'

    return int(inverted, 2)


print(flippingBits(1))

1111111111111111111111111111111