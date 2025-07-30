import numpy
import numpy.char as nchar

# list_nama_pertama = numpy.array(["riski", "ramat", "joe"])
# list_nama_kedua = numpy.array(["gema", "gempi", "gemu"])
# hasil = nchar.add(nchar.add(list_nama_pertama, ' '), list_nama_kedua)
# print(f"hasilnya adalah: {hasil}")

# list_nama = numpy.array(["data_kita", "data_lapor", "data_makan"])
# tambahin_format = nchar.add(list_nama, '.csv')
# print(f"file dengan ekstensi csv: {tambahin_format}")

# list_data_nama = numpy.array(["james", "doe", "jack"])
# list_data_nama_kedua = numpy.array(["RICK", "BLACK", "DoE"])
# nama_huruf_besar = nchar.upper(list_data_nama)
# nama_huruf_kecil = nchar.lower(list_data_nama_kedua)
# print(nama_huruf_besar)
# print(nama_huruf_kecil)

# list_kata = numpy.array(["indonesia", "pasal 1 adalah pasal kesatuan", "indonesia merupakan negara republik"])
# kata_title = nchar.title(list_kata)
# print(kata_title)
# kapitalisasi = nchar.capitalize(list_kata)
# print(kapitalisasi)

# data_email = numpy.array(["wello@gmail.com", "dede@yahoo.com", "gema@proton.com"])
# data_update = nchar.replace(data_email, 'gmail', 'google')
# print(data_update)

data_string = numpy.array(["Wello Apa Kabar", "WELLO APA"])
replace_dta = nchar.replace(data_string, 'Wello', 'oe bro')
print(replace_dta)
