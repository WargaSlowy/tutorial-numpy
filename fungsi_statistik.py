import numpy

# data = numpy.array([1, 2, 3, 4, 5])
# nilai_mean = numpy.mean(data)
# print(f"perseberan data: {data}")
# print(f"nilai rata-rata adalah: {nilai_mean}")

# matriks = numpy.array([[1, 2, 3], [4, 5, 6]])
# baris_mean = numpy.mean(matriks, axis=1)
# kolom_mean = numpy.mean(matriks, axis=0)
# print(f"mean dari baris adalah: {baris_mean}")
# print(f"mean dari kolom adalah: {kolom_mean}")

# data = numpy.array([1, 2, 3, 4, 5])
# nilai_median = numpy.median(data)
# print(f"median dari datanya adalah: {nilai_median}")

# data = numpy.array([1, 2, 3, 4, 100])
# nilai_mean = numpy.mean(data)
# nilai_median = numpy.median(data)
#
# print(f"nilai mean dengan outlier: {nilai_mean}")
# print(f"nilai median dengan outlier: {nilai_median}")

# data = numpy.array([1, 2, 3, 4, 5])
# std_deviasi = numpy.std(data)
# print(f"nilai standar deviasinya adalah: {std_deviasi}")

# data = numpy.array([1, 2, 3, 4, 5])
# pop_stdeviasi = numpy.std(data, ddof=1)
# print(pop_stdeviasi)
# varience = numpy.var(data)
# print(varience)

# data = numpy.array([3, 1, 4, 1, 5, 9, 2, 6])
# nilai_min = numpy.min(data)
# nilai_max = numpy.max(data)
# print(f"nilai min adalah: {nilai_min}")
# print(f"nilai max adalah: {nilai_max}")

# data = numpy.array([1, 3, 5, 7, 9])
# range_data = numpy.ptp(data)
# print(range_data)

data_value = numpy.array([1, 2, 3, 4])
data_bobot = numpy.array([1, 2, 3, 4])

bobot_nilai_rata_rata = numpy.average(data_value, weights=data_bobot)
rata_rata_simple = numpy.average(data_value)
print(f"rata-rata nilai bobot: {bobot_nilai_rata_rata}")
print(f"\nrata rata sederhana: {rata_rata_simple}")
