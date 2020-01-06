import sys
import os
import json
import requests
import datetime
import filecmp


class Facebook:
    @staticmethod
    def get_access_token(token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()

        return 'Not found'

    def __init__(self):
        self.page_id = Facebook.get_access_token('FACEBOOK_PAGE_ID')
        self.page_access_token = Facebook.get_access_token('FACEBOOK_PAGE_ACCESS_TOKEN')


    # Parameters
    # ----------
    # message : string
    #     message to be posted
    # image_url : string
    #     publicly accessible URL of the image to be posted
    # Return Type: None

    def publish_photo_msg(self, message, image_url):
        data={
            'url':image_url,
            'caption':message,
            'access_token':self.page_access_token
        }
        pst=requests.post("https://graph.facebook.com/"+str(self.page_id)+"/photos",data=data)
        print(pst)


if __name__ == '__main__':
    facebook = Facebook()

    # 1) Search for your favorite picture on images.google.com
    # 2) Copy the URL of the image and assign it to the 'image_url' variable
    #    Eg: image_url = 'http://ksmartstatic.sify.com/cmf-1.0.0/appflow/bawarchi.com/Image/oeturjecjjdah_bigger.jpg'
    # 3) Fill the 'my_name' variable with your name so that your friends know the posts you have created
    image_url = None
    my_name = None

    message = my_name + ' likes this ice-cream!'
    facebook.publish_photo_msg(message, image_url)
