#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '12-Feb-2015'
__purpose__ = "Extract log FilePath from build logs"

Master_build_log = """
[02/12/15 02:11] Master database built, log file /usr2/smartfilter/build/logs/master/log.201502120810
[02/12/15 02:11] XL_Current_Serial_Num=10025
[02/12/15 02:11] TS_Current_Serial_Num=10025
[02/12/15 02:11] BuildScript=finished at Thu Feb 12 02:11:51 CST 2015
"""

Xl_build_log = """
[02/12/15 02:14] TEST MODE: Skipping rysnc of SA files to the sa_export directory.
[02/12/15 02:14] TEST MODE: Skipping rysnc of TS MIGT urls file to the publication_history directory.
[02/12/15 02:14] Done staging files at: Thu Feb 12 02:14:31 CST 2015
[02/12/15 02:14] Removing XL .webdata.lock file.
[02/12/15 02:14] Cleaning up old files
[02/12/15 02:14] MIGT XL database built, log file /usr2/smartfilter/build/logs/migt/xl/log.201502120814
[02/12/15 02:14] XL_Current_Serial_Num=10026
[02/12/15 02:14] TS_Current_Serial_Num=10026
[02/12/15 02:14] BuildScript=finished at Thu Feb 12 02:14:31 CST 2015
"""

Ts_build_log = """
[02/12/15 02:13] Running URLHistoryLoader....
[02/12/15 02:13] Cleaning up old files
[02/12/15 02:13] MIGT TS database built, log file /usr2/smartfilter/build/logs/migt/ts/log.201502120813
[02/12/15 02:13] Running the DMS check...
[02/12/15 02:13] Find any matches to the sanity_file.txt....
[02/12/15 02:13] Testing Web reputation in the tsdatabase.full.201502120813
[02/12/15 02:13] No sanity check errors found
[02/12/15 02:13] DMS check done...
[02/12/15 02:13] XL_Current_Serial_Num=10025
[02/12/15 02:13] TS_Current_Serial_Num=10026
[02/12/15 02:13] BuildScript=finished at Thu Feb 12 02:13:46 CST 2015
"""

import re

data_list = [Xl_build_log, Master_build_log, Ts_build_log]

def regex_findall(pattern, data_list):
    for data in data_list:
        expr_find = re.findall(pattern, data)
        print(expr_find)

# build_console_log pattern
logfile_pattern = '/[\w|\d|/|.]+'
pattern1 = r'[Master|MIGT XL|MIGT TS] database built, log file (%s)' % (logfile_pattern)

# build XL/TS_Current_Serial_Num pattern
pattern2 = r'XL_Current_Serial_Num=(\d+)'
pattern3 = r'TS_Current_Serial_Num=(\d+)'

pattern_list = [pattern1, pattern2, pattern3]
for pattern in pattern_list:
    regex_findall(pattern, data_list)



