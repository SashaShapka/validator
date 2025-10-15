from logger_config import setup_logger
from validation_strategy.base import Strategy
from phonenumbers import NumberParseException, is_valid_number, parse

log = setup_logger(__name__)


class PhoneValidator(Strategy):
    def do_algorithm(self, validate_field: str):
        regions_to_try = ["UA", "RU"]
        try:
            # If the number starts with '+', we try to parse without the region
            if validate_field.strip().startswith('+'):
                number = parse(validate_field, None)
                if is_valid_number(number) and number.country_code in (380, 7):
                    return True
                else:
                    return False
            else:
                # If there is no country code, first try as Ukrainian, then as Russian
                for region in regions_to_try:
                    try:
                        number = parse(validate_field, region)
                        if is_valid_number(number) and number.country_code in (380, 7):
                            return True
                    except NumberParseException:
                        log.warn(f"[Phone Validator Warning]: Cannot parse with region {region}")
                        continue
                return False
        except Exception as e:
            log.error(f"[Phone Validator Error]: Unexpected parse error: {e}")
            return False