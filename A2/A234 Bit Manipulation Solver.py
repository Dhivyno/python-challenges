def set_bit(num, index):
    """ Set the bit at the given index to 1 """
    mask = 1 << index
    return num | mask

def clear_bit(num, index):
    """ Set the bit at the given index to 0 """
    mask = 1 << index
    return num & ~mask

def toggle_bit(num, index):
    """ Toggle the bit at the given index """
    mask = 1 << index
    return num ^ mask

def get_bit(num, index):
    """ Get the value of the bit at the given index """
    return (num >> index) & 1
