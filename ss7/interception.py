#!/usr/bin/env python3
'''
Created on 1 Feb 2018

@author: loay

@editor: toxic -05-11-2022-

short note update : support python 3.9
'''
import sys
import os
import time
import sigploit
import ss7main
import helpers

from subprocess import *


ul_path = helpers.get_ss7_attacks_interception_ul_payload()		#os.path.join(os.getcwd(),'ss7/attacks/interception/ul')


def ul():
	try:
		updateLocation = check_call(['java', '-jar', ul_path])
		if updateLocation == 0:
			it = input('\nWould you like to go back to Interception Menu? (y/n): ')
			if it == 'y' or it == 'yes':
				ss7main.Interception()
			elif it == 'n' or it == 'no':
				attack_menu = input('Would you like to choose another attacks category? (y/n): ')
				if attack_menu == 'y' or attack_menu == 'yes':
					ss7main.attacksMenu()
				elif attack_menu == 'n' or attack_menu == 'no':
					main_menu = input('Would you like to go back to the main menu? (y/exit): ')
					if main_menu == 'y' or main_menu == 'yes':
						sigploit.mainMenu()
					elif main_menu == 'exit':
						print('TCAP End...')
						time.sleep(1)
						sys.exit(0)

	except CalledProcessError as e:
		print("\033[31m[-]Error:\033[0mUpdateLocation Failed to Launch, Error: ", e)
		time.sleep(2)
		ss7main.Interception()
	
