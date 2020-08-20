
"""
Developer : Aravind S Krishnan
VER : 1.0
Data Source : https://api.covid19india.org/v4/data.json
"""

import urllib.request
import urllib.error
import json
import matplotlib.pyplot as plt
import numpy as np
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


#Graph Plotting Function
def ploting(chart_type,chart_name,lim):
    plt.subplots()
    y_pos=np.arange(len(districts))
    plt.barh(y_pos,chart_type, align='center', alpha=0.6,)
    for i, v in enumerate(chart_type):
        plt.text(v, i-.2, str(v), color='red')
    plt.yticks(y_pos,districts)
    plt.xlabel('Cases')    
    plt.xlim([0,lim])   
    name='Districtwise '+chart_name+' on '+date
    plt.title(name)
    plt.savefig(chart_name+'.png',bbox_inches='tight',pad_inches=0.2)
    plt.show()
    

#District Data Extraction Function
def data_district(data_type):
    name_type=data_type
    confirmed_cases=(Alappuzha["total"][name_type],Ernakulam["total"][name_type],Idukki["total"][name_type],Kannur["total"][name_type],
                     Kasargod["total"][name_type],Kollam["total"][name_type],Kottayam["total"][name_type],
                     Kozhikode["total"][name_type],Malappuram["total"][name_type],Palakkad["total"][name_type],
                     Pathanamthitta["total"][name_type],Thiruvananthapuram["total"][name_type],
                     Thrissur["total"][name_type],Wayanad["total"][name_type])    
    return(confirmed_cases)


#Graph Image Pasting Function
def image_paste(image_name,x_cord,y_cord):
    img_total = Image.open(image_name)
    img_total = img_total.resize((round(img_total.size[0]*2.3), round(img_total.size[1]*2.3)))
    graph_img = img.copy()
    graph_img.paste(img_total, (x_cord, y_cord))
    return graph_img


#Loading Constants and Data
date=time.strftime("%d-%m-%Y")
url = 'https://api.covid19india.org/v4/data.json'
output = urllib.request.urlopen(url).read()
tree = json.loads(output)


#Setting District Constants
Alappuzha=tree["KL"]["districts"]["Alappuzha"]
Ernakulam=tree["KL"]["districts"]["Ernakulam"]
Idukki=tree["KL"]["districts"]["Idukki"]
Kannur=tree["KL"]["districts"]["Kannur"]
Kasargod=tree["KL"]["districts"]["Kasaragod"]
Kollam=tree["KL"]["districts"]["Kollam"]
Kottayam=tree["KL"]["districts"]["Kottayam"]
Kozhikode=tree["KL"]["districts"]["Kozhikode"]
Malappuram=tree["KL"]["districts"]["Malappuram"]
Palakkad=tree["KL"]["districts"]["Palakkad"]
Pathanamthitta=tree["KL"]["districts"]["Pathanamthitta"]
Thiruvananthapuram=tree["KL"]["districts"]["Thiruvananthapuram"]
Thrissur=tree["KL"]["districts"]["Thrissur"]
Wayanad=tree["KL"]["districts"]["Wayanad"]
totalKerala=tree["KL"]["total"]

#Creating District Name Tuple
districts=('Allapuzha','Ernakulam','Idukki','Kannur','Kasargod','Kollam','Kottayam','Kozhikode','Malappuram',
           'Palakkad','Pathnamthitta','Thiruvananthapuram','Thrissur','Wayanad')

#Plotting Bar Charts
cases=data_district('confirmed')#Confirmed Cases 
ploting(cases,'total cases',13500)
recovered=data_district('recovered')#Recovered Cases
ploting(recovered,'recoveries',8000)
death=data_district('deceased')#Deaths
ploting(death, 'total deaths',80)
active_cases=res = tuple(map(lambda i, j,k: i - j - k, cases, recovered,death)) #Active Cases
ploting(active_cases,'active cases',6000)


#Report Text Generation
report_name='COVID-19 Kerala Statistics'
font='lt.otf' #Replace with prefered font name
img = Image.open("template.png")
img = img.convert('RGB')
draw = ImageDraw.Draw(img)
selectFont = ImageFont.truetype(font, size = 130)
draw.text( (200,100), report_name.upper(),(90,115,95), font=selectFont)
selectFont = ImageFont.truetype(font, size = 60)
draw.text( (920,260), 'DATE : '+date,(100,100,100), font=selectFont)
draw.text( (380,660), 'Total Cases : '+str(totalKerala['confirmed']),(200,0,0), font=selectFont)
draw.text( (1350,760), 'Total Recoveries : '+str(totalKerala['recovered']),(0,200,0), font=selectFont)
draw.text( (1350,660), 'Total Deaths : '+str(totalKerala['deceased']),(50,50,50), font=selectFont)
draw.text( (380,760), 'Active Cases : '+str(totalKerala['confirmed']-totalKerala['recovered']-totalKerala['deceased']),(0,0,200), font=selectFont)


#Report Graph Pasteing
tot=image_paste('total cases.png', 80, 1020)#Confirmed cases
img=tot
rec=image_paste('recoveries.png', 1210, 1020)#Recoveries
img=rec
det=image_paste('total deaths.png', 80, 1820)#Deaths
img=det
act=image_paste('active cases.png', 1210, 1820)#Active
act.save('report_'+str(date)+'.png')
