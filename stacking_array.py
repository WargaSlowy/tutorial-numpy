import numpy

# data_a = numpy.array([1, 2, 3])
# data_b = numpy.array([4, 5, 6])
# hasil = numpy.stack((data_a, data_b), axis=1)
# print(hasil)

# data_a = numpy.array([1, 2, 3])
# data_b = numpy.array([4, 5, 6])
# hasil = numpy.vstack((data_a, data_b))
# print(hasil)

# data_a = numpy.array([1, 2, 3])
# data_b = numpy.array([4, 5, 6])
# hasil = numpy.hstack((data_a, data_b))
# print(hasil)

# data_a = numpy.array([[1], [2]])
# data_b = numpy.array([[3, 4], [5, 6]])
# hasil = numpy.hstack((data_a, data_b))
# print(hasil)

# data_a = numpy.array([[1, 2], [3, 4]])
# data_b = numpy.array([[5, 6], [7, 8]])
# hasil = numpy.dstack((data_a, data_b))
# print(hasil)

# data_a = numpy.array([1, 2, 3])
# data_b = numpy.array([4, 5, 6])
# hasil = numpy.column_stack((data_a, data_b))
# print(hasil)

data_a = numpy.array([1, 2, 3])
data_b = numpy.array([4, 5, 6])
hasil = numpy.row_stack((data_a, data_b))
print(hasil)
