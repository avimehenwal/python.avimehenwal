

LOGLINES_OLD = sum(1 for line in open('E:\Lyrids\sample_url_3.txt'))
print(LOGLINES_OLD)
with open('E:\Lyrids\sample_url_3.txt', 'r') as log:
##    print(log)
##    print(log.tell())
##    log.seek(5)
##    print(log.tell())
##    print(log.read())
    
    parsing = False
    for no, line in enumerate(log):
        if no >= 6:

            if line.startswith("\t**** Report 2"):
                parsing = False
            
            elif line.startswith("\t**** Report 1"):
                parsing = True

            if parsing:
                pass
                #Do stuff with data
            else:
                print(no, line)


        
    
    
##    log.seek(LOGLINES_OLD)
##    logging.info('Reading log files after [%s]'%(LOGLINES_OLD))
##    for no, line in enumerate(log):
##        logging.info(no)
