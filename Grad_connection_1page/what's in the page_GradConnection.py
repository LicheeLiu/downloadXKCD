import urllib2
from bs4 import BeautifulSoup
import requests
import re

def findOccurences(s, ch):
	return [i for i, letter in enumerate(s) if letter == ch]

graduate_jobs = 'https://au.gradconnection.com/graduate-jobs/'
page_gra = urllib2.urlopen(graduate_jobs)
soup_graduate_jobs = BeautifulSoup(page_gra, 'html.parser')
html = list(soup_graduate_jobs.children)[2]
body = list(html.children)[3]
body_part = []
for x in body:
	body_part.append(str(x))
part = ''.join(body_part)
position1 = []
position1 = findOccurences(part, '{')
position2 = []
position2 = findOccurences(part, '}')


'''


p = list(body.children)[1]
part = p.find_all(class_="ellipsis-text-paragraph")


internships = 'https://au.gradconnection.com/internships/'
page_intern = urllib2.urlopen(internships)
soup_internships = BeautifulSoup(page_intern, 'html.parser')

part_time = 'https://au.gradconnection.com/part-time-student-jobs/'
page_part = urllib2.urlopen(part_time)
soup_part_time = BeautifulSoup(page_intern, 'html.parser')

entry_level = 'https://au.gradconnection.com/entry-level-jobs/'
page_entry = urllib2.urlopen(entry_level)
soup_entry_level = BeautifulSoup(page_entry, 'html.parser')

clerkship = 'https://au.gradconnection.com/clerkships/'
page_clerkship = urllib2.urlopen(clerkship)
soup_clerkship = BeautifulSoup(page_clerkship, 'html.parser')

scholarships = 'https://au.gradconnection.com/scholarships/'
page_scholarships = urllib2.urlopen(scholarships)
soup_scholarships = BeautifulSoup(page_scholarships, 'html.parser')


print soup
'''