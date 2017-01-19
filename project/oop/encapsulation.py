# hiding the stuff that is not supposed to be shown

import oauth2
import urllib.parse as urlparse # as just renames it


class TwitterConsoleLogin:
    def __init__(self, consumer_key, consumer_secret):
        self.__consumer = oauth2.Consumer(consumer_key, consumer_secret)
    # will kinda global reusable variable

    # That should be the only available method
    # THis method is an API
    def perform_twitter_login(self):
        request_token = self.get_request_token()
        verifier = self.get_oauth_verifier(request_token)
        return self.get_access_token(request_token, verifier)

    # to make the method unavailable for other just add __
    def __get_request_token(self):
        # create a client to perform a request for the request token
        client = oauth2.Client(self.__consumer)
        response, content = client.request('https://api.twitter.com/oauth/request_token', 'POST')
        # left - what the request returns
        # first request
        # refer to the order in the course
        if response.status != 200:  # 200 is everything's fine
            print("An error occured when getting the request token from Twitter")

        # Get the request token parsing the query string returned
        return dict(urlparse.parse_qsl(content.decode('utf-8')))
        # content is in a format of query string parameter
        # we convert it into a dictionary
        # decode converts bytes to strings
        # this is indeed more readable then the ori


    def __get_oauth_verifier(self,request_token):
        # Ask the user
        # We are doing Pin auth. Just for learning purpose. We have a console application
        print("Go to the following web-site:")

        print(self.get_oauth_verifier_url(request_token))
        # User must type the pin

        return input("What is the pin? ")


    def __get_oauth_verifier_url(self,request_token):
        return "{}?oauth_token={}".format('https://api.twitter.com/oauth/authorize', request_token['oauth_token'])


    def __get_access_token(self,request_token, oauth_verifier):

        # Create a token object which contains the request token and the verifier
        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)

        client = oauth2.Client(self.__consumer, token)

        # We use this client to get an access token
        # Ask Twitter for a request token and Twitter knows it should give us it because we verified the request token
        response, content = client.request('https://api.twitter.com/oauth/access_token', 'POST')
        return dict(urlparse.parse_qsl(content.decode('utf-8')))


twitter_login = TwitterConsoleLogin('my_key', 'my_secret')
twitter_login.perform_twitter_login()