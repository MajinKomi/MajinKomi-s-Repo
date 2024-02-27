import time
import sched
import datetime
import notify2  # For Linux-based systems
# For Windows, you can use libraries like win10toast or ToastNotifier

def send_notification():
    # Initialize notification system
    notify2.init("Toothbrush Reminder")

    # Send notification
    notification = notify2.Notification("Time to Brush Your Teeth!", "Don't forget to brush your teeth now.")
    notification.show()

def schedule_notifications():
    # Create a scheduler
    scheduler = sched.scheduler(time.time, time.sleep)

    while True:
        # Grabs current time
        current_time = datetime.datetime.now()

        # Calculates time (12 hours from current time)
        next_notification_time = current_time + datetime.timedelta(hours=12)

        # Schedules notification
        scheduler.enterabs(next_notification_time.timestamp(), 1, send_notification)

        # Runs the scheduler
        scheduler.run()

if __name__ == "__main__":
    schedule_notifications()