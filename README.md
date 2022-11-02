# Tugas Kelompok PBP D04

## 🎋 Nama-nama Anggota Kelompok 🎋

- Alvaro Austin (2106752180)
- Arditio Reihansyah Putra Pradana (2106751972)
- Carlene Annabel (2106752211)
- Natania Deandra (2106633090)
- Ravena Meilani (2106631923)

## 🌈 Tautan Aplikasi Heroku 🌈

**Nama Aplikasi:** `HIVCenter`

**Link Aplikasi:** https://pbp-d04.herokuapp.com/ 

## ☄️ Cerita Aplikasi yang Diajukan Serta Manfaatnya ☄️

<p align="justify"> Sebagaimana yang tertulis pada website resmi <strong>G20</strong> terkait <strong>Arsitektur Kesehatan Global</strong> sebagai berikut, "Indonesia akan mendorong penguatan ketahanan kesehatan dunia serta membantu mewujudkan sistem kesehatan global lebih inklusif, berkeadilan, dan responsif terhadap krisis," kami memiliki visi untuk menambah pengetahuan, mengedukasi, memberi semangat serta kesempatan untuk berobat sekaligus menghilangkan stigma dan miskonsepsi terhadap mereka yang mengidap penyakit menular seksual. Dengan adanya HIVCenter, kami juga berharap masyarakat menjadi lebih sadar terhadap masalah di sekitar mereka serta mampu mewujudkan suatu lingkungan yang inklusif serta mampu merangkul semua anggota masyarakat terutama mereka yang paling membutuhkannya. <p>

<p align="justify"> Rendahnya pengetahuan masyarakat Indonesia akan HIV berakibat pada kenaikan kasus HIV di Indonesia. Berdasarkan data yang diperoleh Kemenkes, pada tahun 2021, sebanyak 36.902 kasus HIV tersebar di penjuru tanah air. Relatif sedikit apabila dibandingkan dengan jumlah kasus HIV pada tahun 2022 yaitu sebanyak 519.158 kasus.  HIV dikenal sebagai penyakit menular yang tidak bisa disembuhkan karena hal tersebut muncullah banyak stigma negatif terhadap pasien-pasien HIV. Oleh karena itu, diperlukan adanya suatu upaya pencegahan pada masyarakat di segala usia, salah satunya adalah pemberian pengetahuan akan HIV kepada masyarakat. Ada banyak upaya untuk melakukan penyuluhan tentang HIV. Salah satu upaya untuk memberikan penyuluhan tentang HIV kepada masyarakat adalah melalui HIVCenter. </p>

<p align="justify"> HIVCenter memiliki visi untuk menghilangkan stereotip yang melekat pada sebagian besar masyarakat Indonesia mengenai ODHA sekaligus meningkatkan kesadaran akan pentingnya pencegahan penyakit menular seksual. Selain itu, HIVCenter juga berharap dengan adanya aplikasi ini, ODHA dapat merasa lebih diterima tanpa adanya stereotip dari masyarakat pada umumnya. </p>

<p align="justify"> HIVCenter memiliki fitur-fitur yang dapat memberikan pengetahuan seputar HIV kepada pengguna. Fitur-fitur tersebut diantaranya ada forum untuk pengguna dokter yang dapat memberikan postingan seputar informasi HIV. Fitur lainnya adalah forum untuk pengguna pasien guna saling bertukar pengalaman dan informasi seputar HIV. Selain fitur-fitur forum, terdapat juga fitur yang menampilkan daftar-daftar dari rumah sakit terdekat apabila pengguna membutuhkan info lokasi rumah sakit untuk melakukan pengecekan atau konsultasi kepada dokter terkait HIV. Fitur terakhir adalah fitur pengguna pasien untuk membuat reservasi atau booking kepada pengguna dokter untuk melakukan konsultasi atau pemeriksaan HIV. </p>

<p align="justify"> Fitur-fitur tersebut disediakan sebagai upaya penyuluhan dan tindakan preventif HIV. Dengan adanya fitur-fitur yang disediakan pada HIVCenter diharapkan dapat mengedukasi masyarakat tentang info seputar HIV, dapat mengubah stigma negatif masyarakat terhadap pengidap HIV, dan juga yang paling penting adalah dapat mengurangi kasus HIV yang ada di Indonesia. </p>

## 💫 Daftar Modul yang Diimplementasikan 💫

1. **Homepage** <br>
    Modul di atas merupakan halaman utama dari aplikasi `HIVCenter`. Pada halaman utama, terdapat informasi terkait HIV/AIDS, fakta, serta miskonsepsi yang banyak dipercayai oleh masyarakat awam. Pada halaman ini juga terdapat fitur gamifikasi di mana para pengguna dapat mengirimkan semangat kepada sesama penderita HIV. Pada bagian ini juga diperlihatkan preview blogpost yang paling terbaru dibuat.

2. **Login, Logout, dan Register** <br>
    Modul di atas mengimplementasikan fitur login, logout, pendaftaran akun, serta pembagian peran pengguna ke dalam beberapa kelompok, yaitu rumah sakit, dokter, dan pasien.
    
3. **Blogpost** <br>
    Forum blogpost dimana pasien hanya memiliki view (read-only) sedangkan dokter dapat (post, delete, update).
    
4. **Booking** <br>
    Fitur booking agar pasien dapat membuat janji dengan dokter dan dokter dapat melihat jadwal dari setiap janji yang ia miliki.
    
5. **Experience** <br>
    Forum pengalaman dimana pasien dapat menceritakan pengalaman mereka.
    
6. **Feedback** <br>
    Fitur feedback dimana pasien dapat memberikan feedback terhadap website `HIVCenter`.

## 🍀 Role Atau Peran Pengguna Beserta Deskripsinya 🍀

1. **Dokter** <br>
    User dapat memposting, menghapus, serta mengupdate informasi pada forum blogpost terkait HIV.
    
2. **Pasien** <br>
    User dapat membagikan pengalamannya pada forum experience serta reservasi kepada dokter untuk melakukan konsultasi atau pemeriksaan dan melakukan feedback terhadap website. Pasien juga dapat melihat blogpost

3. **Visitor** <br>
    Non user yang dapat melihat homepage namun tidak dapat mengakses banyak fitur yang diinginkan. Ini artinya visitor tidak dapat melihat blogpost maupun fitur-fitur lain seperti experience dan booking.

## Bonus (Pipeline Status)
<label> Pipeline status </label>
 ![Pipeline Status](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg)

<label> Pipeline status main</label>
![Pipeline Status main](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg?branch=main)

<label> Pipeline status branch alvaro/homepage </label>
![Pipeline Status Branch](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg?branch=alvaro/homepage)

<label> Pipeline status branch alvaro/blogposts </label>
![Pipeline Status Branch](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg?branch=alvaro/blogposts)


<label> Pipeline status branch carlenee/Experience </label>
![Pipeline Status Branch](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg?branch=carlenee/Experience)

<label> Pipeline status branch natania/booking </label>
![Pipeline Status Branch](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg?branch=natania/booking)

<label> Pipeline status branch tio </label>
![Pipeline Status Branch](https://github.com/Emilicos/D04-PBP/actions/workflows/dpl.yml/badge.svg?branch=tio)
