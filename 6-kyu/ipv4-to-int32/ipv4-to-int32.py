def ip_to_int32(ip):
    return int(
        ''.join(bin(int(octet))[2:].zfill(8) for octet in ip.split('.')), 2
    )
