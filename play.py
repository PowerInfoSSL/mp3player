#!/usr/bin/python




#///////////bANNER
"""
          __        _______ _     ____ ___  __  __ _____ 
          \ \      / / ____| |   / ___/ _ \|  \/  | ____|
           \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
            \ V  V / | |___| |__| |__| |_| | |  | | |___  _   _   _ 
             \_/\_/  |_____|_____\____\___/|_|  |_|_____|(_| |_| |_)
                                               
                        Script Crearor: 
     _   _    _____ _    ____    _____  ___     ___    _   _    _    
    | | / \  |  ___/ \  |  _ \  |_   _|/ \ \   / / \  | \ | |  / \   
 _  | |/ _ \ | |_ / _ \ | |_) |   | | / _ \ \ / / _ \ |  \| | / _ \  
| |_| / ___ \|  _/ ___ \|  _ <    | |/ ___ \ V / ___ \| |\  |/ ___ \ 
 \___/_/   \_\_|/_/   \_\_| \_\   |_/_/   \_\_/_/   \_\_| \_/_/   \_\
                                                                     
Tell:  +989170118221   		  Mail: PowerInfoSSL@Gmail.com
"""



import sys,os
from glob import glob
import random


f=glob('*.mp3')
#print '\n\n\n\n              F\n\n\n\n'
#print f,'\n\n\n\n'
while True:
    h=random.randrange(len(f))
    print '\n\n            Playing ' + str(h) + ' from ' + str(len(f)) + '\n\n'
    print '          '+str(f[h]) + '\n'
    #print "@"*20
    os.system("mplayer -really-quiet '" + str(f[h]) + "'")

