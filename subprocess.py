import subprocess

def run(command):
    cmd_args_lst = command.split()
    print("Executing :", cmd_args_lst)
    ex = subprocess.Popen(cmd_args_lst, stdout=subprocess.PIPE)
    out, err = ex.communicate()
    print(out, err)

if __name__ == '__main__':
    run("pwd")
    run("ls -la")
    run("which python")
    run("date")
