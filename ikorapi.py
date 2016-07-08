#!/bin/python
import urllib
from bs4 import BeautifulSoup
import time
from datetime import date
import json
from urlparse import urlparse


kategori = ['persib','bandung','bandung-juara','jabar','jabar-kahiji','sport','edukasi','ekonomi','serba-serbi','selebritas','life-style','syiar','bogor', 'wonderful-indonesia']
cat_id = [i for i in xrange(len(kategori))]
dict_cat = dict(zip(cat_id, kategori))

urlInilah = 'http://www.inilahkoran.com'
'''
input: url indeks (ikor/berita)
output: data link, url_id, judul dalam bentuk jsonify
'''
def getUrl(url):
    hasil = []
    linkBerita = []
    judul = []
    gambar = []
    penulis = []
    waktu = []
    berita = {}
    link_berita = ''
    url = urllib.urlopen(url)
    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")

    for link in soup.find_all('li',{'class':'cssLineB'}):
        #ambil link gambar
        if(link.find('img') is None):
            gambar.append('')
        else:
            for g in link.find_all('img'):
                gmbr = urlInilah + g.get('src')
                q = urlparse(gmbr).query.split('&')[0].strip('file=')
                qgambar = urlInilah + '/gallery/' + q
                gambar.append(qgambar)
        #ambil link berita dan judul
        for l in link.find_all('a', {'class':'cssTextHeaderContent'}) or link.find_all('a', {'class':'cssTextHeaderHeadline'}):
            link_berita = l.get('href')
            judul_berita = l.get_text().strip().encode("utf-8")
            link_berita = urlInilah + link_berita
            linkBerita.append(link_berita)
            judul.append(judul_berita)

        #ambil link gambar
        # for g in link.find_all('img'):
        #     gmbr = urlInilah + g.get('src')
        #     q = urlparse(gmbr).query.split('&')[0].strip('file=')
        #     qgambar = urlInilah + '/gallery/' + q
        #     print qgambar
        #     gambar.append(qgambar)
        #ambil nama penulis
        pi = 0
        for p in link.find_all('div',{'class':'cssTextSmall'}):
            for r in p.find_all('span'):
                if pi ==1:
                    pen = r.get_text().strip().encode("utf-8").partition(" ")[2]
                    penulis.append(pen)
                if pi == 2:
                    wkt = r.get_text().strip().encode("utf-8")
                    waktu.append(wkt)
                pi += 1

    # lg = len(gambar)
    # llb= len(linkBerita)
    # if(lg < llb):
    #     #ada berita yang tak pake gambar
    #     beda = llb - lg
    #     print beda, llb, lg
    #     for i in xrange(beda):
    #         gambar.append('')


    # masukkan ke dict
    dicSize = len(linkBerita)
    for k in xrange(dicSize):
        berita['id'] = k
        berita['url_id'] = int(linkBerita[k].split('/')[5])
        berita['kategori'] = linkBerita[k].split('/')[4]
        berita['kategori_id'] = getIdFromCat(linkBerita[k].split('/')[4])
        berita['link'] = linkBerita[k]
        berita['judul'] = judul[k]
        berita['img'] = gambar[k]
        berita['penulis'] = penulis[k]
        berita['waktu'] = waktu[k]
        hasil.append(berita)
        berita = {}

    return hasil

'''
kategori berita
input: id
output: nama kategori
'''
def getCatFromId(id):
    return dict_cat[id]
'''
id kategori berita
input: nama kategori
output: id

'''
def getIdFromCat(cat):
    for k, v in dict_cat.iteritems():
        if v == cat:
            return k

# tes ambil data penulis dan tanggal. kalau berhasil nanti dimasukkan ke getUrl
def getDate(url):
    url = urllib.urlopen(url)
    result = url.read()
    url.close()
    soup = BeautifulSoup(result, "html.parser")
    for link in soup.find_all('li',{'class':'cssLineB'}):
        i = 0
        for p in link.find_all('div',{'class':'cssTextSmall'}):
            for r in p.find_all('span'):
                if i == 1:
                    print r.get_text().strip().encode("utf-8").partition(" ")[2]
                if i == 2:
                    print r.get_text().strip().encode("utf-8")
                i += 1

# getUrl('http://www.inilahkoran.com/berita?page=1')
