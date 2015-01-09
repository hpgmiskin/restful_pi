# Include the Dropbox SDK
import dropbox
from shared import *
from secret import ACCESS_TOKEN

class DropboxAPI():
	"""Class for communication with Dropbox"""

	def __init__(self,logFilename=False):
		self.logFilename = logFilename
		self.client = dropbox.client.DropboxClient(ACCESS_TOKEN)

	def saveFile(self,filename):
		"method to save the given content with the given filename to dropbox"

		with open(filename,"rb") as localFile:
			response = self.client.put_file("/{}".format(filename),localFile,overwrite=True)

		self.saveLog(response)
		
	def loadFile(self,filename):
		"method to load a file to local with the given filename"

		remoteFile,metadata = self.client.get_file_and_metadata("/{}".format(filename))
		with open(filename,"wb") as localFile:
			localFile.write(remoteFile.read())

		self.saveLog(response)

	def saveLog(self,logData):
		"method to update the log file"

		if not self.logFilename: return

		log = "File: {} - {}".format(logData['path'],logData['client_mtime'])

		fullLog = loadFile(self.logFilename)
		fullLog += log + "\n"

		saveFile(self.logFilename,fullLog)

if __name__ == "__main__":
	dropboxAPI = DropboxAPI()
	dropboxAPI.saveFile("requirements.txt")