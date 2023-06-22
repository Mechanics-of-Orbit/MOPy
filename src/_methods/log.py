from colorama import Fore, init
import datetime as dt
import os, sys
import inspect

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class Log:
    def __init__(self, loglevel=6, tofile=False, log_filename='mopy.log') -> None:
        """Print or Save to a log file.
        
        | Log Level | Log Type      | Print Color | Background Color |
        | ---------:| ------------- | ----------- | ---------------- |
        |         0 | Emergency     | Black       | Red              |
        |         1 | Alert         | Black       | Yellow           |
        |         2 | Critical      | Black       | Magenta          |
        |         3 | Error         | Red         | No Color         |
        |         4 | Warning       | Yellow      | No Color         |
        |         5 | Notice        | White       | Blue             |
        |         6 | Debug         | Cyan        | No Color         |
        |         7 | Informational | White       | No Color         |
        |         8 | None          | NA          | NA               |
 
        
        Parameters
        ----------
        loglevel     : int, optional > log level 0-7, by default 7
        log_filename : str, optional > if you want to change the log file name, by default 'mopy.log'
        """
        self.loglevel = loglevel
        self.tofile = tofile
        self.logfile = log_filename
        self.color_lookup = {
            'emergency' : {'color' : '\033[30;41m' , 'loglevel' : 0},
            'alert'     : {'color' : '\033[30;43m' , 'loglevel' : 1},
            'critical'  : {'color' : '\033[30;45m' , 'loglevel' : 2},
            'error'     : {'color' : '\033[31m'    , 'loglevel' : 3},
            'warning'   : {'color' : '\033[33m'    , 'loglevel' : 4},
            'notice'    : {'color' : '\033[37;44m' , 'loglevel' : 5},
            'info'      : {'color' : ''            , 'loglevel' : 6},          # '\033[32m',
            'debug'     : {'color' : '\033[36m'    , 'loglevel' : 7},
            # 'process'   : '\033[35m',
        }
        pass
    
    def emergency(self, message):
        """Emergency Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
    def alert(self, message):
        """Alert Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color', 'info')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
    def critical(self, message):
        """Critical Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
    def error(self, message):
        """Error Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
    
    def warning(self, message):
        """Warning Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
    def notice(self, message):
        """Notice

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
    def debug(self, message):
        """Debug Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
    def info(self, message):
        """Info Message

        Parameters
        ----------
        message : str > message to print
        """
        type = inspect.stack()[0][3]
        text_color = self.color_lookup.get(type.lower()).get('color')
        method_called_from = inspect.stack()[1][3]
        file_called_from = os.path.basename(sys.argv[0])
        date_time = str(dt.datetime.now())[0:19]
        
        if self.loglevel >= self.color_lookup.get(type.lower()).get('loglevel'):
            print(f'{text_color}{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\033[00m')
        if self.tofile:
            with open(self.logfile, 'a') as _l: _l.write(f'{date_time} [{type.upper()}] ({file_called_from} > {method_called_from}): {message}\n')
            
def main():
    log = Log()
    log.debug('Test Debug Message', 'log.py')

if __name__ == '__main__':
    main()