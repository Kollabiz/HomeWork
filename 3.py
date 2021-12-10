import requests
import datetime as dt

def get_currency(code):
	code = code.encode().upper()
	url = 'http://www.cbr.ru/scripts/XML_daily.asp'
	xml = requests.get(url).content
	if not code in xml:
		return
	data = xml[xml.find(code):].split(b'/Valute')[0]
	nominal = int(data.split(b'Nominal>')[1].split(b'<')[0])
	value = float(data.split(b'Value>')[1].split(b'<')[0].replace(b',', b'.')) / nominal
	
	date = xml.split(b'Date="')[1].split(b'"')[0].split(b'.')
	
	year, month, day = date[::-1]
	
	date = f'{year.decode()}-{month.decode()}-{day.decode()}'
	
	return value, date


if __name__ == '__main__':
	print(get_currency('AMD'))