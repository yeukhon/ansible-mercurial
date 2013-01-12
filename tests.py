import os
os.system('cd ansible && sudo make install && hacking/test-module -m /home/glasslab/ansible/library/mercurial -a "repo=https://bitbucket.org/yeukhon/scm-hook state=present dest=/home/glasslab/scm-hook"')

if os.path.exists("/home/glasslab/scm-hook"):
    print("scm-hook is cloned down.")
else:
    raise Exception("scm-hook IS NOT CLONED DOWN")
os.system("rm -rf /home/glasslab/scm-hook")

print("now tests on the server")
os.system("ansible-playbook tests.yml -u vagrant -k")
#os.system("ansible/hacking/test-module -m
