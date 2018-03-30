#The Pokemon Game
import time

time.sleep(1)
print('Welcome to the pokemon game,')
time.sleep(1)
print("Time to catch some pokemon..!!!!")
time.sleep(1)
print('')
print('')

time.sleep(2)
print('|-------------------------------------------|')
time.sleep(0.4)
print('|              GAME INSTRUCTIONS            |')
time.sleep(0.4)
print('|-------------------------------------------|')
time.sleep(0.4)
print('| 1. Type Y or YES to say YES               |')
time.sleep(0.4)
print('| 2. Press ENTER to say NO                  |')
time.sleep(0.4)
print('|-------------------------------------------|')
print('')
print('')
time.sleep(2)

z = [] #pokemon catching net
a = input('Which Pokemon have u caught (Enter its name): ')
z.append(a)
print(z)

c = input('Would u like to keep catching Pokemons : ')
while (c == 'y' or c == 'yes' ):
	b = input('Which Pokemon have u caught : ')
	z.append(b)
	print(z)
	c = input('Would u like to keep catching Pokemon : ')
	
else :
	print('')
	print('')
	print('You have the following Pokemons ')
	print(z)
	

time.sleep(1)
print('Lets move to the Pokemon Gym.....')
time.sleep(2)
print('------------------------------------------------------')
print('     	   Welcome to the POKEMON gym!!!             ')
print('------------------------------------------------------')
time.sleep(0.8)

print("Pokemon in your collection : ")
print(z)

time.sleep(1)
s = []  #gym team
print('Pokemon in your gym team : ')
print(s)

time.sleep(1)
d = input('which pokemon will you add to your team? (pick from the pokemon net) : ')
print(0.5)
print('I choose you , ' + d)
z.remove(d)
s.append(d)

time.sleep(0.5)
e = input('would you like to stay in Pokemon gym? : ')
while(e == 'y' or e == 'yes'):
        print("Pokemon in your collection : ")
        print(z)
        time.sleep(1)
        print('Pokemon in your gym team : ')
        print(s)
        time.sleep(1)
        d = input('which pokemon will you add to your team? : ')
        print('I choose you , ' + d)
        z.remove(d)
        s.append(d)
        e = input('would you like to stay in Pokemon gym? : ')
if c=='n' or c=='no' :
	g = input("Press Enter to Exit....")
        
