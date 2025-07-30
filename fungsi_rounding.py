import numpy

# value_koma = numpy.array([3.14159, 2.71828, 1.14121])
# rounding = numpy.around(value_koma, decimals=2)
# print(f"nilai tanpa rounding: {value_koma}")
# print(f"nilai dengan rounding: {rounding}")

# value_koma = numpy.array([1.4, 1.6, 2.5, 3.5])
# rounding = numpy.around(value_koma)
# print(f"rounding angka ke integer terdekat: {rounding}")

# nilai_value = numpy.array([3.7, 3.2, -3.2, -3.7])
# floring = numpy.floor(nilai_value)
# ceiling = numpy.ceil(nilai_value)
# print(f"nilai value: {nilai_value}\n")
# print(f"nilai hasil flooring: {floring}\n")
# print(f"nilai hasil ceiling adalah: {ceiling}\n")

value_nilai = numpy.array([3.7, 3.2, -3.2, -3.7])
# hapus_bilangan_koma = numpy.trunc(value_nilai)
koma_nol = numpy.fix(value_nilai)
print(f"hasilnya adalah: {koma_nol}")
# print(f"value nilai adalah: {value_nilai}\n")
# print(f"hasil bilangan yang dihapus komanya: {hapus_bilangan_koma}")
