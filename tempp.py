spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat'] * 10
print(spam)
print(len(spam))
for i in range(len(spam)):
    try:
        spam.remove('cat')
        print(spam)
    except:
        print('Done')
        break
