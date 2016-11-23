
import time
import _thread

def runner(arg):
    for i in range(6):
        print str(i)+':'+arg

        time.sleep(1)
    #结束当前线程
    thread.exit_thread()  #等同于thread.exit()
       
#启动一个线程，第一个参数为函数名，
#第二个参数为一个tuple类型，是传给函数的参数
thread.start_new_thread(runner, ('hello world',))   #等同于thread.start_new(runner, ('hello world'))

#创建一个锁，锁用于线程同步，通常控制对共享资源的访问
lock = thread.allocate_lock()  #等同于thread.allocate()
num = 0
#获得锁，成功返回True，失败返回False
if lock.acquire():
    num += 1
    #释放锁
    lock.release()
#thread模块提供的线程都将在主线程结束后同时结束，因此将主线程延迟结束
time.sleep(10)
print 'num:'+str(num)
