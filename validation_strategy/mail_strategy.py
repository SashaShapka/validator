from logger_config import setup_logger

from validation_strategy.base import Strategy
from email_validator import validate_email, EmailNotValidError

log = setup_logger(__name__)


class MailValidator(Strategy):
    """Based on https://pypi.org/project/email-validator/"""

    def do_algorithm(self, validate_field: str,):
        try:
            validate_email(validate_field, allow_smtputf8=True, check_deliverability=True)
            return True
        except EmailNotValidError as e:
            log.warn("[Mail Validator Warning] Invalid email:", str(e))
            return False
        except Exception as e:
            log.error(f"[Mail Validator Error]: Unexpected error {e}")
            return False