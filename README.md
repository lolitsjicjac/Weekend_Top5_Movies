# Weekend_Top5_Movies
The top 5 movies of every week per BoxofficeMojo

## How the function works

### change_string(year = '2018', week = '45')

This function allows a user to change the year and week. This way they are able to pull that givens years week top 5 performing movies.
The Year is in 'YYYY' format and the weeks are 0-52 format.

By default if you do not pass anything it will go to second week of 2019.

### get_weekend_movie_top5_performers()

This function returns the top 5 movies in a dataframe with their weeklky gross.

## To run the code

### get_weekend_movie_top5_performers(change_string())
