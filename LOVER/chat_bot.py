database = {
   "boy": ["I am a boy", "I am not a girl", "I like girls", "I want to fly",],
   "girl": ["I am not a boy", "I am a girl", "I like boys", "I want to fly",],
   "iron": ["I sharpen my mate", "I don't break, I bend", "I detest fire", "I melt for you",],
   "thunder": ["thunder never strike twice", "I am a god and I never answer to no man", "Sango is your producer", "I want to fly",],
}

print("Hi, I am Alexis. What can I answer for you today?")

while True:
    sentence = input().split()
    
    if ['exit'] == sentence:
        print("Exiting...")
        break
    
    options = []
    
    for word in sentence:
        word = word.lower()
        if word in database.keys():
            options.append(random.choice(database[word]))
        if options:
            print(random.choice(option))
        else:
            print("No Match. Ask another question.")