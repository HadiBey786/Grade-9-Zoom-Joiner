import setup
import webbrowser
import datetime
import time

#Use the other main function and comment this one out if you dont want it to run in the background and only when pressed

def main():

    def open_link(hrs, mins, day):

        setup.main(hrs, mins, day)
        if setup.link:
            webbrowser.open_new_tab(setup.link)

    def class_time(hrs, mins):                                                                                                                                   
        if hrs == 8 and mins == 0 or hrs == 8 and mins == 20 or hrs == 9 and mins == 30 or hrs == 10 and mins == 50 or hrs == 11 and mins == 40 or hrs == 12 and mins == 10 or hrs == 12 and mins == 40 or hrs == 13 and mins == 0 or hrs == 13 and mins == 45:
            return True
    
    running = True
    while running:

        date_time = datetime.datetime.now()
        hrs, mins = date_time.hour, date_time.minute
        day = date_time.isoweekday()
        day = 1

        if class_time(hrs, mins):
            open_link(hrs, mins, day)
            #This is so that it doesnt start spam opening the link. By the time two minutes has passed, it wont trigger the link open anymore because its passed the timeframe
            time.sleep(120)
       
        else:
            #This is so that it only checks once every 30 secs, so it doesnt use up too much background resources
            time.sleep(30)


#Use this function and comment out other main if you want it to only run once when clicked
# def main():
#         setup.main()
#         if setup.link:
#             webbrowser.open_new_tab(setup.link)


if __name__ == '__main__':
    main()
