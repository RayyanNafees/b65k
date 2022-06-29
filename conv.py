
from string import printable


def file_to_int(path: str) -> int:
    with open(path, 'rb') as file:
        bytez = file.read()

    return int.from_bytes(bytez, 'big')


def int_to_bytes(intdata: int) -> bytes:
    bits = (intdata.bit_length()+7) // 8
    bytez = intdata.to_bytes(bits, 'big')
    return bytez


def int_to_file(intdata: int, filepath: str) -> None:
    bytez = int_to_bytes(intdata)
    with open(filepath, 'wb') as file:
        file.write(bytez)


def intfile_to_mediafile(intpath: str, mediapath: str) -> None:
    with open(intpath) as file:
        int_to_file(int(file.read()), mediapath)


def mediafile_to_intfile(filepath: str, savepath: str) -> None:
    bytez = open(filepath, 'rb').read()
    intz = int.from_bytes(bytez, 'big')
    print(intz, file=open(savepath, 'w'))


def toInt(intstr: str, chars: str) -> int:
    base = len(chars)
    def ind(char): return chars.find(char)
    dec_encoding = (ind(i)*(base**n) for n, i in enumerate(intstr[::-1]))
    return sum(dec_encoding)


def safe_toInt(intstr: str, chars) -> int:

    if type(chars) == int:
        assert chars <= len(printable), \
            f'integer conversions only supported till base {len(printable)} (not base {chars})'
        chars = printable[:chars]

    assert all([i in chars for i in intstr]), \
        'The supplied number has characters not in base i'

    return toInt(intstr, chars)


def highpow(base: int, num: int) -> int:
    expo = 0
    while base**expo <= num:
        expo += 1
    return expo-1


def highmul(base: int, num: int) -> int:
    mul = 0
    while base*mul <= num:
        mul += 1
    return mul-1


def highpowmul(base: int, num: int) -> dict:
    # divs = [base**i for i in reversed(range(highpow(base, num)+1))]
    pows = reversed(range(highpow(base, num)+1))

    while num:
        for p in pows:
            d = base**p
            div = highmul(d, num)
            num -= d*div
            yield div


def toBin(num: int) -> str:
    pows = {i: 0 for i in range(highpow(2, num), -1, -1)}

    while num:
        for p in pows:
            div = 2**p
            if div <= num:
                pows[p] = 1
                num -= div
    return ''.join(str(i) for i in pows.values())


def toTri(num: int) -> str:
    base = 3
    powmul = highpowmul(base, num)
    return ''.join(str(v) for v in powmul)


def toBase(num: int, chars: str) -> str:
    base = len(chars)    # chars = ''.join(str(i) for i in range(base))
    powmul = highpowmul(base, num)
    return ''.join(chars[v] for v in powmul)


def safe_toBase(num: int, chars: str) -> str:

    if type(chars) == int:
        assert chars <= len(printable), \
            f'integer conversions only supported till base {len(printable)} (not base {chars})'
        chars = printable[:chars]

    assert all([i in chars for i in str(num)]), \
        'The supplied number has characters not in base i'

    return toBase(num, chars)


1114111  # unicode
65536  # ascii


def toB65K(): pass
def toB1M(): pass
