import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

text = open(r'text.txt',mode='r', encoding='utf-8').read()

# To create a simple wordcloud:
wc = WordCloud(stopwords = STOPWORDS,
               background_color = "white",
               max_words = 2000, max_font_size = 500,
               random_state = 42)
wc.generate(text)
plt.imshow(wc, interpolation="None")
plt.axis('off')
plt.show()

# To create a wordcloud of any particular shape or image:
mask = np.array(Image.open(r'gfg.png'))
wc = WordCloud(stopwords = STOPWORDS,
               mask = mask, background_color = "white",
               max_words = 2000, max_font_size = 500,
               random_state = 42, width = mask.shape[1],
               height = mask.shape[0])
wc.generate(text)
plt.imshow(wc, interpolation="None")
plt.axis('off')
plt.show()



### resources: https://www.geeksforgeeks.org/generate-word-clouds-of-any-shape-in-python/
