def run():
    
    print('Masukan Identitas KTP ')
    NIK = input('No NIK : ')
    nama = input('Nama : ')
    ttl = input('Tempat/Tanggal Lahir : ')
    kecamatan = input('Kecamatan : ')
    print('Agama')
    print('1:Islam')
    print('2:Kristen')
    print('3:Khatolik')
    print('4:Hindu')
    print('5:Budha')
    agama =input('Pilihan : ')
    if agama == 1:
            print('Islam')
    elif agama == 2:
            print('Islam')
    elif agama == 3:
            print('Islam')
    elif agama == 4:
            print('Islam')
    elif agama == 5:
            print('Islam')

    pekerjaan = input('Pekerjaan : ')
    negara = input('Kewarga Negaraan : ')
    berlaku = input('Berlaku Hingga : ')
 
    print('================================')
    print('Identitas KTP')
    print('NIK : '+NIK)
    print('Nama : ' + nama)
    print('Tempat/Tanggal Lahir : ' + ttl)
    print('Kecamatan : ' + kecamatan)
    print('Agama : ' + agama)
    print('Pekerjaan : ' + pekerjaan)
    print('KewargaNegaraan: ' + negara)
    print('Berlaku Hingga: ' + berlaku)
 
if __name__ == '__main__':
    run()
