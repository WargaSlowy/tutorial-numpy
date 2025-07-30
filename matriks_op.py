import numpy
# from numpy.linalg import inv
# from numpy.linalg import det
# from numpy.linalg import eig
# from numpy.linalg import solve
from numpy.linalg import svd

# matriks_pertama = numpy.array([[1, 2], [3, 4]])
# matriks_kedua = numpy.array([[5, 6], [7, 8]])
# vektor = numpy.array([1, 2])
# hasil = numpy.dot(matriks_pertama, vektor)
# print(hasil)

# matriks_a = numpy.array([[4, 7], [2, 6]])
# hasil_invers = inv(matriks_a)
# hasil_indentitas = numpy.dot(matriks_a, hasil_invers)
# print(hasil_indentitas)
# print(hasil_invers)

# matriks_a = numpy.array([[1, 2], [3, 4]])
# hasil_determinan = det(matriks_a)
# print(hasil_determinan)

# matriks_b = numpy.array([[1, 2], [2, 4]])
# hasil_determinan_matriks_b = det(matriks_b)
# print(hasil_determinan_matriks_b)

# matriks_a = numpy.array([[4, 2], [1, 3]])
# eigenvalue, eigenvektor = eig(matriks_a)
# print(f"eigen valuenya adalah: {eigenvalue}")
# print(f"eigen vektornya adalah: {eigenvektor}")

# matriks_a = numpy.array([[2, 3], [1, -1]])
# vektor_b = numpy.array([7, 1])
# hasil_nilai_x = solve(matriks_a, vektor_b)
# hasil_verif = numpy.dot(matriks_a, hasil_nilai_x)
# print(hasil_verif)

matriks_a = numpy.array([[1, 2], [3, 4], [5, 6]])

U, S, VT = svd(matriks_a, full_matrices=False)
print(U)
print(S)
print(VT)

rekonsturksi_data = numpy.dot(U * S, VT)
print(rekonsturksi_data)
