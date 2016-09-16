#!/usr/bin/env python

from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import requests

URLS = list()
with open('url_list_file.txt', 'r') as FD:
    URLS = FD.read().splitlines()
#print(URLS)

def get_url(url):
    return requests.get(url).status_code, url

pool = ThreadPoolExecutor()
jobpool = list()
for url in URLS:
    jobpool.append(pool.submit(get_url, url))

print(jobpool, type(jobpool), len(jobpool))
# yielding the future job results
for job in as_completed(jobpool):
    print(job.result())

print(wait(jobpool))
