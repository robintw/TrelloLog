import json
import requests
import datetime

html_file = 'log.html'
temp_file = 'log.txt'

data = json.loads(requests.get('https://api.trello.com/1/search?query=is:archived%20edited:day&boards_limit=1000&cards_limit=1000&key=929470fcedf0e012b8d8b77e03d3e824&token=24bf22a217610e1f81e7606add59baacd162a931e342fdf77938478d421fa565').text)

finished_cards = [x['name'] for x in data['cards']]

date = datetime.datetime.now().strftime('%Y-%m-%d')


html = """<h2>{date}</h2>
<ul>""".format(date=date)

for card in finished_cards:
	html += "\n<li>{item}</li>".format(item=card)

html += "\n</ul>"

print html

with open('log.txt', 'r') as f:
	prev_contents = f.read()


new_contents = html + "\n" + prev_contents

with open('log.txt', 'w') as f:
	f.write(new_contents)

html_top = """<html>
<head>
<title>Trello Log</title>
</head>

<body>
<h1>Trello Log</h1>
"""

html_bottom = """</body>
</html>"""

full_html = html_top + new_contents + html_bottom

with open('log.html', 'w') as f:
	f.write(full_html)