import requests
import pandas as pd

def download_csv_files(urls):
    dataframes = []

    for year_urls in urls:
        for url in year_urls:
            try:
                response = requests.get(url)

                if response.status_code == 200:
                    # Extract the file name from the URL
                    file_name = url.split('/')[-1]

                    # Save the content to a local file
                    with open(file_name, 'wb') as file:
                        file.write(response.content)
                        print(f"File '{file_name}' downloaded successfully!")

                    # Read the CSV file into a DataFrame
                    df = pd.read_csv(file_name)
                    dataframes.append(df)
                    print(f"File '{file_name}' converted to DataFrame")
                else:
                    print(f"Failed to download the file from {url}")

            except requests.exceptions.RequestException as e:
                print(f"An error occurred while downloading the file: {e}")

    return dataframes

# Example usage: Download CSV files for multiple years and convert to DataFrames
urls_2010 = ['https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/41b08d9bd4733b4647f0d52b605e96f5/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/6f1870c76251f77151374654b3e77b05/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/760d7447182e836ef74856d81c6bdd15/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/559a137d215110a1e878d4b5a5c632e5/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/28ea0dbb227233695d9888cf6e824999/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/786be94a21d5fe355391da03476b10f6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/669303cb235bf6f54dfe6b7890c69004/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/bbf5d9bda507bfd0829fbc0a48b1f42f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/308cd75945f07720307f941e367673c9/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/db655284b1201ea0a7a72f75f82a691b/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/0e3f26e54d40ff68c757b6e7235d2bbe/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2010.csv',
             'https://data.jakarta.go.id/dataset/40e5625d25852f1369c054acd1157491/resource/c7ded1f23c1af95823d7dc0e5d970047/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2010.csv'
    
]
urls_2011= ['https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/91aec72f1ce62b700e98acf4c27880b0/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/71b34fdd641f07e569483f7ac93de598/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/5293336fe38e189a0084c7bd5aac70ad/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/ac1b316f48a7a1cd8fd16a78cb7fa3a4/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/44525203a75f2a8b5b68e405215b1e94/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/4ea457ccca13234bd3986bab07a3ff12/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/302b732dfe736f191691fe10f089d05a/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/41dc0f05f240f8373cc7ad9e16ae2779/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/9129053ad2f678a001158fb1dccd1fd0/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/160bc49fca7136854d1fdc34325b7522/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/7fe52f289eb401ac77cc5612b067dddf/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2011.csv',
           'https://data.jakarta.go.id/dataset/bb29408e8acb38423aeb29875249eccd/resource/4eaabe688a72de58b9b868af5b6f0acb/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2011.csv'   
]
urls_2012=['https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/c731c8af6adb95c806ad556ce2a24529/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/449b0a843bea45f2f95e136c23ba26ed/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/95e397e43f3fefb9ee55a057ae7ee775/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/85d48d2494744cf0acf6f34f61b89c22/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/c7df13ece7af7b52faf4ce29fb7b2268/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/5f17641daaa02d3a3686e34072ba11d3/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/330c3a7969391a804b89104a9f9b4e96/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/51c8eee467cb31afbedbb8f85a1eb206/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/e9b3f94c22f3c8a93274d492f56d8bed/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/7379eaf1c3007b0c8f5911059a160429/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/4c15125bfbf3b0c78d739fea204c955d/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2012.csv',
           'https://data.jakarta.go.id/dataset/9cc1f18b8ae89a1503e0de3d28f85610/resource/f0130a3405cf556b2ea6b228cf049323/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2012.csv'
]
urls_2013=['https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/ffab75141ee67fd1621c131c93c838cf/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/3bfce369844cd45f554d971246d28dd5/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/5a86556b7590bdce035c8d6f6559f9ed/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/84586bcfdd07710f059284e51ed0563f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2013.csv'
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/a4738026981605ba4d4f9f73194344e7/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/5b5f318a6847b3aa9dd546bffef7193d/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/3b6b5c0d0ba05be1a040b0eda7e38d96/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/3c4fdd0808cb7da8c89e1114e6b24e14/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/96af600a2d439809522d3bfd9c423aa7/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/dde9e46a666daf1f02c321553be39f6f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/65c5a6d888536e2e95a2ca3ea506ab99/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2013.csv',
           'https://data.jakarta.go.id/dataset/8286f7c40a328bead5465112cb10c35d/resource/c502d877dfcaa4bcd63dd592fe910d89/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2013.csv'
]
urls_2014=['https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/23fa548d468d650bc8bd5058fec784aa/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/87f6175eb5f3b37425949f20260e9d72/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/523070ee388e02e4358f8c5f196e10de/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/241a200e7d9d11c8579946b065d622a8/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/ae71fc78d527c5cf6b76d168fc8b6beb/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/062bf86efc98efa63897ae2eb6c80479/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/af9921320cab5766318573f988493d31/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/d806cfe06338dec39f4c9ff299b51770/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/e6c81f16fdc541b8a9844546ae22e2a4/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/619499be0733fc44ced2f8a70fdcb010/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/7f23854b07c31669bf794b38c115ccfe/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2014.csv',
           'https://data.jakarta.go.id/dataset/261f29c7a1503f0b753b985a56fecffc/resource/897422a5babfaf21bd6e9bb5b3535fa2/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2014.csv'
]
urls_2015=['https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/e4e551b06873e264f82c2fc781ba50c8/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/7ba050c8b3616a12969817d4af6a94bd/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/750d77309766c104d20645c97c45344c/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/e2a10a0deb93fb3c2ea76bcd2d14b82c/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/6aa890ab63934df8f6e758088b64bc3f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/bf183c83da6496314c9b582a3237f5bf/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/bef876dc24a8b51d5585057f079f89ef/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/4f3ab9fb5a6b609b5a13a30ea022254f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/7839066084ccfe511169e19257a3afe4/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/a938016c592a7351f31c96032d566ed6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/51e373fb34f98ac5d7dab87f31373099/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2015.csv',
           'https://data.jakarta.go.id/dataset/8091a3655ef6a834432fb6b6501b9e94/resource/b60a8320f4b7c5b53c5a83c39821bde3/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2015.csv'
]
urls_2016=['https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/3934386f484faffff4a1f1e76fc0d4b9/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/18dbfbb564378e1323bce163e2044d76/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/6244d016a77e7dd53931df83bec8a71d/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/0d90ec62e422311a4d4a785f4f46d0b6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/650aed01361b553d0dd900fba0b9d6ba/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/0b1e6eca4d6f8653e1bbc2ebd1162755/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/91fcd752846949e517f8dd528b805020/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/3f0200c0858e2c3f0621702f6d282dc6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/bf27eb0d3eccb57dec8dd1983803a3ef/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/5ec64e33cbb639a9389fee702206727b/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/f03fd10a48f06a821de4db4026d03ab5/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2016.csv',
           'https://data.jakarta.go.id/dataset/2760a0c2076f906e7dae3ff66ab18bb6/resource/a442253bd2f0c76d798452fb3bc798ea/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2016.csv'    
]

urls_2017=['https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/f34a3884bff07895953d106b18758ad9/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/75494a32d90bac2ccd15779742572f65/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/84728695d49e076116bd21aaefc66447/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/837ee4f2a524cbacb841de08575b0532/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/dbe4df25f3b47615fb9c3957200412e6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/10c99031744ead0b2c5dbefa5620947a/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/f4225d5ee898def362e206d938cf427a/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/7b034c90483c3cc85d2c3ce9a37a2213/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/ff82082850f517310c155d58e1d0a83a/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/7904cc1befdb984b9d14b6ef811e595a/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/5217788fef002ca570dbeedb1d1e47e5/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2017.csv',
           'https://data.jakarta.go.id/dataset/d5f44adc75dab5c36fe9ccd46d3ac4b1/resource/32dde206e7790caa8aabe2f2a8052e91/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2017.csv'
]

urls_2018=['https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/8a219bca-d0b5-448d-b568-b33fedef6b52/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/d3178c76-8650-43f4-964a-e16a58687b24/download/Data-Indeks-Standar-Pencemar-Udara-di-Provinsi-DKI-Jakarta-Bulan-Februari-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/deadcc5e-9593-414a-8448-f254c78cc293/download/Data-Indeks-Standar-Pencemar-Udara-di-Provinsi-DKI-Jakarta-Bulan-Maret-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/f6a84399-aff0-4b52-b74b-a53984ffda57/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/25c8b390-7556-4616-a617-8a87ef6d537b/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/a1cf40ec-873d-4c9e-8936-a483b77546b8/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/5b040e92-243b-4f3d-98c9-11e1545d0d11/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/fb014573-8ce7-49c7-8582-26ba40e3951a/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/8bc5de4a-eaa3-4043-829d-21d42aeb9af4/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/c050ecb6-54c7-449d-9b45-f74f08db4a76/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/f3093692-eacf-4b12-9c17-a273123a6ab4/download/Data-Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2018.csv',
           'https://data.jakarta.go.id/dataset/e6e00f41-e007-4978-9c83-a6e43f3caaeb/resource/74aad9c2-b1b9-4607-8435-dd44c60f1d4e/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2018.csv'
]

urls_2019=['https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/b0b02c60-a4e2-4a16-acd6-5f6bbdfbdcd7/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/57de0e96-f412-4949-8695-2cb04f2f8c56/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/f0e396ab-fe10-42c8-8695-76661a229946/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/c09090fa-8913-4a34-8294-310d7573b45e/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/f9169f23-d211-470c-b052-c13050d9c21f/download/Indeks-Standar-Pencemar-Udara-di-Provinsi-DKI-Jakarta-Bulan-Mei-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/c5b4db86-51d0-489c-a119-e7e6cb82c923/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/f54b50a8-76f5-443c-831c-4e5d0390dbf3/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/e45c9079-1dd7-42cb-89b4-5dd8c2a056cb/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/4fa6b097-b0d3-4e79-ab20-d5513d95ee5f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/374c123c-c4b2-494f-9f4d-2908f2135657/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/3c29d60c-51a2-446a-a001-bd93191571d8/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2019.csv',
           'https://data.jakarta.go.id/dataset/a05a0872-1d6d-4747-82a7-de200ff571c2/resource/23c393da-635b-4fc5-aef3-f6c8e2bd5ab4/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2019.csv'

]

urls_2020=['https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/0f168955-5771-43a2-9fed-9c74ac3c268e/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/67f87e67-4edd-4e5b-94f9-36f40f9295e2/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/22e21493-0c34-4255-95a4-b13f3c93bbab/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/3fa0ddf9-1aee-4fc6-b751-eb52f71af1c6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/d40162f0-1a2b-40a5-8d53-c52a38b33550/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/6541c39e-6c56-490a-ae16-2a78ae67fa73/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/dd5b5b60bfba593c41e8615269d9d221/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/c1fb35547ac7117719b7f3ac71d6f385/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/3ad9f00b71e2f67f8fecf53cbf5a1fc7/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/b037e029b2ca89430ec64e62817e79bf/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/46a23fa64e3adb97f38191164e60694f/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2020.csv',
           'https://data.jakarta.go.id/dataset/dd749a07-d36d-4f13-9e86-7d0a84bb90f3/resource/d3e2e8c2a651743aadf09c734e937ce7/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Desember-Tahun-2020.csv'
]

urls_2021=['https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/c710303c60631a904b4f0896a842c685/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Januari-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/fd7baa5eb1fe779e2d43f7ce1ff88ee3/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Februari-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/b93b0a07d5f4ba9cad459748d0ed06c0/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Maret-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/225e6e838312eed24d951f0fca58596e/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-April-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/2e39ba6178a132a381ec073b94c9ede6/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Mei-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/cd2399dab95d976c11c42d7909aba0eb/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juni-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/2c22721cfcd2f932e8bb7a0e2a22e82a/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Juli-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/ae98bb60b96c74627ece0c274186043d/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Agustus-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/79aac0c6384472d1c3687f5a968e74ab/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-September-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/3777775ea4652ce8b140ac56f75c912e/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-Oktober-Tahun-2021.csv',
           'https://data.jakarta.go.id/dataset/3b56c00404adf8feb3f667cbbd700b7c/resource/f06cd7ab4925d3ac6c800a46101a130d/download/Indeks-Standar-Pencemar-Udara-di-SPKU-Bulan-November-Tahun-2021.csv'           
]

urls = [urls_2010, urls_2011, urls_2012, urls_2013, urls_2014,urls_2015,urls_2016,urls_2017,urls_2018,urls_2019,
        urls_2020,urls_2021]
dataframes = download_csv_files(urls)

# Concatenate the DataFrames and reset the index
merged_df = pd.concat(dataframes, ignore_index=True)

# Print the merged DataFrame
print(merged_df)

# Save merged DataFrame to CSV
merged_df.to_csv('/Users/rianrachmanto/pypro/project/Jakarta-Air-Quality-Prediction/data/raw/merged_data.csv', index=False)