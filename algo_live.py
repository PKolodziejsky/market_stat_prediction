import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from functools import reduce        # takes function as argument
from alpha_vantage.foreignexchange import ForeignExchange
import time

alpha_key = 'VSCB9AMAH2RJVBV1'


fx = ForeignExchange(key=alpha_key, output_format='pandas')
df, meta_data = fx.get_currency_exchange_intraday('EUR', 'USD', '1min', 'full')
print(df['4. close'])
avg_price = df['4. close']
pattern_arr = []        #array of patterns created from points (see path_store)
perf_arr = []           #array of future outcomes of patterns in pattern_arr
pattern_for_rec_arr = []    #current pattern
preds = []      #predictions for current pattern

def per_change(start,curr):

    try:
        x = ((float(curr)-start)/abs(start))*100
        if(x == 0.0):
            return 0.000000001
        else:
            return x
    except Exception as e:
        print (str(e))
        return 0.0001

def path_store():       #storing patterns

    x = len(avg_price) - 30
    if(len(pattern_arr) > 1300):
        y = len(avg_price)-31
    else:
        y = 31
    
    while y < x:
        pattern = []    #single pattern, array of x points

        p1 = per_change(avg_price[y - 30], avg_price[y - 29])
        p2 = per_change(avg_price[y - 30], avg_price[y - 28])
        p3 = per_change(avg_price[y - 30], avg_price[y - 27])
        p4 = per_change(avg_price[y - 30], avg_price[y - 26])
        p5 = per_change(avg_price[y - 30], avg_price[y - 25])
        p6 = per_change(avg_price[y - 30], avg_price[y - 24])
        p7 = per_change(avg_price[y - 30], avg_price[y - 23])
        p8 = per_change(avg_price[y - 30], avg_price[y - 22])
        p9 = per_change(avg_price[y - 30], avg_price[y - 21])
        p10 = per_change(avg_price[y - 30], avg_price[y - 20])

        p11 = per_change(avg_price[y - 30], avg_price[y - 19])
        p12 = per_change(avg_price[y - 30], avg_price[y - 18])
        p13 = per_change(avg_price[y - 30], avg_price[y - 17])
        p14 = per_change(avg_price[y - 30], avg_price[y - 16])
        p15 = per_change(avg_price[y - 30], avg_price[y - 15])
        p16 = per_change(avg_price[y - 30], avg_price[y - 14])
        p17 = per_change(avg_price[y - 30], avg_price[y - 13])
        p18 = per_change(avg_price[y - 30], avg_price[y - 12])
        p19 = per_change(avg_price[y - 30], avg_price[y - 11])
        p20 = per_change(avg_price[y - 30], avg_price[y - 10])

        p21 = per_change(avg_price[y - 30], avg_price[y - 9])
        p22 = per_change(avg_price[y - 30], avg_price[y - 8])
        p23 = per_change(avg_price[y - 30], avg_price[y - 7])
        p24 = per_change(avg_price[y - 30], avg_price[y - 6])
        p25 = per_change(avg_price[y - 30], avg_price[y - 5])
        p26 = per_change(avg_price[y - 30], avg_price[y - 4])
        p27 = per_change(avg_price[y - 30], avg_price[y - 3])
        p28 = per_change(avg_price[y - 30], avg_price[y - 2])
        p29 = per_change(avg_price[y - 30], avg_price[y - 1])
        p30 = per_change(avg_price[y - 30], avg_price[y])

        outcome_range = avg_price[y+20:y+30]

        try:
            avg_outcome = reduce(lambda x,y: x+y,outcome_range) / len(outcome_range)
        except Exception as e:
            print (str(e))
            avg_outcome = 0

        curr = avg_price[y]     # "current" element
        future_outcome =per_change(curr,avg_outcome)

        pattern.append(p1)
        pattern.append(p2)
        pattern.append(p3)
        pattern.append(p4)
        pattern.append(p5)
        pattern.append(p6)
        pattern.append(p7)
        pattern.append(p8)
        pattern.append(p9)
        pattern.append(p10)

        pattern.append(p11)
        pattern.append(p12)
        pattern.append(p13)
        pattern.append(p14)
        pattern.append(p15)
        pattern.append(p16)
        pattern.append(p17)
        pattern.append(p18)
        pattern.append(p19)
        pattern.append(p20)

        pattern.append(p21)
        pattern.append(p22)
        pattern.append(p23)
        pattern.append(p24)
        pattern.append(p25)
        pattern.append(p26)
        pattern.append(p27)
        pattern.append(p28)
        pattern.append(p29)
        pattern.append(p30)

        pattern_arr.append(pattern)
        perf_arr.append(future_outcome)

        if (y%10000==0):
            print(y,"- patterns stored")

        y += 1

    if(len(pattern_arr) == len(perf_arr)):
        print("Stored",len(pattern_arr),"patterns")
    else:
        print("Arrays not equal")


def curr_patt():    #storing current pattern

    cp1 = per_change(avg_price[-31], avg_price[-30])
    cp2 = per_change(avg_price[-31], avg_price[-29])
    cp3 = per_change(avg_price[-31], avg_price[-28])
    cp4 = per_change(avg_price[-31], avg_price[-27])
    cp5 = per_change(avg_price[-31], avg_price[-26])
    cp6 = per_change(avg_price[-31], avg_price[-25])
    cp7 = per_change(avg_price[-31], avg_price[-24])
    cp8 = per_change(avg_price[-31], avg_price[-23])
    cp9 = per_change(avg_price[-31], avg_price[-22])
    cp10 = per_change(avg_price[-31], avg_price[-21])

    cp11 = per_change(avg_price[-31], avg_price[-20])
    cp12 = per_change(avg_price[-31], avg_price[-19])
    cp13 = per_change(avg_price[-31], avg_price[-18])
    cp14 = per_change(avg_price[-31], avg_price[-17])
    cp15 = per_change(avg_price[-31], avg_price[-16])
    cp16 = per_change(avg_price[-31], avg_price[-15])
    cp17 = per_change(avg_price[-31], avg_price[-14])
    cp18 = per_change(avg_price[-31], avg_price[-13])
    cp19 = per_change(avg_price[-31], avg_price[-12])
    cp20 = per_change(avg_price[-31], avg_price[-11])

    cp21 = per_change(avg_price[-31], avg_price[-10])
    cp22 = per_change(avg_price[-31], avg_price[-9])
    cp23 = per_change(avg_price[-31], avg_price[-8])
    cp24 = per_change(avg_price[-31], avg_price[-7])
    cp25 = per_change(avg_price[-31], avg_price[-6])
    cp26 = per_change(avg_price[-31], avg_price[-5])
    cp27 = per_change(avg_price[-31], avg_price[-4])
    cp28 = per_change(avg_price[-31], avg_price[-3])
    cp29 = per_change(avg_price[-31], avg_price[-2])
    cp30 = per_change(avg_price[-31], avg_price[-1])

    pattern_for_rec_arr.append(cp1)
    pattern_for_rec_arr.append(cp2)
    pattern_for_rec_arr.append(cp3)
    pattern_for_rec_arr.append(cp4)
    pattern_for_rec_arr.append(cp5)
    pattern_for_rec_arr.append(cp6)
    pattern_for_rec_arr.append(cp7)
    pattern_for_rec_arr.append(cp8)
    pattern_for_rec_arr.append(cp9)
    pattern_for_rec_arr.append(cp10)

    pattern_for_rec_arr.append(cp11)
    pattern_for_rec_arr.append(cp12)
    pattern_for_rec_arr.append(cp13)
    pattern_for_rec_arr.append(cp14)
    pattern_for_rec_arr.append(cp15)
    pattern_for_rec_arr.append(cp16)
    pattern_for_rec_arr.append(cp17)
    pattern_for_rec_arr.append(cp18)
    pattern_for_rec_arr.append(cp19)
    pattern_for_rec_arr.append(cp20)

    pattern_for_rec_arr.append(cp21)
    pattern_for_rec_arr.append(cp22)
    pattern_for_rec_arr.append(cp23)
    pattern_for_rec_arr.append(cp24)
    pattern_for_rec_arr.append(cp25)
    pattern_for_rec_arr.append(cp26)
    pattern_for_rec_arr.append(cp27)
    pattern_for_rec_arr.append(cp28)
    pattern_for_rec_arr.append(cp29)
    pattern_for_rec_arr.append(cp30)

def path_finder():  #find patterns similar to the current one

    matches =[]     #similar patterns

    for pattern in pattern_arr:

        sim1 = 100.00 - abs(per_change(pattern[0],pattern_for_rec_arr[0]))
        sim2 = 100.00 - abs(per_change(pattern[1], pattern_for_rec_arr[1]))
        sim3 = 100.00 - abs(per_change(pattern[2], pattern_for_rec_arr[2]))
        sim4 = 100.00 - abs(per_change(pattern[3], pattern_for_rec_arr[3]))
        sim5 = 100.00 - abs(per_change(pattern[4], pattern_for_rec_arr[4]))
        sim6 = 100.00 - abs(per_change(pattern[5], pattern_for_rec_arr[5]))
        sim7 = 100.00 - abs(per_change(pattern[6], pattern_for_rec_arr[6]))
        sim8 = 100.00 - abs(per_change(pattern[7], pattern_for_rec_arr[7]))
        sim9 = 100.00 - abs(per_change(pattern[8], pattern_for_rec_arr[8]))
        sim10 = 100.00 - abs(per_change(pattern[9], pattern_for_rec_arr[9]))

        sim11 = 100.00 - abs(per_change(pattern[10], pattern_for_rec_arr[10]))
        sim12 = 100.00 - abs(per_change(pattern[11], pattern_for_rec_arr[11]))
        sim13 = 100.00 - abs(per_change(pattern[12], pattern_for_rec_arr[12]))
        sim14 = 100.00 - abs(per_change(pattern[13], pattern_for_rec_arr[13]))
        sim15 = 100.00 - abs(per_change(pattern[14], pattern_for_rec_arr[14]))
        sim16 = 100.00 - abs(per_change(pattern[15], pattern_for_rec_arr[15]))
        sim17 = 100.00 - abs(per_change(pattern[16], pattern_for_rec_arr[16]))
        sim18 = 100.00 - abs(per_change(pattern[17], pattern_for_rec_arr[17]))
        sim19 = 100.00 - abs(per_change(pattern[18], pattern_for_rec_arr[18]))
        sim20 = 100.00 - abs(per_change(pattern[19], pattern_for_rec_arr[19]))

        sim21 = 100.00 - abs(per_change(pattern[20], pattern_for_rec_arr[20]))
        sim22 = 100.00 - abs(per_change(pattern[21], pattern_for_rec_arr[21]))
        sim23 = 100.00 - abs(per_change(pattern[22], pattern_for_rec_arr[22]))
        sim24 = 100.00 - abs(per_change(pattern[23], pattern_for_rec_arr[23]))
        sim25 = 100.00 - abs(per_change(pattern[24], pattern_for_rec_arr[24]))
        sim26 = 100.00 - abs(per_change(pattern[25], pattern_for_rec_arr[25]))
        sim27 = 100.00 - abs(per_change(pattern[26], pattern_for_rec_arr[26]))
        sim28 = 100.00 - abs(per_change(pattern[27], pattern_for_rec_arr[27]))
        sim29 = 100.00 - abs(per_change(pattern[28], pattern_for_rec_arr[28]))
        sim30 = 100.00 - abs(per_change(pattern[29], pattern_for_rec_arr[29]))

        is_sim = (sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+sim11+sim12+sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+
                  sim21+sim22+sim23+sim24+sim25+sim26+sim27+sim28+sim29+sim30) / 30.00

        if is_sim > 60:     #75% similarity
            ix =pattern_arr.index(pattern)

            print("--------------------------------------------------")
            print("Current pattern:",pattern_for_rec_arr)
            print("--------------------------------------------------")
            print("Matched pattern:",pattern,"- appending to matched patterns array...")
            print("-------------------------")
            print("Future outcome of matched pattern:",perf_arr[ix])
            print("--------------------------------------------------\n\n")

            xaxis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28,
                     29, 30]

            matches.append(pattern)

    fig = plt.figure(figsize=(10, 6))

    if(len(matches)==0):
        print("No matching patterns found")
        return False

    print("Number of matched patterns:",len(matches))

    for match in matches:

        future = pattern_arr.index(match)       # indexes of matched patterns in main pattern array, to use in perf_arr (performance array)
                                                # as they have (see line 131) identical length (the same index in pattern_arr and perf_arr is (pattern -> its' "future" value) "pair")

        if perf_arr[future] > pattern_for_rec_arr[29]:

            pcolor = '#24bc00'
            preds.append(perf_arr[future])

        else:
            pcolor = '#d40000'
            preds.append(perf_arr[future])

        plt.plot(xaxis, match)          # plot matched pattern
        plt.scatter(35, perf_arr[future], c=pcolor, alpha=.4)   # outcome of this (^) match, green dot - long, red - short , repeat loop for another match


    plt.plot(xaxis, pattern_for_rec_arr, '#54fff7', linewidth=3)    # current (last) pattern - dataset[-30:]
    plt.grid(True)

    predsAvgOutcome = reduce(lambda x, y: x + y, preds) / len(preds)    # avg val of matches' outcomes, blueish dot, most possible predict for current pattern

    if(predsAvgOutcome > pattern_for_rec_arr[29] * 1.001):

        print("Advice - execute trade LONG")

    elif(predsAvgOutcome < pattern_for_rec_arr[29] * 0.999):

        print("Advice - execute trade SHORT")

    plt.scatter(37, predsAvgOutcome, c='#008db8', s=25)
    plt.show()


def graph_raw():

    figure = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40) ,(0,0) ,colspan=40, rowspan=40)

    ax1.plot(date,open)
    ax1.plot(date,close)

    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(60)

    ax1_2 = ax1.twinx()
    ax1_2.fill_between(date,0,(open-close),facecolor='g',alpha=.3)


    plt.subplots_adjust(bottom=.23)

    plt.grid(True)
    plt.show()

while(True):
    path_store()
    curr_patt()
    path_finder()
    
    print("Pattern arr: ",len(pattern_arr))
    print("for rec arr: ",len(pattern_for_rec_arr))
    print("perf_arr : ", len(perf_arr))
    print("preds: ", len(preds))
    pattern_for_rec_arr = []
    time.sleep(60)       #change to 60 in real-time pred
    

