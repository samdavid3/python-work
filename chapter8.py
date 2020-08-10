from user_profile import build_profile as bp
def greetme():
	print(f"hello there")

greetme()

def fav_book(incoming):
	print(f"My Fav book is: {incoming}")

fav_book("Bible")

def shirtSize(size='large', message='I love Python'):
	print(f"A shirt size {size} with the messaage '{message}' will be produced")
shirtSize(13, 'I am Sam')
shirtSize(size=14, message='Hey there')
shirtSize()
shirtSize(size='medium')

def countryMessage(city, country='USA'):
	print(f"{city} is in {country}")

countryMessage('Des Moines')
countryMessage(city='Madras', country='India')

def city_country(city, country):
	temp= f"{city}, {country}"
	return temp.title()

print(city_country('madras','india'))

def musicLib(artist, album, songnos=None):
	musicdictionary = {"artist":artist, "album": album}
	if songnos:
		musicdictionary['number of songs']= songnos
	return musicdictionary

print(musicLib("Clapton", "Tears in Heaven"))
print(musicLib("Bon Jovi", "Live and let die"))
print(musicLib("Jeremy Camp", "my jesus", 14))

# while True:
# 	artist=input("Enter the artist. Press q to quit anytime")
# 	if artist=='q':
# 		break
# 	album= input("Enter the album. Press q to quit anytime")
# 	if album=='q':
# 		break
# 	print(musicLib(artist,album))

# Lists
messageList= ['hello', 'vanakam', 'guten tag', 'namaste']
def show_messages(mess):
	for m in mess:
		print(f"{m}")

show_messages(messageList)

sent_m=[]
def send_messages(mess):
	while mess:
		sent_m.append(mess.pop())
send_messages(messageList[:])

print(f"{messageList}")
print(f"{sent_m}")

# Arbitrary arguments
def sandwich(*args):
	for a in args:
		print(f"{a}")
sandwich("lettuce", "tomato", "onions")


user = bp("sam", "david", age=48, weight=203, height="5'9" )
print(f"{user}")