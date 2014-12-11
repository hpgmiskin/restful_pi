def saveFile(filename,content):
  "Save a file with the given filename and content"

  with open(filename,"w") as openFile:
    openFile.write(content)