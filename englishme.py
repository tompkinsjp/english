be_pre = ['am', 'is', 'are', 'was', 'were']
have_pre = ['has', 'have', 'had']
do_pre = ['do', 'did']
past_pre = ['was', 'were', 'had', 'did', "didn't"]
pres_pre = ['am', 'is', 'are', 'has', 'have', 'do', "don't", 'does', "doesn't"]

modals = ['can', 'could', 'shall', 'should', 'will', "won't", 'would', 'may', 'might', 'must']

Verb2 = ['arose', 'awoke', 'bore', 'was', 'were', 'beat', 'became', 'began', 'bent', 'bet', 
'bound', 'bit', 'bled', 'blew', 'broke', 'bred', 'brought', 'built', 'burst', 'burnt',   
'bought', 'cast', 'caught', 'chose', 'clung', 'came', 'cost', 'crept', 'cut', 'dealt', 
'dug', 'did', 'drew', 'dreamt', 'drank', 'drove', 'ate', 'fell', 'fed', 'felt', 
'fought', 'found', 'fled', 'flung', 'flew', 'forbade', 'forgot', 'forgave', 'froze', 'got', 
'gave', 'went', 'ground', 'grew', 'hung', 'had', 'heard', 'hid', 'hit', 'held', 
'hurt', 'kept', 'knew', 'laid', 'led', 'leant', 'left', 'lent', 'let', 'lay', 
'lit', 'lost', 'made', 'meant', 'met', 'mislaid', 'misled', 'paid', 'put', 'quit', 
'read', 'rode', 'rang', 'rose', 'ran', 'sawed', 'said', 'saw', 'sought', 'sold', 
'wordList', 'set', 'sewed', 'shook', 'shone', 'shot', 'showed', 'shrank', 'shut', 'sang', 
'sank', 'sat', 'slept', 'slid', 'sowed', 'spoke', 'spent', 'spun', 'spilt', 'spread', 
'sprang', 'stood', 'stole', 'stuck', 'stung', 'stank', 'strode', 'struck', 'swore', 'swept', 
'swam', 'swung', 'took', 'taught', 'tore', 'told', 'thought', 'threw', 'trod', 'understood', 
'woke', 'wore', 'wept', 'won', 'wound', 'wrote']

Verb3 = ['arisen', 'awoken', 'born', 'been', 'beaten', 'become', 'begun', 'bent', 'bet', 'bound', 
'bitten', 'bled', 'blown', 'broken', 'bred', 'brought', 'built', 'burst', 'burnt', 'bought', 
'cast', 'caught', 'chosen', 'clung', 'come', 'cost', 'crept', 'cut', 'dealt', 'dug', 
'done', 'drawn', 'dreamt', 'drunk', 'driven', 'eaten', 'fallen', 'fed', 'felt', 'fought', 
'found', 'fled', 'flung', 'flown', 'forbidden', 'forgotten', 'forgiven', 'frozen', 'got', 'given', 
'gone', 'ground', 'grown', 'hung', 'had', 'heard', 'hidden', 'hit', 'held', 'hurt', 
'kept', 'known', 'laid', 'led', 'leant', 'left', 'lent', 'let', 'lain', 'lit', 
'lost', 'made', 'meant', 'met', 'mislaid', 'misled', 'paid', 'put', 'quit', 'read', 
'ridden', 'rung', 'risen', 'run', 'sawn', 'said', 'seen', 'sought', 'sold', 'sent', 
'set', 'sewn', 'shaken', 'shone', 'shot', 'shown', 'shrunk', 'shut', 'sung', 'sunk', 
'sat', 'slept', 'slid', 'sown', 'spoken', 'spent', 'spun', 'spilt', 'spread', 'sprung', 
'stood', 'stolen', 'stuck', 'stung', 'stunk', 'stridden', 'struck', 'sworn', 'swept', 'swum', 
'swung', 'taken', 'taught', 'torn', 'told', 'thought', 'thrown', 'trodden', 'understood', 'woken', 
'worn', 'wept', 'won', 'wound', 'written']

punct = ['.', ',', '!', '?', ':', ';']

rawsent = "Hello! I am computer trying to learn good English. Can you write me something so I can learn?"
print(rawsent)

while "quit" not in rawsent:

	rawsent = input().lower()
	print()
	
	for item in punct:
		if item in rawsent:
			stripsent = rawsent.strip(item)
		else:
			stripsent = rawsent

	if rawsent == 'quit':
		break
    
	wordList = stripsent.split(' ')
    
	time = 'Unknown'
	tense = 'Unknown'

	#Start Time Test
	for item in past_pre:
		if item in wordList:
			time = 'in the past.'
			
	for item in Verb2:
		if item in wordList:
			time = 'in the past.'
            
	for item in pres_pre:
		if item in wordList and item != 'have':
			time = 'now.'
    
	#End Time Test
    
	# Start Modals Test
	for item in modals:
		if item in rawsent:
			if 'have' in wordList or 'been' in wordList:
				time = 'by some time.'
			elif item == 'could' and 'if' not in wordList and '?' not in rawsent:
				time = 'before.'
			else:
				time = 'some time soon.'
			thismodal = item
			if thismodal == 'can':
				tense = "believes something is possible, or has the ability to do something"
			if thismodal == 'could' and time != 'the past.':
				if '?' in rawsent:
					tense = "is talking to me, requesting me to do something"
				else:
					tense = "imagines something to be one possible option"
			elif thismodal == 'could' and time == 'in the past.':
				tense = "had the ability to do something"
			if thismodal == "shall":
				tense = "is inviting me to join someone else in activity"
			if thismodal == 'should':
				tense = 'believes something to be right or wrong choice'
			if thismodal == 'will':
				tense = "intend or promise to do something, or predicts a positive outcome"
			if thismodal == "won't":
				tense = "doesn't want to do something, or predicts a negative outcome"
			if thismodal == 'would':
				if '?' in rawsent:
					tense = "is requesting me to do something, or are making an offer"
				elif wordList[wordList.index(item)+1] == 'like':
					tense = "is making a request for something"
				else:
					tense = "is speaking hypothetically about something"
			if thismodal == 'may':
				if '?' in rawsent:
					tense = "is asking permission to do something"
				else:
					tense = "is giving permission to do something"
			if thismodal == 'might':
				tense = "isn't sure about the outcome"
			if thismodal == 'must':
				tense = "requires that something be done, or believe that something is actually true"
    
	# End Modals Test                
    
	if tense == 'Unknown':
		# Start Continuous/Simple Test            
		for item in be_pre:
			if item in wordList:
				if 'ing' in rawsent:
					tense = 'is in the middle of doing or feeling something'
				else:
					for item in Verb3:
						if item in wordList or 'ed' in rawsent:
							tense = "is passive about something"
							break
						else:
							tense = "embodies a special quality"
							break
				if 'being' in wordList:
					for item in Verb3:
						if item in wordList or 'ed' in rawsent:
							tense = 'is continuing to be passive about something'
							break
						else:
							tense = "is continuing to have a special quality"
							break
		#End Continuous/Simple Test
    
	if tense == 'Unknown':
		#Start Perfect/Perfect Continuous Test
		have_count = 0
		for item in have_pre:
			if item in rawsent:
				have_count = rawsent.count('has') + rawsent.count('have') + rawsent.count('had')
				if 'been' in wordList:
					if 'ing' in rawsent:
						tense = 'is continuing to do something that started before'
						break
					for item in Verb3:
						if (item in wordList and item != 'been') or 'ed' in rawsent:
							tense = 'is the receiver of an action or feeling up to'
							break
					else:
						tense = "has a special quality up to"
						break                    
				else:
					for item in Verb3:
						if have_count == 1 and (item not in wordList or item == 'had') and 'ed' not in rawsent:
							tense = "possesses something"
							continue
						elif (item in wordList and item != 'been') or 'ed' in rawsent:
							tense = ' is looking back to something from'
							break
						else:
							continue          
		#End Perfect/Perfect Continuous Test
    
	# Start Past Simple Test
	if tense == 'Unknown':
		for item in Verb2:
			if item in wordList or 'did' in rawsent or 'ed' in rawsent:
				time = 'the past.'
				tense = 'completed something in'
				break
    
	# Catch-all category: Present Simple
	if time == 'Unknown':
		time = 'now.'
	if tense == 'Unknown':
		tense = 'feels or act this way a lot'

	print ()
	print ("My English not so good, but I think someone", tense, time)
	print ()

print ()
print ('OK, bye!')
