import re

txt = 'I am the servant of Lord Shree Ram'
x = re.search('^I.*Ram$', txt)

if x: 
    print('Yes we have the match')
else:
    print('No match')