import numpy

# def fungsi_linear(x):
#     return x

# def fungsi_step(x, threshold: int = 0):
#     return numpy.where(x >= threshold, 1, 0)


# def fungsi_sigmoid(x):
#     kalkulasi_x = numpy.clip(x, -500, 500)
#     return 1 / (1 + numpy.exp(-kalkulasi_x))
#
# def turunan_sigmoid(x):
#     sig = fungsi_sigmoid(x)
#     return sig * (1 - sig)
#
# nilai_x = numpy.array([-2, -1, 0, 1, 2])
# output = fungsi_sigmoid(nilai_x)
# print(f"hasil sigmoid adalah: {output}")
# print(f"hasil turunan sigmoid di nilai x = 0: {turunan_sigmoid(0)}")
# output = fungsi_step(nilai_x)
# print(output)
# output = fungsi_linear(nilai_x)
# print(f"inputnya adalah: {nilai_x}")
# print(f"linear outputnya adalah: {output}")


# def fungsi_aktivasi_tanh(x):
#     return numpy.tanh(x)
#
#
# def turunan_tanh(x):
#     return 1 - numpy.tanh(x) ** 2
#
#
# nilai = numpy.array([-2, 1, 3, 4, 1])
# output = fungsi_aktivasi_tanh(nilai)
# print(output)
# print(turunan_tanh(0))

def fungsi_relu(x):
    return numpy.maximum(0, x)

def turunan_relu(x):
    return numpy.where(x > 0, 1, 0)

nilai_x = numpy.array([-2, 4, 3, 12, -1, 20])
output = fungsi_relu(nilai_x)
print(turunan_relu(nilai_x))
