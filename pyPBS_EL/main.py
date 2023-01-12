import argparse, os
import subprocess

def main():

    parser = argparse.ArgumentParser(description=("Generate PBS commandlines by python code"))
    parser.add_argument('-P', '--path', metavar='P', help="Path of input file(s)", nargs='+', default=0)
    parser.add_argument('-c', '--command', metavar='c', help="Command line", default=0)
    parser.add_argument('-t', '--thread', metavar='t', help="Number of thread (ppn)", default=8)
    parser.add_argument('-m', '--memory', metavar='m', help="Memory for process (gb)", default=64)
    parser.add_argument('-p', '--prefix', metavar='p', help="Prefix of the PBS script file", default='PBS_script')
    parser.add_argument('-w', '--walltime', metavar='w', help="Time set for usage (Walltime)", default='48:00:00')
    parser.add_argument('-o', '--outdir', metavar='o', help="Output dir name")
    args = parser.parse_args()

    # Check the user name
    user_name = os.path.expanduser('~').split('/')[-1]

    # Check the required arguments
    if args.path == 0:
        raise ValueError("The path option is not entered!")
    if args.command == 0:
        raise ValueError("The command line option is not entered!")

    # Command for implementation
    command = args.command

    # Set the commandline class
    class outcommand:
        # Class initialization
        def __init__(self, path, file):
            self.path = path
            self.file = file
            self.memory = args.memory
            self.command = args.command

        def set_command(self):
            # # Check the mail option was set
            # if args.mail:
            #     #수정
            #     mail_fmt = f"#PBS -m ae -M {args.mail}"
            # else:
            #     mail_fmt = ''
            # Check the commandline variables
            if '(base)' in self.command:
                self.command = self.command.replace('(base)', self.file)
            if '(dir)' in command:
                if args.outdir:
                    self.command = self.command.replace('(dir)', args.outdir)
                else:
                    self.command = self.command.replace('(dir)', self.path)

            outcommand_fmt = f"""
#!/bin/bash
#PBS -N {self.file}
#PBS -q batch
#PBS -l nodes=1:ppn={args.thread}
##PBS -l mem={self.memory}gb
##PBS -l walltime={args.walltime}

cd {self.path}

{self.command}
            """
            #PBS -e {self.path + '/' + self.file}.err
            #PBS -o {self.path + '/' + self.file}.out
            return outcommand_fmt

    # Set the list input files including absolute path
    input_list = []
    if len(args.path) >= 2:
        input_list = args.path
    else:
        inp_path, inp_file = os.path.dirname(args.path[0]), os.path.basename(args.path[0])
        input_list = subprocess.check_output(["find", inp_path, "-name", inp_file]).decode('utf-8').split('\n')
        del input_list[-1]


    # Check the number of command lines
    com_num = len(input_list)

    # Create bash files
    bash_list = []
    for i in range(com_num):
        abs_file = os.path.abspath(input_list[i])
        abs_path = os.path.dirname(abs_file)
        abs_base = os.path.basename(abs_file)
        # Set the format of filename
        filename_fmt = f'{args.prefix}_{abs_base}.sh'
        bash_list.append(filename_fmt)
        with open(filename_fmt, 'w') as shf:
            shf.write(outcommand(abs_path, abs_base).set_command())

    # execute bash scripts
    print(f"\nHello, {user_name}! Thank you for using the pyPBS script!\n")
    print("\nThe Following process will be started:\n")
    print("---------------------------------------")

    for n in bash_list:
        print(f"qsub {n}")

    print("---------------------------------------")

    for n in bash_list:
        os.system(f"qsub {n}")