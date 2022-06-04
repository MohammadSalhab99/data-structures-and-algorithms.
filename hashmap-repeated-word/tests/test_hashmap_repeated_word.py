from hashmap_repeated_word.hashmap import repeatedWord
print( repeatedWord(
    'Once upon a time, there was a brave princess who...') )

print (repeatedWord('''It was the best of times, it was the worst of times,
                     it was the age of wisdom, it was the age of foolishness,
                     it was the epoch of belief, it was the epoch of incredulity,
                     it was the season of Light, it was the season of Darkness,
                     it was the spring of hope, it was the winter of despair, 
                     we had everything before us, we had nothing before us, we were
                     all going direct to Heaven, we were all going direct the other way – 
                     in short, the period was so far like the present period, that some of 
                     its noisiest authorities insisted on its being received, for good or for 
                     evil, in the superlative degree of comparison only...''')) 
print(repeatedWord('''It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...

'''))

str1 =  'Once upon a time, there was a brave princess who...'

str2 = '''It was the best of times, it was the worst of times,
                     it was the age of wisdom, it was the age of foolishness,
                     it was the epoch of belief, it was the epoch of incredulity,
                     it was the season of Light, it was the season of Darkness,
                     it was the spring of hope, it was the winter of despair, 
                     we had everything before us, we had nothing before us, we were
                     all going direct to Heaven, we were all going direct the other way – 
                     in short, the period was so far like the present period, that some of 
                     its noisiest authorities insisted on its being received, for good or for 
                     evil, in the superlative degree of comparison only...'''

str3 = '''It was a queer, sultry summer, the summer they electrocuted the Rosenbergs,
             and I didn’t know what I was doing in New York...'''
def test_str1():
    actual =  repeatedWord(str1)
    expected =  'a'
    assert actual ==expected

def test_str2():
    actual = repeatedWord(str2)
    expected =  'it'
    assert actual ==expected

def test_str3():
    actual =  repeatedWord(str3)
    expected =  'summer'
    assert actual ==expected

def test_empty_str():
    actual =  repeatedWord("")
    expected =  'empty string'
    assert actual ==expected
    
    

