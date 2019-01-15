# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

### Box Office Mojo ###



def change_string(year = None, week = None):
    """
    This will change the year and week to get the weekly information form 
    boxofficemojo.
    """
    weekend_top5 = "https://www.boxofficemojo.com/weekend/chart/?yr=2019&wknd=02&p=.htm"
    if year is not None or week is not None:
        weekend_top5 = weekend_top5.replace("2019", year)
        weekend_top5 = weekend_top5.replace("02", week)
    else:
        return weekend_top5
    return weekend_top5


def get_weekend_movie_top5_performers(link):
    """
    Will return the top 5 movies of the weekend.
    """
    web_link = requests.get(link)
    soup = bs(web_link.content, "lxml")
    weekend_gross = soup.select("tr td font b")
    
    for index, value in enumerate(weekend_gross):
        if "Weekend Gross" in str(value):
            first_slice = index+1
        elif "TOTAL (" in str(value):
            end_slice = index+2
        
    weekend_gross = weekend_gross[first_slice:end_slice]
    clean_movies = [re.sub("<.*?>", "", str(movie)) for index, movie in enumerate(weekend_gross) if index % 2 == 0]
    clean_wknd_gross = ["{:.2f}".format(round((float(re.sub("\D", "", str(movie)))/1000000),2)) for index, movie in enumerate(weekend_gross) if index % 2 == 1 ]
    weekend_box_office = pd.DataFrame({"Movie_Name": clean_movies, "Weekend_Gross": clean_wknd_gross})
    return weekend_box_office.iloc[0:5]

 ########################################################   
        
get_weekend_movie_top5_performers(change_string())
    
###################################    




#
##weekend_top5 = weekend_top5.replace("wknd=02", "wknd=01")     
#link = requests.get(weekend_top5)
#soup = bs(link.content, "lxml")
#weekend_gross = soup.select("tr td font b")
#
##Slicing the data to only include movies
#for index, value in enumerate(weekend_gross):
#    if "Weekend Gross" in str(value):
#        first_slice = index+1
#    elif "TOTAL (" in str(value):
#        end_slice = index+2
#
##for index, value in enumerate(weekend_gross):
##    print(index, value)
#
##Removing all the uneccessary stuff
#weekend_gross = weekend_gross[first_slice:end_slice]
#clean_movies = [re.sub("<.*?>", "", str(movie)) for index, movie in enumerate(weekend_gross) if index % 2 == 0]
#clean_wknd_gross = ["{:.2f}".format(round((float(re.sub("\D", "", str(movie)))/1000000),2)) for index, movie in enumerate(weekend_gross) if index % 2 == 1 ]
#weekend_box_office = pd.DataFrame({"Movie_Name": clean_movies, "Weekend_Gross": clean_wknd_gross})
#
##The top 5 movies of the weekend
#print(weekend_box_office.iloc[0:5])
##print(weekend_box_office)



#If you want to change the year of the link
#weekend_top5 = "https://www.boxofficemojo.com/weekend/chart/?yr=2019&wknd=02&p=.htm"
#weekend_top5 = weekend_top5.replace("yr=2019", "yr=2018")

##Gets the top 5 movies from box office mojo
#weekend_top5 = "https://www.boxofficemojo.com/weekend/chart/?yr=2019&wknd=02&p=.htm"
    
    
    
    
    
    