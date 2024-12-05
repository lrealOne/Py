from pathlib import Path
# Abstração
# Log
# Herança = É um
LOG_FILE = Path(__file__).parent / "log.txt"

class Log:
    def _log(self, message):
        raise NotImplementedError("Implement o método Log")
    
    def log_error(self, message):
        self._log(f"Error: {message}")

    def log_success(self, message):
        self._log(f"Success: {message}")
    

#LogFileMixin é um log
class LogFileMixin(Log):
    def _log(self, message):
        formatMessage = f"{message}, {self.__class__.__name__}"
        print("Saving on log:", formatMessage)
        with open(LOG_FILE, "a") as archive: 
            archive.write(formatMessage + "\n")


#LogPrintMixin é um log
class LogPrintMixin(Log):
    def _log(self, message):
        print(f"{message}, {self.__class__.__name__}")



if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error("Anything")
    lp.log_success("Awesome")
    lf = LogFileMixin()
    lf.log_error("Anything")
    lf.log_success("Awesome")
    