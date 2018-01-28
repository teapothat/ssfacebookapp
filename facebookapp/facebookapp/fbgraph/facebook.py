import urllib2
import json


PROFILE = "https://graph.facebook.com/v2.11/{uid}?access_token={access_token}"
PICTURE = "https://graph.facebook.com/v2.11/{uid}/picture?access_token={access_token}&type=large"
TOKEN = "https://graph.facebook.com/v2.11/oauth/access_token?fb_exchange_token={access_token}&grant_type=fb_exchange_token&client_id=542921746076070&client_secret=bb4ec7370b3db7e3fcd59c9747e1a964"


def get_user_full_name(uid, access_token):
    url = PROFILE.format(uid=uid, access_token=access_token)
    r = urllib2.urlopen(url)
    data = json.loads(r.read().decode('utf-8'))
    return data['name']


def get_picture_url(uid, access_token):
    url = PICTURE.format(uid=uid, access_token=access_token)
    return url


def get_long_standing_token(access_token):
    url = TOKEN.format(access_token=access_token)
    r = urllib2.urlopen(url)
    data = json.loads(r.read().decode('utf-8'))
    return data['access_token']


