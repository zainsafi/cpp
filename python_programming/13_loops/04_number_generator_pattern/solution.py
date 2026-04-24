def number_pattern(n):
    if not isinstance(n,int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'
    result = ''
    for num in range(1,n + 1):
        result +=  str(num) + ' '
    return result.strip() # remove extra space


print(number_pattern(8))