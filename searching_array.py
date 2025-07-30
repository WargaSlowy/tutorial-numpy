import numpy

# data = numpy.array([20, 30, 40, 80, 120, 300, 650, 90])
# indexing_data = numpy.where(data > 80, 100, data)
# print(f"valuenya adalah: {indexing_data}")

# data = numpy.array([30, 20, 50, 80, 90, 100])
# maks_index = numpy.argmax(data)
# minimal_index = numpy.argmin(data)
# print(f"datanya adalah: {data}")
# print(f"maksimal indexnya adalah: {maks_index}")
# print(f"maksimal valuenya adalah: {data[maks_index]}")
# print(f"minimal data indexnya adalah: {minimal_index}")
# print(f"minimal valuenya adalah: {data[minimal_index]}")

# matriks = numpy.array([[1, 5, 3], [9, 2, 8], [4, 7, 6]])
# flat_index = numpy.argmax(matriks)
# baris, kolom = numpy.unravel_index(flat_index, matriks.shape)
# print(f"posisi: baris -> {baris}, kolom -> {kolom}")
# print(f"valuenya adalah: {matriks[baris, kolom]}")

vektor = numpy.array([1, 3, 5, 7, 9])
# valuenya: int = 6
value = numpy.array([0, 4, 6, 10])
posisi = numpy.searchsorted(vektor, value)
print(f"posisi yang di insert: {posisi}")
# posisi = numpy.searchsorted(vektor, valuenya)
# print(f"posisi yang akan di sisip: {posisi}")
# print(
#     f"array nilai yang akan dimasukkan valuenya: {numpy.insert(vektor, posisi, valuenya)}"
# )
