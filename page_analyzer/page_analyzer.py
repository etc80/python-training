import csv
import bs4
import requests


def main():
	result_file = 'analyzed_results.csv'
	init_file(result_file)
	with open('Page__c.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			current_url = row['Page_URL__c']
			new_url, new_title = check_url(current_url)
			update_file(result_file, row['Id'], new_url, new_title)


def check_url(url):
	header = {
	'User-agent': 
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
	}
	try:
		r = requests.get(url, headers=header)
		html = bs4.BeautifulSoup(r.text, 'html.parser')
		new_url = r.url
		new_title = html.title.text
	except:
		return '', ''
	return new_url, new_title


def init_file(file_name):
	with open(file_name, 'w') as csvfile:
		csv_writer = csv.writer(csvfile)
		header = ['id', 'Page_URL__c', 'Page_title__c' ]
		csv_writer.writerow(header)


def update_file(file_name, page_id, page_url, page_title):
	with open(file_name, 'a') as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow([page_id, page_url, page_title])


if __name__ == '__main__':
	main()