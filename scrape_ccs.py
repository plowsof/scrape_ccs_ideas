import requests
from bs4 import BeautifulSoup
import pprint
import string
d = dict(enumerate(string.ascii_lowercase, 1))

resp = requests.get("https://ccs.getmonero.org/ideas/")
soup = BeautifulSoup(resp.content, 'html.parser')

soup = soup.find('section', class_='ideas')
ideas = soup.children

ideas_data = []

for idea in ideas:
	try:
		for item in idea.find_all('a'):
			title = item.find('h3').text
			link = item['href']
			data = { "title": title, "href": link}
			ideas_data.append(data)
	except:
		pass

template = """<pre>Plowsof has just saved you atleast 15 minutes of your life, do the needful sir:
88UbURD1esv6wJNqLEvJFn82JbX6awYW2BW4Sj2E3rahQbxP2C4FgGS6tdLp2wdPHJZ4PjgjuZbfi139oZ3LK9gcMXugv7C

Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
xx:xx UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: Unknown

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
News: [Monero Observer](https://www.monero.observer/) - [Monero Moon](https://www.themoneromoon.com/) - [Monero Revuo](https://revuo-xmr.com/)
4. [CCS updates](https://ccs.getmonero.org/)    """

i = 0
for idea in ideas_data:
	x=(i+1)
	try:
		template += f"  {d[x]}. [{idea['title']}]({idea['href']})    \n"
	except Exception as e:
		raise e
		pass
	i+=1

template += """5. Workgroup reports    </br>
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
6. Open ideas time    
7. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/)    

Meeting logs will be posted here afterwards.    </pre>"""

with open("/var/www/html/meeting_template.html", "w+") as f:
	f.write(template)

print("done")
