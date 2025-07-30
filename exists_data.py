import numpy

# data_list = [1, 2, 3, 4, 5]
# matriks_kita = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# tuple_kita = (20, 30, 40, 50)
# array_kita = numpy.array(tuple_kita)
# print(array_kita)
# print(array_kita.dtype)

# data_kita = numpy.array([1, 2, 3])
# data_view = numpy.asarray(data_kita)
# print(data_view)

# array_kita = numpy.loadtxt('data.csv', delimiter=',', dtype=numpy.float32)
# print(array_kita)
# print(array_kita.shape)
# print(array_kita.dtype)

# numpy.array([1, 2, 3, 4], dtype=numpy.int32).tofile('data.bin')
# load_data = numpy.fromfile('data.bin', dtype=numpy.int32)
# print(load_data)

# array_kita = numpy.array(range(10))
# print(array_kita)

# def generator_data(n):
#     for i in range(n):
#         yield i ** 2
#
# array_kita = numpy.fromiter(generator_data(5), dtype=numpy.int32, count=5)
# print(array_kita)

# data_kita= b'\x00\x00\x00\x00\x00\xf0\x00@'
# array_kita= numpy.frombuffer(data_kita, dtype=numpy.float64)
# print(array_kita)

data_kita = {'x': [1, 2], 'y': [3, 4]}
values = list(data_kita.values())
array_kita = numpy.array(values)
print(array_kita)
print(array_kita.shape)
