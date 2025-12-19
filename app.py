import streamlit as st

# ===============================
# DATA CERITA
# ===============================
stories = {
    "🐢 Kelinci dan Kura-Kura": {
        "color": "#4CAF50",  # Hijau
        "story": """
Suatu hari, seekor kelinci sombong menantang kura-kura lomba lari.
Kelinci sangat percaya diri karena merasa paling cepat.
Saat lomba dimulai, kelinci berlari sangat kencang.
Namun di tengah jalan ia berhenti dan tidur karena merasa pasti menang.
Sementara itu, kura-kura berjalan perlahan tapi tidak pernah berhenti.
Pada akhirnya, kura-kura yang sampai duluan ke garis finish!
Kelinci pun malu dan menyesal karena terlalu sombong.

**Pesan moral: Jangan sombong, dan jangan meremehkan orang lain.**
"""
    },

    "🦊 Rubah dan Anggur": {
        "color": "#FF9800",  # Oranye
        "story": """
Seekor rubah lapar melihat anggur yang tampak segar di pohon.
Ia melompat berkali-kali untuk mengambilnya, tapi tetap tidak bisa.
Akhirnya rubah menyerah, lalu berkata,
"Ah, pasti anggurnya asam!"

Padahal sebenarnya ia hanya tidak mampu mengambilnya.

**Pesan moral: Jangan menjelekkan sesuatu hanya karena kita tidak bisa mendapatkannya.**
"""
    },

    "🦁 Singa dan Tikus": {
        "color": "#E91E63",  # Pink Merah
        "story": """
Pada suatu hari, seekor singa menangkap seekor tikus kecil.
Tikus memohon agar dibebaskan, dan berjanji akan menolong singa suatu hari nanti.
Singa tertawa, tapi akhirnya melepaskannya.

Beberapa hari kemudian, singa terjebak dalam jaring pemburu.
Tikus datang dan menggigit jaring tersebut hingga putus.
Singa pun bebas dan berterima kasih kepada tikus.

**Pesan moral: Jangan meremehkan makhluk yang lebih kecil.**
"""
    },
}

# ===============================
# LOGIKA APLIKASI
# ===============================
if "page" not in st.session_state:
    st.session_state.page = "menu"

st.set_page_config(page_title="Website Dongeng Anak", page_icon="📖")

# ===============================
# HALAMAN MENU
# ===============================
if st.session_state.page == "menu":
    st.title("📖 Kumpulan Cerita Dongeng Anak")
    st.write("Silakan pilih salah satu judul cerita di bawah ini:")

    for title, data in stories.items():
        if st.button(title, use_container_width=True):
            st.session_state.page = title

        st.markdown(
            f"""
            <style>
            div[data-testid="stButton"] button {{
                background-color: {data['color']} !important;
                color: white !important;
                font-weight: bold;
                border-radius: 10px;
                height: 50px;
                font-size: 18px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# ===============================
# HALAMAN CERITA
# ===============================
else:
    st.title(st.session_state.page)
    st.write(stories[st.session_state.page]["story"])

    if st.button("⬅️ Kembali ke Daftar Cerita"):
        st.session_state.page = "menu"
