from git import Repo

repo = Repo('.')
commits = list(repo.iter_commits('bsl'))
for i in commits:
  print i
  print str(i.hexsha)
  print str(i.committed_date)
  print str(i.message)
  print "----- end -----\n\n"
