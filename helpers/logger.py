# colored_logger.py
import logging
from colorama import init, Fore, Back, Style

init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """Custom formatter to colorize log messages based on severity level.

    This class extends the default logging.Formatter to add color codes to log
    messages, making them visually distinct based on their severity (DEBUG,
    INFO, WARNING, ERROR, CRITICAL).
    """
    level_colors = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.WHITE + Back.RED
    }
    
    def format(self, record):
        """Format the log record with appropriate colors.

        This method overrides the default formatting behavior to add color codes
        to the log message based on the severity level. It ensures that the
        level name and the message itself are displayed with distinct colors.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message string.
        """
        level_color = self.level_colors.get(record.levelno, Fore.WHITE)
        record.levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        record.msg = f"{Fore.WHITE}{record.msg}{Style.RESET_ALL}"
        return super().format(record)

def setup_logger(name=__name__):
    """Set up a colored logger.

    This function configures a logger with a colored formatter and a stream
    handler, ensuring that log messages are displayed with appropriate colors
    based on their severity level. It avoids adding multiple handlers to the
    same logger.

    Args:
        name (str, optional): The name of the logger. Defaults to __name__.

    Returns:
        logging.Logger: The configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:  # Avoid adding multiple handlers
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        formatter = ColoredFormatter(
            '[%(levelname)s] - %(message)s'
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    
    return logger