import pyautogui
import time

# Input for the time sleep
time_for_alert_second = int(input('How many seconds for the alert? Enter an integer number: '))
time_for_alert_minute = int(input('How many minutes for the alert? Enter an integer number: '))
time_for_alert_hours = int(input('How many hours for the alert? Enter an integer number: '))

# Sleep for the specified time
time.sleep(time_for_alert_second)
time.sleep(time_for_alert_minute * 60)
time.sleep(time_for_alert_hours * 3600)

# Display the alert
pyautogui.alert(text='Give up, donkey', title='المنبه', button='OK')
