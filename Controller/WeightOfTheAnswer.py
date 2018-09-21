import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer




# part1 = 0
# # CC	coordinating conjunction
# # CD	cardinal digit
# # DT	determiner
# # EX	existential there (like: "there is" ... think of it like "there exists")
# # FW	foreign word
# # IN	preposition/subordinating conjunction
#
#
# part2 = 0
# # JJ	adjective	'big'
# # JJR	adjective, comparative	'bigger'
# # JJS	adjective, superlative	'biggest'
#
# part3 = 0
# # LS	list marker	1)
# # MD	modal	could, will
#
# part4 = 0
# # NN	noun, singular 'desk'
# # NNS	noun plural	'desks'
# # NNP	proper noun, singular	'Harrison'
# # NNPS	proper noun, plural	'Americans'
# # PDT	predeterminer	'all the kids'
# # POS	possessive ending	parent's
# # PRP	personal pronoun	I, he, she
# # PRP$	possessive pronoun	my, his, hers
#
# part5 = 0
# # RB	adverb	very, silently,
# # RBR	adverb, comparative	better
# # RBS	adverb, superlative	best
# # RP	particle	give up
#
# part6 = 0
# # TO	to	go 'to' the store.
# # UH	interjection	errrrrrrrm
#
# part7 = 0
# # VB	verb, base form	take
# # VBD	verb, past tense	took
# # VBG	verb, gerund/present participle	taking
# # VBN	verb, past participle	taken
# # VBP	verb, sing. present, non-3d	take
# # VBZ	verb, 3rd person sing. present	takes
#
# part8 = 0
# # WDT	wh-determiner	which
# # WP	wh-pronoun	who, what
# # WP$	possessive wh-pronoun	whose
# # WRB	wh-abverb	where, when







def process_content(useranswer):
    train_text = state_union.raw("2005-GWBush.txt")
    sample_text = state_union.raw("2006-GWBush.txt")

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

    tokenized = custom_sent_tokenizer.tokenize(useranswer)
    part1 = 0
    part2 = 0
    part3 = 0
    part4 = 0
    part5 = 0
    part6 = 0
    part7 = 0
    part8 = 0

    try:
        tagged = []
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

        for j in tagged:

            if(j[1] in ("CC","CD","DT","EX","FW","IN")):
                part1 = 1

            if (j[1] in ("JJ","JJR","JJS")):
                part2 = 1

            if (j[1] in ("LS","MD")):
                part3 = 1

            if (j[1] in ("NN", "NNS","NNP","NNPS","PDT","POS","PRP","PRP$")):
                part4 = 1

            if (j[1] in ("RB","RBR","RBS","RP" )):
                part5 = 1

            if (j[1] in ("TO","UH" )):
                part6 = 1

            if (j[1] in ("VB" ,"VBD" ,"VBG" ,"VBN" ,"VBP" ,"VBZ")):
                part7 = 1

            if (j[1] in ("WDT" ,"WP","WP$","WRB")):
                part8 = 1

        result = part1+part2+part3+part4+part5+part6+part7+part8
        if result>=3:
            return 0.1
        else:
            return 0.0

    except Exception as e:
        print(str(e))


