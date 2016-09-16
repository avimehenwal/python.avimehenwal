#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import requests

URLS = list()
with open('url_list_file.txt', 'r') as FD:
    URLS = FD.read().splitlines()
#print(URLS)

def get_url(url):
    return requests.get(url).status_code, url

jobpool = list()
with ThreadPoolExecutor() as pool:
    for job in pool.map(get_url, URLS):
        print(job, type(job), len(job))
