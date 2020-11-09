import datetime
import links


link = ''

def main(hrs, mins, day):

    #How many mins before class starts do you want it to start joining
    leeway = 2
       
    #8:10 - 8:18:
    if hrs == 8 and mins < 10-leeway:
        link = links.morning_quran


    def monday():
        global link

        #8:20 - 9:30
        if hrs == 8 and mins >= 20-leeway or hrs == 9 and mins < 30-leeway:
            link = links.physics
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.alg_2

        #10:45 - 11:40
        elif hrs == 10 and mins >= 45-leeway or hrs == 11 and mins < 40-leeway:
            link = links.english

        #11:40 - 12:00  
        elif hrs == 11 and mins >= 40-leeway or hrs == 12 and mins < 0-leeway:
            link = links.assembly

        #12:10 - 1:00
        elif hrs == 11 and mins >= 45-leeway or hrs == 12 and mins < 45-leeway: 
            link = links.pe

        #1:45 - 3:00           
        elif hrs == 13 and mins >= 45-leeway or hrs == 14 and mins < 0-leeway:
            link = links.comp_science
        
        else:
            link = ''

   
    def tuesday():

        global link

        #8:20 - 9:30
        if hrs == 8 and mins >= 20-leeway or hrs == 9 and mins < 30-leeway:
            link = links.islamic_talebi
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.alg_2

        #10:50 - 11:40
        elif hrs == 10 and mins >= 50-leeway or hrs == 11 and mins < 40-leeway:
            link = links.mafahim
            
        #11:40 - 12:00  
        elif hrs == 11 and mins >= 40-leeway or hrs == 12 and mins < 0-leeway:
            link = links.assembly

        #12:40 - 1:40
        elif hrs == 12 and mins >= 40-leeway or hrs == 13 and mins < 40-leeway: 
            link = links.sociology_taymaz
            
        #1:45 - 3:00   
        elif hrs == 13 and mins >= 45-leeway:
            pass
            #For this (study time) I need a way to send notifications saying that there is no class :)
            
        else:
            link = '' 

    def wednesday():

        global link

        #8:20 - 9:30
        if hrs == 8 and mins >= 20-leeway or hrs == 9 and mins < 30-leeway:
            link = links.physics
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.alg_2

        #10:50 - 11:40
        elif hrs == 10 and mins >= 50-leeway or hrs == 11 and mins < 40-leeway:
            link = links.english

                #11:40 - 12:00  
        elif hrs == 11 and mins >= 40-leeway or hrs == 12 and mins < 0-leeway:
            link = links.assembly

        #12:40 - 1:40
        elif hrs == 12 and mins >= 40-leeway or hrs == 13 and mins < 40-leeway:
            link = links.english
            
        #1:45 - 3:00
        elif hrs == 13 and mins >= 45-leeway or hrs == 14 or hrs == 0:
            link = links.islamic_abidi

        else:
            link = '' 


    def thursday():

        global link

        #8:20 - 9:30
        if hrs == 8 and mins >= 20-leeway or hrs == 9 and mins < 30-leeway:
            link = links.islamic_talebi
        
        #9:30 - 10:30
        elif hrs == 9 and mins >= 30-leeway or hrs == 10 and mins < 30-leeway:
            link = links.alg_2

        #10:50 - 11:40
        elif hrs == 10 and mins >= 45-leeway or hrs == 11 and mins < 45-leeway:
            link = links.mafahim
            
        #11:40 - 12:00  
        elif hrs == 11 and mins >= 40-leeway or hrs == 12 and mins < 0-leeway:
            link = links.assembly

        #12:40 - 1:40
        elif hrs == 12 and mins >= 40-leeway or hrs == 13 and mins < 40-leeway: 
            link = links.sociology_nooh
            
        #1:45 - 3:00   
        elif hrs == 13 and mins >= 45-leeway:
            pass
            #For this (async) I need code that opens up a new window, new tab, goes to https://classroom.google.com/u/2/c/MTI2OTM0NjE2MDYw and then sends a notifcation saying its aync :)
            
        else:
            link = '' 

    def friday():

        global link

        #8:20 - 9:30
        if hrs == 8 and mins >= 20-leeway or hrs == 9 and mins < 20-leeway :
            link = links.physics
       
        else:
            link = '' 

    def weekday():
        #here based on which weekday it is it executes the corresponding function

        if day == 1:
            monday()
        
        elif day == 2:
            tuesday()

        elif day == 3:
            wednesday()

        elif day == 4:
            thursday()
        
        elif day == 5:
            friday()

    weekday()
    
#I need code that joins link = links.salaam_rise every other Sunday at 9:30 am.
