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

	#get the input data
	data = get_data()
	data.reverse()

	#get the number of TCs
	TC = int(data.pop())

	#main loop
	while (TC > 0):

		#data about the next few lines
		initial = data.pop()
		n = int(initial[0:1]) #number of valid values
		k = int(initial[2:3]) #number of positions
		q = int(initial[4:5]) #number of guesses
		player2 = []
		for i in range(q):
			player2.append(data.pop())

		print search_for_key(n,k,q,player2)

		TC -= 1

####################################################
# Routine to determine if there exists a valid key #
####################################################
def search_for_key(n,k,q,player2):

	guesses = {}
	possible = [[y+1 for y in range(n)] for x in range(k)]
	fast_check = False

	#Store the player 2 results
	for results in player2:
		print 'results:', results
	return
#		z = int(results[-1])
#		if z in guesses:
#			guesses[z].append([int(results[x]) for x in range(len(results)-1) if results[x] != " "])
#		else:
#			guesses[z] = [[int(results[x]) for x in range(len(results)-1) if results[x] != " "]]

	#Start with the most limiting scenario (correct = k)
	if k in guesses:
		temp = guesses[k]
		for i in range(k):
			possible[i] = [temp[0][i]]
		fast_check = True

	#Second most-limiting scenario (correct = 0)
	if 0 in guesses and not(fast_check):
		eraser = []
		for guess in guesses[0]:
			print 'guess: ', guess






#		temp = guesses[0]
#		for guess in temp:
#			for i in range(k):
#				for guess[i] in possible[i]: 
#					possible[i].remove(guess[i])
#		fast_check = True
#		for i in range(k):
#			if len(possible[i]) != 0:
#				fast_check = False
#				break

	#Check for fast-check execution
	#if fast_check:
	return validate_mm(possible,guesses)

	#No fast-check execution - slower processing






	#keys = guesses.keys()


	#print 'keys: ', keys
	#print 'guesses: ', guesses

	#return 'undef'

def validate_mm(possible,guesses):

	print 'possible', possible
	for guess in guesses:
		print 'guesses: ', guesses[guess]

	for guess in guesses:
		temp = guesses[guess]
		for act_guesses in temp:
			check = 0
			for x in range(len(act_guesses)):
				if act_guesses[x] in possible[x]:
					check += 1
			if check != guess:
				return 'No'

	return 'Yes'



mastermind()
