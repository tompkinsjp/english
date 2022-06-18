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
'sent', 'set', 'sewed', 'shook', 'shone', 'shot', 'showed', 'shrank', 'shut', 'sang', 
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
questwords = ['who', 'what', 'when', 'where', 'why', 'which', 'whose', 'how']

rawsent = ' '
while rawsent !='quit':

    rawsent = input("Enter a sentence or type 'quit' to exit: ").lower()

    for item in punct:
        if item in rawsent:
            stripsent = rawsent.strip(item)

    if rawsent == 'quit':
        break
    
    sent = stripsent.split(' ')
    
    time = 'Unknown'
    tense = 'Unknown'
    
    #Start Time Test
    for item in past_pre:
        if item in sent:
            time = 'the past.'
            
    for item in pres_pre:
        if item in sent and item != 'have':
            time = 'the present.'
    
    #End Time Test
    
    # Start Modals Test
    for item in modals:
        if item in rawsent:
            if 'have' in sent or 'been' in sent:
                time = 'time for a deadline.'
            elif item == 'could' and 'if' not in sent and '?' not in rawsent:
                time = 'the past.'
            else:
                time = 'the present-to-future.'
            thismodal = item
            if thismodal == 'can':
                tense = "believes the action to be possible or has this ability in"
            if thismodal == 'could' and time != 'the past.':
                if '?' in rawsent:
                    tense = "is addressing the listener, requesting him/her to do something in"
                else:
                    tense = "imagines the action to be one of many options in"
            elif thismodal == 'could' and time == 'the past.':
                tense = "had the ability to do the action in"
            if thismodal == "shall":
                tense = "is inviting/telling the listener to join the Subject in an activity in"
            if thismodal == 'should':
                tense = 'believes the action to be the correct one in'
            if thismodal == 'will':
                tense = "intends/promises to do the action, or predicts an outcome in"
            if thismodal == "won't":
                tense = "doesn't intend to do the action, or predicts a negative outcome in"
            if thismodal == 'would':
                if '?' in rawsent:
                    tense = "is requesting the listener to do something, or is making an offer in"
                elif sent[sent.index(item)+1] == 'like':
                    tense = "is making a request or stating a preference in"
                else:
                    tense = "is making a hypothetical offer or prediction in"
            if thismodal == 'may':
                if '?' in rawsent:
                    tense = "is asking permission to do something in"
                else:
                    tense = "is giving permission to do something, or is not sure about the outcome in"
            if thismodal == 'might':
                tense = "is not sure about the outcome in"
            if thismodal == 'must':
                tense = "is requiring that an action be done, or believes that an event is objectively true in"
    
    # End Modals Test                
    
    if tense == 'Unknown':
        # Start Continuous/Simple Test            
        for item in be_pre:
            if item in sent:
                formofbe = item
                if 'ing' in sent[sent.index(item)+1] or 'ing' in sent[sent.index(item)+2]:
                    tense = 'is mid-action or eliciting a feeling in'
                else:
                    for item in Verb3:
                        if item in sent or 'ed' in rawsent:
                           tense = "is the receiver of an action or feeling in"
                           break
                    else:
                        tense = "embodies a quality or characteristic in"
                        break
                if 'being' in sent:
                    for item in Verb3:
                        if item in sent or 'ed' in rawsent:
                            tense = 'is continuing to receive an action or feeling in'
                            break
                    else:
                        tense = "is continuing to embody a characteristic in"
                        break
        #End Continuous/Simple Test
    
    if tense == 'Unknown':
        #Start Perfect/Perfect Continuous Test
        have_count = 0
        for item in have_pre:
            if item in rawsent:
                have_count = rawsent.count('has') + rawsent.count('have') + rawsent.count('had')
                if 'been' in sent:
                    if 'ing' in rawsent:
                        tense = 'is continuing to do an activity which started some time before'
                        break
                    for item in Verb3:
                        if (item in sent and item != 'been') or 'ed' in rawsent:
                            tense = 'is the receiver of an action or feeling up to'
                            break
                    else:
                        tense = "has embodied a quality or characteristic up to"
                        break                    
                else:
                    for item in Verb3:
                        if have_count == 1 and (item not in sent or item == 'had') and 'ed' not in rawsent:
                            tense = "possesses something in"
                            continue
                        elif (item in sent and item != 'been') or 'ed' in rawsent:
                            tense = 'is looking back to a previous time or times from'
                            break
                        else:
                            continue          
        #End Perfect/Perfect Continuous Test
    
    # Start Past Simple Test
    if tense == 'Unknown':
        for item in Verb2:
            if item in sent or 'did' in rawsent or 'ed' in rawsent:
                time = 'the past.'
                tense = 'completed an action in'
                break
    
    # Catch-all category: Present Simple
    if time == 'Unknown':
        time = 'the present.'
    if tense == 'Unknown':
        tense = 'is expressing an internal state or regular activity in'

    print ()
    print ('The Subject', tense, time)
    print ()

print ()
print ('Goodbye!')