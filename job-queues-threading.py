import logging
import os.path
import threading as t
import queue as q
from time import sleep
from datetime import datetime as dt

############
# GLOBALS  #
############
LOG_LEVEL = logging.DEBUG
LOG_PATH = "logfile.log"

############
# LOGGING  #
############
log = logging.getLogger(__name__)
handler = logging.FileHandler(LOG_PATH)
handler.setLevel(LOG_LEVEL)
log.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(threadName)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


############
# JOB 1    #
############
job_1_counter = 0
job_1_queue = q.SimpleQueue()


def run_job_1():
    log.debug("Job 1 starting")
    # Create a queue of jobs
    for task in range(10000):
        job_1_queue.put("Task: " + str(task))
    # Worker threads will be created to complete all jobs in the queue
    start_threads_job_1()
    log.debug("Job 1 completed")


def start_threads_job_1():
    # MainThread creates and sets worker threads as daemon threads for safety
    job_1_thread_1 = t.Thread(target=threaded_func_job_1)
    job_1_thread_2 = t.Thread(target=threaded_func_job_1)
    job_1_thread_3 = t.Thread(target=threaded_func_job_1)
    job_1_thread_4 = t.Thread(target=threaded_func_job_1)
    job_1_thread_5 = t.Thread(target=threaded_func_job_1)
    job_1_thread_1.setDaemon(True)
    job_1_thread_2.setDaemon(True)
    job_1_thread_3.setDaemon(True)
    job_1_thread_4.setDaemon(True)
    job_1_thread_5.setDaemon(True)
    # MainThread starts each worker thread
    job_1_thread_1.start()
    job_1_thread_2.start()
    job_1_thread_3.start()
    job_1_thread_4.start()
    job_1_thread_5.start()
    log.debug("Job 1 worker threads started")
    # MainThread instructed to wait until all worker threads have completed
    job_1_thread_1.join()
    job_1_thread_2.join()
    job_1_thread_3.join()
    job_1_thread_4.join()
    job_1_thread_5.join()
    log.debug("Job 1 worker threads completed")


def threaded_func_job_1():
    global job_1_counter
    while not job_1_queue.empty():
        job_1_counter += 1
        task = job_1_queue.get()
        log.debug(task)
        # This is where you would perform an action on each queued task


############
# Main     #
############
def main():
    log.info("Program starting")
    main_timer_start = dt.now()

    # Job 1
    main_timer_start_job1 = dt.now()
    run_job_1()
    log.info("Job 1 took " + str((dt.now()-main_timer_start_job1).seconds) +
             " seconds to complete " + str(job_1_counter) + " tasks")

    # Add job 2 here
    # main_timer_start_job2 = dt.now()
    # run_job_2()
    # log.info("Job 2 took " + str((dt.now()-main_timer_start_job2).seconds)
    #     + " seconds to complete " + str(job_2_counter) + " tasks")

    log.info("Program took " + str((dt.now()-main_timer_start).seconds) +
             " seconds to complete")

if __name__ == "__main__":
    main()
