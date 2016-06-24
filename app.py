
from flask import Flask, jsonify, abort, make_response, request, url_for
import authapp
import ikorapi
app = Flask(__name__)

url_base = "http://www.inilahkoran.com"
urlindeks = url_base + "/berita"
defroute = "/api/v1.0/news"
news = []
news = ikorapi.getUrl(urlindeks)

@app.route(defroute, methods=['GET'])
# @authapp.require_appkey #jika ingin pake keyapi
def get_news():
    total = len(news)
    return jsonify({'total': total, 'status': 'ok', 'page': '1', 'results': news})

@app.route(defroute + '/page/<int:page>', methods=['GET'])
# @authapp.require_appkey #jika ingin pake keyapi
def get_news_page(page):
    if page < 1:
        abort(404)
    urlp = urlindeks + '?page=' + str(page-1)
    newspage = ikorapi.getUrl(urlp)
    total = len(newspage)
    return jsonify({'total': total, 'status': 'ok', 'page': (page), 'results': newspage})

@app.route(defroute + '/<int:news_id>', methods=['GET'])
# @authapp.require_appkey #jika ingin pake keyapi
def get_news_from_id(news_id):
    t = [t for t in news if t['url_id'] == news_id]
    if len(t) == 0:
        abort(404)
    return jsonify({'news': t[0]})

@app.route(defroute + '/cat/<int:cat_id>', methods=['GET'])
# @authapp.require_appkey #jika ingin pake keyapi
def get_news_cat(cat_id):
    newscat = []
    #ambil cat dari id
    catname = ikorapi.getCatFromId(cat_id)
    urlcat = urlindeks + '/' + catname
    newscat = ikorapi.getUrl(urlcat)
    total = len(newscat)
    if( total == 0):
        return make_response(jsonify({'error': 'Not found', 'status': '200'}), 404)
    else:
        return jsonify({'total': total, 'status': 'ok', 'results': newscat})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status': '200'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
