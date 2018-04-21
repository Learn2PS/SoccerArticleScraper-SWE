import requests
import datetime
from bs4 import BeautifulSoup, SoupStrainer

time = str(datetime.datetime.now())
today = str(datetime.date.today())

#Change this keyword to change which kind of articles are showing up!
keyword = 'aik'

#Switch for logging. If True will log to file named 'Script.log'. If False will run without logging.
logging = True

def response(url):
	resp = requests.get(url)
	if resp.status_code == 200:
		return resp.text

def html_parse(html):
	soup = BeautifulSoup(html, 'lxml')
	return soup

def append_file(link):

	file_object = open('links.txt','a')
	file_read = open('links.txt', 'r')
	link_already = 0
	date_already = 0
	status_str = ''

	for line in file_read:
		if today in line:
			date_already = date_already + 1
		else:
			continue
	if date_already == 0:
		file_object.write(today + '\n')

	file_object.close()
	file_read.close()
	file_object = open('links.txt','a')
	file_read = open('links.txt', 'r')

	if 'sportbladet' in link:
		for line in file_read:
			if link in line:
				link_already = link_already + 1
			else:
				continue

		if link_already == 0:
			file_object.write(link + '\n')
			print('Found new url: ' + link)
			status_str = status_str + 'Found new url: ' + link + '\n'
		if link_already == 1:
			print('URL found on Sportbladet Fotboll but has already been added!')
			status_str = status_str + 'URL found on Sportbladet Fotboll but has already been added!\n'
		return status_str

	if 'expressen' in link:
		for line in file_read:
			if link in line:
				link_already = link_already + 1
			else:
				continue
		if link_already == 0:
			file_object.write(link + '\n')
			print('Found new url: ' + link)
			status_str = status_str + 'Found new url: ' + link + '\n'
		if link_already == 1:
			print('URL found on Expressen Fotboll but has already been added!')
			status_str = status_str + 'URL found on Expressen Fotboll but has already been added!\n'
		return status_str

	if 'fotbollskanalen' in link:
		for line in file_read:
			if link in line:
				link_already = link_already + 1
			else:
				continue
		if link_already == 0:
			file_object.write(link + '\n')
			print('Found new url: ' + link)
			status_str = status_str + 'Found new url: ' + link + '\n'
		if link_already == 1:
			print('URL found on Fotbollskanalen but has already been added!')
			status_str = status_str + 'URL found on Fotbollskanalen but has already been added!\n'
		return status_str

	file_object.close()
	file_read.close()

def aftonbladet(keyword):
	resp = response("https://www.aftonbladet.se/sportbladet/fotboll")
	htmlparsed = html_parse(resp)
	result = ''

	for link in htmlparsed.find_all('a', href=True):
		if keyword in link['href']:
			result = result + append_file(str('https://www.aftonbladet.se' + link['href']))
	return result
def expressen(keyword):
	resp = response("https://www.expressen.se/sport/fotboll/")
	htmlparsed = html_parse(resp)
	result = ''

	for link in htmlparsed.find_all('a', href=True):
		if keyword in link['href']:
			result = result + append_file(str(link['href']))
	return result
def fotbollskanalen(keyword):
	resp = response('https://fotbollskanalen.se')
	htmlparsed = html_parse(resp)
	result = ''
	
	for link in htmlparsed.find_all('a', href=True):
		if keyword in link['href']:
			result = result + append_file(str('https://fotbollskanalen.se' + link['href']))
	return result

if logging == True:
	file_log = open('script.log', 'a')
	file_log.write('Script started : ' + time + '\n')

	file_log.write(aftonbladet(keyword))
	file_log.write(expressen(keyword))
	file_log.write(fotbollskanalen(keyword))

	file_log.close()
else:
	aftonbladet(keyword)
	expressen(keyword)
	fotbollskanalen(keyword)
