import streamlit as st

st.set_page_config(page_title="Dongeng Anak", page_icon="📖", layout="wide")

st.title("📖 Kumpulan Cerita Dongeng Anak")
st.write("Klik judul cerita di bawah untuk membaca cerita lengkap 5 halaman per cerita.")

# ===========================
# DATA CERITA (3 cerita, 5 halaman)
# ===========================
stories = {
    "🐢 Kelinci dan Kura-Kura": [
        "Halaman 1:\nPada suatu hari, seekor kelinci sombong menantang kura-kura lomba lari. Ia merasa pasti menang karena sangat cepat.",
        "Halaman 2:\nSaat lomba dimulai, kelinci berlari sangat cepat. Ia tertawa melihat kura-kura berjalan pelan di belakangnya.",
        "Halaman 3:\nDi tengah jalan, kelinci merasa capek dan memutuskan untuk beristirahat sejenak di bawah pohon. Ia tertidur karena terlalu percaya diri.",
        "Halaman 4:\nSementara itu, kura-kura terus berjalan perlahan tapi pasti, tidak pernah berhenti, dan semakin mendekati garis finish.",
        "Halaman 5:\nAkhirnya, kura-kura sampai duluan di garis finish. Kelinci pun terbangun dan malu. Pesan moral: Jangan sombong, tetap tekun, dan jangan meremehkan orang lain."
    ],
    "🦊 Rubah dan Anggur": [
        "Halaman 1:\nSeekor rubah lapar melihat anggur segar di pohon. Ia ingin memakannya dan langsung melompat untuk meraihnya.",
        "Halaman 2:\nRubah melompat berkali-kali, namun tetap tidak bisa meraih anggur yang tinggi. Ia mulai merasa frustrasi.",
        "Halaman 3:\nRubah mencoba berbagai cara: memanjat, melompat dari batu, bahkan menggali tanah, tetapi tetap gagal.",
        "Halaman 4:\nAkhirnya, rubah menyerah dan berkata, 'Ah, pasti anggurnya asam!' meskipun sebenarnya ia hanya tidak mampu mengambilnya.",
        "Halaman 5:\nPesan moral: Jangan menjelekkan sesuatu hanya karena kita tidak bisa mendapatkannya. Terkadang usaha dan kesabaran lebih penting daripada hasil instan."
    ],
    "🦁 Singa dan Tikus": [
        "Halaman 1:\nSeekor singa menangkap tikus kecil yang sedang bermain. Tikus memohon agar dibebaskan.",
        "Halaman 2:\nTikus berjanji suatu saat akan menolong singa jika singa membebaskannya. Singa tertawa namun akhirnya membebaskan tikus.",
        "Halaman 3:\nBeberapa hari kemudian, singa terjebak dalam jaring pemburu. Ia berusaha melepaskan diri tapi tidak berhasil.",
        "Halaman 4:\nTikus kecil datang dan mulai menggigit jaring. Lambat laun tali jaring putus, dan singa akhirnya bebas.",
        "Halaman 5:\nSinga berterima kasih kepada tikus. Pesan moral: Sekecil apapun, makhluk bisa membantu orang lain. Jangan meremehkan siapapun."
    ]
}

# ===========================
# LOGIKA HALAMAN STREAMLIT
# ===========================
if "page" not in st.session_state:
    st.session_state.page = "menu"

# Halaman menu
if st.session_state.page == "menu":
    st.subheader("Daftar Cerita:")
    for title in stories.keys():
        if st.button(title, use_container_width=True):
            st.session_state.page = title

# Halaman cerita
else:
    st.subheader(st.session_state.page)
    for page_content in stories[st.session_state.page]:
        st.markdown(page_content)
        st.markdown("---")  # garis pemisah seperti halaman

    if st.button("⬅️ Kembali ke Daftar Cerita"):
        st.session_state.page = "menu"
