import streamlit as st

st.set_page_config(layout='wide')
st.title('Portfolio Saya')
st.header('Data Scientist')

st.sidebar.title('Navigasi')

page = st.sidebar.radio('Pilih halaman', ['Tentang saya', 'Proyek', 'Prediction', 'Kontak'])

if page == 'Tentang saya':
    import tentang_saya
    tentang_saya.tampilkan()
elif page == 'Proyek':
    import proyek
    proyek.tampilan_proyek()
elif page == 'Prediction':
    import prediksi
    prediksi.lakukan_prediksi()
else:
    import kontak
    kontak.munculkan_kontak()