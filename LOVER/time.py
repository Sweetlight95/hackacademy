import datetime
import random

print("This is Queen Adesuwa. What question do you want to answer today?")

love = ["Yes, I love you!", "No, I don't love you", "What is love?", "Love is wicked"]
age = [num for num in range(1, 100)]
eat = ["No, I haven't", "Yeah, I have had breakfast", "Yeah, I had eba and egusi", "No, I am fasting."]
relationships = ["Wow, even the gods do not know.", "Yes, I am single", "Yes, I am in a relationship", "It is complicated"]

while True:
    question = input()
    if "time" in question:
        print("The time of day is:", datetime.datetime.now().time())
    elif "name" in question:
        print("My name is Adesuwa, How can I help you?")
    elif "old" in question or "age" in question:
        print("I am", random.choice(age), "years old.")
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "single" in question or 'relationships' in question:
        print(random.choice(relationshops))
    elif "break" in question:
        print("seems you want to break up, Bpy Bye!")
        break
    else:
        print("I don't understand you. Do you mind asking another question?")
                            


#question = input().split()
#print(question)
#if "time" in question:
#    print("The time of day is:", datetime.datetime.now().time())
#else:
#    print("I don't understand you, Do you mean 'what is the time of the day?'")