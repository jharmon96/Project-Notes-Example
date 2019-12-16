from os import sys, path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import time
import standard_functions
import user_input
import settings
import project_note

standard_functions.login()

#Run_IMU()

project_note.run()





