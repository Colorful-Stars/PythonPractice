#coding=utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
 
text_from_file_with_apath = open('大学门卫老董未删全本(www.lashu8.com).txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
print(wl_space_split)
my_wordcloud = WordCloud(background_color='white',scale=1.5).generate(wl_space_split)
 
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
