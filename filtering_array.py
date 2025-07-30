import numpy

# data_kita = numpy.array([1, 2, 3, 4, 5])
# masking = data_kita > 3
# filtering = data_kita[masking]
# print(masking)
# print(filtering)

# data_kita = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# masking = (data_kita > 3) & (data_kita < 8)
# filtering = data_kita[masking]
# print(filtering)

# data_kita = numpy.array([10, 20, 30, 40, 50])
# data_indexing = numpy.array([0, 2, 4])
# filtering = data_kita[data_indexing]
# print(filtering)

# matriks = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# baris_matriks = numpy.array([0, 2])
# filtering = matriks[baris_matriks]
# print(filtering)

# data = numpy.array([1, 2, 3, 4, 5])
# hasil = numpy.where(data > 3, data * 2, data)
# print(hasil)

# data = numpy.array([1, 5, 3, 8, 2])
# data_indeks = numpy.where(data > 4)
# print(data[data_indeks])

# data_kita = numpy.array([0, 1, 0, 3, 0, 5])
# data_indeks = numpy.nonzero(data_kita)
# print(data_indeks[0])
# print(data_kita[data_indeks])

data_kita = numpy.array([1, 2, 3, 4, 5])
masking = data_kita > 3
indeks_data = numpy.nonzero(masking)
print(indeks_data[0])
print(data_kita[indeks_data])
