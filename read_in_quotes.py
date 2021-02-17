# Welcome to the real world, I hope you'll enjoy it!
# author: Steve-P42
# creation date: 
# purpose:
# status:

# %%
import re
from random import randint

stoic_quotes_content = open("stoic_quotes.txt", "r", encoding='utf8')
stoic_quotes_content_txt = stoic_quotes_content.read()

distinct_quotes = re.split("\n\n", stoic_quotes_content_txt)

stoic_quotes_content.close()

random_int = randint(1, len(distinct_quotes)-1)
print(distinct_quotes[random_int])
# %%

# %%

# %%

# %%

# %%

# %%

# %%
