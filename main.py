import requests, json


print(r""" ____ _____         _     ____
|  _ |_   ____  ___| |__ / ___|
| |_) || |/ _ \/ __| '_ \\___ \
|  _ < | |  __| (__| | | |___) |
|_| \_\|_|\___|\___|_| |_|____/
""")

listPengirim = {
1:['JNE','jne'], 2: ['POS','pos'], 3:['TIKI','tiki'], 4:['Wahana Express','wahana'], 
5:['J&T','jnt'], 6:['RPX','rpx'], 7:['SAP','sap'], 8:['Sicepat Express','sicepat'], 
9:['JET','jet'], 10:['Ninja Express','ninja'], 11:['Lion Parcel','lion'], 
12:['REX', 'rex']
}

def getData(noresi, kurir):

	namaKurir = listPengirim[kurir][1]
	Perusahaan = listPengirim[kurir][0]
	url =  'https://api.terhambar.com/resi?resi={}&kurir={}'.format(noresi, namaKurir)
	req = requests.get(url)
	js = json.loads(req.text)
	if js['status']['code'] == 400:
		print('Nomor resi {} Tidak ditemukan di {} \nsilahkan pilih Kurir yang benar'.format(noresi, Perusahaan))
	else:
		info = js['result']
		print('''\n\t=========== Informasi ===========
Nama Kurir = {}
Tanggal Pengiriman = {}
Jam Pengiriman = {}
Pengirim = {}
Penerima = {}

From = {}
To = {}
'''.format(
	info['summary']['courier_name'], info['details']['waybill_date'], info['details']['waybill_time'], 
	info['details']['shippper_name'], info['details']['receiver_name'], info['details']['origin'],
	info['details']['destination']))


		for history in info['manifest']:
			print('''=======================================
Status = {}
Tanggal = {}
Jam = {}
Lokasi = {}
=======================================
'''.format(history['manifest_description'], history['manifest_date'], history['manifest_time'], history['city_name']))



if __name__ == "__main__":
	for num,i in enumerate(listPengirim):
		print(num+1,'=', listPengirim[i][0])

	print('\n\n\t\tPilih Kurir Sesuai Nomor')
	pilihan = int(input('Pilih Kurir = '))
	resi = input('Nomor Resi : ')
	getData(resi, pilihan)