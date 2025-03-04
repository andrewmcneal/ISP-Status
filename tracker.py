#!/usr/bin/env python3

###############################
#                             #
#           Imports           #
#                             #
###############################
import datetime
import os
import time




def main():
     format = "%Y-%m-%d %H:%M:%S"                                                             # Sets the formatting for the time stamps
     os.environ['TZ'] = 'America/New_York'                                                    # Places the correct time zone in cache
     time.tzset()                                                                             # Saves the timezone settings from cache
     ip_list = ['8.8.8.8', '208.67.222.222', '1.1.1.1', '192.168.0.1']                        # Builds the list of IP addresses to ping

     mydate = time.strftime('%Y%m%d')                                                         # Gets the current system date and formats it
     logname = "log-" + mydate + ".txt"                                                       # Sets up the file name
     mylog = open(logname, "a")                                                   # Open log file for APPEND ONLY so that additional entries may be added. This also rotates files and names them with the date.

     with open("google.txt", "w+") as google:
#       google = open("google.txt", "w+")                                                    # Open google.txt for READ/WRITE
       google.seek(0)                                                                       # Go to the beginning of the file to read
       print(google.readline())
       googlestatus = google.readline()                                                     # Read first line to get status
#       print(googlestatus)
       googlestatus = googlestatus.replace("\n", "")                                            # Strip \n from the status
       googledatetime = google.readline()                                                   # Read the second line to get the date/time of last change
       googledatetime = googledatetime.replace("\n", "")                                        # Strip \n from the date/time



       for ip in ip_list:                                                                       # Cycles through the following code for each ip in the list
           response = os.popen(f"ping -c1 {ip}").read()                                         # Pings the the ip address and saves the result in the 'response' variable
           if " 0% packet loss" in response:                                                  # Performs the next lines of code if there is NO packet loss meaning the host is UP
               mytime = time.strftime(format)                                                   # Gets the current system time and formats it as defined above
               if ip == '8.8.8.8':                                                              # Checks to see if this is for Google
#                  if googlestatus != 'UP':                                                      # Checks to see if the previous status was DOWN (Currently UP for testing)
                  google.write("UP\n")
#                  print(googlestatus)
#                  google.write(mytime + "\n")
#                  mylog.write(mytime +" - " + ip + " Ping Successful, Google Host is UP!\n")    # Adds to the log file
                  print(f"{mytime} - {ip} Ping Successful, Host is UP!")                        # Prints the up status for the device
               elif ip == '208.67.222.222':                                                     # Checks to see if this is OpenDNS
                  mylog.write(mytime +" - " + ip + " Ping Successful, OPENDNS Host is UP!\n")   # Adds to the log file
                  print(f"{mytime} - {ip} Ping Successful, Host is UP!")                        # Prints the up status for the device
               elif ip == '1.1.1.1':                                                            # Checks to see if this is Cloudflare
                  mylog.write(mytime +" - " + ip + " Ping Successful, Cloudflare Host is UP!\n")  # Adds to the log file
                  print(f"{mytime} - {ip} Ping Successful, Host is UP!")                        # Prints the up status for the device
               elif ip == '192.168.0.1':                                                        # Checks to see if this is the local network gateway
                  mylog.write(mytime +" - " + ip + " Ping Successful, Network Gateway is UP!\n")  # Adds to the log file
                  print(f"{mytime} - {ip} Ping Successful, Host is UP!")                        # Prints the up status for the device
               else:                                                                            # Catch all
                  mylog.write(mytime +" - " + ip + " Ping Successful, Unknown Host is UP!\n")   # Adds to the log file
                  print(f"Error " + {ip} + "not in list but Host is UP!")                       # Prints an error message

           else:                                                                                # Performs the next lines of code if there IS packet loss meaning the host is DOWN
               mytime = time.strftime(format)                                                   # Gets the current system time and formats it as defined above
               print(f"{mytime} - {ip} Ping Unsuccessful, Host is DOWN.")                       # Prints the down status for the device


       google.close()
       mylog.close()

if __name__ == "__main__":
    main()
