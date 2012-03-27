# -*- encoding: utf-8 -*-
from subprocess import Popen, PIPE
import re

name = 'make_gitignore'
desc = u'''
savedataが「Untracked files」(gitで管理されてないファイル)として表示されたはず
savedataの変更はgitで管理したくないので無視する設定をしよう。
.gitignoreというファイルにsavedataと書こう
'''

def goal():
    p = Popen(["git", 'status'], stdout=PIPE)
    stdout, stderr = p.communicate()
    m = re.search("Untracked files:.*\tsavedata", stdout, re.DOTALL)
    if m: return False
    return True
