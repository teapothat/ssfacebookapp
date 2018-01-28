import urllib2
import base64
import hashlib
import hmac
import json
import time


SECRET = "bb4ec7370b3db7e3fcd59c9747e1a964"
APP_ID = "542921746076070"

PROFILE = "https://graph.facebook.com/v2.11/{uid}?access_token={access_token}"
PICTURE = "https://graph.facebook.com/v2.11/{uid}/picture?access_token={access_token}&type=large"
TOKEN = "https://graph.facebook.com/v2.11/oauth/access_token?fb_exchange_token={access_token}&grant_type=fb_exchange_token&client_id={app_id}&client_secret={app_secret}"



def get_user_full_name(uid, access_token):
    url = PROFILE.format(uid=uid, access_token=access_token)
    r = urllib2.urlopen(url)
    data = json.loads(r.read().decode('utf-8'))
    return data['name']


def get_picture_url(uid, access_token):
    url = PICTURE.format(uid=uid, access_token=access_token)
    return url


def get_long_standing_token(access_token):
    url = TOKEN.format(access_token=access_token, app_id=APP_ID, app_secret=SECRET)
    r = urllib2.urlopen(url)
    data = json.loads(r.read().decode('utf-8'))
    return data['access_token']


def base64_url_decode(input):
    input = input.encode(u'ascii')
    input += '=' * (4 - (len(input) % 4))
    return base64.urlsafe_b64decode(input)


def parse_signed_request(input, max_age=3600):
    encoded_sig, encoded_envelope = input.split('.', 1)
    envelope = json.loads(base64_url_decode(encoded_envelope))
    algorithm = envelope['algorithm']

    if algorithm != 'HMAC-SHA256':
        raise Exception('Invalid request. (Unsupported algorithm.)')

    if envelope['issued_at'] < time.time() - max_age:
        raise Exception('Invalid request. (Too old.)')

    if base64_url_decode(encoded_sig) != hmac.new(
            SECRET, msg=encoded_envelope, digestmod=hashlib.sha256).digest():
        raise Exception('Invalid request. (Invalid signature.)')

    return envelope
