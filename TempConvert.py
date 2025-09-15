#TempConvert.py
#Name: Macy Dube
#Date: 9/14/2025 m  
#Assignment: Lab 3 Temp Convert


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter a Temperature in Fahrenheit: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (tempF - 32) * 5 / 9
  tempC = round(tempC, 1)
  #Output converted temperature.
  
  print(tempF, "degrees fahrenheit is", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
