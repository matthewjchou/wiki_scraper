# Pretty simple program - practice with requests/html/web stuff
# Gets the Wikipedia page for a user's input

import requests
import html

wikipedia_url = 'https://en.wikipedia.org/wiki/Main_Page'

response = requests.get(wikipedia_url)
if (response.status_code is requests.codes.ok):
	print(response.status_code)
	print('Get request successful')
	print(response.url)
else:
	print('Something went wrong, Wikipedia might be down')
	quit()

# Get that search term
search = input('Search for: ')
payload = {'search' : search}

# Get the web page off wikipedia and put it in a .txt file and a .html file
# The .txt file is still in html
poster = requests.post(wikipedia_url, data = payload)
if (poster.status_code is requests.codes.ok):
	print(poster.status_code)
	print('Post request successful')
	print(poster.url)
	# Not sure what chunks are or how to use it
	# Chunks are in bytes
	# 'wb'opens the file with write permissions in binary mode
	with open('wiki_text.txt', 'w', encoding = 'utf-8') as text_file:
		for chunk in poster.iter_content(chunk_size = 50000):
			text_file.write(chunk.decode('utf-8'))
	with open('wiki_text.html', 'wb') as html_file:
		for chunk in poster.iter_content(chunk_size = 50000):
			html_file.write(chunk)
else:
	print('Something went wrong')
	quit()

#Convert the html .txt file to regular string

