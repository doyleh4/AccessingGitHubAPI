from django.shortcuts import render
from django.http import HttpResponse
import requests 
from github import Github
import json
# Create your views here.

Git_user_data = [
        {'login' : None,
        'name' : None,
        'location' : None,
        'no_of_repos': None,
        'repos' : [],
        'date_created' : None
        }
    ]

####
# inputs
####
yourUsername = 'doyleh4'

# from https://github.com/user/settings/tokens
token = '1cac1dbc068a4e45440aa8893989d16ffa6a8161'

gh_session = requests.Session()
gh_session.auth = (yourUsername, token)

r = gh_session.get(url = 'https://api.github.com/rate_limit', params = {})
data = r.json()
print (data)

username = "torvalds"
url = f"https://api.github.com/users/{username}"
user_data = gh_session.get(url).json()

def home(request):
    g = Github(token)
    #g = Github()
    user = g.get_user(username)

    Git_user_data[0]['login'] = user_data['login']
    Git_user_data[0]['name'] = user_data['name']
    Git_user_data[0]['location'] = user_data['location']
    Git_user_data[0]['no_of_repos'] = str(user.get_repos().totalCount)
    for repo in user.get_repos():
        Git_user_data[0]['repos'].append(repo.full_name)
    
    #Git_user_data[0]['repos'] = user.get_repos()

    data = {
        'Git_user_data' : Git_user_data
    }
    return render(request, 'visualiser/home.html', data)

def about(request):
    return render(request, 'visualiser/about.html', {'title':'About'})


# import requests 
# from github import Github
# from pprint import pprint

# ####
# # inputs
# ####
# yourUsername = 'doyleh4'

# # from https://github.com/user/settings/tokens
# token = '1cac1dbc068a4e45440aa8893989d16ffa6a8161'

# gh_session = requests.Session()
# gh_session.auth = (yourUsername, token)

# r = gh_session.get(url = 'https://api.github.com/rate_limit', params = {})
# data = r.json()
# print (data)

# username = "doyleh4"
# url = f"https://api.github.com/users/{username}"
# user_data = gh_session.get(url).json()
# pprint(user_data)       #using pprint() as regular print() prints it with no line breaks

# print("-----------------------------------------------------------------------------------------------------------------")
# #using PyGitHub to get this data thee resst is using requests still havent decided what i want to do for most of this 
# g = Github(token)
# #g = Github()
# user = g.get_user(username)
# login = "Not applied"
# name = "Not applied"
# location = "Not applied"
# if (user.login is not None):
#     login = user.login
#     print("Login: " + login)
# if (user.name is not None):
#     name = user.name
#     print("Name: " + name)
# if (user.location is not None):
#     location = user.location
#     print("Name: " + location)
# print("-----------------------------------------------------------------------------------------------------------------")
# print('Total number of public repositories: ' + str(user.get_repos().totalCount))
# for repo in user.get_repos():
#     print(repo)

# print("-----------------------------------------------------------------------------------------------------------------")
# print("Total followers: " + str(user.get_followers().totalCount))

# print("-----------------------------------------------------------------------------------------------------------------")
# url = "https://api.github.com/repos/torvalds/linux/commits"
# linux_repo = gh_session.get(url)
# print("Total commmits to Linux repository: " + str(len(linux_repo.content)))

# data = [
#     {
#     'user' : login,
#     'name' : name,
#     'location' : location
#     }
# ]