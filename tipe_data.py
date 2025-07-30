# dtype
# integer -> integer, unsigned integer
# floating point
# complex
# boolean
# string
# object
# datetime

# integer
# int8, int16
import numpy

# array_kita = numpy.array([1, 2, 3], dtype=numpy.int16)
# print(array_kita)
# print(array_kita.dtype)
# print(array_kita.itemsize)

# uint8, uint16
# array_kita = numpy.array([5], dtype=numpy.uint8)
# print(array_kita - 10)

# float32, float64
# array_kita = numpy.array([3.14159265718238123], dtype=numpy.float32)
# array_kita = numpy.array([3.1415926512873811236], dtype=numpy.float64)
# print(array_kita[0])

# complex64, complex128
# array_kita = numpy.array([1 + 2j, 3 - 4j], dtype=numpy.complex64)
# print(array_kita[0])
# print(array_kita.dtype)

# nilai = numpy.array([True, False, True], dtype=bool)
# print(nilai.dtype)

# str_
# nama = numpy.array(["Riski", "Nongpal", "Nizwa"], dtype='U10')
# nama = numpy.array([b'hello', b'apa kabar mawokoawkoakwoka asduhuahsd'], dtype='S10')
# print(nama)
# print(nama.dtype)

# objek_array = numpy.array([[1, 2], {'b': 1}, lambda x: x ** 2], dtype=object)
# print(objek_array)
# print(objek_array.dtype)

# waktu = numpy.array(['2020-01-01', '2025-01-02'], dtype='datetime64[D]')
# print(waktu)
# print(waktu[1] - waktu[0])
