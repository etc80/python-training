import csv


def main():
	result_file = 'file_to_import_2016.csv'
	init_file(result_file)
	with open('analyzed_results.csv', 'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			current_url = row['Page_URL__c'].lower()
			page_id = row['id']
			pageviews, unique_pageviews, time_on_screen = search_GA_data(current_url)
			update_file(result_file, page_id, pageviews, unique_pageviews, time_on_screen)


def search_GA_data(url):
	with open('Analytics_2016.csv', 'r') as csvfile:
		csv_reader = csv.DictReader(csvfile)
		for row in csv_reader:
			page_url = 'https://www.totallybarbados.com/' + row['Page'].strip('/').lower() + '/'
			if page_url == url:
				return row['Pageviews'], row['Unique Pageviews'], row['Avg. Time on Screen']
		else:
			return '','',''


def update_file(file_name, page_id, page_previews, page_unique_previews, page_time_on_screen):
	with open(file_name, 'a') as csvfile:
		csv_writer = csv.writer(csvfile)
		to_write = [page_id, page_previews, page_unique_previews, page_time_on_screen]
		csv_writer.writerow(to_write)


def init_file(file_name):
	with open(file_name, 'w') as csvfile:
		csv_writer = csv.writer(csvfile)
		header = ['id', 'Pageviews', 'Unique Pageviews', 'Avg. Time on Screen']
		csv_writer.writerow(header)


if __name__ == '__main__':
	main()