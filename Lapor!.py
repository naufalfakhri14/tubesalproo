import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from datetime import datetime
from PIL import Image
import io

if 'validasi' not in st.session_state:
    st.session_state.validasi = False
if 'username' not in st.session_state:
    st.session_state.username = False
    
if st.session_state.validasi == True:

    html_code = "<body style='background-image: url(\"./b1.jpg\"); background-size: cover;'></body>"
    st.markdown(html_code, unsafe_allow_html=True)


    
    df_laporan = pd.read_csv("./main.csv ")
    def buat_laporan(jenis_laporan,nama_pengirim,nomor_telepon,deskripsi_laporan, tanggal_laporan,instansi_laporan,kategori,file):
        waktu_laporan = datetime.now()
        df_laporan.loc[len(df_laporan)] = [jenis_laporan,nama_pengirim,nomor_telepon,deskripsi_laporan, tanggal_laporan,instansi_laporan,kategori,file]
        df_laporan.to_csv("./data.csv")

    def tampilkan_notifikasi(tipe, pesan):
        st.sidebar.text("")
        if tipe == "info":
            st.sidebar.info(pesan)
        elif tipe == "success": 
            st.sidebar.success(pesan)
        elif tipe == "warning":
            st.sidebar.warning(pesan)
        elif tipe == "error":
            st.sidebar.error(pesan)


    def load_data():
        df = pd.read_csv("/tubes/main.csv")
        return df 

    df_laporan = load_data()


    def buat_halaman_laporan():
        st.subheader("Sampaikan Laporan Anda")
        jenis_laporan = st.radio("Jenis Laporan", ["Pengaduan"])
        nama_pengirim = st.text_input("Nama Pengirim", help="Masukkan nama lengkap Anda")
        nomor_telepon = st.text_input("Nomor Telepon", help="Masukkan nomor telepon anada")
        deskripsi_laporan = st.text_area("Deskripsi Laporan", help="Deskripsikan laporan Anda secara singkat")
        tanggal_laporan = st.date_input("Tanggal Laporan")
        instansi_laporan = st.text_input("Instansi Laporan", help="Maksukan Perusahaan terkait penyalahgunaan")
        kategori = st.selectbox("Jenis Korupsi", ["penyuapan", "mark-up anggaran", "penyalahgunaan kekuasaan"])
        file = st.file_uploader("Upload a Laporan",type=["pdf"])
        size=st.empty()
        mode=st.empty()
        format_=st.empty()

        if file:
            with io.BytesIO(file.getvalue()) as f:
                size.markdown(f"<h6>size: {len(f.read())}</h6>", unsafe_allow_html=True)
                mode.markdown(f"<h6>mode: {file.type}</h6>", unsafe_allow_html=True)
                format_.markdown(f"<h6>format: {file.name.split('.')[-1]}</h6>", unsafe_allow_html=True)



        
        if st.button("Kirim Laporan"):
            if nama_pengirim and deskripsi_laporan:
                new_data = {"Jenis Laporan": jenis_laporan,
                            "Nama Pengirim": nama_pengirim,
                            "Deskripsi Laporan": deskripsi_laporan,
                            "Tanggal Laporan": tanggal_laporan,
                            "Instansi Laporan": instansi_laporan,
                            "Kategori": kategori,
                            "file": file}
                global df_laporan
                df_laporan.loc[len(df_laporan.index)] = [jenis_laporan,nama_pengirim,nomor_telepon,deskripsi_laporan, tanggal_laporan,instansi_laporan,kategori,file]
            

                st.success("Laporan berhasil dikirim!")

                df_laporan.to_csv("main.csv", index=False)

    
    def Tentang_Lapor():
            
            st.image('foto kelompok.jpg', caption='Kelompok 5',width=600)
            st.subheader("Apa itu Lapor!")
            st.write("Pengelolaan pengaduan pelayanan publik di setiap organisasi penyelenggara di Indonesia belum terkelola secara efektif dan terintegrasi. Masing-masing organisasi penyelenggara mengelola pengaduan secara parsial dan tidak terkoordinir dengan baik. Akibatnya terjadi duplikasi penanganan pengaduan, atau bahkan bisa terjadi suatu pengaduan tidak ditangani oleh satupun organisasi penyelenggara, dengan alasan pengaduan bukan kewenangannya. Oleh karena itu, untuk mencapai visi dalam good governance maka perlu untuk mengintegrasikan sistem pengelolaan pengaduan pelayanan publik dalam satu pintu. Tujuannya, masyarakat memiliki satu saluran pengaduan secara Nasional.")
            st.write("Lembaga pengelola SP4N-LAPOR! adalah Kementerian Pendayagunaan Aparatur Negara dan Reformasi Birokrasi (Kementerian PANRB) sebagai Pembina Pelayanan Publik, Kantor Staf Presiden (KSP) sebagai Pengawas Program Prioritas Nasional dan Ombudsman Republik Indonesia sebagai Pengawas Pelayanan Publik. LAPOR! telah ditetapkan sebagai Sistem Pengelolaan Pengaduan Pelayanan Publik Nasional (SP4N) berdasarkan Peraturan Presiden Nomor 76 Tahun 2013 dan Peraturan Menteri Pendayagunaan Aparatur Negara dan Reformasi Birokrasi Nomor 3 Tahun 2015.")
            st.write("SP4N-LAPOR! dibentuk untuk merealisasikan kebijakan “no wrong door policy” yang menjamin hak masyarakat agar pengaduan korupsi akan disalurkan kepada penyelenggara pelayanan publik yang berwenang menanganinya. SP4N bertujuan agar:")
            st.write("Penyelenggaraan mengelola pengaduan dari masyarakat secara sederhana, cepat, tepat, tuntas, dan terkoordinasi dengan baik,Penyelenggara memberikan akses untuk partisipasi masyarakat dalam menyampaikan pengaduan dan Meningkatkan kualitas pelayanan publik.")
            st.image('map.jpg',width=600)
            


    def lihat_daftar_laporan():
        st.subheader("Daftar Laporan")
        df_laporan = load_data()
        if not df_laporan.empty:
            st.dataframe(df_laporan)
        else:
            st.info("Belum ada laporan yang tercatat.")

    def load_data():
        df = pd.read_csv("/tubes/main.csv")
        return df 
    
    df_biodata = pd.read_csv("./biodata.csv")
              
    def biodata():
        st.subheader("Isi Biodata diri anda")   
        nama = st.text_input("Nama Lengkap", help="Deskripsikan laporan Anda secara singkat")
        nama_pengirim = st.text_input("username", help="Deskripsikan laporan Anda secara singkat")
        bio = st.text_area ("Bio", help="Deskripsikan laporan Anda secara singkat")
        email = st.text_input("email", help="Deskripsikan laporan Anda secara singkat")
        telp = st.text_input("No Telepeon", help="Deskripsikan laporan Anda secara singkat")
        ttl = st.date_input("Tanggal Lahir")
        nik = st.text_input("No. Induk Kependudukan (KTP)", help="Deskripsikan laporan Anda secara singkat")
        gender = st.selectbox("Jenis Kelamin", [

            "Laki-laki", "Perempuan"])
        perkerjaan = st.text_input("pekerjaan", help="Deskripsikan laporan Anda secara singkat")
        dis = st.selectbox("Penyandang Disabilitas?", ["Iya Disabilitas", "Tidak Disabilitas"])
        date = st.text_input("Tempat tinggal saat ini", help="Deskripsikan laporan Anda secara singkat")

        if 'biodata' not in st.session_state:
            st.session_state.biodata = False

        if st.button('SIMPAN'):
            st.session_state.biodata = True
            if nama and nama_pengirim and bio and email and telp and ttl and nik and gender and perkerjaan and dis and date:
                if 'biodata' not in st.session_state:
                    st.session_state['biodata'] = {
                        nama,
                        nama_pengirim,
                        bio,
                        email,
                        telp,
                        ttl,
                        nik,
                        gender,
                        perkerjaan,
                        dis,
                        date
                    }
                global df_biodata
                df_biodata.loc[len(df_biodata.index)] = [nama,nama_pengirim,bio,email,telp,ttl,nik,gender,perkerjaan,dis,date]
                df_biodata.to_csv("biodata.csv", index=False)

                st.success("sukses")
                st.balloons()

            else:
                st.error("Harus mengisi form")
                
   

    


    
    def PROFILE():
        df = pd.read_csv("./biodata.csv")
        df = df[df['nama_pengirim'] == st.session_state.username]
        print(df)
        st.write(df)

    def main():
        st.markdown("<h2 style='text-align: center; color: #FFFFFF; font-size: 20px;'>Aplikasi Layanan Laporan Korupsi Online</h2>", unsafe_allow_html=True)
        menu = ["About","Tentang Lapor", "Pengisian biodata diri","PROFILE","Sampaikan Laporan Anda", "Lihat Laporan" ]
        choice = st.sidebar.selectbox("Menu", menu)   
        print(choice)
        if choice == "About":
            st.subheader("Pengaduan")
            st.write("pengaduan adalah keluhan yang disampaikan kepada pengelola pengaduan pelayanan publik pada instansi Pemerintah atas pelayanan pelaksana yang tidak seusai dengan standar Pelayanan atas pelayanan pelaksana yang tidak sesuai dengan Standar Pelayanan atau pengabaian kewajiban dan/atau pelanggaran larangan oleh pengelola pengaduan pelayanan publik")


            st.subheader("wajib")
            st.write("1. Isi Biodata diri Anda Terebih Dahulu")
            st.write("2. Isi laporan : Menceritakan kronologis kejadian yang ingin dikeluhkan.Jika dibutuhkan sertakan juga data diri anda berupa nama dan NIK")
            st.write("3. Tanggal Kejadian: Tanggal ketika anda menerima pelayanan yang kurang memuaskan ")
            st.write("4. Pemilihan Jenis Korupsi: mengidentifikasi atau mengategorikan jenis tindak korupsi yang dilakukan")
            st.write("4. Dekripsi Laporan, mendeskripsikan pengalaman anda menerima pelayanan yang kurang memuaskan, lebih spesifik anda menginput, lebih baik")
            st.subheader("Opsional")
            st.write("1. Instansi Tujuan : Instansi yang berwenang terhadap pengaduan yang diberikan")
            st.write("2. Upbload File Laporan : meminta anda untuk mengunggah fie yang berisi bukti,dokumen,atau informasi tambahan yang mendukung laporan korupsi yang anda ajukan")

            st.subheader("NOTE")
            st.write("1. Laporan Anda relevan dengan kinerja pemerintah")
            st.write("2. Menggunakan Bahasa Indonesia yang baik dan benar")
            st.write("3. Bukan merupakan ujaran kebencian,SARA, dan caci maki")
            st.write("4. Bukan merupakan laporan yang sudah disampaikan dan masih dalam proses penanganan")
       
        elif choice == "Sampaikan Laporan Anda":
            buat_halaman_laporan()

        elif choice == "Pengisian biodata diri":
            biodata()   

        elif choice == "PROFILE":
            PROFILE()
            
        elif choice == "Lihat Laporan":
            lihat_daftar_laporan()

        elif choice == "Tentang Lapor": 
            Tentang_Lapor()


    if __name__ == "__main__":
        main()
else:
    st.write("Silahkan Login Dulu ")

