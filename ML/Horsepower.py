

from scipy.stats import linregress
import pandas as pd
import numpy as np




def predict(x_arr,y_arr,X):
	m,b,r,p,std_err=linregress(x_arr,y_arr)
	pred=((m*X)+b) #the y we predict
	if -0.7 < r < 0.7 :
		return "weak data correlation"
	significance=0.05
	if p > 0.05:
		return "insignificant linear relationship"
	return pred
	
	
url = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"

df = pd.read_csv(url)		


x=df['mpg'].to_numpy() #miles per gallon
y=df['hp'].to_numpy() #horsepower
z=float(input("miles per gallon :   ")) # our x is miles per gallon to predict horsepower
				
p=predict(x,y,z) #our y is horsepower
f=f"predicted horsepower is {p}"	
print(f)