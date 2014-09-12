Python-Web-Crawler
==================

A simple web crawler written in python. used to scan a list of url's for html keywords. Has the ability to export files in csv format
Based on the Scrapy library. the currently designed web crawler scans the list of courses that are offered in NJIT. The execution requires
the client to have the python-scrapy library installed. The syntax for the execution is "scrapy crawl njit -o '<output file>'.csv -t csv"
This command will generate an 'output file' with csv pairs of classes and the years of introduction.
