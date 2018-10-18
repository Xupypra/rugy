food={"vegetables":["carrots","kale","cucumber","tomato"],"desserts":["cake","ice cream", "donut"]}
for hungry in food["vegetables"]:
        print("My favorite vegetable is " + hungry)

cars={"sports":{"Volkswagen":"Porsche","Dodge":"Viper","Chevy":"Corvette"},"classic":{"Mercedes-Benz":"300SL","Toyota":"2000GT","Lincoln":"Continental"}}
for auto in cars["sports"]:
        print("My favorite sports car is a " + cars["sports"][auto])

dessert={"iceCream":["Rocky Road","strawberry","Pistachio Cashew","Pecan Praline"]}

for sweet in dessert:
	for value in dessert[sweet]:
		print ("Values ist " , value)

soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"good for you"}}

for auto in cars:
        for value1 in cars[auto]:
		print ("Values1 ist ", value1) 
