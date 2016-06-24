'''
Menggunakan key pada api
'''
from flask import make_response, jsonify, request, abort
from functools import wraps
APPKEY = 'd42a9ad09e9778b177d409f5716ac621'     # :D

'''
sumber: https://coderwall.com/p/4qickw/require-an-api-key-for-a-route-in-flask-using-only-a-decorator
'''
# @auth.require_appkey
def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == APPKEY:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify({'error': 'Unauthorized access'}), 403)
    return decorated_function
