import requests
import pandas as pd
from datetime import datetime
import time

base_url = "https://api-sscasn.bkn.go.id/2024/portal/spf"
kode_ref_pend = "4100230"
nama_jurusan = 'DIII Keperawatan'
pengadaan_kd= 4

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7",
    "connection": "keep-alive",
    "host": "api-sscasn.bkn.go.id",
    "origin": "https://sscasn.bkn.go.id",
    "referer": "https://sscasn.bkn.go.id/",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36"
}

def fetch_data(offset, retries=3, delay=5):
    params = {
        "kode_ref_pend": kode_ref_pend,
        "pengadaan_kd": pengadaan_kd,
        "offset": offset
    }
    
    for i in range(retries):
        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code == 200:
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                print(f"Error decoding JSON at offset {offset}: Response is not valid JSON.")
                return None
        elif response.status_code == 504:
            print(f"Request failed at offset {offset}: 504 Gateway Timeout. Retry {i+1}/{retries}...")
            time.sleep(delay) 
        else:
            print(f"Request failed at offset {offset}: {response.status_code}")
            return None
    
    print(f"Failed to fetch data after {retries} retries.")
    return None

print("Memulai proses pengambilan data...")
initial_data = fetch_data(0)
if initial_data:
    total_data = initial_data['data']['meta']['total']
    print(f"Total data ditemukan: {total_data}")
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    txt_output_file = f'data/sscasn_data_{timestamp}.txt'
    with open(txt_output_file, 'w') as txt_file:
        all_data = []
        for offset in range(0, total_data, 10):
            print(f"Mengambil data dengan offset {offset}...")
            data = fetch_data(offset)
            if data:
                all_data.extend(data['data']['data'])
                for record in data['data']['data']:
                    txt_file.write(str(record) + '\n')
        
        print("Konversi data ke DataFrame pandas...")
        df = pd.DataFrame(all_data)
        
        print("Menambahkan kolom link_pengumuman...")
        df['link_pengumuman'] = "https://sscasn.bkn.go.id/detailformasi/" + df['formasi_id']
        
        print("Menghapus kolom yang tidak diperlukan...")
        df = df.drop(columns=['formasi_id', 'disable']) 
        
        
        excel_output_file = f'data/sscasn_data_{timestamp}.xlsx'
        
        print("Menyimpan data ke file Excel...")
        with pd.ExcelWriter(excel_output_file, engine='xlsxwriter') as writer:
            workbook  = writer.book
            worksheet = workbook.add_worksheet(nama_jurusan)
            writer.sheets[nama_jurusan] = worksheet
            
            worksheet.write('A1', 'updated_at')
            worksheet.write('B1', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            worksheet.write('A2', 'auto_update_by')
            worksheet.write('B2', 'rj')
            
            df.to_excel(writer, nama_jurusan, startrow=3, index=False)
            

    print(f"Proses selesai! Data berhasil disimpan dalam file {excel_output_file} dan {txt_output_file}")
else:
    print("Gagal mengambil data awal.")
