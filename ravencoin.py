'''
*Python-based remedy to do moar on RVN

*Author: JonPizza @ Github, UserJonPizza#4510 @ Ravencoin Community Discord
'''
# IMPORT MODULES

import subprocess
from subprocess import call

import time
'''
command = ['echo', 'I like potatoes']
proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()


output = o.decode('ascii')
error = e.decode('ascii')

print(type(output))
'''

base = './raven-cli'

filepath = '~/Downloads/raven-2.2.2.0/bin'
call(f'cd {filepath}', shell=True)
call('./ravend', shell=True)

class ravencoin:
	class mine:
		def begin(cores=2):
			call(f'{base} setgenerate true {cores}', shell=True)
			print(f'Mining on CPU with {cores} core(s).')

		def end():
			call(f'{base} setgenerate true 0', shell=True)
			print(f'Mining across all cores terminated.')
		

	def __init__(self, passphrase, sender_addr, open_ravend_on_start = True):
		self.passphrase = passphrase
		self.sender_addr = sender_addr

		if open_ravend_on_start == True:
			call('./home/jon/Downloads/raven-2.2.2.0/bin/ravend', shell=True)
		print('The Ravencoin Module Has Started')


	'''
	Some general stuff Here:
	'''


	def unlock(self, timeout=600):
		call(f'{base} walletpassphrase {self.passphrase} {timeout}', shell=True)
		print(f'Wallet unlocked for {timeout} seconds.')

	def get_bal():
		call(f'{base} getbalance', shell=True)
		return get_bal


	# To Go into sending 
	def send_rvn(self, amount, reciver):
		pass

	def send_asset(self, asset, amount, reciver):
		pass



if __name__ == '__main__':
	rvn = ravencoin('my_passphrase', 'my_address')

	rvn.unlock(3600)
	rvn.mine.begin()
	time.sleep(10)
	rvn.mine.end()

