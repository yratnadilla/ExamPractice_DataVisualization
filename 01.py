from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

x = MongoClient('mongodb://localhost:27017/')

# access database and collections
db = x['kampus']
colDosen = db['dosen']
colMhs = db['mahasiswa']

# create list for 'dosen' from collection
dbDosen = []
for i in list(colDosen.find()):
    dbDosen.append(i)

dbDosenSort = []
for i in range(len(dbDosen)):
    dosen = {}
    dosen['nama'] = dbDosen[i]['nama']
    dosen['usia'] = dbDosen[i]['usia']
    dosen['asal'] = dbDosen[i]['asal']
    dosen['status'] = 'dosen'
    dbDosenSort.append(dosen)

# create dataframe for 'dosen'
dfDosen = pd.DataFrame(dbDosenSort)

# create list for 'mahasiswa' from collection
dbMhs = []
for i in list(colMhs.find()):
    dbMhs.append(i)

dbMhsSort = []
for i in range(len(dbMhs)):
    mhs = {}
    mhs['nama'] = dbMhs[i]['nama']
    mhs['usia'] = dbMhs[i]['usia']
    mhs['asal'] = dbMhs[i]['asal']
    mhs['status'] = 'mahasiswa'
    dbMhsSort.append(mhs)

# create dataframe for 'mahasiswa'
dfMhs = pd.DataFrame(dbMhsSort)

# plot dataframe
plt.bar(dfDosen['nama'], dfDosen['usia'], color = 'blue')
plt.bar(dfMhs['nama'], dfMhs['usia'], color = 'orange')

plt.legend(['Dosen', 'Mahasiswa'])
plt.show()