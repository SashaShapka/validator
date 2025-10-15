import logging

def setup_logger(name: str, log_file: str = "app.log", level=logging.INFO):
    # Створюємо логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Уникнути дублювання хендлерів
    if not logger.handlers:
        # Файл
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s"))

        # Консоль
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
