import requests 
from github import Github
from pprint import pprint

gh_session = requests.Session()

r = gh_session.get(url = 'https://api.github.com/rate_limit', params = {})
data = r.json()
print (data)

username = "doyleh4"
url = f"https://api.github.com/users/{username}"
user_data = gh_session.get(url).json()
pprint(user_data)       #using pprint() as regular print() prints it with no line breaks

print("-----------------------------------------------------------------------------------------------------------------")
#using PyGitHub to get this data thee resst is using requests still havent decided what i want to do for most of this 
#g = Github(token)
g = Github()
user = g.get_user(username)
login = user.login
name = user.name
location = user.location
if (login is not None):
    print("Login: " + login)
if (name is not None):
    print("Name: " + name)
if (location is not None):
    print("Name: " + location)
print("-----------------------------------------------------------------------------------------------------------------")
print('Total number of repositories: ' + str(user.get_repos().totalCount))
for repo in user.get_repos():
    print(repo)

print("-----------------------------------------------------------------------------------------------------------------")
print("Total followers: " + str(user.get_followers().totalCount))

print("-----------------------------------------------------------------------------------------------------------------")
url = "https://api.github.com/repos/torvalds/linux/commits"
linux_repo = gh_session.get(url)
print("Total commmits to Linux repository: " + str(len(linux_repo.content)))