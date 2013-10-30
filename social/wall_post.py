# -*- encoding: utf-8 -*-
# Post on social network wall
import requests
from bs4 import BeautifulSoup
from social.models import FacebookAccessToken, VkontakteAccessToken


def vk_wall_post(message, link):
    try:
        VK_WALL_GROUP_ID = '-' + VkontakteAccessToken.objects.all()[0].vkontakte_group_id
        VK_ACCESS_TOKEN = VkontakteAccessToken.objects.all()[0].vkontakte_access_token

        soup = BeautifulSoup(message)

        parameters = { 
            'owner_id'   : VK_WALL_GROUP_ID, 
            'from_group' : '1',
            'message'    : (' '.join(soup.get_text().split()[:20]) + '...').encode('utf-8'),
            'attachments': link, 
            'access_token' : VK_ACCESS_TOKEN
            }

        url = 'https://api.vk.com/method/wall.post?\
owner_id={owner_id}&from_group={from_group}\
&message={message}&attachments={attachments}&\
access_token={access_token}'.format(**parameters)

        post = requests.post(url)

    except IndexError:
        pass

def facebook_wall_post(name, message, link, picture=None):

    try:

        FACEBOOK_WALL_GROUP_ID = FacebookAccessToken.objects.all()[0].facebook_group_id
        FACEBOOK_ACCESS_TOKEN = FacebookAccessToken.objects.all()[0].facebook_access_token

        soup = BeautifulSoup(message)

        parameters = {
            'access_token' : FACEBOOK_ACCESS_TOKEN,
            'message'      : (' '.join(soup.get_text().split()[:20]) + '...').encode('utf-8'),
            'link'         : link,
            'name'         : name,
            'picture'      : picture
        }

        url = 'https://graph.facebook.com/{group_id}/feed'.format(
            group_id=FACEBOOK_WALL_GROUP_ID)
        post = requests.post(url, params=parameters)

    except IndexError:
        pass


