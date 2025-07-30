import numpy

# angle = numpy.array([0, numpy.pi / 2, numpy.pi, 3 * numpy.pi / 2, 2 * numpy.pi])
# nilai_sin = numpy.sin(angle)
# nilai_cos = numpy.cos(angle)
# nilai_tangen = numpy.tan(angle)
# print(f"sudut dalam radian: {angle}\n")
# print(f"nilai sin nya adalah: {nilai_sin}\n")
# print(f"nilai cosinusnya adalah: {nilai_cos}\n")
# print(f"nilai tangennya adalah: {nilai_tangen}")

# value_nilai = numpy.array([-1, -0.5, 0, 0.5, 1])
# arcsin_nilai = numpy.arcsin(value_nilai)
# derajat = numpy.degrees(arcsin_nilai)
# print(f"nilai arcsin adalah (radian): {derajat}")

# nilai_arcos = numpy.arccos(value_nilai)
# derajat = numpy.degrees(nilai_arcos)
# print(f"arccos nilai (dalam radian): {derajat}")

# nilai_kita = numpy.array([-1, 0, 1])
# nilai_sinh = numpy.sinh(nilai_kita)
# print(f"sin hiperbolik adalah: {nilai_sinh}")
# nilai_cosh = numpy.cosh(nilai_kita)
# print(f"nilai cos hiperbolik adalah: {nilai_cosh}")

nilai_logit = numpy.array([-2, -1, 0, 1, 2])
output_nilai_tanh = numpy.tanh(nilai_logit)
print(f"fungsi aktivasi tanh: {output_nilai_tanh}")

output_dari_sigmoid = (1 + numpy.tanh(nilai_logit / 2)) / 2
print(f"fungsi aktivasi sigmoid: {output_dari_sigmoid}")
