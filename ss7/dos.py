#!/usr/bin/env python3

'''
Created on 8 Feb 2018

@author: loay

@editor: toxic -05-11-2022-

short note update : support python 3.9
'''
import sys
import os
import time

import helpers
import sigploit
import ss7main
from subprocess import *


purge_path = helpers.get_ss7_attacks_dos_prgms_payload()		#os.path.join(os.getcwd(),'ss7/attacks/dos/prgms')


def purge():
	try:
		purgeMS = check_call(['java', '-jar', purge_path])
		if purgeMS == 0:
			ds = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if ds == 'y' or ds == 'yes':
				ss7main.DoS()
			elif ds == 'n' or ds == 'no':
				attack_menu = input('Would you like to choose another attacks category? (y/n): ')
				if attack_menu == 'y' or attack_menu == 'yes':
					ss7main.attacksMenu()
				elif attack_menu == 'n' or attack_menu == 'no':
					main_menu = input('Would you like to go back to the main menu? (y/exit): ')
					if main_menu == 'y' or main_menu == 'yes':
						sigploit.mainMenu()
					elif main_menu == 'exit':
						print('TCAP End...')
						sys.exit(0)

	except CalledProcessError as e:
		print("\033[31m[-]\033[0mError:PurgeMS Failed to Launch, ", e)
		time.sleep(2)
		ss7main.DoS()

