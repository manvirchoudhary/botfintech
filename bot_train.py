
ai = "Artificial intelligence ai is an area of computer science that emphasizes \n the creation of intelligent machines that work and react like humans"

founder_fin = "Abhipriya gupta and Abhishek Batra"

day_trade = "Day trading is only profitable when traders take it seriously and do their research."

human = None
while human != "Bye".lower():
		human = input("Human :  ")

		if human != "Bye".lower():

			if human.lower() == "Hi".lower():
				print("Bot: Hi")

			elif human.lower() == "Hello".lower():
				print("Bot: Hello")	

			elif human.lower() == "How are You".lower():
				print("Bot: I am good")

			elif human.lower() == "I need your Help".lower():
				print("Bot: how can i help you")

			elif human.lower() == "What is FinHawk".lower():
				print("Bot: It is a growing fintech startup based out in Gurugram") 	

			elif human.lower() == "Who is the founder of FinHawk".lower():
				print(f"Bot:  {founder_fin}")

			elif human.lower() in ai.lower():
				print(f"Bot:  {ai}")	

			elif human.lower() == "What is ai".lower():
				print(f"Bot:  {ai}")		

			elif human.lower() == "What is day trading".lower():
				print(f"BoT: {day_trade}") 	

			else:
				print("Bot: I don't know, Please Talk with Human \n Have a Good Day :) ")	
				break
			  

			
else:
	print("Bot: bye")			

