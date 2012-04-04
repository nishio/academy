# -*- encoding: utf-8 -*-
from subprocess import Popen, PIPE
import re

name = 'commit_gitignore'
desc = u'''
さて、.gitignoreをコミット対象に登録することができた
ではgit commitしてみよう。
'''

def goal():
    raise NotImplementedError
    p = Popen(["git", 'status'], stdout=PIPE)
    stdout, stderr = p.communicate()
    m = re.search(r"Untracked files:.*\.gitignore", stdout, re.DOTALL)
    if m: return False
    m = re.search(r"new file:   .gitignore", stdout)
    if m: return True
    return True
