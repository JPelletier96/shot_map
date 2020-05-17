#This first draw_pitch function is a slightly edited version of the code from Peter McKeever's blog post: http://petermckeever.com/2019/01/plotting-pitches-in-python/
import matplotlib.pyplot as plt

def draw_pitch(pitch, line, orientation,view):
    
    orientation = orientation
    view = view
    line = line
    pitch = pitch
    
    if orientation.lower().startswith("h"):
        
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(7.0,10.5))
            plt.xlim(50,106)
            plt.ylim(-1,71)
        else:
            fig,ax = plt.subplots(figsize=(10.5,7.0))
            plt.xlim(-1,106)
            plt.ylim(-1,71)
        ax.axis('off') # this hides the x and y ticks
    
        # side and goal lines #
        ly1 = [0,0,70,70,0]
        lx1 = [0,105,105,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        ly2 = [13,13,57,57] 
        lx2 = [105,87,87,105]
        plt.plot(lx2,ly2,color=line,zorder=5)

        ly3 = [13,13,57,57] 
        lx3 = [0,18,18,0]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        ly4 = [31,31,38,38]
        lx4 = [105,105.2,105.2,105]
        plt.plot(lx4,ly4,color=line,zorder=5)

        ly5 = [31,31,38,38]
        lx5 = [0,-0.2,-0.2,0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        ly6 = [25,25,45,45]
        lx6 = [105,99,99,105]
        plt.plot(lx6,ly6,color=line,zorder=5)

        ly7 = [25,25,45,45]
        lx7 = [0,6,6,0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        ly8 = [0,70] 
        lx8 = [52.5,52.5]
        plt.plot(lx8,ly8,color=line,zorder=5)


        plt.scatter(93,35,color=line,zorder=5)
        plt.scatter(12,35,color=line,zorder=5)
        plt.scatter(52.5,35,color=line,zorder=5)

        circle1 = plt.Circle((93.5,35), 10,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((11.5,35), 10,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((52.5, 35), 10,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)

        ## Rectangles in boxes
        rec1 = plt.Rectangle((87,20), 18,30,ls='-',color=pitch, zorder=1,alpha=1)
        rec2 = plt.Rectangle((0, 20), 18,30,ls='-',color=pitch, zorder=1,alpha=1)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 107,72,ls='-',color=pitch, zorder=1,alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)
        
    else:
        if view.lower().startswith("h"):
            fig,ax = plt.subplots(figsize=(10.5,7.0))
            plt.ylim(50,106)
            plt.xlim(-1,71)
        else:
            fig,ax = plt.subplots(figsize=(7.0,10.5))
            plt.ylim(-1,106)
            plt.xlim(-1,71)
        ax.axis('off') # this hides the x and y ticks

        # side and goal lines #
        lx1 = [0,0,70,70,0]
        ly1 = [0,105,105,0,0]

        plt.plot(lx1,ly1,color=line,zorder=5)


        # boxes, 6 yard box and goals

            #outer boxes#
        lx2 = [13,13,57,57] 
        ly2 = [105,87,87,105]
        plt.plot(lx2,ly2,color=line,zorder=5)

        lx3 = [13,13,57,57] 
        ly3 = [0,18,18,0]
        plt.plot(lx3,ly3,color=line,zorder=5)

            #goals#
        lx4 = [31,31,38,38]
        ly4 = [105,105.2,105.2,105]
        plt.plot(lx4,ly4,color=line,zorder=5)

        lx5 = [31,31,38,38]
        ly5 = [0,-0.2,-0.2,0]
        plt.plot(lx5,ly5,color=line,zorder=5)


           #6 yard boxes#
        lx6 = [25,25,45,45]
        ly6 = [105,99,99,105]
        plt.plot(lx6,ly6,color=line,zorder=5)

        lx7 = [25,25,45,45]
        ly7 = [0,6,6,0]
        plt.plot(lx7,ly7,color=line,zorder=5)

        #Halfway line, penalty spots, and kickoff spot
        lx8 = [0,70] 
        ly8 = [52.5,52.5]
        plt.plot(lx8,ly8,color=line,zorder=5)


        plt.scatter(35,93,color=line,zorder=5)
        plt.scatter(35,12,color=line,zorder=5)
        plt.scatter(35,52.5,color=line,zorder=5)

        circle1 = plt.Circle((35,93.5), 10,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle2 = plt.Circle((35,11.5), 10,ls='solid',lw=1.5,color=line, fill=False, zorder=1,alpha=1)
        circle3 = plt.Circle((35,52.5), 10,ls='solid',lw=1.5,color=line, fill=False, zorder=2,alpha=1)


        ## Rectangles in boxes
        rec1 = plt.Rectangle((20, 87), 30,18,ls='-',color=pitch, zorder=1,alpha=1)
        rec2 = plt.Rectangle((20, 0), 30,18,ls='-',color=pitch, zorder=1,alpha=1)

        ## Pitch rectangle
        rec3 = plt.Rectangle((-1, -1), 72,107,ls='-',color=pitch, zorder=1,alpha=1)

        ax.add_artist(rec3)
        ax.add_artist(circle1)
        ax.add_artist(circle2)
        ax.add_artist(rec1)
        ax.add_artist(rec2)
        ax.add_artist(circle3)
        
        
        
import csv
import pandas as pd
draw_pitch("#199905","#faf0e6","h","full")
from matplotlib.patches import Rectangle

#########################   USER INPUTS  ##########################
#match odds based on simulating all shots. I get these numbers from copying and pasting all the Hxg and Axg values into https://danny.page/expected_goals.html
HomeWin = 47.26
draw = 22.56
AwayWin = 30.18

#team colors
home_color = 'blue'
away_color = 'yellow'
goal_color = 'red'
###################################################################
zo=12
#read the csv into a data frame (make sure the csv is in the same directory as the python file or put the correct path to the file)
df = pd.read_csv('UDvCCevents.csv', header=0)

#assign columns to variables
home_away = df['teamFor'].values.tolist()
xg = df['xG'].values.tolist()
x = df['x'].values.tolist()
y = df['y'].values.tolist()
outcome = df['outcome'].values.tolist()
minute = df['min'].values.tolist()
sec = df['sec'].values.tolist()
home = df['home'][0]
away = df['away'][0]

#Home values
Hx = []
Hy = []
Hxg = []
Hscore = 0
Hpenalties = 0
Hshape = 'o'
Hcolor = []
Hmin = []
Hsec = []

#Away values 
Ax = []
Ay = []
Axg = []
Ascore = 0
Apenalties = 0
Ashape = 'o'
Acolor = []
Amin = []
Asec = []

#populate lists
count = 0
for value in home_away:
    if value == 'home':
        if situation[count] == 'Penalty':
            Hpenalties += 1
            Hscore += 1
            continue
        Hx.append(x[count])
        Hy.append(y[count])
        Hxg.append(xg[count])
        Hmin.append(minute[count])
        Hsec.append(sec[count])
        if outcome[count] == 'Goal':
            Hcolor.append('goal_color')
            Hscore += 1
        else:
            Hcolor.append('home_color')
    else:
        if situation[count] == 'Penalty':
            Apenalties += 1
            Ascore += 1
            continue
        Ax.append(x[count])
        Ay.append(y[count])
        Axg.append(xg[count])
        Amin.append(minute[count])
        Asec.append(sec[count])
        if outcome[count] == 'Goal':
            Acolor.append('goal_color')
            Ascore += 1
        else:
            Acolor.append('away_color')
    count += 1
    
#invert the y coordinates so they line up properly
x1 = [105 - i for i in Hx]
y1 = [70 - i for i in Hy]
Hxg_scaled = [900 * i for i in Hxg] # This is to scale the "xG" values for plotting
for i in range(len(Hxg)): 
    mi = Hshape #marker for ith feature 
    xi = x1[i]
    yi = y1[i] 
    ci = Hcolor[i] 
    si = Hxg_scaled[i]
    plt.scatter(xi,yi,s=si,marker=mi,color=ci,edgecolors="black",zorder=zo) 

Axg_scaled = [900 * i for i in Axg] # This is to scale the "xG" values for plotting
for i in range(len(Axg)): 
    mi = Ashape #marker for ith feature 
    xi = Ax[i]
    yi = Ay[i] 
    ci = Acolor[i] 
    si = Axg_scaled[i]
    plt.scatter(xi,yi,s=si,marker=mi,color=ci,edgecolors="black",zorder=zo) 

#xG legend
mSize = [0.05,0.10,0.2,0.4,0.6,1] 
mSizeS = [900 * i for i in mSize]
mx = [2,4,6.5,10,14.5,20]
my = [6.2,6.2,6.2,6.2,6.2,6.2]
plt.scatter(mx,my,s=mSizeS,facecolors="white",edgecolor="white",zorder=zo)
plt.plot([2,21],[3,3],color="white",lw=2,zorder=zo)
font = {'fontname':'Century Gothic'}


i = 0
for i in range(len(mx)):
    plt.text(mx[i],my[i],mSize[i],fontsize=mSize[i]*18,color="#195905",zorder=zo,ha="center",va="center")
    plt.text(11,1.20,"xG",**font,color="white",ha="center",va="center",zorder=zo,fontsize=16)
    
    #title. I left it in the loop to make the font a little bolder
    plt.text(53,67,f"{home}  {Hscore} - {Ascore}  {away}",**font,color="black",ha="center",va="center",zorder=zo,fontsize=23)
    if Apenalties > 0:
        plt.text(55,62,f"xG: {round(sum(Hxg),2)} - {round(sum(Axg),2)} (+{Apenalties} PK)",**font,color="black",ha="center",va="center",zorder=zo,fontsize=23)
    elif Hpenalties > 0:
        plt.text(55,62,f"xG: (+{Hpenalties} PK) {round(sum(Hxg),2)} - {round(sum(Axg),2)}",**font,color="black",ha="center",va="center",zorder=zo,fontsize=23)
    else:
        plt.text(47.5,62,f"xG: {round(sum(Hxg),2)} - {round(sum(Axg),2)}",**font,color="black",ha="center",va="center",zorder=zo,fontsize=23)
    plt.text(43.3,57,f"xG/shot: {round(sum(Hxg)/len(Hxg),2)} - {round(sum(Axg)/len(Axg),2)}",**font,color="black",ha="center",va="center",zorder=zo,fontsize=23)
    


home_odds = (HomeWin/100) * 20
draw_odds = (draw/100) * 20 + home_odds

ax = plt.gca()
away_win_rect = Rectangle((42.5,51.5),20,3.5,color='yellow',ec='black',zorder=zo)
tie_rect = Rectangle((42.5,51.5),draw_odds,3.5,color='silver',ec='black',zorder=zo)
home_win_rect = Rectangle((42.5,51.5),home_odds,3.5,color='blue',ec='black',zorder=zo)

ax.add_patch(away_win_rect)
ax.add_patch(tie_rect)
ax.add_patch(home_win_rect)


plt.text(58,52.75,'{:2.0f}%'.format(HomeWin),**font,color="black",zorder=zo,fontsize=9)
plt.text(52.8,52.75,'{:2.0f}%'.format(draw),**font,color="black",zorder=zo,fontsize=9)
plt.text(46,52.75,'{:2.0f}%'.format(AwayWin),**font,color="black",zorder=zo,fontsize=9)


plt.show()
