# Put the Food In Recreation
# © 2025 DenCodez
import builds
import time as t
print("Put the Food In! (Recreation)")
t.sleep(2)
print("Loading some dumb assets, may take a few seconds.")

# Asset loader
loadassets = builds.assetloads()
t.sleep(10)

print("Your fridge:",builds.Fridge)
print("Goal: You have to fit 10 items.")

shop = input("Type 'Start' ")

# GAME START
large_beef = input("Would you like to buy and fit in a LARGE beef? ($20) ")
if large_beef == "Yes" or large_beef == "yes":
    print("Removing Skibidi toilet plushie extra large...")
    t.sleep(4)
    builds.Fridge.pop(2)
    builds.Fridge.append("LARGE Beef")

    print(builds.Fridge)
    t.sleep(0.45)
    Astronaut = input("Do you want to fit an astronaut, you are a psycho if you type yes. ")
    if Astronaut == "Yes" or Astronaut == "yes":
        print("I mean they will still survive for some days.")
        print("Removing c00lkidd...")
        builds.Fridge.pop(1)
        builds.Fridge.append("Astronaut")
        t.sleep(2)
        print(builds.Fridge)
        print("YOU ARE STILL A PSYCHO-")
        print("Ok, next one is...")
        t.sleep(4)
        space_ahhgalaxy = input("Would you like to fit the entire milky way galaxy into your fridge? ")
        if space_ahhgalaxy == "Yes" or space_ahhgalaxy == "yes":
            print("WHAT ARE YOU PLOTTING ABOUT-")
            t.sleep(.2)
            print("Game over, you lost.")
        elif space_ahhgalaxy == "no" or space_ahhgalaxy == "No":
            print("You are not weird, confirmed.")
            t.sleep(3)
            scp_67_2 = input("Would you like to store SCP-067_2? ")
            if scp_67_2 == "yes" or scp_67_2 == "Yes":
                print("You really wanna scream 67 2 every second, eh? YOU LOST, 67 KID.")
            elif scp_67_2 == "no" or scp_67_2 == "No":
                print("Same man, I don't wanna hear 67 every single second.")
                t.sleep(2)
                remove_67 = input("So you wanna remove SCP_067 from your fridge? Idk who put that. ")
                if remove_67 == "Yes" or remove_67 == "yes":
                    print("You are not a 67 fan, good. Removing...")
                    builds.Fridge.remove("SCP-067")
                    t.sleep(1)
                    print("Done, fridge:",builds.Fridge)
                    t.sleep(3)
                    store_cloud = input("Would you like to store the whole cloud database? ")
                    if store_cloud == "Yes" or store_cloud == "yes":
                        print("Storing...")
                        t.sleep(4)
                        builds.Fridge.append("Cloud Database")
                        print(builds.Fridge)
                        print("How could you even fit that in there-")
                        t.sleep(3)
                        print("Ok whatever, this is the end of this. More stuff coming soon.")
                    elif store_cloud == "No" or store_cloud == "no":
                        print("You could've stored it, you lost!")
                elif remove_67 == "No" or remove_67 == "no":
                    print("I am speechless.")
                    exit()
                elif remove_67 == "67!" or remove_67 == "67":
                    quit()
    elif Astronaut == "no" or Astronaut == "No":
        print("Cool, but you lost.")
elif large_beef == "no" or large_beef == "No":
    print("Uh I guess that works.")
    dog = input("Would you like to fit in a living medium sized dog?")
    if dog == "yes" or dog == "Yes":
        print('You wanna kill an animal by freezing it to death? Nah.')
        t.sleep(5)
        print("LOSER!")
    elif dog == "no" or dog == "No":
        print("You have a soul and some kindness.\nPART IS STILL W.I.P, COMING SOON.")
        # COMING SOON
else:
    print("Invalid one bro-")