from threading import Lock

class Foo:
    def __init__(self):
        self.first_mutex = Lock()
        self.second_mutex = Lock()
        self.first_mutex.acquire()
        self.second_mutex.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_mutex.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_mutex.acquire()
        printSecond()
        self.first_mutex.release()
        self.second_mutex.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_mutex.acquire()
        self.first_mutex.acquire()
        printThird()
        self.first_mutex.release()
        self.second_mutex.release()


from threading import Lock

class Foo:
    def __init__(self):
        self.first_mutex = Lock()
        self.second_mutex = Lock()
        self.first_mutex.acquire()
        self.second_mutex.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_mutex.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_mutex.acquire()
        printSecond()
        self.first_mutex.release()
        self.second_mutex.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_mutex.acquire()
        printThird()
        self.second_mutex.release()
    

from threading import Event

class Foo:
    def __init__(self):
        self.first_event = Event()
        self.second_event = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_event.wait()
        printSecond()
        self.second_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_event.wait()
        printThird()
