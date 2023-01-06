def set_bit(num, index):
    mask = 1 << index
    return num | mask

def clear_bit(num, index):
    mask = 1 << index
    return num & ~mask

def toggle_bit(num, index):
    mask = 1 << index
    return num ^ mask

def get_bit(num, index):
    return (num >> index) & 1
