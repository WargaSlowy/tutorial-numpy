import numpy

# 1. jika array tidak punya dimensi yang sama axis=0
# 2. untuk setiap dimensi, dimensinya akan dianggap kompatible
# array_data = numpy.array([1, 2, 3])
# hasil = array_data + 10
# print(hasil)

# matriks = numpy.array([[1, 2, 3], [4, 5, 6]])
# vektor = numpy.array([10, 20, 30])
# hasil = matriks + vektor
# print(matriks.shape)
# print(vektor.shape)
# print(hasil)

# matriks = numpy.array([[1, 2, 3], [4, 5, 6]])
# vektor = numpy.array([10, 20, 30])
# hasil = matriks + vektor
# print(hasil)

data = numpy.array([100, 200, 300])

min_value = data.min()
max_value = data.max()
normalisasi = (data - min_value) / (max_value - min_value)
print(normalisasi)
