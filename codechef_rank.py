'''Description:Get current codechef ranks of all your friends at one place,no need to open their id's seperately'''

# File name: codechef_rank.py
# Author: Arpit Kathuria
# Date created: 22/12/2015
# Date last modified: 22/12/2015
# Python Version: 3.5
# Modules required:beautifulsoup4,requests.

import requests
from bs4 import BeautifulSoup

def get_rank(user_name):
    url="https://www.codechef.com/users/"+str(user_name)
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    rating_table=soup.find('table',{'class':'rating-table'})
    rank_list=[]
    try:
        for _ in rating_table.find_all('a'):
            try:
                rank_list.append(int(_.string))
            except:
                if _.string=="NA":
                    rank_list.append("NA")
                    rank_list.append("NA")
        name=soup.find('div',{'class':'user-name-box'})
        print("Name:"+str(name.string))
        print("Long:")
        print("Global:"+str(rank_list[0])+"/Country:"+str(rank_list[1]))
        print("Short:")
        print("Global:"+str(rank_list[2])+"/Country:"+str(rank_list[3]))
        print("LTime(All):")
        print("Global:"+str(rank_list[4])+"/Country:"+str(rank_list[5]))
        print("")
    except:
        check_error=soup.find('div',id='lightboxAutoModal')
        error=str(check_error.contents[0].string.strip()).split()
        error[2]="'"+user_name+"'"
        error=" ".join(str(i) for i in error)
        print(error)
user_names=input('Enter username(s)(space seperated if more than one):').split()
for user_name in user_names:
    get_rank(user_name)
console_open=input('Press any key to close!')#just to keep console open.