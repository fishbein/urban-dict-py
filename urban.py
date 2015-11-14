from lxml import html
import requests

def define(word):
	'''returns a list of definitions from the first page of urban dictionary for a term'''
	page = requests.get("http://urbandictionary.com/define.php?term="+word)
	tree = html.fromstring(page.content)
	defcount = len(tree.xpath('//a[@class="word"]/text()'))
	defs = []
	for i in range(defcount):
		defs += [[tree.xpath('//a[@class="word"]/text()')[i], (tree.xpath('//div[@class="meaning"]/text()')[i]).strip()]]
	return defs

def random():
	'''returns a list of definitions for a random word'''
	page = requests.get("http://urbandictionary.com/random.php")
	tree = html.fromstring(page.content)
	return define(tree.xpath('//a[@class="word"]/text()')[0])