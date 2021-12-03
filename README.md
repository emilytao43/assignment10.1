Emily Tao
CSE20-03
Assignment 10.1

Link to repository: https://github.com/emilytao43/assignment10.1

Description of the class:
	The Phone class is used to get and analyze elements of an iPhone. For instance, in a phone, there will always be a screen. Additionally, the Phone class has elements like storage and price, in which we can check. In this class, we can get and set the storage size and budget price. The class also has a method that deals with calling people. The overall purpose of the class is to look at one’s budget and see which phones best fits that budget. Additionally, we can compare all the iPhones’ storage sizes, which is useful if we want to get the phone(s) with the most amount of storage. *note that this data does not include iPhones released in 2021

Class variable (screen):
	Screen is a class variable in which we set to True since all phones have a screen. In this case, we’re dealing with only Apple iPhones. 

Data variable (price):
	Price is a data variable and it represents the budget the user has (not the price of an individual phone).

Data variable (storage):
	Storage is a data variable because the storage size varies depending on the phone. There are only seven possible storage sizes (8, 16, 32, 64, 128, 256, 512).

Method (__init__):
	__init__ takes in three arguments: self, price, and storage. Price and storage are both integers. The constructor method does not return anything, rather it simply sets the arguments equal to variables, so that we can store their values. 

Method (set_price):
	set_price takes in two arguments and returns the new or existing price, if the price argument is not acceptable. The arguments are self and price, where price is an integer. If the price argument is greater than 0, that will be the new price, however, if the price is less than 0, the price argument is returned.

Method (get_price):
	get_price takes in one argument, self. In this method, we are only returning the price we set in the method, set_price.

Method (set_storage):
	set_storage takes in two arguments, self and storage, which is an integer. This method will return the new storage size or return the existing storage argument if the storage argument is not acceptable.

Method (get_storage):
	get_storage takes in one argument, self. This method will return the storage size we set in set_storage.

Method (phone_price_dict):
	phone_price_dict takes in self as an argument. The method returns a dictionary where the keys are the iPhone model names and the values are the prices.

Method (create_dictionary):
	create_dictionary takes in self as an argument. This method returns a dictionary where the keys are the iPhone model names and the values are lists of storage sizes.

Method (find_phone_storage):
	find_phone_storage takes in self and phonemodel as arguments. phonemodel is a string of iPhone model name (notes: there is a space between “iPhone” and the number. Models that have “plus” in the name use a plus sign (“+”)). find_phone_storage returns that phone’s list of storage sizes.

Method (call_friend):
	call_friend takes in self and a person’s name, which is a string. The method will return a string that says who we called, but as we progress through the method, the method will generate a random phone number.

Description of the demo program:
	The demo program first finds and prints out a list of iPhones with a specified storage size. Else, we will print out a statement that says that storage size doesn’t exist. In this case, the demo program is retrieving the iPhones with the greatest storage size (512 GBs) because we want to see and compare all the phones that have the greatest amount of storage.
	In the second code block, we will see if we will be able to purchase a group of phones (or one phone) based on our specified budget. If the budget is too small, we will print a statement saying that our budget is too small. However, if we have enough money in our budget, then we can “buy” the phone(s) by calling a specified person, which in our demo program, is named Stephen. The code will print out a statement listing our budget (in dollars), the remainder (in dollars), the phone(s) we want to purchase and how much those phone(s) cost all together. In the demo program, we have a budget of $6000 and we’re seeing if we can purchase the iPhone SE, iPhone SE 2nd Gen, iPhone 6S and the iPhone 11 Pro Max.

How to run the demo program:
	To run the code, in line 208, change the first argument (price) to your budget and the second argument (storage size) to what storage size you want. Then, run the code in the terminal to view the results (the user doesn’t need to import anything).
