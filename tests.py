import os
import getpass
os.system('cd ansible && sudo make install && hacking/test-module -m /home/$USER/ansible/library/hg -a "repo=https://bitbucket.org/yeukhon/scm-hook state=present dest=/home/$USER/scm-hook"')

if os.path.exists("/home/{user}/scm-hook".format(user=getpass.getuser())):
    print("scm-hook is cloned down.")
else:
    raise Exception("scm-hook IS NOT CLONED DOWN")
os.system("rm -rf /home/{user}/scm-hook".format(user=getpass.getuser()))

print("now tests on the server")
os.system("ansible-playbook tests.yml -u vagrant -k")
os.system("ansible-playbook tests.yml -u vagrant --tags 'bad_url'")
os.system("ansible-playbook tests.yml -u vagrant --tags 'bad_revision'")

#os.system("ansible/hacking/test-module -m
