#import stuff
#you need to install selenium and uszipcode
import time
import sys
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import chromedriver_binary
driver = webdriver.Chrome()
from uszipcode import ZipcodeSearchEngine
zcdb = ZipCodeDatabase()

#get user input
zipcode = input("Town zip code: ")
if town.isdigit() == False:
  sys.exit()
cityName = zipcode.city

gym = input("Do you have a membership to a gym that you use regularly? Y/N: ")
while gym.lower() != 'y' or 'n':
  print('Invalid Input')
  gym = input("Do you have a membership to a gym that you use regularly? Y/N: ")

if gym.lower() == 'y':
  gymBool = True
if gym.lower() == 'n':
  gymBool = False

if gymBool == False:
  print("Okay, first things first we need to help you get a membership and/or some equipment.")
  print("Do you have an extra $50 you can spare every month? Y/N")
  afford = input(": ")
  while afford.lower() != 'y' or 'n':
    print('Invalid input.')
    print("Okay, first things first we need to help you get a membership and/or some equipment.")
    print("Do you have an extra $50 you can spare every month? Y/N")
    afford = input(": ")
  if afford.lower() == 'y':
    print('Okay, searching for gyms near your area..')
    que=driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys("Gyms near " + cityName)
    que.send_keys(Keys.RETURN)  
    inShape = False
  if afford.lower() == 'n':
    print("That's okay, we can still get you some equipment to use at home.")
    driver.get('https://www.amazon.com/Best-Home-Workout-Equipment/s?k=Best+Home+Workout+Equipment')
    inShape = False
if gymBool == True:
  print("What goal do you hope to reach by going to the gym?")
  print("\tA) Body Build")
  print("\tB) Get in shape/lose weight")
  print("\tC) Stay in shape")
  print("\tD) Gain muscle/definition")
  purpose = input(": ")
while purpose.lower() != 'a' or 'b' or 'c' or 'd':
  print('Invalid input')
  print("What goal do you hope to reach by going to the gym?")
  print("\tA) Body Build")
  print("\tB) Get in shape/lose weight")
  print("\tC) Stay in shape")
  print("\tD) Gain muscle/definition")
  purpose = input(": ")

if purpose.lower() == 'a':
  print("Okay, you are a bodybuilder.")
  print("Consider drinking protein shakes to gain more mass.")
  driver.get("https://www.amazon.com/Best-Sellers-Grocery-Gourmet-Food-Protein-Drinks/zgbs/grocery/5782436011")
  print('This program is not intended for people that are already in shape. Sorry, have a nice day :)')
  inShape = True
if purpose.lower() == 'b':
  print('So you need to get in shape. We can help you with that!')
  inShape = False
if purpose.lower() == 'c':
  print('We can help you stay in shape!')
  inShape = False
if purpose.lower() == 'd':
  print('We can help you with that!')
  inShape = True
time.sleep(3)
print(chr(27) + "[2J")

#giant while loop
while True:
  if inShape == True:
    print('Welcome! Congratulations on being in shape! You can choose what you want to do next: ')
    print('\tA) Find great workouts!')
    print('\tB) Protein Shakes')
    print('\tC) Diet')
    inShapeChoice = input(': ')
  if inShapeChoice.lower() != 'a' or 'b' or 'c':
    continue
  if inShapeChoice.lower() == 'a':
    print('Here are some muscle-demanding workouts that you can implement in your routine:')
    print('\tA) Leg Day')
    print('\tB) Arms')
    print('\tC) Core')
    print('\tD) Back')
    print('\tE) Exit')
    inShapeWorkout = input(': ')
  while inShapeWorkout.lower() != 'a' or 'b' or 'c' or 'd' or 'e':
    print('Invalid Input')
    print('Here are some muscle-demanding workouts that you can implement in your routine:')
    print('\tA) Leg Day')
    print('\tB) Arms')
    print('\tC) Core')
    print('\tD) Back')
    print('\tE) Exit')
    inShapeWorkout = input(': ')
  if inShapeWorkout.lower() == 'a':
    driver.get('https://www.youtube.com/watch?v=GfAlPURwcVI')
    continue
  if inShapeWorkout.lower() == 'b':
    driver.get('https://www.youtube.com/watch?v=te9cDgeql70')
    continue
  if inShapeWorkout.lower() == 'c':
    driver.get('https://www.youtube.com/watch?v=dJlFmxiL11s')
    continue
  if inShapeWorkout.lower() == 'd':
    driver.get('https://www.youtube.com/watch?v=lA7dbOmxs5I')
    continue
  if inShapeWorkout.lower() == 'e':
    continue
  if inShapeChoice.lower() == 'b':
    print('Protein Shakes give you mass that can be molded into solid muscle. Here are some well known protein shake brands: ')
    print('\tA) Ensure')
    print('\tB) SIS')
    print('\tC) KIN')
    print('\tD) Optimim Nutrition')
    print('\tE) Sales and deals')
    print('\tF) Exit')
    proteinChoice = input(': ')
  while proteinChoice.lower() != 'a' or 'b' or 'c' or 'd' or 'e' or 'f':
    print('Invalid Input')
    print('Protein Shakes give you mass that can be molded into solid muscle. Here are some well known protein shake brands: ')
    print('\tA) Ensure')
    print('\tB) SIS')
    print('\tC) KIN')
    print('\tD) Optimim Nutrition')
    print('\tE) Sales and deals')
    print('\tF) Exit')
    proteinChoice = input(': ')
  if proteinChoice.lower() == 'a':
    driver.get('https://ensure.com/')
    continue
  if proteinChoice.lower() == 'b':
    driver.get('https://www.scienceinsport.com/us/shop-sis/protein-range')
    continue
  if proteinChoice.lower() == 'c':
    driver.get('https://kin-nutrition.com/')
    continue
  if proteinChoice.lower() == 'd':
    driver.get('https://www.optimumnutrition.com/en-us')
    continue
  if proteinChoice.lower() == 'e':
    driver.get('https://www.amazon.com/Best-Sellers-Grocery-Gourmet-Food-Protein-Drinks/zgbs/grocery/5782436011')
    continue
  if proteinChoice.lower() == 'f':
    continue
  if inShapeChoice.lower() == 'c':
    print('People looking to gain muscle must eat lots of protein but should also watch what they eat as to not gain too much bad fats.')
    print('Here are some foods that you should be eating: ')
    driver.get('https://www.bodybuilding.com/content/meal-plan-for-every-guy.html')
    continue
  if inShape == False:
    print('You may be comfortable where you are now, but you can go further! Here, you can choose what you want to do next to help acheive your goal!')
    print('\tA) How often should I be working out and for how long?')
    print('\tB) Am I really in good shape? (BMI)')
    print('\tC) Diet')
    print('\tD) Workouts')
    notInShape = input(': ')
  if notInShapeChoice.lower() != 'a' or 'b' or 'c' or 'd':
    print('Invalid input')
    continue
  if notInShapeChoice.lower() == 'a':
    print("Good question! First I'll be needing your age: ")
    age = int(input(': '))
    if age <= 12:
      print("As a kid, you should be running around for about an hour every day. The fact that you're probably getting enough exercise as is.")
    if age > 12 and age < 20:
      print("You are around the age where people begin to look at their external image. You should strive to start gaining muscle tone and definition. You should be going to the gym around 3-4 times per week for about an hour and a half.")
    if age >= 20 and age < 29:
      print("Your body is probably in its prime, I hate to break it to you. You should be exercising for 30 minutes a day, five times a week. ")
    if age >= 30 and age < 39:
      print("Your body has begun deteriorating! You should be exercising for 30 minutes, five times a week. Try jogging or swimming as those will keep you well rounded.")
    if age >= 40 and age < 49:
      print("In this stage of your life, it is ESSENTIAL for you to be working out if you plan to have a long life. Your muscles are losing mass and your weight will increase. You should be working out 45 minutes to an hour for 3-5 times a week.") 
    if age >= 50 and age < 59:
      print("Welcome to the midpoint of your life! You may have aches and pains but thats okay, adjust your workout to be a less intense bike, swim, or jog. Make sure your working on your core, check the exercise tab after this to find out how!")
    if age >= 60 and age < 69:
      print("You're old now. Its a fact, but that's okay. You should be exercising 2-3 times a week for 30 minutes. Stay safe!")
    if age <= 70:
      print("Good job on surviving! You have a decent chance at living a long life. You should be exercising 2-3 times a week for 30 minutes. Usually just stretch and take a walk, if you can.")
    continue
  if notInShapeChoice.lower() == 'b':
    print("To find out whether you are really in shape, I'll need your weight(lbs) and height(in).")
    weight = int(input('What is your weight in LBS: '))
    weight = weight * 0.453592
    height = int(input('What is your height in INCHES: '))
    height = height * 0.0254
    bmi = weight/(height**2)
    print('Here is your BMI: ' + bmi)
    if bmi < 19:
      print("You're pretty underweight, you should probably be eating more.")
    if bmi >= 19 and bmi < 24:
      print("You're in a good weight range, keep it up!")
    if bmi >= 25 and bmi < 29:
      print("You're a little overweight, consider dieting. Don't know how? Check out our diet tab!")
    if bmi >= 30 and bmi < 39:
      print("You are obese, consider going on a diet by going to our diet tab before its to late!")
    if bmi >= 40:
      print("Okay, you are excessively obese, you should get treatment, here's a link. ")
      driver.get('https://www.google.com/search?q=hospitals+near+me&rlz=1CAJIKU_enUS884&oq=hospitals+near+me&aqs=chrome..69i57j0i402j0l2j0i131i433j0l3.2903j0j7&sourceid=chrome&ie=UTF-8')
    continue
  if notInShapeChoice.lower() == 'c':
    print("Here are some healthy, somewhat good tasting foods you can eat to get/stay in shape!")
    driver.get('https://www.shape.com/healthy-eating/healthy-drinks/4-smoothie-recipes-weight-loss')
    continue
  if notInShapeCHoice.lower() == 'd':
    print("Since your goal is to stay or get in shape, the workouts will not be as concentrated on a specific area of your body compared to a bodybuilder's workout.")
    print("With covid, I am sure that you have to stay home, which is why this workout helps: ")
    driver.get('https://blog.swim.com/covid-19-easy-ways-to-stay-in-shape-at-home/')
    continue
  


