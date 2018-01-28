import urllib2
import json


PROFILE = "https://graph.facebook.com/v2.11/{uid}?access_token={access_token}"
PICTURE = "https://graph.facebook.com/v2.11/{uid}/picture?access_token={access_token}&type=large"
TOKEN = "https://graph.facebook.com/v2.11/oauth/access_token={}"

class Facebook(object):
    def __init__(self, uid, access_token):
        self.uid = uid
        self.access_token = access_token

    def get_user_full_name(self):
        url = PROFILE.format(uid=self.uid, access_token=self.access_token)
        r = urllib2.urlopen(url)
        data = json.loads(r.read().decode('utf-8'))
        return data['name']

    def get_picture_url(self):
        url = PICTURE.format(uid=self.uid, access_token=self.access_token)
        return url
