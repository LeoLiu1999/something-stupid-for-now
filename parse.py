from functools import reduce

punctuation = ''',.?/'";:()!'''
white_space = "\n\t "

with open('trial.txt', 'rb') as trial:
    trial_text = trial.read()
    trial_words = trial_text.split()
    for words in trial_words:
        words.strip(punctuation + white_space)
        
group = ["people" , "justice", "guilty", "free", "mean", "door"]
    
freq_people = reduce((lambda x, y: x + y), [1 if word == 'people' else 0 for word in trial_words] )



for sel_word in group:
    freq_people = reduce((lambda x, y: x + y), [1 if word == sel_word else 0 for word in trial_words] )
    print freq_people
    
freak_group = reduce((lambda x, y: x + y), [1 if word in group else 0 for word in trial_words] )

print freak_group

'''
The PLan:
lam

    
    
