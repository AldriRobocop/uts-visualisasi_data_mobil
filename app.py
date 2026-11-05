from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analisis Mobil Bekas", page_icon="🚗", layout="wide")
DATA_PATH = Path(__file__).parent / "data" / "used_cars_clean.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["tahun"] = pd.to_numeric(df["tahun"], errors="coerce")
    df["harga"] = pd.to_numeric(df["harga"], errors="coerce")
    df["jarak_tempuh_km"] = pd.to_numeric(df["jarak_tempuh_km"], errors="coerce")
    return df.dropna(subset=["tahun", "harga", "jarak_tempuh_km"])

df = load_data()
st.title("🚗 Dashboard Analisis Harga Mobil Bekas")
st.caption("Eksplorasi harga, merek, tahun produksi, jarak tempuh, bahan bakar, dan persebaran kota.")

with st.sidebar:
    st.header("Filter Data")
    cities = st.multiselect("Pilih kota", sorted(df.kota.unique()), default=sorted(df.kota.unique()))
    brands = st.multiselect("Pilih merek", sorted(df.merek.unique()), default=sorted(df.merek.unique()))
    fuels = st.multiselect("Jenis bahan bakar", sorted(df.bahan_bakar.unique()), default=sorted(df.bahan_bakar.unique()))
    year_min, year_max = int(df.tahun.min()), int(df.tahun.max())
    years = st.slider("Rentang tahun produksi", year_min, year_max, (year_min, year_max))

filtered = df[df.kota.isin(cities) & df.merek.isin(brands) & df.bahan_bakar.isin(fuels) & df.tahun.between(*years)]
if filtered.empty:
    st.warning("Tidak ada data untuk kombinasi filter ini. Silakan ubah filter.")
    st.stop()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Jumlah mobil", f"{len(filtered):,}".replace(',', '.'))
c2.metric("Rata-rata harga", f"₹ {filtered.harga.mean():,.0f}")
c3.metric("Median harga", f"₹ {filtered.harga.median():,.0f}")
c4.metric("Rata-rata jarak tempuh", f"{filtered.jarak_tempuh_km.mean():,.0f} km")
st.divider()

left,right = st.columns(2)
with left:
    by_year = filtered.groupby('tahun',as_index=False).harga.mean()
    fig = px.line(by_year,x='tahun',y='harga',markers=True,title='Tren Rata-rata Harga berdasarkan Tahun Produksi',labels={'tahun':'Tahun produksi','harga':'Rata-rata harga (₹)'})
    st.plotly_chart(fig,use_container_width=True)
with right:
    by_brand = filtered.groupby('merek',as_index=False).harga.median().sort_values('harga',ascending=False).head(12)
    fig = px.bar(by_brand,x='harga',y='merek',orientation='h',title='12 Merek dengan Median Harga Tertinggi',labels={'harga':'Median harga (₹)','merek':'Merek'})
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig,use_container_width=True)
left,right = st.columns(2)
with left:
    fuel = filtered.bahan_bakar.value_counts().rename_axis('bahan_bakar').reset_index(name='jumlah')
    fig = px.pie(fuel,names='bahan_bakar',values='jumlah',hole=.45,title='Komposisi Jenis Bahan Bakar')
    st.plotly_chart(fig,use_container_width=True)
with right:
    fig = px.scatter(filtered,x='jarak_tempuh_km',y='harga',color='bahan_bakar',hover_data=['merek','model','kota','tahun'],title='Hubungan Jarak Tempuh dan Harga',labels={'jarak_tempuh_km':'Jarak tempuh (km)','harga':'Harga (₹)'})
    st.plotly_chart(fig,use_container_width=True)

city = filtered.groupby('kota',as_index=False).agg(jumlah_mobil=('harga','size'),median_harga=('harga','median')).sort_values('jumlah_mobil',ascending=False)
st.subheader('Persebaran Mobil per Kota')
st.plotly_chart(px.bar(city,x='kota',y='jumlah_mobil',color='median_harga',title='Jumlah Mobil dan Median Harga per Kota',labels={'kota':'Kota','jumlah_mobil':'Jumlah mobil','median_harga':'Median harga (₹)'}),use_container_width=True)

st.subheader('Insight berdasarkan filter aktif')
most_city = filtered.kota.value_counts().idxmax()
most_brand = filtered.merek.value_counts().idxmax()
most_fuel = filtered.bahan_bakar.value_counts().idxmax()
corr = filtered[['jarak_tempuh_km','harga']].corr().iloc[0,1]
st.markdown(f"""
- Kota dengan listing terbanyak pada filter aktif adalah **{most_city}** ({filtered.kota.value_counts().max()} mobil).
- Merek yang paling sering muncul adalah **{most_brand}** ({filtered.merek.value_counts().max()} mobil).
- Bahan bakar terbanyak adalah **{most_fuel}** ({filtered.bahan_bakar.value_counts().max()} mobil).
- Korelasi Pearson antara jarak tempuh dan harga adalah **{corr:.2f}**. Nilai ini menunjukkan arah/kekuatan hubungan linear, bukan sebab-akibat.
""")

st.subheader('Data mobil sesuai filter')
st.dataframe(filtered.sort_values('harga',ascending=False),use_container_width=True,hide_index=True)
st.download_button('Unduh data hasil filter (CSV)',filtered.to_csv(index=False).encode('utf-8'),file_name='used_cars_filtered.csv',mime='text/csv')
st.caption('Catatan: harga mengikuti satuan pada dataset sumber (₹/Rupee India). Data merupakan listing mobil bekas, bukan harga transaksi final.')
