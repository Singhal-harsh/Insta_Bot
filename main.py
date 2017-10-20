import requests


ACCESS_TOKEN = '1401555512.bc72bfa.d6029801e180428298aad72b14933a58'
BASE_URL = 'https://api.instagram.com/v1/'

def self_info():
    own_url = BASE_URL+'users/self/?access_token='+ACCESS_TOKEN
    print 'GET request of self url is: ' + own_url
    user_info = requests.get(own_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'Bio: %s' %(user_info['data']['bio'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

def get_user_id(insta_username):
  request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username,ACCESS_TOKEN)
  print 'GET request of another user url : %s' % (request_url)
  user_info = requests.get(request_url).json()

  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          return user_info['data'][0]['id']
      else:
          return None
  else:
      print 'Status code other than 200 received!'
      exit()

def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)
  print 'GET request of another user url : %s' % (request_url)
  user_info = requests.get(request_url).json()

  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
          print 'Username: %s' % (user_info['data']['username'])
          print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
          print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
          print 'No. of posts: %s' % (user_info['data']['counts']['media'])
      else:
          print 'There is no data for this user!'
  else:
      print 'Status code other than 200 received!'

self_info()
get_user_info('snTest12345')