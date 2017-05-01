from timer import Timer
##from apscheduler.schedulers.background import BackgroundScheduler
##
###Start the scheduler 
##schedule = Scheduler()
##schedule.daemonic = False
##schedule.start()
##
##def job_func():
##    print("hello world")
##    print(datetime.datetime.now())
##    time,sleep(20)
##
##schedule.add_cron_job(job_func, minute = '0-59')




s = Timer()

s.start()

print("I am waiting")
for i in range(1,50):
    print(i)

print(s.elapsed())
print(s.now())
   
