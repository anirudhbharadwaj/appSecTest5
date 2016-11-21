from git import Repo

repo = Repo('.')
commits = list(repo.iter_commits('bsl'))
content1=""
for i in commits:
  content2=str(i.tree.blobs[0].data_stream.read())
  if content1:
    print content1.replace(content2,"")
    print "----- end -----\n\n"
  content1=content2
  print i
  print str(i.hexsha)
  print str(i.committed_date)
  print str(i.message)
print content1
print "----- end -----\n\n"
