def remove_zeros(number):
    number_str = str(number)
    return str(number_str).rstrip('0').rstrip('.') if '.' in number_str else number_str
