# A Hand Cricket Game

import random
import time


time.sleep(0.5)
print('|-----------------------------------------------|')
time.sleep(0.5)
print('|--        Welcome to ODD-OR-EVEN GAME        --|')
time.sleep(0.5)
print('|-----------------------------------------------|')
time.sleep(0.5)
print('|            - a Five Wicket hand cricket game  |')
time.sleep(0.5)
print('|                            Author - soorajsp  |')
time.sleep(0.5)
print('|-----------------------------------------------|')
print('')
print('')
time.sleep(1)
print('|-----------------------------------------------|')
time.sleep(0.4)
print('|--              GAME INSTRUCTIONS            --|')
time.sleep(0.4)
print('|-----------------------------------------------|')
time.sleep(0.4)
print('| 1. Enter numbers from 0-6 only                |')
time.sleep(0.4)
print('| 2. Type \'odd\' or \'even\' according to ur choice|')
time.sleep(0.4)
print('| 3. Final result will be published at the end  |')
time.sleep(0.4)
print('|-----------------------------------------------|')
print("")
print('LOADING...!!!')
time.sleep(2)


def oddoreven():
    while True:
        b = input('Enter a number from 0-6 : ')

        try:
            while int(b) not in range(0, 7, 1):
                print('Wrong Input')
                b = input('Enter a number from 0-6 : ')
        except ValueError:
            print('"Wrong Input"')

        else:
            c = str(random.randint(0, 6))
            print('My number is ' + c)
            time.sleep(0.3)
            d = int(b) + int(c)
            print('Total is ' + str(d))
            time.sleep(0.3)
            return d % 2


def bat_code(usr, pc):
    while True:

        z = []  # my_run
        y = []  # comp_run
        w1 = []  # wicket user
        w2 = []  # wicket comp
        j = 1
        k = 1

        while len(w1) < 6 and j < 6:
            p = input('Enter your number: ')
            try:
                while int(p) not in range(0, 7, 1):
                    print('Wrong Input')
                    p = input('Enter your number: ')
            except ValueError:
                print('Wrong Input')
            else:
                q = random.randint(0, 6)
                print('I put ' + str(q))
                if int(p) != int(q):
                    z.append(int(p))
                    print(usr + ' have scored ' + str(p) + ' Runs')
                elif int(p) == int(q):
                    print('OUT, ' + usr + ' HAVE LOST A WICKET')
                    z.append(0)
                    w1.append(9)
                    r = sum(z)
                    print(usr + ' HAVE SCORED ' + str(r) + ' RUNS WITH ' + str(j) + ' WICKETs')
                    j = j + 1

        if len(w1) == 5:
            r = sum(z)
            print('')
            print('|-----------------|')
            print('|---Turn Change---|')
            print('|-----------------|')
            print(usr + ' are now Bowling')

            # bowling after 1st batting.
            while len(w2) < 6 and k < 6:
                q = random.randint(0, 6)
                p = input('Enter your number: ')
                try:
                    while int(p) not in range(0, 7, 1):
                        print('Wrong Input')
                        p = input('Enter your number: ')
                except ValueError:
                    print('Wrong Input')
                else:
                    print('I put ' + str(q))
                    if int(q) != int(p):
                        y.append(int(q))
                        print(pc + ' have scored ' + str(q) + ' Runs')
                    elif int(q) == int(p):
                        print('OUT, ' + pc + ' HAVE LOST A WICKET')
                        y.append(0)
                        w2.append(9)
                        s = sum(y)
                        print(pc + ' HAVE SCORED ' + str(s) + ' RUNS WITH ' + str(k) + ' WICKETs')
                        k = k + 1

            if len(w2) == 5:
                s = sum(y)
                print('')
                print('--END OF INNINGS--')
                print('')

                if r > s:  # here r is user and s is computer
                    print('YOU HAVE SCORED ' + str(r))
                    print('I HAVE SCORED ' + str(s))
                    print('')
                    print('    -----CONGRATZ-----    ')
                    print('---YOU HAVE WON THE GAME---')
                    print('        :(      ')


                elif s > r:
                    print('YOU HAVE SCORED ' + str(r))
                    print('I HAVE SCORED ' + str(s))
                    print('')
                    print('    -----BETTER LUCK NEXT TIME-----    ')
                    print('      ---YOU HAVE LOST THE GAME---      ')
                    print('        :D      ')


                elif s == r:
                    print('YOU HAVE SCORED ' + str(r))
                    print('I HAVE SCORED ' + str(s))
                    print('')
                    print('      ---THAT\'S A DRAW MATCH---      ')
                    print('     :p         ')


def ball_code(usr, pc):
    while True:

        z = []  # my
        y = []  # comp
        w2 = []  # wicket comp
        w1 = []  # wicket user
        k = 1
        j = 1
        while len(w2) < 6 and k < 6:
            p = input('Enter your number: ')
            try:
                while int(p) not in range(0, 7, 1):
                    print('Wrong Input')
                    p = input('Enter your number: ')
            except ValueError:
                print('Wrong Input')
            else:
                q = random.randint(0, 6)
                print('I put ' + str(q))
                while int(q) != int(p):
                    y.append(int(p))
                    print(usr + ' have scored ' + str(p) + ' runs')
                    break
                if int(q) == int(p):
                    print('OUT, ' + usr + ' HAVE LOST A WICKET')
                    print('')
                    y.append(0)
                    w2.append(9)
                    s = sum(y)
                    print(usr + ' HAVE SCORED ' + str(s) + ' RUNS WITH ' + str(k) + ' WICKETs')
                    k = k + 1

        if len(w2) == 5:
            s = sum(y)
            print('')
            print('|-----------------|')
            print('|---Turn Change---|')
            print('|-----------------|')
            print(pc + ' are now Batting')

            # batting after 1st bowling.
            while len(w1) < 6 and j < 6:
                p = input('Enter your number: ')
                try:
                    while int(p) not in range(0, 7, 1):
                        print('Wrong Input')
                        p = input('Enter your number: ')
                except ValueError:
                    print('Wrong Input')
                else:
                    q = random.randint(0, 6)
                    print('I put ' + str(q))
                    while int(p) != int(q):
                        z.append(int(p))
                        print(pc + ' have scored ' + str(p) + ' runs')
                        break
                    if int(p) == int(q):
                        print('OUT, ' + pc + ' HAVE LOST A WICKET')
                        print('   :D   ')
                        z.append(0)
                        w1.append(9)
                        r = sum(z)
                        print(pc + ' HAVE SCORED ' + str(r) + ' RUNS WITH ' + str(j) + ' WICKETs')
                        j = j + 1

            if len(w1) == 5:
                r = sum(z)
                print('')
                print('--END OF INNINGS--')

                if r > s:  # here r is user and s is computer
                    print('YOU HAVE SCORED ' + str(r))
                    print('I HAVE SCORED ' + str(s))
                    print('')
                    print('    -----CONGRAATZ-----    ')
                    print('---YOU HAVE WON THE GAME---')
                    print('            :(             ')


                elif r < s:
                    print('YOU HAVE SCORED ' + str(r))
                    print('I HAVE SCORED ' + str(s))
                    print('')
                    print('    -----BETTER LUCK NEXT TIME-----    ')
                    print('      ---YOU HAVE LOST THE GAME---      ')
                    print('            :D           ')


                elif r == s:
                    print('YOU HAVE SCORED ' + str(r))
                    print('COMPUTER HAVE SCORED ' + str(s))
                    print('')
                    print('      ---THAT\'S A DRAW MATCH---      ')
                    print('                   :p               ')


def toss():
    while True:

        print('')
        print('--Choose weather to Bat ot Bowl first: --')
        print('')
        print('|-------------------------------------------|')
        choice = input('|--Enter your choice, [BATTING or BOWLING]--|').lower()
        print('|-------------------------------------------|')
        if choice == 'batting':
            time.sleep(0.2)
            print('HI BATSMAN')
            time.sleep(0.2)
            print('''   -----You have chosen to Bat 1st,
                scroll up to see the rules and instructions----''')
            time.sleep(0.5)
            usr = 'YOU'
            pc = 'I'
            bat_code(usr, pc)
        elif choice == 'bowling':
            time.sleep(0.2)
            print('HI BOWLER')
            time.sleep(0.2)
            print('''   -----You have chosen to Ball 1st,
              scroll up to see the rules and instructions----''')
            time.sleep(0.5)
            usr = 'I'
            pc = 'YOU'
            ball_code(usr, pc)
        else:
            print('Make a Valid decision')


def machine_decision():
    cycle = ['bat', 'ball']
    if random.choice(cycle) == 'bat':
        print('I\'ve chosen to BAT')
        print('--GET READY TO BOWL--')
        time.sleep(0.4)
        usr = 'I'
        pc = 'YOU'
        bat_code(usr, pc)
    else:
        print('I\'ve chosen to BOWL')
        print('--KEEP YOUR BAT READY--')
        time.sleep(0.4)
        usr = 'YOU'
        pc = 'I'
        ball_code(usr, pc)


while True:
    print('')
    print('|--------------------|')
    a = input('|    Odd or Even.??  |').lower()
    print('|--------------------|')
    print('')
    time.sleep(1)
    if a == 'odd':
        r = oddoreven()
        if r == 1:
            time.sleep(0.5)
            print('which is ODD.')
            print('You\'ve won the toss.!!')
            time.sleep(0.5)
            print('Good Luck, Hope you make a right choice')
            time.sleep(0.3)
            toss()
        else:
            print('which is EVEN.')
            print('I\'ve won the toss.!!')
            time.sleep(0.5)
            machine_decision()

    elif a == 'even':
        r = oddoreven()
        if r == 1:
            time.sleep(0.5)
            print('which is ODD.')
            print('I\'ve won the toss.!!')
            time.sleep(0.5)
            machine_decision()
        else:
            time.sleep(0.5)
            print('which is EVEN.')
            print('You\'ve won the toss.!!')
            time.sleep(0.5)
            print('Good Luck, Hope you make a right choice')
            time.sleep(0.3)
            toss()

input()
