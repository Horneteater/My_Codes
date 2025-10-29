

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


pd.set_option('future.no_silent_downcasting', True)



url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"


columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df = pd.read_csv(url, names=columns)



d={ 'low' : -1 , 'med' : 0 , 'high' :1 , 'vhigh' : 2 , '5more' : 5 , 'small' : -1 , 'big' : 1 ,'more' : 5 , 'unacc' : -1 , 'acc' : 0 , 'good' : 1 , 'vgood' : 2}


df=df.replace(d)
df=df.astype(int)


features = ['maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

x=df[features]
y=df['buying']


dtree = DecisionTreeClassifier()
dtree = dtree.fit(x , y)

data=pd.DataFrame([[2,2,2,-1,-1,-1]],columns=features)

pred=dtree.predict(data)

if pred == -1 :
	f='low'
elif pred == 0 :
	f='medium'
elif pred == 1 :
	f = 'high'
elif pred == 2 :
	f= 'very high'
else :
	f = '{invalid}'

f1=f"the buying price range for this car is {f}"

print(f1)





