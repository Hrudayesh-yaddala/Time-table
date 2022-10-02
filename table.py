import datetime
import pandas as pd

w=['monday','tuesday','wednesday','thursday','friday','saturday']
now = datetime.datetime.now()
try:
    da = int(input('want to know present day or someother day\npresent_day: press 1\nother_day:press 2 : '))
    if(da == 1):
        x = now.strftime("%A")
    elif(da == 2):
        x = input('DAY:')
        if(x.lower() not in w):
            print('please enter valid day name 🌲🌲🌲')
            exit()
        if(x.lower() == 'sunday'):
            print('sorry sessions are not scheduled for sunday 🏮🏮🏮')
            exit()
    else:
        print(' 🚩🚩🚩 provide input properly')
        exit()
    s = input().split()
    if(int(s[1])>8 or int(s[1])<1):
        print('sessions are in the range 1 to 8 only  🏮🏮🏮')
        exit()
    df = pd.read_csv(s[0]+'.csv')
    df.set_index('DAY', inplace=True)
    perd = df.loc[x.lower()].iat[int(s[1]) - 1]
    print('subject name:{}\nfaculty name:{}'.format(perd,df.loc[perd].iat[0]))
except Exception as e:
    print(e)
