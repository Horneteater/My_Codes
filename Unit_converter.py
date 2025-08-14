

#python unit converter
#convert imperial to metric

from decimal import Decimal


select=str(input("1 for km to mile conversion , 2 for Fahrenheit and celsius to kelvin conversion, 3 for pound to kilogram conversion"))


#converting mile to kilometers
#target unit is km
# 1km==0.6214 miles

if select=="1":

  mile=Decimal(input("select distance in miles? "))
 
  km=Decimal("0.6214*mile")

  meter=km*1000
  
  meter_convert=f"{mile} miles is {meter} meters"

  print(meter_convert)
  
  #temperature conversion
  #kelvin=Celsius+273.15
  #kelvin=(farenheit-32)*5/9+273.15

if select=="2":
  unit_temp=str(input("clesius or fahrenheit?  ")).lower()
  if unit_temp=="celsius" :
    celsius=Decimal(input('degree of clesius?  '))
  
   
    kelvin_c=celcius+Decimal(273.15)
    kelvin_c_convert=f"{celsius} celsius is {kelvin_c} kelvin"
    print(kelvin_c_convert)
  elif unit_temp=="fahrenheit":
    fahrenheit=Decimal(input("degree of fahrenheit?  "))
    kelvin_f=((fahrenheit-32)*5/9+Decimal(273.15))
    kelvin_f_convert=f"{farenheit} farenheit is {kelvin_f} kelvin"
    print(kelvin_f_convert)
    
    
   #now pound to kilo
   
if select=="3":
  	pound=float(input("select weight in pounds?  "))
  	kilogram=pound*0.453592
  	kilogram_convert=f"{pound} pound is {kilogram} kilograms"
  	print(kilogram_convert)
  	
  	
	
	



