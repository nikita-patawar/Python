import os
import sys
import time
import schedule

def main():
    border = "-" * 50
    print(border)
    print("-----------Marvellous Data Shield System----------")
    print(border)
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to")
            print("1: Takes Auto Backup at given time")
            print("2: Backup only new and updated files")
            print("3: create an archive of the backup perioically")
            print("4: Sends Mail with the log and zip file")
            print("5: Stores information about backup history")
            print("6: Restore backup from zip file")
            print("7: Display backup history")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory Name")
            print("TimeInterval: the time in minutes for periodic scheduling")
            print("SourceDirectory Name: Name of SourceDirectory to backedup")
            print("Optional: You can also provide a comma separated list of file extensions to exclude from backup")
            print("Example: ScriptName.py 5 Data .temp,.log,.exe")
        elif sys.argv[1] == "--history":
             pass
            # display_backup_history()

        else: 
                print("Unable to proceed as there is no such option")
                print("Please use --h or --u to get more details")

    elif len(sys.argv) >= 4 and sys.argv[1] == "--restore":
            print(len(sys.argv))
            if len(sys.argv) == 4:
                zip_file = sys.argv[2]
                destination = sys.argv[3]
                # restore_backup(zip_file, destination)
            else:
                print("Usage:")
                print("python script.py --restore ZipFileName DestinationFolder")

    #python3 Demo.py 5 Data
    elif len(sys.argv) >= 3 and sys.argv[1] != "--restore":
        interval = sys.argv[1]
        source = sys.argv[2]
        # Optional user exclusions
        user_exclusions = set()
        if len(sys.argv) == 4:
            user_exclusions = set(sys.argv[3].split(","))
        schedule.every(int(interval)).minutes.do(
            marvellousDataShieldStart, source, user_exclusions
        )

        print("Data Shield System Started Successfully")
        print("Excluded Extensions:", user_exclusions)
        print("Press Ctrl + C to stop execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

            
    print(border)
    print("---------Thank you fro using our script-----------")
    print(border)

if __name__ =="__main__":
    main()