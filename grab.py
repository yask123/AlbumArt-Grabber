from bs4 import BeautifulSoup
import urllib2,cookielib
import re
from urllib import quote_plus as qp
import urllib
import os
import eyed3
def grab(search=''):
	search = qp(search)
	site = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1112&bih=613&q="+search+"&oq=backst&gs_l=img.3.0.0l10.1011.3209.0.4292.8.7.1.0.0.0.246.770.0j3j1.4.0..3..0...1.1.64.img..3.5.772.KyXkrVfTLT4#tbm=isch&q=back+street+boys+I+want+it+that+way"
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	       'Accept-Encoding': 'none',
	       'Accept-Language': 'en-US,en;q=0.8',
	       'Connection': 'keep-alive'}
	req = urllib2.Request(site, headers=hdr)

	try:
	    page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
	    print e.fp.read()

	content = page.read()
	end =  content.find('jpg')
	start= content[:end].rfind('http')

	return content[start:end+3]

import glob
import urllib2
from bs4 import BeautifulSoup

song_name= glob.glob("*.mp3")
for name in song_name:
	search =  name[:-4]
	image_link= grab(search)	
	os.system('wget '+image_link)
	str = name
	str = unicode(str, errors='replace')
	name = str.encode('utf8')
	print name
	audiofile = eyed3.load((name))
	if audiofile.tag is None:
		audiofile.tag = eyed3.id3.Tag()
		audiofile.tag.file_info = eyed3.id3.FileInfo("foo.id3")
	response = urllib2.urlopen(image_link)
	imagedata = response.read()

	audiofile.tag.images.set(0,imagedata,"image/jpeg",u"Album Art")
	audiofile.tag.save()

