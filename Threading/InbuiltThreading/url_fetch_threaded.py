import threading
import requests
import time

start = time.time()
urls = list()
with open('url_list_file.txt', 'r') as F:
    # readlines() adds \n to each line in the end
    urls = F.read().splitlines()

def fetch_url(url):
    urlHandler = requests.get(url)
    html = urlHandler.status_code
    print "{} fetched in {}".format(url, (time.time() - start))

threads = [threading.Thread(target=fetch_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print "Elapsed Time: %s" % (time.time() - start)
