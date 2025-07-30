from asyncio import as_completed
import numpy

# reshape
# array_kita = numpy.arange(6)
# reshaping = array_kita.reshape(2, 3)
# print(array_kita)
# print(reshaping)
# print(reshaping.flags['OWNDATA'])

# array_kita = numpy.array([1, 2, 3])
# hasil = numpy.resize(array_kita, (2, 3))
# print(hasil)

# matriks = numpy.array([[1, 2], [3, 4]])
# print(matriks.T)
# tensor = numpy.random.rand(2, 3, 4)
# hasil = numpy.transpose(tensor, (2, 0, 1))
# print(tensor.shape)
# print(hasil.shape)

# array_kita = numpy.array([1, 2, 3])
# flipping = numpy.flip(array_kita)
# print(array_kita)
# print(flipping)

# matriks = numpy.array([[1, 2], [3, 4]])
# print(numpy.flipud(matriks))

# matriks = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# subsetnya = matriks[0:2, 1:3]
# print(subsetnya)

# array_kita = numpy.array([1, 2, 3, 4, 5])
# filtering = array_kita > 3
# hasil = array_kita[filtering]
# print(hasil)

# matriks_a = numpy.array([[1, 2], [3, 4]])
# matriks_b = numpy.array([[5, 6], [7, 8]])
#
# hasil = numpy.concatenate((matriks_a, matriks_b), axis=1)
# print(hasil)

# array_kita = numpy.arange(8)
# hasil = numpy.split(array_kita, 4)
# print(array_kita)
# print(hasil)

# array_kita = numpy.array([1, 2, 3])
# print(array_kita.shape)
# hasil = numpy.expand_dims(array_kita, axis=0)
# print(hasil.shape)

# matriks_a = numpy.array([[1, 2, 3], [4, 5, 6]])
# matriks_b = numpy.array([10, 20, 30])
#
# hasil = matriks_a + matriks_b
# print(hasil)

data_ori = numpy.array([1, 2, 3])
# view = data_ori[:]
# view[0] = 20
# print(data_ori)
kopi = data_ori.copy()
kopi[0] = 90
print(data_ori)
print(kopi)
