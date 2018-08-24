spam = ['apples', 'bananas', 'tofu', 'cats']
spamString = ''
for i in range(len(spam)):
    if i == (len(spam) - 1):
#        print('and ' + spam[i])
        spamString += ('and ' + spam[i])
    else:
#        print(spam[i])
        spamString += (spam[i]+', ')
print(spamString)
