KEYNOTFOUND = '<KEYNOTFOUND>'       # KeyNotFound for dictDiff

def dict_diff(first, second):
    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    # Check all keys in first dict
    for key in first.keys():
        if (not second.has_key(key)):
            diff[key] = (first[key], KEYNOTFOUND)
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second.keys():
        if (not first.has_key(key)):
            diff[key] = (KEYNOTFOUND, second[key])
    return diff

if __name__ == '__main__':
    import datetime
    
    new_addition = []
    updated_list = []
    removed_list = []
    no_change = []
    previous = {"date" : datetime.datetime(2014,9,27) , "color" : "red"}
    latest = {"date" : datetime.datetime(2014,9,28) , "color" : "green"}
    for k, v in previous.items():
##        print(k,v)
        if k in latest.keys():
            print('Key found in latest',k)
            if v == latest[k]:
                print('value match', v, latest[k])
                no_change.append(k)
            else :
                print('Value changed',v , latest[k])
                updated_list.append(k)
        else:
            print('Key not found in latest : ', k)
            removed_list.append(k)
    print(new_addition)
    print(updated_list)
    print(removed_list)
    print(no_change)
        
##    d = [x for x in first.keys() if x in second.keys() ]
##    print(d)
##    dict_diff(first, second)
