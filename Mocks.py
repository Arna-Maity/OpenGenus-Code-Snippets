import time
import github
import os

ACCESS_TOKEN = os.environ.get('GITHUB_AUTH_TOKEN')

if not ACCESS_TOKEN:
    print('Please set an Access Token for User Authentication!')


def 
try:
    gacc = github.Github(ACCESS_TOKEN)


    #start = time.time()
    #for repo in gacc.get_user().get_repos():
    #    print(repo.name)
    #
    #end = time.time()

    #print("\nTime Elapsed: ",(end - start),"s")

    print(list(gacc.get_user().get_repos()))


except github.GithubException:
    print('Sorry, Failed to fetch your Repos!')