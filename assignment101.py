#Emily Tao
#assignment 10.1
#In this assignment, we will be implementing our own custom class based on a real-world object, in this case, an iphone.

#ACKNOWLEDGMENTS
#phone_price_dict: I used https://mashable.com/article/size-and-price-of-every-iphone-ever-released to see the prices of iphones.
#find_phone_storage code: I used https://pythonexamples.org/python-if-or/#4 to see how to use or operators in if...elif statements.
    #I also used https://www.bankmycell.com/blog/how-to-check-storage-on-iphone/ to see how much storage each iphone model has.
#main(): I received inspiration from https://thispointer.com/python-how-to-find-all-indexes-of-an-item-in-a-list/ to see how to index
    #items in a list (although I ended up not using this information)

import random
import time

class Phone:
    screen = True
    def __init__(self, price, storage):
        self.__price = price
        self.__storage = storage

    def set_price(self, price):
        #changes the price of the phone
        if price < 0:
            #the price cannot be less than $0
            print("The price cannot be negative.")
        else:
            self.__price = price
        return self.__price

    def get_price(self):
        #get the price
        return self.__price

    def set_storage(self, storage):
        #changes the phone's storage capacity (in GB); takes in storage size (an int) as an argument and returns the storage size
        if storage == 8:
            self.__storage = storage
        elif storage == 16:
            self.__storage = storage
        elif storage == 32:
            self.__storage = storage
        elif storage == 64:
            self.__storage = storage
        elif storage == 128:
            self.__storage = storage  
        elif storage == 256:
            self.__storage = storage
        elif storage == 512:
            self.__storage = storage 
        else:
            print("The storage size is not valid.")
        return self.__storage

    def get_storage(self):
        #get the storage size
        return self.__storage

    def phone_price_dict(self):
        #takes in only self as an argument; returns a dictionary where the iphone models are the keys and prices are the values
        prices = {
            'IPHONE': 499,
            'IPHONE 3G': 499,
            'IPHONE 3GS': 599, 
            'IPHONE 4': 649, 
            'IPHONE 5C': 549,
            'IPHONE 4S': 649,#5
            'IPHONE 5': 649, 
            'IPHONE 5S': 649,
            'IPHONE SE': 399,
            'IPHONE 6': 649, 
            'IPHONE 6+': 749, #10
            'IPHONE 6S': 649,
            'IPHONE 6S+': 749,
            'IPHONE 7': 649,
            'IPHONE 7+': 769, 
            'IPHONE 8': 699, #15
            'IPHONE 8+': 799,
            'IPHONE X': 999,
            'IPHONE XR': 749,
            'IPHONE XS': 999,
            'IPHONE XS MAX': 1099, #20
            'IPHONE 11': 699,
            'IPHONE 11 PRO': 999,
            'IPHONE 11 PRO MAX': 1099,
            'IPHONE SE 2ND GEN': 399,
            'IPHONE 12': 799, #25
            'IPHONE 12 MINI': 699,
            'IPHONE 12 PRO': 999,
            'IPHONE 12 PRO MAX': 1099,
            }
        return prices

    def phone_storage_dict(self):
        #takes in only self as an argument; returns a dictionary where the iphone models are the keys and list of
        #storage sizes are the values
        conversion = {
            'IPHONE': [4, 8, 16],
            'IPHONE 3G': [8, 16],
            'IPHONE 3GS': [8, 16, 32], 
            'IPHONE 4': [8, 16, 32], 
            'IPHONE 5C': [8, 16, 32],
            'IPHONE 4S': [8, 16, 32, 64], #5
            'IPHONE 5': [16, 32, 64],
            'IPHONE 5S': [16, 32, 64],
            'IPHONE SE': [16, 32, 64, 128],
            'IPHONE 6': [16, 32, 64, 128], 
            'IPHONE 6+': [16, 32, 64, 128], #10
            'IPHONE 6S': [16, 32, 64, 128],
            'IPHONE 6S+': [16, 32, 64, 128],
            'IPHONE 7': [32, 128, 256],
            'IPHONE 7+': [32, 128, 256], 
            'IPHONE 8': [64, 128, 256], #15
            'IPHONE 8+': [64, 128, 256],
            'IPHONE X': [64, 256],
            'IPHONE XR': [64, 128, 256],
            'IPHONE XS': [64, 256, 512],
            'IPHONE XS MAX': [64, 256, 512], #20
            'IPHONE 11': [64, 128, 256],
            'IPHONE 11 PRO': [128, 256, 512],
            'IPHONE 11 PRO MAX': [128, 256, 512],
            'IPHONE SE 2ND GEN': [64, 128, 256],
            'IPHONE 12': [64, 128, 256], #25
            'IPHONE 12 MINI': [64, 128, 256],
            'IPHONE 12 PRO': [128, 256, 512],
            'IPHONE 12 PRO MAX': [128, 256, 512],
            }
        return conversion

    def find_phone_storage(self, phonemodel):
        #takes in a string of the iphone model; returns the iphone model's storage size options
        #change the string to be all uppercase 
        key = phonemodel.upper()
        conversion = {
            'IPHONE': [4, 8, 16],
            'IPHONE 3G': [8, 16],
            'IPHONE 3GS': [8, 16, 32], 
            'IPHONE 4': [8, 16, 32], 
            'IPHONE 5C': [8, 16, 32],
            'IPHONE 4S': [8, 16, 32, 64], #5
            'IPHONE 5': [16, 32, 64],
            'IPHONE 5S': [16, 32, 64],
            'IPHONE SE': [16, 32, 64, 128],
            'IPHONE 6': [16, 32, 64, 128], 
            'IPHONE 6+': [16, 32, 64, 128], #10
            'IPHONE 6S': [16, 32, 64, 128],
            'IPHONE 6S+': [16, 32, 64, 128],
            'IPHONE 7': [32, 128, 256],
            'IPHONE 7+': [32, 128, 256], 
            'IPHONE 8': [64, 128, 256], #15
            'IPHONE 8+': [64, 128, 256],
            'IPHONE X': [64, 256],
            'IPHONE XR': [64, 128, 256],
            'IPHONE XS': [64, 256, 512],
            'IPHONE XS MAX': [64, 256, 512], #20
            'IPHONE 11': [64, 128, 256],
            'IPHONE 11 PRO': [128, 256, 512],
            'IPHONE 11 PRO MAX': [128, 256, 512],
            'IPHONE SE 2ND GEN': [64, 128, 256],
            'IPHONE 12': [64, 128, 256], #25
            'IPHONE 12 MINI': [64, 128, 256],
            'IPHONE 12 PRO': [128, 256, 512],
            'IPHONE 12 PRO MAX': [128, 256, 512],
            }
        #check if the string argument is in the dictionary and if it isn't, print an error statement
        if key not in conversion:
            print("ERROR: not a valid iPhone model.")
        #get the value of the iphone model by calling/finding the key in the dictionary
        value = conversion[key]
        #create an empty string where we'll add the list of the phone's storage sizes
        emptystring = ""
        #create a for loop that goes through the phone's storage sizes and adds the sizes to the empty string
        for size in value:
            emptystring = emptystring + str(size) + " GBs" + "\n\t" 
        #remove the '\n\t' from the last storage size
        stripped = emptystring.strip('\n\t')
        #replace when we converted the argument to all uppercase lettering to normal lettering
        replaced = key.replace('IPHONE', 'iPhone')
        #return a print statement that tells the user the iphone type and the corresponding storage size options
        return (f"Storage size options for the {replaced}:\n\t{stripped}")

    def call_friend(self, name):
            #this method takes in a person's name as the argument and generates a random phone number for that person
            #create an empty string that we will add the phone numbers to
            emptystring = ""
            #create a for loop where we will generate 10 numbers. each number will be a random number from 0-9
            #the first digit cannot be 0 or 1
            for i in range(0, 1):
                numbers = str(random.randint(2, 9))
                emptystring = emptystring + numbers
            for i in range(0, 9):
                numbers = str(random.randint(0, 9))
                emptystring = emptystring + numbers
            #splice the generated phone number by the grouping of digits (xxx-xxx-xxxx)
            first_three = emptystring[:3]
            second_three = emptystring[3:6]
            last_four = emptystring[6:]
            #string concatenate the groups of digits and add a dash to separate the groups
            phone_number = first_three + "-" + second_three + "-" + last_four
            print(f"Calling {name} at {phone_number}...")
            #wait three seconds until the person answers the phone
            for i in range(0, 3):
                time.sleep(1)
                print("ringing...")
            return (f"Hello, you've reached {name}.")

def main():
    #in this demo program, we have a budget of $6000 and we want to get a list of the phones with a storage size of 512 GBs
    phone = Phone(6000, 512)
#find_phone_storage
    #print statement of what find_phone_storage does (if we just want to see the storage options for one phone)
    print(phone.find_phone_storage("iPhone 12"))
#find_phone_storage
    #~call the storage size (second argument) in the Phone class. the reason we used get_storage is because theoretically,
    #~the storage should be correct since it comes after the set_storage_size function and is able to access private variables
    phone.get_storage()
    #call the dictionary in the Phone class and access only the values
    #~we are using the method that returned the dictionary of phones and storage sizes, so we can use the dictionary to only get its values
    dictionary = phone.phone_storage_dict()
    listofvalues = dictionary.values()
    #this list represents the positions of the dictionary items
    length_of_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 
        24, 25, 26, 27, 28]
    #zip together the storage size values and their respective positions
    zipped = zip(listofvalues, length_of_list)
    #convert that to a list
    convertlist = list(zipped)
    #create an empty list where we will add the positions only of the storage size that we want to find (either 4, 8, 16, 32, 64, 128, 256 or 512)
    emptylist = []
    #create a for loop that goes through each tuple 
    for values in convertlist:
        try:
            #check if the storage size argument (phone.get_storage()) is in the values[0]. values[0] is the zero-th position in the tuple, which
            #is the list of storage sizes. so we're going through the list of storage sizes and seeing if the argument is in there.
            #~phone.get_storage() refers to the storage size argument. that method can access the private data variable, which is why we're using that method
            if phone.get_storage() in values[0]:
                #append the storage sizes' positions to the empty list we created
                emptylist.append(values[1])
        #index errors occur when we are indexing too high for a list (ex. '512' only appears in position 2, but some storage size lists only go up to position 1)
        #so this is to ignore those cases and continue on with the rest of the for loop
        except IndexError:
            continue
    #create an empty list where we will add the iphone model names (only the ones that contain the storage size we put in our argument)
    list_of_phone_names = []
    #create an empty string where we will add the iphone model names
    emptystring = ""
    #create a for loop that goes through the keys in our dictionary and add all the names to a list
    for phone_name in dictionary:
        list_of_phone_names.append(phone_name)
    #create a for loop that goes through the list of positions of the specific storage size
    for position in emptylist:
        #refer to the list of keys (phone names) and index at the specified position (we're only going through the list of positions that have our argument's
        #storage size, and then getting their respective phone names)
        indexed = list_of_phone_names[position]
        #add those phone names to the empty string and separate with a new line and tab/indent
        emptystring = emptystring + indexed + "\n\t"
    #remove the new line and tab from the last phone name
    stripped = emptystring.strip("\n\t")
    #if the string is empty, meaning that it could not find the storage size in the dictionary, then print an error statement
    if stripped == "":
        print(f"There are no iPhones that have {phone.get_storage()} GBs of storage.")
    #else, print a statement with the GB we specified and list of phones that contain that storage size
    else:
        print(f"List of iPhone(s) with {phone.get_storage()} GBs of storage:\n\t{stripped}")
#get_price
    #the contents in this variable will change based on which prices/phone models the user wants to look at
    list_of_phones = ['iphone se', 'iphone se 2nd gen', 'iphone 6s', 'iphone 11 pro max']
    #set the function phone_price_dict() equal to a variable so that we can access the dictionary
    #~we are using the method that returned the dictionary of phones and prices, so we can use the dictionary to later go through the iphone names
    phone_dict = phone.phone_price_dict()
    #empty will contain the addednphones' prices
    empty = 0
    #emptystring will contain the phones but we separate them by a comma and space
    emptystring = ''
    #create a for loop that goes through the list of phones in the argument
    for phone_argument in list_of_phones:
        #convert the phones to uppercase
        uppercase = phone_argument.upper()    
        #add them to the empty string so that we can separate them    
        emptystring = emptystring + uppercase + ", "
        #if the phone is in the phone and price dictionary, get the respective value
        if uppercase in phone_dict:
            actualprice = phone_dict[uppercase]
        #add the value (price of the phone) to the previous prices
        empty += actualprice
    #however, if the phone price argument is less than 0, then remove the negative sign and print a statement saying that
    #the budget is too small
    #~the method, phone.get_price(), refers to the price we have in our argument and it can also access the private data variable
    if phone.get_price() < 0:
        strconvert = str(phone.get_price())
        stripped = strconvert.strip("-")
        print(f"Your budget of -${stripped} is too small.")
    #but, if that total sum of the phones' prices is greater than our budget (in our argument), then 
    #print a statement saying that the budget is too small
    elif empty > phone.get_price():
        print(f"Your budget of ${phone.get_price()} is too small.")
    #else, get the remainder of the budget/phone price and print a bunch of statements. also, use the call_friend
    #method to "test" our new phone! (we won't call the friend when our budget is too small because that means we 
    #didn't have enough money to purchase the phones)
    else:
        stripped = emptystring.strip(", ")
        remainder = phone.get_price() - empty
        print(f"The sum of the price(s) of the {stripped} is ${empty}.\nGiven your budget of ${phone.get_price()}, you will have ${remainder} left.")
        print("Now, let's test your brand new iPhone by calling a friend!")
        print(phone.call_friend("Stephen"))

if __name__ == "__main__":
    main()