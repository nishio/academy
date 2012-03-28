=============
 academy/git
=============

Step by step git learning


story (I appreciate your comment!)

- level1
  - git clone from github
  - git status
  - make .gitignore
  - git add .gitignore
  - git commit

- level2
  - touch / add / commit
  - git add -p (add only AAA line)
  - git commit -v
  - git add -u (add all)
  - git reset -p (reset CCC line)
  - git checkout -p (discard local modification)

- level3 (get information)
  - git log
  - git reflog
  - git <command> --help
  - git show --pretty=raw COMMIT
  - (and other 'read' command)

- level4 (remote repos)
  - git init
  - git clone
  - git pull
  - git init --bare
  - git push

- level5 (branches)
  - git branch
  - git checkout -b
  - git merge
  - resolve conflict
  - here some nice practice to use branches
  - git rebase -i
  - git cherry-pick

- level6 (dive into .git)
  - ls .git
  - cat .git/HEAD
  - cat .git/refs/heads/master
  - ls .git/objects
  - use zlib to see in obj and index

- undo
  - undo of commit --amend (git reset HEAD@{1})

