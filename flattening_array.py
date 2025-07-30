import numpy

# matriks = numpy.array([[1, 2], [3, 4], [5, 6]])
# flattening = numpy.ravel(matriks, order='C')
# print(flattening)

# matriks = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# flattening = matriks.flatten(order='F')
# print(flattening)

# matriks = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
# flattening = matriks.reshape(-1)
# print(flattening)

data_tensor = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
flattening = data_tensor.reshape(-1)
print(flattening)
