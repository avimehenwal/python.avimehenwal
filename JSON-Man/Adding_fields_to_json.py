import datetime
import pprint

data = {'adcash.com': {'attr_flags': '2',
                'cats': '105',
                'color': 'gray',
                'geo': '',
                'ms': False,
                'rep': 17},
 'canadaalltax.com': {'attr_flags': '2',
                      'cats': '130',
                      'color': 'red',
                      'geo': '',
                      'ms': False,
                      'rep': 127},
 'extratorrent.cc': {'attr_flags': '2',
                     'cats': '109 118',
                     'color': 'yellow',
                     'geo': '',
                     'ms': False,
                     'rep': 30},
 'facebook.com': {'attr_flags': '2',
                  'cats': '127',
                  'color': 'green',
                  'geo': '',
                  'ms': False,
                  'rep': -42},
 'free-tv-video-online.me': {'attr_flags': '2',
                             'cats': '109 118',
                             'color': 'yellow',
                             'geo': '',
                             'ms': False,
                             'rep': 30},
 'google.com': {'attr_flags': '98',
                'cats': '145',
                'color': 'green',
                'geo': '',
                'ms': False,
                'rep': 0},
 'kickass.to': {'attr_flags': '2',
                'cats': '109 118',
                'color': 'gray',
                'geo': '',
                'ms': False,
                'rep': 25},
 'mp3skull.com': {'attr_flags': '2',
                  'cats': '109 118',
                  'color': 'yellow',
                  'geo': '',
                  'ms': False,
                  'rep': 30},
 'thefreecamsecret.com': {'attr_flags': '2',
                          'cats': '149',
                          'color': 'red',
                          'geo': '',
                          'ms': False,
                          'rep': 55},
 'xhamster.com': {'attr_flags': '2',
                  'cats': '149',
                  'color': 'gray',
                  'geo': '',
                  'ms': False,
                  'rep': 17},
 'youtube.com': {'attr_flags': '8',
                 'cats': '140 147',
                 'color': 'green',
                 'geo': '',
                 'ms': False,
                 'rep': 6},
 'zeroredirect2.com': {'attr_flags': '0',
                       'cats': '130',
                       'color': 'red',
                       'geo': '',
                       'ms': False,
                       'rep': 127}
}

def data_in_mongo_format(data=None):
    if isinstance(data, dict):
        print('Data is dict')
        final = []
        for url in data.keys():
            temp = data[url]
            temp['date'] = datetime.datetime.utcnow()
            # pprint.pprint(temp)
            result = { "url" :  url,
                   "canon_url" : url.strip(),
                   "lastest_seen_date" : datetime.datetime.utcnow(),
                   "reputation_color" : data[url]['color']   ,
                   "results"    : temp    ,
                  }
            final.append(result)
        return final
    else:
        print('Please provide a Python Dict object')
        return False

if __name__ == '__main__':

    r = data_in_mongo_format(data=data)
    if r:
        print(r)
        print(len(r))
    else:
        print('ERROR')

