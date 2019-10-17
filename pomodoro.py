from PySide2.QtCore import QObject, Signal, Slot, QThread, Property
from time import sleep
from datetime import timedelta, datetime
from models import Database, PomodoroTask, PomodoroSettings


class PomodoroWorker(QThread):
    """Worker for countdown-timer in Pomodoro View."""
    on_start = Signal(object)
    on_stop = Signal()
    on_completed = Signal(object)
    on_is_pomodoro = Signal(object)
    on_is_pause = Signal(object)

    def __init__(self, pomodoro_length, pause_length, has_auto_pause, has_auto_pomodoro):
        QThread.__init__(self)
        self.running_pomodoro_flag = False
        self.running_pause_flag = False
        self.pomodoro_length = int(pomodoro_length)
        self.pause_length = int(pause_length)
        self.has_auto_pause = has_auto_pause
        self.has_auto_pomodoro = has_auto_pomodoro
        self.time = timedelta(minutes=self.pomodoro_length)

    def run(self):
        self.running_pomodoro_flag = True
        print("Pomodoro running")
        while self.running_pomodoro_flag:
            if self.time != timedelta(seconds=0):
                # Send signals with the state of the clock (pomodoro or pause)
                self.on_is_pomodoro.emit(True)
                self.on_is_pause.emit(False)
                self.display_clock()
            else:
                self.running_pomodoro_flag = False
                date = datetime.now()
                self.on_completed.emit(date)

                # Start of the pause                 
                self.running_pause_flag = True
                self.on_is_pomodoro.emit(False)
                self.on_is_pause.emit(True)
                if self.has_auto_pause:               
                    self.run_pause()                    
                
                if self.has_auto_pomodoro:
                    # Recursive calling of "run" in case the option of auto pomodoro is True. 
                    # TODO: Is a good solution? Check the situation
                    self.run()
    
    def display_clock(self):
        self.on_start.emit(self.time)
        self.time = self.time - timedelta(seconds=1)
        sleep(1)
    
    def run_pause(self):
        print("Pause running")        
        self.time = timedelta(minutes=self.pause_length)
        while self.running_pause_flag:
            if self.time != timedelta(seconds=0):
                self.display_clock()
            else:
                self.running_pause_flag = False
                break

    def stop(self):
        self.running_pomodoro_flag = False
        self.running_pause_flag = False
        self.time = timedelta(minutes=self.pomodoro_length)        
        self.on_stop.emit()


class Pomodoro(QObject):
    """Manager of the Pomodoro View."""
    def __init__(self):
        QObject.__init__(self)        
        self.db = Database()        

        # Shared properties with QML
        self._count_total = self.count()
        self._count_today = self.count(date=datetime.today())
        self._start_visibility = True
        self._stop_visibility = False
        self._pomodoro_length = None
        self._pause_length = None
        self._has_auto_pause = None
        self._has_auto_pomodoro = None
        self._pomodoro_flag = True
        self._pause_flag = False

        # Check default settings in DB. If there is none settings, create a default one.
        self.default_settings()

        # Set starting time text after reading default values
        self._text = str(timedelta(minutes=self._pomodoro_length))

        # Pomodoro Thread
        self.thread = PomodoroWorker(
            pomodoro_length=self._pomodoro_length, 
            pause_length=self._pause_length,
            has_auto_pause=self._has_auto_pause,
            has_auto_pomodoro=self._has_auto_pomodoro
        )
        self.thread.on_start.connect(self.on_start)
        self.thread.on_stop.connect(self.on_stop)
        self.thread.on_completed.connect(self.on_completed)

    def count(self, date=None):
        """Return the number of pomodoro tasks.
        Parameters:
            date (DATETIME): Date used to filter the task query        
        Returns:
            count (int): Number of pomodoro tasks
        """
        if date:
            count = self.db.session.query(PomodoroTask).filter_by(date=date).count()
        else:
            count = self.db.session.query(PomodoroTask).count()
        return count

    def _get_text(self):
        return self._text

    def _set_text(self, value):
        self._text = value
        self.on_text.emit()
    
    def _get_pomodoro_flag(self):
        return self._pomodoro_flag
    
    def _set_pomodoro_flag(self, value):
        self._pomodoro_flag = value
    
    def _get_pause_flag(self):
        return self._pause_flag
    
    def _set_pause_flag(self, value):
        self._pause_flag = value

    def _get_start_visibility(self):
        return self._start_visibility

    def _set_start_visibility(self, value):
        self._start_visibility = value
        self.on_start_visibility.emit()

    def _get_stop_visibility(self):
        return  self._stop_visibility

    def _set_stop_visibility(self, value):
        self._stop_visibility = value
        self.on_stop_visibility.emit()

    def _get_pomodoro_length(self):
        return self._pomodoro_length
    
    def _get_pause_length(self):
        return self._pause_length
    
    def _get_has_auto_pause(self):
        return self._has_auto_pause
    
    def _get_has_auto_pomodoro(self):
        return self._has_auto_pomodoro
    
    def _get_count_total(self):
        return self._count_total
    
    def _get_count_today(self):
        return self._count_today

    @Slot(object)
    def on_start(self, value):
        self._set_text(str(value))
    
    @Slot()
    def on_stop(self):
        self._set_text(str(timedelta(minutes=self._pomodoro_length)))

    @Slot(object)
    def on_completed(self, date):
        # Pomodoro is done
        new_pomodoro = PomodoroTask(date=date)
        self.db.session.add(new_pomodoro)
        self.db.session.commit()

    @Slot(object)
    def on_is_pomodoro(self, value):
        pass

    @Slot(object)
    def on_is_pause(self, value):
        pass                  

    @Slot()
    def start_clock(self):
        self._set_start_visibility(False)
        self._set_stop_visibility(True)
        self.thread.start()     

    @Slot()
    def stop_clock(self):
        self._set_start_visibility(True)
        self._set_stop_visibility(False)
        self._set_text(timedelta(minutes=self._pomodoro_length))
        self.thread.stop()
        self.thread.quit()
    
    def default_settings(self):
        """Load default settings values. If there is no record, create the first one."""
        settings = self.db.session.query(PomodoroSettings)
        if settings.count() > 0:
            settings = settings.order_by(PomodoroSettings.id.desc()).first()
            self._pomodoro_length = settings.pomodoro_length
            self._pause_length = settings.pause_length
            self._has_auto_pause = settings.has_auto_pause
            self._has_auto_pomodoro = settings.has_auto_pomodoro
        else:
            self._pomodoro_length = 25
            self._pause_length = 5
            self._has_auto_pause = True
            self._has_auto_pomodoro = True
            default_settings = PomodoroSettings(
                pomodoro_length=self._pomodoro_length,
                pause_length=self._pause_length,
                has_auto_pause=self._has_auto_pause,
                has_auto_pomodoro=self._has_auto_pomodoro,
            )
            self.db.session.add(default_settings)
            self.db.session.commit()        
    
    @Slot(str, str, bool, bool)
    def save_settings(self, pomodoro_length, pause_length, has_auto_pause, has_auto_pomodoro):
        new_settings = PomodoroSettings(
            pomodoro_length=int(pomodoro_length),
            pause_length=int(pause_length),
            has_auto_pause=bool(has_auto_pause),
            has_auto_pomodoro=bool(has_auto_pomodoro)
        )
        self.db.session.add(new_settings)
        self.db.session.commit()
        self._set_text(str(timedelta(minutes=int(pomodoro_length))))   

    on_start_visibility = Signal()
    on_stop_visibility = Signal()
    on_text = Signal()
    on_pomodoro_length = Signal()
    on_pause_length = Signal()
    on_has_auto_pause = Signal()
    on_has_auto_pomodoro = Signal()
    on_count_total = Signal()
    on_count_today = Signal()
    on_pomodoro_flag = Signal()
    on_pause_flag = Signal()

    start_visibility = Property(bool, _get_start_visibility, notify=on_start_visibility)
    stop_visibility = Property(bool, _get_stop_visibility, notify=on_stop_visibility)
    text = Property(str, _get_text, notify=on_text)
    pomodoro_length = Property(int, _get_pomodoro_length, notify=on_pomodoro_length)
    pause_length = Property(int, _get_pause_length, notify=on_pause_length)
    has_auto_pause = Property(bool, _get_has_auto_pause, notify=on_has_auto_pause)
    has_auto_pomodoro = Property(bool, _get_has_auto_pomodoro, notify=on_has_auto_pomodoro)
    count_total = Property(int, _get_count_total, notify=on_count_total)
    count_today = Property(int, _get_count_today, notify=on_count_today)
    pomodoro_flag = Property(bool, _get_pomodoro_flag, notify=on_pomodoro_flag)
    pause_flag = Property(bool, _get_pause_flag, notify=on_pause_flag)
