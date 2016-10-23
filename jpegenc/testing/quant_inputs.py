"""
Test inputs for the quantizer.
"""
# @todo: How were these generated ???  Create a github issue
#     How were these test inputs generated.  These should be replaced
#     with a model/function/object that generates the inputs instead
#     of static inputs


quant_rom = [
    16, 11, 10, 16, 24, 40, 51, 61,
    12, 12, 14, 19, 26, 58, 60, 55,
    14, 13, 16, 24, 40, 57, 69, 56,
    14, 17, 22, 29, 51, 87, 80, 62,
    18, 22, 37, 56, 68, 109, 103, 77,
    24, 35, 55, 64, 81, 104, 113, 92,
    49, 64, 78, 87, 103, 121, 120, 101,
    72, 92, 95, 98, 112, 100, 103, 99,

    17, 18, 24, 47, 99, 99, 99, 99,
    18, 21, 26, 66, 99, 99, 99, 99,
    24, 26, 56, 99, 99, 99, 99, 99,
    47, 66, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99,
    99, 99, 99, 99, 99, 99, 99, 99
]

quant_in = [
    10, 1000, 2047, 3, 4, 5, 6, 7,
    -1, -2, -3, -4, -5, -6, -7, -8,
    12, 13, 16, 17, 18, 18, 19, 20,
    111, 112, 113, 114, 115, 116, 117, 190,
    1111, 1112, 1113, 1212, 1232, 1214, 1542, 1432,
    999, -999, -1221, -1232, -12, -298, -123, 123,
    -111, -112, -113, -114, -115, -116, -117, -190,
    -12, -13, -16, -17, -18, -18, -19, -2048
]
