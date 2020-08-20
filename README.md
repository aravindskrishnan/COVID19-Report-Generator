# Automatic COVID19 Report Generator
This project aims to reads web data about districtwise COVID19 data for states in India and plot districtwise bar graph for total cases, total recoveries, total deaths and active cases.
The code contained in this repository is based on Kerala, but the same code can be adapted for all the states in India with relatively minor modifications to the constants section. The output of the programme is a png image containing the stats and bar chart of COVID cases on the day the code was run.



## Environment and Library Installation
The project script is implemented in python 3, with pillow,urllib,matplotlib and numpy libraries.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install openCV and numpy. Copy paste the following commands in your terminal/power shell one after the other.

```bash
pip install urllib
```
```bash
pip install numpy
```
```bash
pip install pillow
```
```bash
pip install numpy
```
```bash
pip install matplotlib
```

## Code Adaptations
```python
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
 ```
 chart_type is the type of data ( total cases, recoveries etc) that needed to be passed on as argument. chart_name is the name of the chart as required, it accepts a string input. lim specifies the x axis limit of the bar chart.
```python 
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
```
To change the state and district, change the state code to the required state code ( Example for changing state to Andhra Pradesh, change ["KL"] to ["AP"] ). Be sure to change the district name as well and add/remove the districts as per requirements.
```python
districts=('Allapuzha','Ernakulam','Idukki','Kannur','Kasargod','Kollam','Kottayam','Kozhikode','Malappuram',
           'Palakkad','Pathnamthitta','Thiruvananthapuram','Thrissur','Wayanad')
```
change the districts tuple in the same order as given in the json file. The json file can be found here : https://api.covid19india.org/v4/data.json
```python
report_name='COVID-19 Kerala Statistics'
font='lt.otf' #Replace with prefered font name
img = Image.open("template.png")
```
The above 3 lines are the most important for modification. Give a report_name of your choice and provide the path to your prefered font in the font constant.
The template.png is included in this repo, but if you wish to change the base image on which the report is made, feel free to replace the template.jpg with an image of your choice ( be sure to adjust the coordinates of the text and images after doing so, as this programme is adjusted for this particular base image )
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
The [MIT](https://choosealicense.com/licenses/mit/) License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

