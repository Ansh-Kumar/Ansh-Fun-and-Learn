rainy = input("How is the weather? Is it raining?  (y/n)").lower()
cold = input("Is it cold outside? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):
    print("You should wear something extra warm and take an umbrella.")
elif (rainy == 'y' and cold != 'y'):
    print("Just take an umbrella.")
elif (rainy != 'y' and cold == 'y'):
    print("Take something warm")
elif(rainy != 'y' and cold != 'y'):
    print("Wear anything you want")
    
