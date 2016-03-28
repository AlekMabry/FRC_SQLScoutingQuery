import MySQLdb
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Red1 = sys.argv[1]
Red2 = sys.argv[2]
Red3 = sys.argv[3]

Blue1 = sys.argv[4]
Blue2 = sys.argv[5]
Blue3 = sys.argv[6]

RedName = [None,None,None]
RedNumber = [None,None,None]
RedLowGoal = [None,None,None]
RedHighGoal = [None,None,None]
RedClimb = [None,None,None]
RedPortcullis = [None,None,None]
RedChevelDeFrise = [None,None,None]
RedRamparts = [None,None,None]
RedMoat = [None,None,None]
RedDrawbridge = [None,None,None]
RedSallyPort = [None,None,None]
RedRockwall = [None,None,None]
RedRoughTerrain = [None,None,None]
RedLowBar = [None,None,None]
RedVisibility = [None,None,None]
RedAutoDefenses = [None,None,None]
RedAutostrategy = [None,None,None]
RedTeleopStrategy = [None,None,None]
RedBreakPercentage = [None,None,None]
RedAveragePoints = [None,None,None]

BlueName = [None,None,None]
BlueNumber = [None,None,None]
BlueLowGoal = [None,None,None]
BlueHighGoal = [None,None,None]
BlueClimb = [None,None,None]
BluePortcullis = [None,None,None]
BlueChevelDeFrise = [None,None,None]
BlueRamparts = [None,None,None]
BlueMoat = [None,None,None]
BlueDrawbridge = [None,None,None]
BlueSallyPort = [None,None,None]
BlueRockwall = [None,None,None]
BlueRoughTerrain = [None,None,None]
BlueLowBar = [None,None,None]
BlueVisibility = [None,None,None]
BlueAutoDefenses = [None,None,None]
BlueAutostrategy = [None,None,None]
BlueTeleopStrategy = [None,None,None]
BlueBreakPercentage = [None,None,None]
BlueAveragePoints = [None,None,None]

def printInfo(variableName, variableValue):
    if variableValue == 0:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.FAIL+bcolors.BOLD+"Can't Do"+bcolors.ENDC
    if variableValue == 1:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.WARNING+bcolors.BOLD+"Can Do"+bcolors.ENDC
    if variableValue == 2:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.OKGREEN+bcolors.BOLD+"Can Do"+bcolors.ENDC
    if variableValue == None:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.OKBLUE+bcolors.BOLD+"Unknown"+bcolors.ENDC

def standardPrint(variableName, variableValue):
    if variableValue != None:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.BOLD+str(variableValue)+bcolors.ENDC
    if variableValue == None:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.OKBLUE+bcolors.BOLD+"Unknown"+bcolors.ENDC

def printAutoStrategy(variableName, variableValue):
    if variableValue == 0:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.FAIL+bcolors.BOLD+"Do Nothing"+bcolors.ENDC
    if variableValue == 1:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.OKBLUE+bcolors.BOLD+"Drive Forward"+bcolors.ENDC
    if variableName == 2:
        print bcolors.BOLD+str(variableName) + " = "+bcolors.OKGREEN+bcolors.BOLD+"Drive Forward & Shoot"+bcolors.ENDC

db = MySQLdb.connect("localhost", "root", "temppwd", "scouting")
cursor = db.cursor()

query = ("SELECT Name, Number, LowGoal, HighGoal, Climb, Portcullis, ChevelDeFrise, Ramparts, Moat, Drawbridge, SallyPort, Rockwall, RoughTerrain, LowBar, Visibility, AutoDefenses, Autostrategy, TeleopStrategy, BreakPercentage, AveragePoints FROM TeamData WHERE Number = %s")

def Query(BotNumber, TeamNumber, Color):
    cursor.execute(query, BotNumber)

    for (Name, Number, LowGoal, HighGoal, Climb, Portcullis, ChevelDeFrise, Ramparts, Moat, Drawbridge, SallyPort, Rockwall, RoughTerrain, LowBar, Visibility, AutoDefenses, Autostrategy, TeleopStrategy, BreakPercentage, AveragePoints) in cursor:
        if (Color == "Red"):
            print(bcolors.FAIL + bcolors.BOLD + "Team {} (#{}) is {} on {} Alliance".format(Name, Number, TeamNumber, Color) + bcolors.ENDC)
        if (Color == "Blue"):
            print(bcolors.OKBLUE + bcolors.BOLD + "Team {} (#{}) is {} on {} Alliance".format(Name, Number, TeamNumber, Color) + bcolors.ENDC)
        if (Color == "Red"):
            RedName[TeamNumber] = Name
            RedNumber[TeamNumber] = Number
            RedLowGoal[TeamNumber] = LowGoal
            RedHighGoal[TeamNumber] = HighGoal
            RedClimb[TeamNumber] = Climb
            RedPortcullis[TeamNumber] = Portcullis
            RedChevelDeFrise[TeamNumber] = ChevelDeFrise
            RedRamparts[TeamNumber] = Ramparts
            RedMoat[TeamNumber] = Moat
            RedDrawbridge[TeamNumber] = Drawbridge
            RedSallyPort[TeamNumber] = SallyPort
            RedRockwall[TeamNumber] = Rockwall
            RedRoughTerrain[TeamNumber] = RoughTerrain
            RedLowBar[TeamNumber] = LowBar
            RedVisibility[TeamNumber] = Visibility
            RedAutoDefenses[TeamNumber] = AutoDefenses
            RedAutostrategy[TeamNumber] = Autostrategy
            RedTeleopStrategy[TeamNumber] = TeleopStrategy
            RedBreakPercentage[TeamNumber] = BreakPercentage
            RedAveragePoints[TeamNumber] = AveragePoints

        if (Color == "Blue"):
            BlueName[TeamNumber] = Name
            BlueNumber[TeamNumber] = Number
            BlueLowGoal[TeamNumber] = LowGoal
            BlueHighGoal[TeamNumber] = HighGoal
            BlueClimb[TeamNumber] = Climb
            BluePortcullis[TeamNumber] = Portcullis
            BlueChevelDeFrise[TeamNumber] = ChevelDeFrise
            BlueRamparts[TeamNumber] = Ramparts
            BlueMoat[TeamNumber] = Moat
            BlueDrawbridge[TeamNumber] = Drawbridge
            BlueSallyPort[TeamNumber] = SallyPort
            BlueRockwall[TeamNumber] = Rockwall
            BlueRoughTerrain[TeamNumber] = RoughTerrain
            BlueLowBar[TeamNumber] = LowBar
            BlueVisibility[TeamNumber] = Visibility
            BlueAutoDefenses[TeamNumber] = AutoDefenses
            BlueAutostrategy[TeamNumber] = Autostrategy
            BlueTeleopStrategy[TeamNumber] = TeleopStrategy
            BlueBreakPercentage[TeamNumber] = BreakPercentage
            BlueAveragePoints[TeamNumber] = AveragePoints

        printInfo("Low Goal",LowGoal)
        printInfo("High Goal",HighGoal)
        printInfo("Climb",Climb)
        printInfo("Porticullis",Portcullis)
        printInfo("Chevel De Frise",ChevelDeFrise)
        printInfo("Ramparts",Ramparts)
        printInfo("Moat",Moat)
        printInfo("Drawbridge", Drawbridge)
        printInfo("Sally Port",SallyPort)
        printInfo("Rockwall", Rockwall)
        printInfo("Rough Terrain",RoughTerrain)
        printInfo("LowBar", LowBar)
        standardPrint("Visibility", Visibility)
        standardPrint("Autonomous Defenses", AutoDefenses)
        printAutoStrategy("Autonomous Strategy",Autostrategy)
        standardPrint("Teleop Strategy",TeleopStrategy)
        standardPrint("Percentage of Tournament Broken", BreakPercentage)
        standardPrint("Average Points Per Game", AveragePoints)

print(bcolors.FAIL + bcolors.BOLD + "RED ALLIANCE" + bcolors.ENDC)
print(bcolors.FAIL + bcolors.BOLD + "----------------------------------------" + bcolors.ENDC)
Query(Red1,0,"Red")
print(bcolors.FAIL + bcolors.BOLD + "----------------------------------------" + bcolors.ENDC)
Query(Red2,1,"Red")
print(bcolors.FAIL + bcolors.BOLD + "----------------------------------------" + bcolors.ENDC)
Query(Red3,2,"Red")
print(bcolors.FAIL + bcolors.BOLD + "-----------END OF RED ALLIANCE----------" + bcolors.ENDC)

print("\n")

print(bcolors.OKBLUE + bcolors.BOLD + "BLUE ALLIANCE" + bcolors.ENDC)
print(bcolors.OKBLUE + bcolors.BOLD + "----------------------------------------" + bcolors.ENDC)
Query(Blue1,0,"Blue")
print(bcolors.OKBLUE + bcolors.BOLD + "----------------------------------------" + bcolors.ENDC)
Query(Blue2,1,"Blue")
print(bcolors.OKBLUE + bcolors.BOLD + "----------------------------------------" + bcolors.ENDC)
Query(Blue3,2,"Blue")
print(bcolors.OKBLUE + bcolors.BOLD + "----------END OF BLUE ALLIANCE----------" + bcolors.ENDC)

cursor.close()
db.close()

