import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
np.random.seed(10)

minutes = np.array([1,1,1,1,2,1,2,1,3,0,1,0,1,2,1,1,0,2,2,1,1,1,2,2,1,2\
                   ,1,2,4,1,2,3,1,1,2,1,2,1,1,1,1,1,1,2,2,2,2,1,1,1,1\
                       ,3,2,3,1])
seconds = np.array([31,35,21,16,43,31,59,42,17,42,20,38,59,9,30,45,57,\
                    6,59,43,42,24,4,21,50,59,23,24,18,\
                        35,32,46,26,35,42,56,47,34,50,41,42,\
                            51,3,8,21,47,52,55,51,54,1,15,11,49,8])
min_to_sec = minutes*60

total_seconds = min_to_sec+seconds

total_minutes = total_seconds/60

df = pd.DataFrame()
df['Train_type'] = [1,1,0,1,0,0,0,1]
t_minutes = np.array([4,2,2,5,3,3,3,5])
t_seconds = np.array([0,40,58,30,15,0,0,50])
t_min_to_sec = t_minutes*60
t_total_seconds = t_min_to_sec+t_seconds
t_total_minutes = t_total_seconds/60
df['min_to_arrive'] = t_total_minutes

bts_cond = np.empty(1000)
bts_non_cond = np.empty(1000)
for i in range(1000):
    t_sample = np.random.choice(df['Train_type'],size=1000)
    cond_train = t_sample[:350]
    non_cond = t_sample[350:]
    cond_num = sum(cond_train)
    non_cond_num = len(non_cond)-sum(non_cond)
    bts_cond[i]=cond_num/(cond_num+non_cond_num)
    bts_non_cond[i] = non_cond_num/(cond_num+non_cond_num)

#now that we are sure that 35% of the trains that pass in the timeline are air-conditioned

#is this mean& median Due to chance?
#Null Hypothesis is that the mean of the observed data is the True mean, The alternative hypothesis says no.
bts_mean = np.empty(1000)
bts_median= np.empty(1000)

for i in range(1000):
    means = np.mean(np.random.choice(total_minutes,size=len(total_minutes)))
    bts_mean[i] = means
for i in range(1000):
    medians = np.median(np.random.choice(total_minutes,size=len(total_minutes)))
    bts_median[i] = medians
    
    
sample_mean = np.mean(bts_mean)
hyp_mean = np.mean(total_minutes)
std_err = np.std(bts_mean,ddof=1)
z_score = (hyp_mean-sample_mean)/std_err
p_val = 1-norm.cdf(z_score)

print(p_val)

#Hypothesis tests Suggests that the observed values are actually not due to random chance!

trains = int(input("عاوز تسافر كام محطه؟\n"))
transition_station = input("\n True\False هتعدي علي محطات انتقاليه؟\n")
    
if trains <18 and transition_station is not True:
    print(f"الوقت المقدر لكل رحله من{np.percentile(bts_median,[2.5,97.5])[0]} الي {np.percentile(bts_median,[2.5,97.5])[1]} دقيقه")
    print(f"الوقت المقدر للوصول الي وجهتك يتأرجح بين {np.percentile(bts_median,[2.5,97.5])[0]*trains} دقيقه الي {np.percentile(bts_median,[2.5,97.5])[1]*trains} دقيقه")
    print(f"لو انت لسه داخل المترو حالا احتمال انك تلاقي عربيه مكيفه هو {np.percentile(bts_median,[2.5,97.5])[0]/20*100}% الي : {np.percentile(bts_median,[2.5,97.5])[1]/20*100}%")
else:
    print(f"الوقت المقدر لكل رحله من {np.percentile(bts_mean,[2.5,97.5])[0]} الي {np.percentile(bts_mean,[2.5,97.5])[1]} دقيقه")
    print(f"الوقت المقدر للوصول الي وجهتك يتأرجح بين {np.percentile(bts_mean,[2.5,97.5])[0]*trains} دقيقه الي {np.percentile(bts_mean,[2.5,97.5])[1]*trains} دقيقه")
    print(f"لو انت لسه داخل المترو حالااحتمال انك تلاقي عربيه مكيفه هو %{np.percentile(bts_mean,[2.5,97.5])[0]/20*100} الي : %{np.percentile(bts_mean,[2.5,97.5])[1]/20*100}")

fig,ax = plt.subplots(figsize=(15,10))

#since we now know what the Mean time of travelling from a to b is
#we can perform poisson distribution.

def cdf(data):
    x = np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)
    return x,y

pois = np.random.poisson(np.mean([1.833,2.232]),size=10000)

x,y = cdf(pois)

arrowprops = dict(
    arrowstyle = "->",
    connectionstyle = "angle, angleA = 0, angleB = 90,\
    rad = 10")

_=ax.plot(x,y,marker='.',linestyle='none')
_=plt.title("Poission Distribution ECDF for the posssible averages of trip duration")
ax.annotate("As you can see most of the time our average is from 1.833 to 2.23",
            (2.23,0.5),(4,0.2),
            arrowprops= arrowprops)
plt.show()


