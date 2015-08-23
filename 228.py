#!/usr/bin/env python

'''
Description

A handful of words have their letters in alphabetical order, that is nowhere in the word do you change direction in the word if you were to scan along the English alphabet. An example is the word "almost", which has its letters in alphabetical order.
Your challenge today is to write a program that can determine if the letters in a word are in alphabetical order.
As a bonus, see if you can find words spelled in reverse alphebatical order.
Input Description

You'll be given one word per line, all in standard English. Examples:
almost
cereal
Output Description

Your program should emit the word and if it is in order or not. Examples:
almost IN ORDER
cereal NOT IN ORDER

Challenge Input

billowy
biopsy
chinos
defaced
chintz
sponged
bijoux
abhors
fiddle
begins
chimps
wronged

Challenge Output

billowy IN ORDER
biopsy IN ORDER
chinos IN ORDER
defaced NOT IN ORDER
chintz IN ORDER
sponged REVERSE ORDER 
bijoux IN ORDER
abhors IN ORDER
fiddle NOT IN ORDER
begins IN ORDER
chimps IN ORDER
wronged REVERSE ORDER
'''

def main(): 
	## open the file first
	with open('228.txt', 'r') as f: 
		var = f.readlines()
		lines = [x.strip() for x in var]
		## now all the lines are stored as a list in lines variable

		for line in lines : 
			flag = 0
			i = 0
			## traversing the individual characters 
			while i < len(line):
				if i >=len(line): 
					break 
				else :
					try : 
						if ord(line[i]) > ord(line[i+1]) : 
							flag = 1
					except Exception as e : 
						pass
				i += 1

			if flag == 1 : 
				print line + ' NOT IN ORDER'
			else : 
				print line + ' IN ORDER'

if __name__ == '__main__' : 
	main()

