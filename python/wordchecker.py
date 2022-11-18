""" A code to create a search engine """

word = input('Enter the word you want to search: ')
word_con = word.upper()
text = 'd would a worshiper who misses three of the four rak\'ahs say on his own (a) three (b) two (c) one (d) five. A Muslim should not practice the following Shirk: (a) superstitions (b) consultation of elders (c) participation on the recitation of the Quran (d) none of the above. One of the following is not an example of superstition (a) using Rosary for the glorification of Allah (b)Ascribing evil to twin babies (c) ascribing ill- luck to sitting at the door of a house (d) regarding a number as an unlucky number'
text_up = text.upper()
text_list = text_up.split()
text_length = len(text_list)
word_count = text_list.count(word_con)
word_perc = word_count/text_length*100
word_perc_round = round(word_perc, 2)

#print(word_count)
if word_con in text_up:
    print(f'{word} is found in the text {word_count} times making {word_perc_round} % of the whole text')
else:
    print(f'word {word} not found')
