from Crypto.Util.py3compat import *

def pad(data_to_pad, block_size):
    padding_len = block_size - len(data_to_pad) % block_size
    padding = b''.join([bchr(i + 1) for i in range(padding_len)])
    return data_to_pad + padding


def unpad(padded_data, block_size):
    pdata_len = len(padded_data)
    if pdata_len % block_size:
        raise ValueError("Input data is not padded")
    padding_len = bord(padded_data[-1])
    if padding_len < 1 or padding_len > min(block_size, pdata_len):
        raise ValueError("Padding is incorrect.")
    padding = b''.join([bchr(i + 1) for i in range(padding_len)])
    if padded_data[-padding_len:] != padding:
        raise ValueError("Padding is incorrect.")
    return padded_data[:-padding_len]
