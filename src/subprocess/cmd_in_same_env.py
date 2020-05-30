#!/usr/bin/env python

import subprocess
import select

"""
Run muliple shell commands with in same environment and
try to fetch there exit status
"""

cmd1 = ['cat', '-ldsfsdd']
cmd2 = ['echo', '$?']
#batch = b"""\
#set TEST_VAR=Hello World
#echo $?
#set TEST_VAR
#echo $?
#echo %TEST_VAR%
#echo $?
#echo $TEST_VAR
#echo $?
#exit
#echo $?
#"""
#
exe = subprocess.Popen(cmd1, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
o, e = exe.communicate()
print cmd1, o, e, exe.returncode

exe = subprocess.Popen(cmd2, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
o, e = exe.communicate()
print cmd2, o, e, exe.returncode

#cmdline = ['bash']
#cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#cmd.stdin.write(batch)
#cmd.stdin.flush() # Must include this to ensure data is passed to child process
#
#result = cmd.stdout.read()
#print(result.decode())


#cmd = subprocess.Popen(['bash'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#
#poll = select.poll()
#poll.register(cmd.stdout.fileno(),select.POLLIN)
#
## Write the first command
#command = "export greeting=hello\n"
#cmd.stdin.write(command)
#cmd.stdin.flush() # Must include this to ensure data is passed to child process
#ready = poll.poll(500)
#if ready:
#   result = cmd.stdout.readline()
#   print(result)
#
## Write the second command
#command = "echo $greeting world\n"
#cmd.stdin.write(command)
#cmd.stdin.flush() # Must include this to ensure data is passed to child process
#ready = poll.poll(500)
#if ready:
#   result = cmd.stdout.readline()
#   print(result)
