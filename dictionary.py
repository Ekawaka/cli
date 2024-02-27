# dictionary -> data structure that allows you to store data in a key-value format

#words = {"city": "Big town with a population of over 5 million",
        #"continent": "A geographical location the size of over 1M square"}
#print(words["city"])
#print (words.get["city"])

#words["continent"] = "fjjuiloklk mokjukkjj mokjgt"
#print(words["continent"])


#print(words.keys())
#print(words.value())

#new_words ={}









# challenge: write a python function called create_word() that creates an empty dictionary. create another function 
# called add_word() that adds words in key_value pairs to the empty dictionary created above

# function 
def create_word ():
    empty_dict = {}
    return empty_dict
print(create_word())

def add_word():
    new_dict = create_word().update(words)
    return new_dict 

def add_word():
    dictionary = create_word().update(words)
    dictionary.update(words)
    return dictionary

print(add_word)

