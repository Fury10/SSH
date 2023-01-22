credits = '''

███████╗███████╗██╗  ██╗
██╔════╝██╔════╝██║  ██║
███████╗███████╗███████║
╚════██║╚════██║██╔══██║
███████║███████║██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝
'''
print(credits)

# Ensures Linux System
import platform
system = platform.system()

if system != 'Linux':
   print('You Are Currently Using The Linux Script Of SSH.\n Please check for any new updates as currently Only Linux Is supported')
   exit()

# Checks If Packages Are Installed
try:
   import re
except ImportError:
   print('Error, PiP Module re is required.\nPlease Run "pip install re" in the terminal to install')
   exit()

try:
   import bullet
except ImportError:
   print('Error, PiP Module bullet is required.\nPlease Run "pip install bullet" in the terminal to install')
   exit()

import os # used to run commands
import re # used for validation
import pyperclip # used for clipboard copying
from bullet import Bullet # pretty menu
from bullet import colors # colours for bullet

# Selects SSH Mode To Use
Modes = Bullet(
        prompt = 'Please Choose A SSH Mode: ',
        choices = ['Quick Connect', 'Search Profiles', 'Open Profiles', 'Create New Profile', 'Generate SSH Keys','Exit'],
        indent = 0,
        align = 2,
        margin = 1,
        bullet = '>',
        bullet_color=colors.bright(colors.foreground['white']),
        word_color=colors.bright(colors.foreground['green']),
        word_on_switch=colors.bright(colors.foreground['yellow']),
        background_color=colors.background['black'],
        background_on_switch=colors.background['black'],
        pad_right = 5
   )

sshMode = Modes.launch() # starts selector and saves choice as variablea

def QuickConnect():
# regex for validating Ip
    regex = '^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
# 255.255.255.255 is highest ip

# validate an Ip address
    def validateIp():
    # checks Ip against regex rules
    # If it follows the rules it allows the program to continue overwise shows Invalid Ip and stops code
            if(re.search(regex, Ip)):
                    x = True
            else:
                    print('\nNot A Valid Ip Address -->',Ip)
                    print('Exiting Code')
                    exit()

# validate the Port
    def validatePort():
            if Port > 65535:
                    print('\nThat Not A Valid Port! -->',Port)
                    exit()

            if Port < 1:
                    print('\nThats Not A Valid Port! -->',Port)
                    exit()

# Asks For Username
    Username = input('\nEnter A Username: ')

# Measures the amount of characters in the username
    Unamelength = len(Username)

# if username is more than 15 characters stop script
    if Unamelength > 15:
        print('Please Use a Username Length Of Less Than 15 characters!')
        exit()

# Asks For The Ip address
    Ip = input('Enter IP Address: ')

# runs validation check for ip
    validateIp()

# Asks For The Port Number
    Port = int(input('Enter Port Number: '))

# runs validation check for port
    validatePort()

# Turn Port Into Str For .Join (already been validated by now so should be safe. I think?)
    Port=str(Port)


# sets the private key ssh to a function to be easily decided
    def key():

        anyuser = os.path.expanduser('~')

    # The directory where items will be listed
        dirtypath = [anyuser,'/.ssh/']
        path = ''.join(dirtypath)

    # List of files in complete directory
        file_list = []

#           -- IN CASE I FORGET --
#      Path --> Name of each directory
#      Folders --> List of subdirectories inside current 'path'
#      Files --> List of files inside current 'path'
#
    # for every file and folder? in path add it to file_list
        for path,folders, files in os.walk(path):
               for file in files:
                          file_list.append(os.path.join(path, file))

        print('\n01)',file_list[0],'\n02)',file_list[1],'\n03)',file_list[2],'\n04)',file_list[3])
            # Prints List Of Keys

        arraylist = len(file_list) # Counts How Many SSH Keys There Are (This Will Also Count Folders Need To Change This)

        print('\nPlease Pick An SSH Key Between 1 to ',arraylist - 1,sep='') # Show Max Number Of SSH Keys To Choose From

        select = int(input('Select SSH Key: ')) #

        finalfinal = file_list[select - 1] # Because arrary starts at 0 has to take off 1

    #Uses The Extra Private Key Thing
        privateconnection = ['ssh ',Username,'@',Ip,' -p ',Port,' -i ',finalfinal]

    # stops trying to join using the non private key

        privatefinalcommand = ''.join(privateconnection)

        print('\n','   === Attempting Connection To ===\n\n','    ',privatefinalcommand,'\n\n','   ================================\n',sep='')

        os.system(privatefinalcommand)

    def nonkey():
    # turns all info into a list
        connection = ['ssh ',Username,'@',Ip,' -p ',Port]

    # the full ssh command ot be run
        finalcommand = ''.join(connection)

        print('\n','   === Attempting Connection To ===\n\n','    ',finalcommand,'\n\n','   ================================\n',sep='')

        os.system(finalcommand)


# Chooses which function to use, which will or won't show the prompt to use a private key
    type = input('Would You Like To Use A Private Key? Y / N ')
    if type == 'Y':
        print('Private Key Selected!')
        key()
    else:
        nonkey()


def genKey():
    bits = Bullet(
         prompt = '\nPlease choose a Bit Size To Generate: ',
         choices = ['1024', '2048', '4096', '8192', 'Custom'],
         indent = 0,
         align = 5,
         margin = 2,
         bullet = '>',
         bullet_color=colors.bright(colors.foreground['red']),
         word_color=colors.bright(colors.foreground['cyan']),
         word_on_switch=colors.bright(colors.foreground['cyan']),
         background_color=colors.background['black'],
         background_on_switch=colors.background['black'],
         pad_right = 5
        )

    keybit = bits.launch() #starts bits and outputs as variable
    print('\nYou have chosen: ', keybit,' Bits',sep='')

    # if slected on menu allows to choose custom bit number
    if keybit == 'Custom':
        keybit = int(input('Select Custom Bit Number: '))
        print('You have chosen ',keybit,' Bits',sep='')

    filename = input('Enter Name For Private Key File: ')
    print('Your Public Key Will Be In The Same Directory With The .pub prefix')

    # the full command which needs to be run in cmd prompt etc (but has too many spaces + brackets)
    part1 = ['ssh-keygen ','-f ~/.ssh/',filename,' -t ','rsa ','-b ',keybit,]
    # turns part1 into proper command removing brackets and fixing spaces
    final = ''.join(part1)

    print('\n')
    os.system(final) # runes full command in cmd prompt


############################################################

def saveNewProfile():
    print('this feature is still being developed')
    profileName = input('Enter Name Of New Profile: ')
    profileHostName = input('Enter HostName For New Profile: ')
    profileUser = input('Enter Username For New Profile: ')
    profilePort = input('Enter Port For New Profile: ')
    profileKey = input('Enter Private Key Name For New Profile: ')

    Line1 = ['Host ',profileName]
    fLine1 = ''.join(Line1)

    Line2 = ['    HostName ',profileHostName]
    fLine2 = ''.join(Line2)

    Line3 = ['    User ',profileUser]
    fLine3 = ''.join(Line3)

    Line4 = ['    Port ',profilePort]
    fLine4 = ''.join(Line4)

    Line5 = ['    IdentityFile ',profileKey]
    fLine5 = ''.join(Line5)

    if profileKey == '':
        Line5 = ''
        fLine5 = ''

    userpath = os.path.expanduser('~') # works out homepath

    sshconfig = [userpath,'/.ssh/config']

    fsshconfig = ''.join(sshconfig)

    append1 = open(fsshconfig, 'at') #
    append1.write(fLine1)
    append1.close()

    append1 = open(fsshconfig, 'at')
    append1.write('\n'+fLine2)
    append1.close()

    append1 = open(fsshconfig, 'at')
    append1.write('\n'+fLine3)
    append1.close()

    append1 = open(fsshconfig, 'at')
    append1.write('\n'+fLine4)
    append1.close()

    append1 = open(fsshconfig, 'at')
    append1.write('\n'+fLine5)
    append1.close()

############################################################
# Search Feature
def searchy():
    searchInput = input('\nPlease Enter Search Details: ')

    cSearch = ['"Host ',searchInput,'"']

    fSearch = ''.join(cSearch)

    suserpath = os.path.expanduser('~')

    ssshconfig = [suserpath,'/.ssh/config']

    fssshconfig = ''.join(ssshconfig)

    command = ['cat ',fssshconfig,' | ','grep ',fSearch]

    fcommand = ''.join(command)

    print('\nResults Found:')

    os.system(fcommand)

    newssh = input('\nEnter Profile Name Exactly Here: ')

    newSSH = ['ssh ',newssh]

    fNewSSH = ''.join(newSSH)

    print('\nStarting SSH Connection')

    os.system(fNewSSH)

############################################################

if sshMode == 'Exit':
    print('\nClosing...')
    exit()

if sshMode == 'Search Profiles':
    searchy()

if sshMode == 'Create New Profile':
    saveNewProfile()

if sshMode == 'Quick Connect':
    QuickConnect()

if sshMode == 'Open Profiles':
    sshmenu = 'sshmenu'
    os.system(sshmenu) #runs the variable like a command in command prompt

if sshMode == 'Generate SSH Keys':
    genKey()
