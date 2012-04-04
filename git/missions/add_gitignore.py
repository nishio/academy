# -*- encoding: utf-8 -*-
from subprocess import Popen, PIPE
import re

name = 'add_gitignore'
desc = u'''
今度は.gitignoreがUntracked filesに表示されている。
今回は.gitignoreはgitで管理することにする。
git addでコミット対象に登録してみよう。
'''

def goal():
    p = Popen(["git", 'status'], stdout=PIPE)
    stdout, stderr = p.communicate()
    m = re.search(r"Untracked files:.*\.gitignore", stdout, re.DOTALL)
    if m: return False
    m = re.search(r"new file:   .gitignore", stdout)
    if m: return True
    return True
