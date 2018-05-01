from functools import reduce

punctuation = ''',.?/'";:()!'''
white_space = "\n\t "

with open('trial.txt', 'rb') as trial:
    trial_text = trial.read()
    trial_words = trial_text.split()
    for words in trial_words:
        words.strip(punctuation + white_space)
        
def freq_word(chosen_word):
    freq = reduce((lambda x, y: x + y), [1 if word == chosen_word else 0 for word in trial_words] )
    #print chosen_word + ":\t" + str(freq)
    return freq

def freq_words(group):
    for sel_word in group: #just for testing purposes, can check the sum if the parts are counted
        freq = reduce((lambda x, y: x + y), [1 if word == sel_word else 0 for word in trial_words] )
        print sel_word + ":\t" + str(freq)
    
    freq = reduce((lambda x, y: x + y), [1 if word in group else 0 for word in trial_words] )
    print "total: \t" + str(freq)
    return freq

def highest_freq_terrible():
    highest_word = ''
    highest_freq = 0
    set_of_words = set(trial_words)
    for word in set_of_words:
        freq = freq_word(word)
        if highest_freq < freq:
            highest_freq = freq
            highest_word = word
            print "new high: " + str(highest_freq)
    print highest_word
    print highest_freq

def highest_freq():
    set_of_words = set(trial_words)
    freqs = [freq_word(word) for word in set_of_words]
    print freqs
    print max(freqs)
    
chosen_word = "people"
group = ["people" , "justice", "guilty", "free", "mean", "door"]

freq_word(chosen_word)
freq_words(group)
#highest_freq_terrible()
highest_freq()

print reduce((lambda x, y: x + y), [1 for word in trial_words] )
