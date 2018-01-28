from django.core.exceptions import ObjectDoesNotExist
from facebookapp.models import User
from facebookapp.fbgraph import facebook

def handle_user(uid, temp_token):

    # Check if user exists in db
    user = get_user_by_fb_id(uid)
    if not user:
        user = create_user_with_temp_token(uid, temp_token)

    link = facebook.get_picture_url(uid, user.access_token),

    return {"user_name": user.name, "image_link": link}


def get_user_by_fb_id(uid):
    try:
        return User.objects.get(fb_id=uid)
    except ObjectDoesNotExist:
        return None


def create_user_with_temp_token(uid, temp_token):
    token = facebook.get_long_standing_token(temp_token)
    name = facebook.get_user_full_name(uid, token)

    user = User(fb_id=uid,
                access_token=token,
                name=name,
                is_active=True)
    user.save()
    return user
