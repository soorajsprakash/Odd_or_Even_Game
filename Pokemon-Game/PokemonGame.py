#The Pokemon Game

print('|-----------------------------------------------|')
print('|--        Welcome to the POKEMON GAME        --|')
print('|-----------------------------------------------|')
print("|              Time to catch some pokemon..!!   |")
print('|                           Author - soorajsp   |')
print('|-----------------------------------------------|')
print('')
print('')
print('|-----------------------------------------------|')
print('|--              GAME INSTRUCTIONS            --|')
print('|-----------------------------------------------|')
print('| 1. Type Y or YES to say YES                   |')
print('| 2. Press ENTER to say NO                      |')
print('|-----------------------------------------------|')
print('')
print('')
print('LET\'S PLAY..!!!')
print('')

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
	

print('Lets move to the Pokemon Gym.....')
print('------------------------------------------------------')
print('     	   Welcome to the POKEMON gym!!!             ')
print('------------------------------------------------------')

print("Pokemon in your collection : ")
print(z)

s = []  #gym team
print('Pokemon in your gym team : ')
print(s)

d = input('which pokemon will you add to your team? (pick from the pokemon net) : ')
print(0.5)
print('I choose you , ' + d)
z.remove(d)
s.append(d)

e = input('would you like to stay in Pokemon gym? : ')
while(e == 'y' or e == 'yes'):
        print("Pokemon in your collection : ")
        print(z)
        print('Pokemon in your gym team : ')
        print(s)
        d = input('which pokemon will you add to your team? : ')
        print('I choose you , ' + d)
        z.remove(d)
        s.append(d)
        e = input('would you like to stay in Pokemon gym? : ')
if c=='n' or c=='no' :
	g = input("Press Enter to Exit....")
        
