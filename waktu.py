import numpy

# data_tanggal = numpy.datetime64("2023-01-01")
# data_detik = numpy.datetime64('2023-01-01T12:30:45.567')
# print(f"waktu ada detik: {data_detik}")
# print(f"waktu: {data_tanggal}")

# data_hari = numpy.datetime64('2025-01-01T12', 'h')
# print(data_hari

# satu_hari = numpy.timedelta64(20, 'm')
# print(satu_hari)

# waktu_mulai = numpy.datetime64('2025-01-01')
# waktu_habis= waktu_mulai + numpy.timedelta64(7, 'D')
# print(waktu_mulai)
# print(waktu_habis)

data_waktu = numpy.datetime64('2025-01-01')
data_waktu_kedua = numpy.datetime64('2025-05-03')
durasi = data_waktu_kedua - data_waktu
print(f"durasi adalah: {durasi}")
print(f"durasi jam yang dihabisin: {durasi / numpy.timedelta64(1, 'h')}")
