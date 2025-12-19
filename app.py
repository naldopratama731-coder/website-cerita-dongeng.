import streamlit as st

st.set_page_config(page_title="Dongeng Anak", page_icon="📚")

st.title("📚 Website Dongeng Anak SD")
st.write("Klik salah satu judul cerita di bawah ini untuk membacanya 👇")

# ===== CERITA 1 =====
with st.expander("🐢🐇  KELINCI DAN KURA-KURA"):
    st.markdown(
        """
        <div style="background:#FFEBEE; padding:12px; border-radius:10px;">
        Pada suatu hari, seekor kelinci selalu mengejek kura-kura karena berjalan sangat lambat.
        Kura-kura pun menantang kelinci untuk lomba lari.

        Saat lomba dimulai, kelinci berlari sangat cepat lalu merasa sombong dan beristirahat.
        Namun ia tertidur, sementara kura-kura terus berjalan perlahan tapi tidak menyerah.
        Akhirnya kura-kura sampai duluan dan menjadi pemenang.

        <b>Pesan Moral:</b> Jangan sombong dan jangan meremehkan orang lain.
        </div>
        """,
        unsafe_allow_html=True
    )

# ===== CERITA 2 =====
with st.expander("🦊🍇  RUBAH DAN ANGGUR"):
    st.markdown(
        """
        <div style="background:#E8F5E9; padding:12px; border-radius:10px;">
        Seekor rubah lapar melihat anggur segar tergantung di dahan yang tinggi.
        Ia melompat berkali-kali, namun tetap tidak bisa meraihnya.

        Karena kesal, rubah pun pergi sambil berkata:
        “Ah, pasti anggurnya asam!”

        Padahal sebenarnya ia hanya tidak mampu mendapatkannya.

        <b>Pesan Moral:</b> Jangan meremehkan sesuatu hanya karena kamu tidak bisa memilikinya.
        </div>
        """,
        unsafe_allow_html=True
    )

# ===== CERITA 3 =====
with st.expander("🦁🐭  SINGA DAN TIKUS"):
    st.markdown(
        """
        <div style="background:#E3F2FD; padding:12px; border-radius:10px;">
        Suatu hari seekor tikus kecil tertangkap oleh singa.
        Tikus memohon agar dibebaskan dan berjanji suatu saat akan membantu singa.

        Beberapa hari kemudian singa terjebak dalam jaring pemburu.
        Tikus datang dan menggigit tali jaring hingga putus.
        Singa pun berhasil bebas.

        <b>Pesan Moral:</b> Sekecil apapun seseorang, ia tetap bisa menolong orang lain.
        </div>
        """,
        unsafe_allow_html=True
    )
