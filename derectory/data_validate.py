import sys

class DataValidation :
  def __init__(self):
    pass

  def CheckIntegers(self,int) :
    try :
      updated_int = float(int)
      return updated_int
    except ValueError:
      print(f"Invalid amount <USAGE : Enter valid Integer [1200.00 or 1200]>\nExiting...")
      sys.exit(1)

  
