import requests, os, bs4
import BeautifulSoup
import string

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
'''Download the page until 'http://xkcd.com/#xkcd' which means no more pages'''
while not url.endswith('#'):
	print ('Downloading page %s...' %url)
	res = requests.get(url)
	res.raise_for_status()

	soup= bs4.BeautifulSoup(res.text)

	'''Find the url of the comic image, <img> elements are within <div id="comic">'''
	comicElem = soup.select('#comic img.')
	if comicElem == []:
		print ('Could not find comic image.')
	else:
		comicUrl = 'http:' + comicElem[0].get('src')
		#download the image
		print ('Downloading image %s...' %(comucUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
		#save the image to ./xkcd
		imageFile = open(os.ath.join('xkcd', os.path.basename(comicUrl), 'wb'))
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Done')