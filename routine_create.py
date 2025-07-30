import numpy


# data = [[1, 2], [3, 4], [5, 6]]
# array_kita = numpy.array(data)
# print(array_kita)
# print(f"tipe datanya adalah: {array_kita.dtype}")
# print(f"shape dari data kita adlaha: {array_kita.shape}")
# array_kita = numpy.array([2, 4, 6, 8], dtype=numpy.int16)
# referensi_array = numpy.asarray(array_kita)
# print(referensi_array)
# print(f"tipe data dari si referensi array: {referensi_array.dtype}")

# array_nol = numpy.zeros((3, 4), dtype=numpy.float32)
# print(array_nol)

# array_satu = numpy.ones((2, 2), dtype=numpy.int32)
# print(array_satu)

# array_kita = numpy.full((2, 3), 200, dtype=numpy.int16)
# print(array_kita)

# array_kita = numpy.arange(0, 1, 0.1)
# print(array_kita)

# array_kita = numpy.linspace(0, 1, 5)
# print(array_kita)

# matriks_identitas = numpy.identity(3)
# print(matriks_identitas)

# matriks_diagonal = numpy.diag([2, 3, 4])
# print(matriks_diagonal)

# random_matriks_2dimensi = numpy.random.rand(2, 3)
# print(random_matriks_2dimensi)

# array_kita = numpy.random.randn(2, 2)
# print(array_kita)

# array_kita = numpy.random.randint(1, 100, size=(3,))
# print(array_kita)

def hitung(i, j):
    return i + j

array_kita = numpy.fromfunction(hitung, (3, 3))
print(array_kita)
