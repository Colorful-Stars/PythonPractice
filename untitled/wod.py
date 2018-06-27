#coding=utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
text_from_file_with_apath = open('recom.txt',encoding='utf-8').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
# print(wl_space_split)
my_wordcloud = WordCloud(background_color='white',width=1000,height=600,min_font_size=20,max_words=50,max_font_size=80).generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
