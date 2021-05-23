import requests
from bs4 import BeautifulSoup


def search_kissanime(anime):
	site_url = "https://ww2.kissanimes.tv"
	search_url = site_url+'/fullsearch?s='+anime.replace(' ','%20')
	results_page = BeautifulSoup(requests.get(search_url).text,'lxml')

	results = results_page.find_all('a',class_="item_movies_link")
	for result in results:
		url = site_url+result['href']
		result_page = BeautifulSoup(requests.get(url).text,'lxml')
		title = result_page.find('div',class_='a_center').img['alt']
		desc = result_page.find('div',class_='summary').p.text
		img = result_page.find('div',class_='a_center').img['src']
		yield {'url':url,'title':title,'desc':desc,'img':img}

def search_gogoanime(anime):
	site_url = "https://www1.gogoanime.ai"
	search_url = site_url+'/search.html?keyword='+anime.replace(' ','%20')
	results_page = BeautifulSoup(requests.get(search_url).text,'lxml')

	results = results_page.find_all('div',class_='img')
	for result in results:
		url = site_url + result.a['href']
		result_page = BeautifulSoup(requests.get(url).text,'lxml')
		title = result_page.find('div',class_="anime_info_body_bg").h1.text
		desc = result_page.find_all('p',class_='type')[1].text.strip()
		img = result_page.find('div',class_="anime_info_body_bg").img['src']
		yield {'url':url,'title':title,'desc':desc,'img':img}

def search_4anime(anime):
	site_url = "https://4anime.to"
	search_url = site_url+"/?s="+anime.replace(' ','+')
	results_page = BeautifulSoup(requests.get(search_url).text,'lxml')

	results = results_page.find_all('div',id="headerDIV_95")
	for result in results:
		url = result.a['href']
		result_page = BeautifulSoup(requests.get(url).text,'lxml')
		title = result_page.find('p',class_="single-anime-desktop").text
		description = result_page.find('div',id="description-mob").find_all('p')
		desc = ''
		for i in range(1,len(description)):
			desc+=description[i].text+'\n\n'

		img = site_url+result_page.find('div',class_="cover").img['src']
		yield {'url':url,'title':title,'desc':desc,'img':img}

def search_9anime(anime):
	site_url = "https://9anime.city"
	search_url = site_url+"/search/?keyword="+anime.replace(' ','+')
	results_page = BeautifulSoup(requests.get(search_url).text,'lxml')

	results = results_page.find_all('a',class_="poster")
	for result in results:
		url = result['href']
		img = result.img['src']
		result_page = BeautifulSoup(requests.get(url).text,'lxml')
		title = result_page.find('h1',class_="title").text
		desc = result_page.find('div',class_='long').text
		yield {'url':url,'title':title,'desc':desc,'img':img}

def search_soap2day(movie):
	site_url = "https://soap2day.cc"
	search_url = site_url+"/search/keyword/"+movie.replace(' ','%20')
	results_page = BeautifulSoup(requests.get(search_url).text,'lxml')

	results = results_page.find_all('div',class_="col-lg-2 col-md-3 col-sm-4 col-xs-6 no-padding")
	for result in results:
		url = site_url+result.a['href']
		result_page = BeautifulSoup(requests.get(url).text,'lxml')
		title = result_page.find('div',class_='col-sm-12 col-lg-12 text-center').h4.text
		desc = result_page.find('p',id='wrap').text.strip()
		img = result_page.find('div',class_='thumbnail').img['src']
		yield {'url':url,'title':title,'desc':desc,'img':img}

def search_dramacool(series):
	site_url = "https://dramacool.ch"
	search_url = site_url+"/search?type=movies&keyword="+series.replace(' ','+')
	results_page = BeautifulSoup(requests.get(search_url).text,'lxml')

	results = results_page.find_all('a',class_="img")
	for result in results:
		url = site_url+result['href']
		result_page = BeautifulSoup(requests.get(url).text,'lxml')
		title = result_page.find('div',class_="info").h1.text
		desc = result_page.find_all('p')[2].text
		img = result_page.find('div',class_="img").img['src']
		yield {'url':url,'title':title,'desc':desc,'img':img}
