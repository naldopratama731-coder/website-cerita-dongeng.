import streamlit as st

st.set_page_config(page_title="Dongeng Anak", page_icon="📚")

st.title("📚 Website Dongeng Anak SD")
st.write("Silahkan pilih cerita dongeng di bawah ini 👇")

# Pilihan cerita
pilihan = st.selectbox(
    "Pilih Cerita:",
    [
        "-- Pilih Cerita --",
        "Kelinci dan Kura-kura",
        "Rubah dan Anggur",
        "Singa dan Tikus"
    ]
)

# Tombol tampilkan
tampilkan = st.button("Tampilkan Cerita")

if tampilkan:

    if pilihan == "-- Pilih Cerita --":
        st.warning("Silahkan pilih cerita terlebih dahulu!")

    elif pilihan == "Kelinci dan Kura-kura":
        st.subheader("🐢🐇 Kelinci dan Kura-kura")
        st.write("""
Pada suatu hari, seekor kelinci selalu mengejek kura-kura karena berjalan sangat lambat.
Kura-kura pun menantang kelinci untuk lomba lari.

Saat lomba dimulai, kelinci berlari sangat cepat lalu merasa sombong dan beristirahat.
Namun ia tertidur, sementara kura-kura terus berjalan perlahan tapi tidak menyerah.
Akhirnya kura-kura sampai duluan dan menjadi pemenang.

Pesan Moral:
Jangan sombong, dan jangan meremehkan orang lain.
""")

    elif pilihan == "Rubah dan Anggur":
        st.subheader("🦊🍇 Rubah dan Anggur")
        st.write("""
Seekor rubah lapar melihat buah anggur segar tergantung di dahan yang tinggi.
Ia melompat berkali-kali namun tetap tidak bisa meraihnya.

Karena kesal, rubah pun pergi sambil berkata:
"Ah, pasti anggurnya asam!"

Padahal sebenarnya ia hanya tidak mampu mendapatkannya.

Pesan Moral:
Jangan menghina sesuatu hanya karena kamu tidak bisa memilikinya.
""")

    elif pilihan == "Singa dan Tikus":
        st.subheader("🦁🐭 Singa dan Tikus")
        st.write("""
Suatu hari seekor tikus kecil tertangkap oleh singa.
Tikus memohon agar dibebaskan dan berjanji suatu saat akan membantu singa.

Beberapa hari kemudian singa terjebak dalam jaring pemburu.
Tikus datang dan menggigit tali jaring hingga putus.
Singa pun berhasil bebas.

Pesan Moral:
Sekecil apapun seseorang, ia tetap bisa membantu orang lain.
""")
