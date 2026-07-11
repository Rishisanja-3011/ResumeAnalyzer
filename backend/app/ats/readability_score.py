def analyze_readability(text):


    words = text.split()


    word_count = len(words)


    if word_count < 200:

        score = 60


    elif word_count <= 700:

        score = 100


    else:

        score = 70



    return {

        "score": score,

        "word_count": word_count
    }