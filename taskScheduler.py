import time,json
from shared import saveRow
from devicesAttached import DevicesAttached
from dropboxAPI import DropboxAPI

from apscheduler.schedulers.background import BackgroundScheduler


def getScheduler():
  "getScheduler constructs and returns a scheduler object"

  #Define default background scheduler
  scheduler = BackgroundScheduler()

  #Define ownerJob to be scheduled
  def ownerJob():
    "ownerJob updates the active_owners file with owner information"

    #Get current list of owners
    data = DevicesAttached().getActiveOwners()

    #Obtain local time and 
    timeStruct = time.localtime()
    [year,month,day,hour,minute,second,weekDay,yearDay,isDes] = timeStruct
    data["timestamp"] = "{:02d}:{:02d}:{:02d}".format(hour,minute,second)

    #Save file with date name
    filename = "active_owners_{:02d}_{:02d}_{:02d}.csv".format(day,month,year)
    saveRow(filename,data)

    #If end of a day upload log to dropbox
    if ((hour == 23) and (minute > 57)):
      try:
        DropboxAPI().saveFile(filename)
      except Exception as exception:
        print str(exception)

  ownerJob()

  scheduler.add_job(ownerJob,'interval',minutes=2,id="owner-job")
  return scheduler