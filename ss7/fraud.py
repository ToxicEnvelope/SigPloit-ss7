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


simsi_path = helpers.get_ss7_attacks_fraud_simsi_payload()		#os.path.join(os.getcwd(), 'ss7/attacks/fraud/simsi')
mtsms_path = helpers.get_ss7_attacks_fraud_mtsms_payload()		#os.path.join(os.getcwd(), 'ss7/attacks/fraud/mtsms')
cl_path = helpers.get_ss7_attacks_fraud_cl_payload()			#os.path.join(os.getcwd(), 'ss7/attacks/fraud/cl')


def simsi():
	try:
		sendIMSI = check_call(['java', '-jar', simsi_path])
		if sendIMSI == 0:
			fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if fr == 'y' or fr == 'yes':
				ss7main.Fraud()
			elif fr == 'n' or fr == 'no':
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
		print("\033[31m[-]Error:\033[0mSendIMSI Failed to Launch, " + str(e))
		time.sleep(2)
		ss7main.Fraud()


def mtsms():
	try:
		mtForwardSMS = check_call(['java', '-jar', mtsms_path])
		if mtForwardSMS == 0:
			fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if fr == 'y' or fr == 'yes':
				ss7main.Fraud()
			elif fr == 'n' or fr == 'no':
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
		print("\033[31m[-]Error:\033[0mMTForwardSMS Failed to Launch, ", str(e))
		time.sleep(2)
		ss7main.Fraud()
	

def cl():
	try:
		cancelLocation = check_call(['java', '-jar', cl_path])
		if cancelLocation == 0:
			fr = input('\nWould you like to go back to Fraud Menu? (y/n): ')
			if fr == 'y' or fr == 'yes':
				ss7main.Fraud()
			elif fr == 'n' or fr == 'no':
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
		print("\033[31m[-]Error:\033[0mCancelLocation Failed to Launch, ", str(e))
		time.sleep(2)
		ss7main.Fraud()
