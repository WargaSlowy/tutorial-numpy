import numpy
from numpy import fft

# nilai_t = numpy.linspace(0, 1, 100, endpoint=False)
# sinyal = numpy.sin(2 * numpy.pi * 1 * nilai_t)
#
# hasil_fft = fft.fft(sinyal)
# frekuensi = fft.fftfreq(len(sinyal), nilai_t[1] - nilai_t[0])
#
# print(f"panjang sinyal: {len(sinyal)}")
# print(f"panjang fast fourier transform adalah: {len(hasil_fft)}")
# print(f"range dari frekuensiL {frekuensi[0]}, ke {frekuensi[-1]}")

# sinyal = numpy.array([1, 2, 3, 4])
# hasil_fft = fft.fft(sinyal)
# rekonstruksi = fft.ifft(hasil_fft)
#
# print(f"sinyal asli: {sinyal}")
# print(f"hasil fast fourier transform: {hasil_fft}")
# print(f"hasil dari rekonstruksi adalah: {rekonstruksi.real}")

n: int = 100
sample_data_rate: int = 1_000

frekuensi = fft.fftfreq(n, 1 / sample_data_rate)
print(f"nilai terakhir dari 10 frekuensi: {frekuensi[-10:]}")
