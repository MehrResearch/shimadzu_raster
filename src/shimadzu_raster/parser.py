import struct

endianness = 'little'

def parse_f64(bin):
    return struct.unpack('<d', bin)[0]

def parse_i32(bin):
    return struct.unpack('<i', bin)[0]

def parse_raster(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()

    chunks = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]

    n_points = parse_i32(chunks[6][4:])
    diameter = parse_f64(chunks[2])
    spacing = parse_f64(chunks[4])

    xy_chunks = chunks[7:]
    xys = [
        (parse_f64(x), parse_f64(y))
        for x, y in zip(xy_chunks[::2], xy_chunks[1::2])
    ]

    return {
        'n_points': n_points,
        'diameter': diameter,
        'spacing': spacing,
        'xys': xys
    }