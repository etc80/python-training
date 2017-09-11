#!/usr/local/bin/python
import csv
import re
import sys


def main():
	page_urls = {}
	if len(sys.argv) > 1:
		basic_file_name = sys.argv[1]
	else:
		basic_file_name = 'AnalyticsDataAll2017.csv'
	analytic_file = basic_file_name
	cleaned_data_file = 'cleared ' + basic_file_name
	import_file = 'import ' + basic_file_name
	searches_file = 'searches ' + basic_file_name
	file_with_urls = 'analyzed_results.csv'
	extract_searches(analytic_file, searches_file)
	with open(analytic_file, 'r') as anal_file:
		csv_reader = csv.DictReader(anal_file)
		for row in csv_reader:
			url = row['Page'].rstrip('/').lower()
			url = clear_url(url)
			if url not in page_urls:
				page_urls[url] = int(row['Pageviews'])
			else:
				page_urls[url] += int(row['Pageviews'])
	init_file(cleaned_data_file, ['page url', 'page views'])
	for key, item in page_urls.items():
	 	update_file(cleaned_data_file, [key, item])
	print('File was cleaned and ',len(page_urls), 'unique records left')
	header = ['id', 'Page URL', 'Pageviews']
	init_file(import_file, header)
	with open(file_with_urls, 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			current_url = row['Page_URL__c'].lower()
			current_id = row['id']
			current_visits = str(page_urls.get(current_url, '0'))
			update_file(import_file, [current_id, current_url, current_visits])
	print("COMPLETED!")


def clear_url(start_url):
	url = start_url
	# url = replace_pattern(url, '.*/(?P<ending>\?s\w*=.*)')    			# remove /?s=...
	url = replace_pattern(url, '.*(?P<ending>/["<]http.*)$')       			# remove extra info after link, like /link/"http://..."
	url = replace_pattern(url, '.*cgi-bin/\w+(?P<ending>/.*)$')				# remove cgi-bin endings
	url = replace_pattern(url, '^(?P<ending>.+translate_c.+totallybarbados\.com).+$') # remove translation links
	url = replace_pattern(url, '.+(?P<ending>/\&usg=.+)$')					# remove translation endings
	url = replace_pattern(url, '.*(?P<ending>/[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+)$') # remove email addresses at the end
	url = replace_pattern(url, '.*(?P<ending>/.+[-\.]html?.*)$')  			# remove ending like 1234-htm and 1234.htm
	url = replace_pattern(url, '.*(?P<ending>/\w+\.php(\?)?.*)$')  			# remove .php endings
	url = replace_pattern(url, '.*(?P<ending>/page/\d+)')        			# remove endings like  /page/2/
	url = replace_pattern(url, '.*(?P<ending>/(\?){0,1}\w+=.*)$')      		# remove ending like /?inf_contact_key=... , /?page_id=123...
	url = replace_pattern(url, '.*(?P<ending>/action~\w+/.*)')  			# remove /action~agenda/... endings
	url = replace_pattern(url, '.*(?P<ending>/\w+~\w+.*)')					# remove other /smt~smt/... endings
	url = replace_pattern(url, '.*(?P<ending>/\d+\,(\d+(\,){0,1}){0,})$') 	# remove /12,102017/... endings
	url = url.replace('//', '/').rstrip('"')
	if len(url) > 0:
		return 'https://www.totallybarbados.com' + url + '/'
	return 'https://www.totallybarbados.com/'


def replace_pattern(url, pat):
	pattern = re.compile(pat)
	result = re.match(pattern, url)
	if result:
		return url.replace(result.group('ending'), '')
	return url


def update_file(file_name, data_to_update):
	with open(file_name, 'a', newline="\n" ) as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(data_to_update)


def init_file(file_name, header):
	with open(file_name, 'w', newline="\n") as csvfile:
		csv_writer = csv.writer(csvfile)
		csv_writer.writerow(header)


def extract_searches(file_name_from, file_name_to):
	searches = {}
	pattern_old = '.+/search2\.cgi\?keywords=(?P<search>.+)\&cat_search=.*$'
	pattern_new = re.compile('.+/\?s\w*=(?P<search>.+)\&lang.*$')
	init_file(file_name_to, ['search', 'times searched'])
	with open(file_name_from, 'r') as csvfile:
		csv_reader = csv.DictReader(csvfile)
		for row in csv_reader:
			url = row['Page'].rstrip('/').lower()
			# looking for searches on new site format
			result = re.match(pattern_new, url)
			if result:
				search = ' '.join(result.group('search').split('+'))
				if search not in searches:
					searches[search] = int(row['Pageviews'])
				else:
					searches[search] += int(row['Pageviews'])
			# looking for searches on old site format
			result = re.match(pattern_old, url)
			if result:
				search = ' '.join(result.group('search').split('+'))
				if search not in searches:
					searches[search] = int(row['Pageviews'])
				else:
					searches[search] += int(row['Pageviews'])
	for key, item in searches.items():
		update_file(file_name_to, [key, str(item)])
	print('File with searches created.')


if __name__ == '__main__':
	main()