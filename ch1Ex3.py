#!/usr/bin/env python3

import random

verbs = ['be', 'have', 'do', 'say', 'go', 'get', 'make', 'know', 'think', 'take', 'see', 'come', 'want', 'use', 'find', 'give', 'tell', 'work', 'call', 'try', 'ask', 'need', 'feel', 'become', 'leave', 'put', 'mean', 'keep', 'let', 'begin', 'seem', 'help', 'show', 'hear', 'play', 'run', 'move', 'live', 'believe', 'bring', 'happen', 'write', 'sit', 'stand', 'lose', 'pay', 'meet', 'include', 'continue', 'set', 'learn', 'change', 'lead', 'understand', 'watch', 'follow', 'stop', 'create', 'speak', 'read', 'spend', 'grow', 'open', 'walk', 'win', 'teach', 'offer', 'remember', 'consider', 'appear', 'buy', 'serve', 'die', 'send', 'build', 'stay', 'fall', 'cut', 'reach', 'kill', 'raise', 'pass', 'sell', 'decide', 'return', 'explain', 'hope', 'develop', 'carry', 'break', 'receive', 'agree', 'support', 'hit', 'produce', 'eat', 'cover', 'catch', 'draw', 'choose']
nouns = ['word', 'letter', 'number', 'person', 'pen', 'class', 'people', 'sound', 'water', 'side', 'place', 'man', 'men', 'woman', 'women', 'boy', 'girl', 'year', 'day', 'week', 'month', 'name', 'sentence', 'line', 'air', 'land', 'home', 'hand', 'house', 'picture', 'animal', 'mother', 'father', 'brother', 'sister', 'world', 'head', 'page', 'country', 'question', 'answer', 'school', 'plant', 'food', 'sun', 'state', 'eye', 'city', 'tree', 'farm', 'story', 'sea', 'night', 'day', 'life', 'north', 'south', 'east', 'west', 'child', 'children', 'example', 'paper', 'music', 'river', 'car', 'foot', 'feet', 'book', 'science', 'room', 'friend', 'idea', 'fish', 'mountain', 'horse', 'watch', 'color', 'face', 'wood', 'list', 'bird', 'body', 'dog', 'family', 'song', 'door', 'product', 'wind', 'ship', 'area', 'rock', 'order', 'fire', 'problem', 'piece', 'top', 'bottom', 'king', 'space']
adverbs = ['often', 'rather', 'ever', 'once', 'thus', 'soon', 'today', 'perhaps', 'probably', 'already', 'however', 'really', 'together', 'quite', 'sometimes', 'therefore', 'else', 'outside', 'besides', 'beyond', 'indeed', 'inside', 'ago', 'how', 'so', 'then', 'there', 'no', 'now', 'just', 'very', 'where', 'too', 'also', 'well', 'again', 'why', 'here', 'still', 'off', 'away', 'always', 'almost', 'enough', 'though', 'never', 'since', 'round', 'instead', 'likely', 'especially', 'according', 'below', 'without', 'through', 'throughout', 'forward', 'forth', 'aside', 'otherwise', 'seldom', 'yesterday', 'tomorrow', 'moreover', 'friendly', 'somehow', 'plenty', 'somewhere', 'apart', 'beneath', 'everywhere', 'anywise', 'when', 'whenever', 'tonight', 'meanwhile', 'nowhere', 'altogether', 'yes', 'alike', 'usually', 'occasionally', 'rarely', 'actually', 'easily', 'hardly', 'quickly', 'slowly', 'above', 'little', 'much', 'even', 'before', 'lately', 'recently', 'almost', 'as', 'only']
articles = ['a', 'the']

counter = 0
while counter < 5:
    counter += 1
    verb = random.choice(verbs)
    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    article = random.choice(articles)
    construction = random.randint(0, 1)
    if construction:
        print(article + ' ' + noun + ' ' + verb + ' ' + adverb)
    else:
        print(adverb + ' ' + article + ' ' + noun + ' ' + verb)



