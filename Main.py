import random

words=["cat", "hello", "turnip", "mathematics", "physics"]
#secret_word=words[int(random.random()*len(words))]
secret_word = random.choice(words)
word = list(secret_word)
dashes = "-"*len(secret_word)
turns = 10
def rep(arr, loc, let):
    arr = list(arr)
    arr[loc] = let
    arr="".join(arr)
    return arr

def get_guess(dashes, word, turns):
    try:
        dashes.index("-")
        print str(turns) + " incorrect guesses left"
        let = raw_input("Guess: ")
        if len(let) > 1:
            print "Your guess must have exactly one character!"
        elif ord(let) < 92:
            print "Your guess must be a lowercase letter!"
        else:
            try:
                if word.index(let) != -1:
                    print "That letter is in the secret word!"
                    dashes = update_hashes(secret_word, dashes, let)
                    print dashes
                    return dashes, turns
            except ValueError as e:
                print "That letter is not in the secret word!"
                print dashes
                turns -= 1
                if turns == 0:
                    print "You lose. The word was: " + secret_word
                return dashes, turns

    except ValueError as e:
        print "Congrats! You win. The word was: "+"".join(word)
        turns = 100
        return dashes, turns

def update_hashes(word, dashes, guess):
    for i in range(len(secret_word)):
        if (guess == secret_word[i]):
            dashes = rep(dashes, i, guess)
    return dashes

print dashes
if turns > 0:
    while turns > 0:
        a = get_guess(dashes, word, turns)
        if a != None:
            dashes, turns = a
        if turns == 100:
            break;
else:
    print "You lose. The word was: " + secret_word
