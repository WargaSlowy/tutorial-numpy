import numpy

# array_kita = numpy.array([1, 2, 3, 4, 5, 6])
# for value in array_kita:
#     print(value)

# array_kita = numpy.array([[1, 2], [3, 4], [5, 6]])
# for baris in array_kita:
#     print("barisnya adalah: ", baris)

# matriks = numpy.array([[1, 2], [3, 4], [5, 6]])
# for value in numpy.nditer(matriks):
#     print(value)

# matriks = numpy.array([[1, 2], [3, 4]], order='F')
# for x in numpy.nditer(matriks, order='C'):
#     print(x)

# matriks = numpy.array([1, 2, 3])
# for x in numpy.nditer(matriks, op_flags=['readwrite']):
#     x[...] = x * 2
# print(matriks)

# def hitung_baris(baris):
#     return numpy.mean(baris)
#
# def hitung_kolom(kolom):
#     return (kolom - numpy.min(kolom)) / (numpy.max(kolom) - numpy.min(kolom))
#
# matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# normalisasi = numpy.apply_along_axis(hitung_kolom, axis=0, arr=matriks)
# print(normalisasi)

array_kita = numpy.arange(1_000_000)
# kali = [x ** 2 for x in array_kita]
kali = array_kita ** 2
