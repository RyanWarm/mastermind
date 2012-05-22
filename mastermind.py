#Mastermind is a game of two players.
#In the beginning, first player decides a secret key, which is a sequence
#(s1,s2,...sk) where 0 < si <= n.  Then second player makes guesses in rounds,
#where each guess is of form (g1,g2,...gk), and after each guess first player
#calculates the score for the guess.   Score for a guess is equal to number of i's 
#for which we have gi = si.
#
#For example, if the secret key is (4,2,5,3,1) and the guess is (1,2,3,7,1), then
#the score is 2, because g2 = s2 and g5 = s5.
#
#Given a sequence of guesses, and scores for each guess, your program must decides
#if there exists at least one secret key that generates those exact scores.
#
#Input
#
#First line of input contains a single integer C (1 <= C <= 100).  C test-cases follow.
#First line of each test-case contains three integers n, k, and q.  (1 <=n, k <= 11,
#1 <= q <= 8).  Next q lines contain the guesses.
#
#Each guess consists of k integers gi,1, gi,2,....gi,k separated by a single space, followed
#by the score for the guess bi (1 <= gi, j <=n for all 1 <=i <=q, 1 <=j <=k; and 0 <= bi <= k)
#
#Output
#
#For each test-case, output "Yes" (without quotes), if there exists at least a secret key which
#generates those exact scores, otherwise output "No".
#
#Sample Input
#2
#
#4 4 2
#2 1 2 2 0
#2 2 1 1 1
#4 4 2
#1 2 3 4 4
#4 3 2 1 1
#
#Sample Output
#
#Yes
#No

#####################
# Get the user data #
#####################
def get_data():
	v = []
	while (True):
		try:
			temp = raw_input()
			if not(temp == ''):
				v.append(temp)
		except:
			return v

#############################
# Main Routine - Mastermind #
#############################
def mastermind():

	#Get the input data
	data = get_data()
	data.reverse()

	#Get the number of TCs
	TC = int(data.pop())

	#Main loop
	while (TC > 0):

		#Data about the next few lines
		initial = data.pop()
		initial = initial.split()
		n = int(initial[0]) #Number of valid values
		k = int(initial[1]) #Number of positions
		q = int(initial[2]) #Number of guesses
		player2 = []
		for i in range(q):
			player2.append(data.pop())

		#Print the result
		print search_for_key(n,k,q,player2)

		#Move on to the next TC
		TC -= 1

####################################################
# Routine to determine if there exists a valid key #
####################################################
def search_for_key(n,k,q,player2):

	#reminder:
	#n = number of valid values
	#k = number of positions
	#q = number of guesses

	#This will hold all the guesses
	guesses = {}
	#This will hold all the valid possibilities
	possible = [[y+1 for y in range(n)] for x in range(k)] 

	#Store the player 2 results in guesses
	#Will take on this format:
	# number correct (key): guesses that resulted in that value (values)
	for results in player2:
		z = int(results[-1])
		if z in guesses:
			guesses[z].append([int(results[x]) for x in range(len(results)-1) if results[x] != " "])
		else:
			guesses[z] = [[int(results[x]) for x in range(len(results)-1) if results[x] != " "]]

	#There are two special scenarios:
	#Correct = 0 (got nothing right)
	#Correct = k (got everything right)
	#In both scenarios, it's clear, without ambiguity, what the implication is
	
	#Start with correct = k
	if k in guesses:
		i = True
		for valids in guesses[k]:
			if i:
				for j in range(k):
					possible[j] = [valids[j]]
				fatal_check = valids
				i = False
			else:
				#Contradiction - can't have more than one type of 'perfect' response
				if fatal_check != valids:
					return 'No'

	#Now process correct = 0
	if 0 in guesses:
		for invalids in guesses[0]:
			for j in range(k):
				new_val = []
				for i in range(len(possible[j])):
					if possible[j][i] != invalids[j]:
						new_val.append(possible[j][i])
				#Exhausted all possibilities - no possibilities left
				if not(new_val):
					return 'No'
				possible[j] = new_val

	#Number of possibilities
	total = 1
	for p in possible:
		total *= len(p)

	#generate possibility blocks
	poss_dictionary = {}
	for i in range(total):
		poss_dictionary[i] = [0 for x in range(k)]

	#populate possibility blocks
	k = 0
	prior = 1
	for pos_i in possible:
		j = 0
		i = 0
		block_size = total / len(pos_i) / prior
		while i < total:
			poss_dictionary[i][k] = pos_i[j]
			i += 1
			if i % block_size == 0:
				j +=1
				if j == len(pos_i):
					j = 0
		k += 1
		prior *= len(pos_i)

	#Now loop through each of the remaining guesses, and validate the score
	#against the possible values array
	for score in guesses:
		if score > 0 and score < k:
			for guess in guesses[score]:
				del_p = []
				for p_key in poss_dictionary:
					if score != compute_score(poss_dictionary[p_key],guess):
						#poss_dictionary.pop(p_key)
						del_p.append(p_key)
				for i in range(len(del_p)):
					poss_dictionary.pop(del_p[i])
				if len(poss_dictionary) == 0:
					return 'No'

	#Success!
	return 'Yes'
	#return poss_dictionary


def compute_score(key,guess):

	score = 0
	for i in range(len(key)):
		if key[i] == guess[i]:
			score += 1

	return score


mastermind()
