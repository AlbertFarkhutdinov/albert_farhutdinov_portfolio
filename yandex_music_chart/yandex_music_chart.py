import requests
import xlrd
from bs4 import BeautifulSoup

workbook = xlrd.open_workbook('songs.xls')
sheet = workbook.sheet_by_index(0)
requested_authors = []
requested_titles = []

for row_index in range(sheet.nrows):
    row = sheet.row_values(row_index)
    requested_authors.append(row[0])
    requested_titles.append(row[1])

coincidences = [False for _ in range(sheet.nrows)]

html = BeautifulSoup(requests.get('https://music.yandex.ru/chart').content, 'html.parser')

print('Coincidences:')
for song_index, song in enumerate(html.select('.d-track__overflowable-wrapper')):
    song_title = song.select('.d-track__name')[0].text
    song_author = song.select('.d-track__artists')[0].text
    if (song_title in requested_titles) and (song_author in requested_authors):
        print(f'{song_index + 1}: {song_author} - {song_title}')
        coincidences[requested_titles.index(song_title)] = True

print('\nNot Found:')
for index in range(len(coincidences)):
    if not coincidences[index]:
        print(f'{requested_authors[index]} - {requested_titles[index]}')
