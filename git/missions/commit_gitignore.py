# -*- encoding: utf-8 -*-
from subprocess import Popen, PIPE
import re

name = 'commit_gitignore'
desc = u'''
さて、.gitignoreをコミット対象に登録することができた。ではgit commitしてみよう。
大丈夫、変なcommitをしてもあなたのマシンの中にcloneした
あなたの個人用リポジトリに書きこむだけだから誰にも迷惑はかからない！
'''

def goal():
    p = Popen(["git", 'status'], stdout=PIPE)
    stdout, stderr = p.communicate()
    m = re.search(r"\.gitignore", stdout)
    if m: return False
    return True
