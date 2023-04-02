import matplotlib.pyplot as plt
import numpy as np

# data
thn = ['2019', '2020', '2021', '2022']
jumlah_mahasiswa = [131, 133, 130, 127]

# visualisasi jumlah mahasiswa
plt.bar(thn, jumlah_mahasiswa)
plt.title('Jumlah Daya Tampung Mahasiswa Baru SNMPTN IF/thn')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Mahasiswa')
plt.show()
