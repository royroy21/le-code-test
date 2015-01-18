# Python Imports

# Django Imports
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from items.models import PhotoItem
from items.models import TweetItem


def view_streams(request):
    """
    View all user streams.
    """
    try:
        # get all active user data
        user_data = []
        for user in User.objects.filter(is_active=True):
            user_data.append([user.first_name, user.last_name, user.id])
        return_data = {'user_data': user_data}

        # return data
        return render_to_response('all_users.html', return_data)

    except Exception as error:
        return HttpResponseBadRequest(error)


def view_stream_for_user(request, user_id):
    """
    View stream for a user.
    """
    try:
        # get data
        return_data = {'photo_items': PhotoItem.objects.filter(user__id=user_id, active=True),
                       'tweet_items': TweetItem.objects.filter(user__id=user_id, active=True),
                       'user_object': User.objects.get(id=user_id)}

        # return data
        return render_to_response('one_user_steam.html', return_data)

    except Exception as error:
        return HttpResponseBadRequest(error)