#!/usr/bin/env python

import pandas as pd 
from matplotlib import pyplot as plt

print('\nCOVID 19 Data Visulaization\n')
print('-------MENU-------\n')
print('1. Plot of total Coronavirus cases in India ')
print('2. Plot of state wise Coronavirus cases in India')
print('3. Plot of total Coronavirus cases in Kerala')
print('4. Plot of district wise Coronavirus cases in Kerala')
ch = int(input('\nEnter a choice: '))


if(ch==1):
    india_data = pd.read_csv("india.csv")
    plt.plot(india_data.Date,india_data.Cases)
    plt.title("Total Coronavirus cases in India")
    plt.xlabel("Date")
    plt.ylabel("Coronavirus Cases")
    ax=plt.gca()
    ax.set_xlim([0,36])
    plt.xticks(rotation=75)
    plt.savefig('india.png', bbox_inches='tight',dpi=350)
    print('\nImage is successfuly generated\n')

elif(ch==2):    
     raw_data = pd.read_csv('states.csv')
     data = raw_data[:36][['Date', 'AN','AP','AR','AS','BR','CH','CG','DL','GA','GJ','HR','HP','JK','JH','KA','KL','LA','MP','MH','MN','MZ','OD','PY','PB','RJ','TN','TS','UK','UP','WB']]
     plt.figure(figsize=(10,7))
     barWidth = 0.65
     plt.bar(x=data.Date, height=data.AN, width=barWidth)
     plt.bar(x=data.Date, height=data.AP, width=barWidth, bottom=data.AN)
     plt.bar(x=data.Date, height=data.AR,width=barWidth,bottom=data.AN+data.AP)
     plt.bar(x=data.Date, height=data.AS,width=barWidth,bottom=data.AN+data.AP+data.AR)
     plt.bar(x=data.Date, height=data.BR,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS)
     plt.bar(x=data.Date, height=data.CH,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR)
     plt.bar(x=data.Date, height=data.CG,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH)
     plt.bar(x=data.Date, height=data.DL,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG)
     plt.bar(x=data.Date, height=data.GA,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL)
     plt.bar(x=data.Date, height=data.GJ,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA)
     plt.bar(x=data.Date, height=data.HR,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ)
     plt.bar(x=data.Date, height=data.HP,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR)
     plt.bar(x=data.Date, height=data.JK,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP)
     plt.bar(x=data.Date, height=data.JH,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK)
     plt.bar(x=data.Date, height=data.KA,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH)                    
     plt.bar(x=data.Date, height=data.KL,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA)
     plt.bar(x=data.Date, height=data.LA,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL)
     plt.bar(x=data.Date, height=data.MP,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA)      
     plt.bar(x=data.Date, height=data.MH,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+                 +data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP)  
     plt.bar(x=data.Date,    height=data.MN,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH) 
     plt.bar(x=data.Date, height=data.MZ,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN) 
     plt.bar(x=data.Date, height=data.OD,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ) 
     plt.bar(x=data.Date, height=data.PY,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD) 
     plt.bar(x=data.Date, height=data.PB,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY)
     plt.bar(x=data.Date, height=data.RJ,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY+data.PB)
     plt.bar(x=data.Date, height=data.TN,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY+data.PB+data.RJ)
     plt.bar(x=data.Date, height=data.TS,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY+data.PB+data.RJ+data.TN)
     plt.bar(x=data.Date, height=data.UK,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY+data.PB+data.RJ+data.TN+data.TS)
     plt.bar(x=data.Date, height=data.UP,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY+data.PB+data.RJ+data.TN+data.TS+data.UK)
     plt.bar(x=data.Date, height=data.WB,width=barWidth,bottom=data.AN+data.AP+data.AR+data.AS+data.BR+data.CH+data.CG+data.DL+data.GA+data.GJ+data.HR+data.HP+data.JK+data.JH+data.KA+data.KL+data.LA+data.MP+data.MH+data.MN+data.MZ+data.OD+data.PY+data.PB+data.RJ+data.TN+data.TS+data.UK+data.UP)
     plt.xticks(rotation=75)
     plt.legend(["Andaman and Nicobar Islands", "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Madhya Pradesh","Maharashtra","Manipur","Mizoram","Odisha","Puducherry","Punjab","Rajasthan","Tamil Nadu","Telangana","Uttarakhand","Uttar Pradesh","West Bengal"],bbox_to_anchor=(1.4, 1))
     plt.title("State wise Coronavirus cases in India")
     plt.xlabel("Date")
     plt.ylabel("Coronavirus Cases")
     plt.xticks(rotation=75)
     plt.savefig('states.png', bbox_inches='tight', dpi=350)
     print('\nImage is successfuly generated\n')



elif(ch==3):
     kerala_data = pd.read_csv("kerala.csv")
     plt.plot(kerala_data.Date,kerala_data.Cases)
     plt.title("Total Coronavirus cases in Kerala")
     plt.xlabel("Date")
     plt.ylabel("Coronavirus Cases")
     ax=plt.gca()
     ax.set_xlim([0,24])
     plt.xticks(rotation=75)
     plt.savefig('kerala.png', bbox_inches='tight',dpi=350)
     print('\nImage is successfuly generated\n')

elif(ch==4):
     district_data = pd.read_csv('districts.csv')
     d_data = district_data[:23][['Date','AL','ER','ID','KN','KS','KL','KT','KZ','MA','PL','PT','TV','TS','WA']]
     plt.figure(figsize=(10,8))
     barWidth = 0.65
     plt.bar(x=d_data.Date, height=d_data.AL,width=barWidth)
     plt.bar(x=d_data.Date, height=d_data.ER,width=barWidth,bottom=d_data.AL)
     plt.bar(x=d_data.Date, height=d_data.ID,width=barWidth,bottom=d_data.AL+d_data.ER)
     plt.bar(x=d_data.Date, height=d_data.KN,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID)
     plt.bar(x=d_data.Date, height=d_data.KS,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN)
     plt.bar(x=d_data.Date, height=d_data.KL,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS)
     plt.bar(x=d_data.Date, height=d_data.KT,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL)
     plt.bar(x=d_data.Date, height=d_data.KZ,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT)
     plt.bar(x=d_data.Date, height=d_data.MA,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT+d_data.KZ)
     plt.bar(x=d_data.Date, height=d_data.PL,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT+d_data.KZ+d_data.MA)
     plt.bar(x=d_data.Date, height=d_data.PT,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT+d_data.KZ+d_data.MA+d_data.PL)
     plt.bar(x=d_data.Date, height=d_data.TV,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT+d_data.KZ+d_data.MA+d_data.PL+d_data.PT)
     plt.bar(x=d_data.Date, height=d_data.TS,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT+d_data.KZ+d_data.MA+d_data.PL+d_data.PT+d_data.TV)
     plt.bar(x=d_data.Date, height=d_data.WA,width=barWidth,bottom=d_data.AL+d_data.ER+d_data.ID+d_data.KN+d_data.KS+d_data.KL+d_data.KT+d_data.KZ+d_data.MA+d_data.PL+d_data.PT+d_data.TV+d_data.TS)
     ax=plt.gca()
     ax.set_ylim([0,40])
     plt.legend(["Alappuzha",   "Ernakulam","Idukki","Kannur","Kasargod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamathitta","Thiruvananthapuram","Thrissur","Wayanad"],bbox_to_anchor=(1.3,0.9))
     plt.title("District wise Coronavirus cases in Kerala")
     plt.xlabel("Date")
     plt.ylabel("Coronavirus Cases")
     plt.xticks(rotation=75)
     plt.savefig('districts.png', bbox_inches='tight', dpi=350)
     print('\nImage is successfuly generated\n')

else:
     print('Invalid Choice')




