import numpy

# data_kita = numpy.array([1, 2, 3, 4, 5])
# hasil = numpy.array_split(data_kita, 3)
# for i, partisi in enumerate(hasil):
#     print(f"bagian dari {i + 1}: {partisi}")


# matriks = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# partisi = numpy.array_split(matriks, 3)
# for i, partisi in enumerate(partisi):
#     print(f"bagian {i + 1}: \n{partisi}")

# data_kita = numpy.array([1, 2, 3, 4, 5, 6])
# partisi_data = numpy.split(data_kita, 3)
# for i, partisi in enumerate(partisi_data):
#     print(f"bagian {i + 1}: {partisi}")

# matriks = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# partisi_data = numpy.split(matriks, 2, axis=1)
# for i, partisi in enumerate(partisi_data):
#     print(f"bagian {i + 1}:\n{partisi}")

# matriks = numpy.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# partisi_data = numpy.vsplit(matriks, 2)
# for i, partisi in enumerate(partisi_data):
#     print(f"bagian dari {i + 1}:\n {partisi}")

# matriks = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# partisi_data = numpy.hsplit(matriks, 2)
# for i, partisi in enumerate(partisi_data):
#     print(f"bagiannya {i + 1}:\n {partisi}")

data_tensor = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
partisi_data = numpy.dsplit(data_tensor, 2)
for i, partisi in enumerate(partisi_data):
    print(f"bagian {i + 1}:\n {partisi}")
