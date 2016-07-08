# apiapi
Latihan (lagi) membuat API menggunakan python dan kawan-kawannya. Kali ini disimpan di Heroku. Hasilnya bisa dicoba di [sini.](https://apiapikor.herokuapp.com/api/v1.0/news)

Studi kasus: mengambil daftar berita (scraping menggunakan librari Bs4) dari situs [inilahkoran](http://www.inilahkoran.com). Keluaran berupa berkas json yang memuat data tautan, judul, kategori, dan id berita.

Contoh hasil keluaran:
```
{
  "page": "1",
  "results": [
    {
      "id": 0,
      "img": "http://www.inilahkoran.com/gallery/content/serba_serbi/nongsa-batam.jpg",
      "judul": "Batam-Bintan Meledak Tanpa Gangguan",
      "kategori": "wonderful-indonesia",
      "kategori_id": 13,
      "link": "http://www.inilahkoran.com/berita/wonderful-indonesia/59250/batam-bintan-meledak-tanpa-gangguan",
      "penulis": "Admin Inilahkoran",
      "url_id": 59250,
      "waktu": "08 Juli 2016 13:12"
    },
    {
      "id": 1,
      "img": "http://www.inilahkoran.com/gallery/content/persib/DedenNatshir.jpg",
      "judul": "Kiper Persib Akui Masih Banyak Kekurangan",
      "kategori": "persib",
      "kategori_id": 0,
      "link": "http://www.inilahkoran.com/berita/persib/59249/kiper-persib-akui-masih-banyak-kekurangan",
      "penulis": "Asep Pupu Saeful Bahri",
      "url_id": 59249,
      "waktu": "08 Juli 2016 08:36"
    },
    ...
    ],
      "status": "ok",
      "total": 10
    }
    ```

    ### Fungsi
* list berita

url: ```namadomain/api/v1.0/news```

* list berita per kategori

url: ```namadomain/api/v1.0/news/cat/kategori_id```

* detail berita per id

url: ```namadomain/api/v1.0/news/url_id```
