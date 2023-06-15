cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
keep_looping = True 
while keep_looping == True:
 user_input = input("Enter a city, or q to quit:")
 if user_input != "q":
  for a_clean_city in cleanest_cities:
    if user_input == a_clean_city:
     print("It's one of the cleanest cities")
 break
 else:
   keep_looping = False
