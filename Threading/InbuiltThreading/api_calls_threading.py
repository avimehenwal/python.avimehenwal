import Queue
import threading
import urllib2

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

theurls = []
with open('url_list_file.txt', 'r') as FD:
    theurls = FD.read().splitlines()
print theurls

q = Queue.Queue()

for u in theurls:
    t = threading.Thread(target=get_url, args = (q,u))
    t.daemon = True
    t.start()

q.join()
print q.qsize()
q.get()
#print s
print q.qsize()
q.get()
print q.qsize()
