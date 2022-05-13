#!/usr/bin/env python3
'''
Created on 1 Feb 2018

@author: loay

@editor: toxic -05-11-2022-

short note update : support python 3.9
'''
import sys
import time
import sigploit
import ss7main
import helpers

from subprocess import *

sri_path = helpers.get_ss7_attacks_tracking_sri_payload() 		#os.path.join(os.getcwd(), 'ss7/attacks/tracking/sri')
srism_path = helpers.get_ss7_attacks_tracking_srism_payload()	#os.path.join(os.getcwd(), 'ss7/attacks/tracking/srism')
psi_path = helpers.get_ss7_attacks_tracking_psi_payload() 		#os.path.join(os.getcwd(), 'ss7/attacks/tracking/psi')
ati_path = helpers.get_ss7_attacks_tracking_ati_payload()		#os.path.join(os.getcwd(), 'ss7/attacks/tracking/ati')


def sri():
	try:
		sendRoutingInfo = check_call(['java', '-jar', sri_path])
		if sendRoutingInfo == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		print("\033[31m[-]Error:\033[0mSendRoutingInfo Failed to Launch, ", e)
		time.sleep(2)
		ss7main.LocationTracking()
	

def psi():
	try:
		psi = check_call(['java', '-jar', psi_path])
		if psi == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		print("\033[31m[-]Error:\033[0m"+psi_path+" Failed to Launch, ", e)
		time.sleep(2)
		ss7main.LocationTracking()


def srism():
	try:
		srism = check_call(['java', '-jar', srism_path])
		if srism == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		print("\033[31m[-]Error:\033[0m"+srism_path+" Failed to Launch, ", e)
		time.sleep(2)
		ss7main.LocationTracking()


def ati():
	try:
		ati = check_call(['java', '-jar', ati_path])
		if ati == 0:
			lt = input('\nWould you like to go back to LocationTracking Menu? (y/n): ')
			if lt == 'y' or lt == 'yes':
				ss7main.LocationTracking()
			elif lt == 'n' or lt == 'no':
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
		print("\033[31m[-]Error:\033[0m"+ati_path+" Failed to Launch, ", str(e))
		time.sleep(2)
		ss7main.LocationTracking()
