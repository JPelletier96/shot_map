# Shot Maps
Using the shot_map.py code with Peter McKeever's openfootball.club, you can create your own xG shot maps for any game. (circle = shot, location = shot location, circle size = xG (see legend at the bottom left), circle color = team colors, red circle = goal, colored bars = % likelihood of home team getting a win(blue), draw(gray), or away team getting a win(yellow) based on the team's xG)
<p align="center">
  <img width="600" height="394" src="https://user-images.githubusercontent.com/57690237/82160978-c3f23680-985e-11ea-9be2-870cd3e8cad3.png">
</p>

Note: I recommend running this as a jupyter notebook, just because it's easier to get the results percentages, but I did include both .py and .ipynb files so go with whichever one you prefer.
1. Collect the shot data for the game using openfootball.club and make sure you fill out every field. If you just want to play around with the code I do have the shot data from our game against Colorado College that you're free to use.
<p align="center">
  <img width="686.7" height="420" src="https://user-images.githubusercontent.com/57690237/82161302-2f3d0800-9861-11ea-845c-7a5020496c6e.png">
</p>


2. Make sure the downloaded CSV is in the same directory as shot_map.py (or shot_map.ipynb), adjust the user inputs, and run the script.
3. Follow the instructions at the bottom of the script to change the results percentages (In the future I'll try and fix this so you don't have to go to another site to get the results percentages data).
4. If you like openfootball.club and up using it a lot, consider buying Peter a beer or 2 ;)


