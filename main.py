import argparse
from typing import Literal

from validation_strategy.base import Context
from validation_strategy.mail_strategy import MailValidator
from validation_strategy.phone_strategy import PhoneValidator
from validation_strategy.regex_expectations_strategy import MailRegexStrategy, PhoneRegexStrategy


def validate_human_identity_value(validate_value: str, input_type: Literal["phone", "mail"]):
    try:
        if input_type == "phone":
            strategies = [PhoneValidator(), PhoneRegexStrategy()]
        else:
            strategies = [MailValidator(), MailRegexStrategy()]

        for strategy in strategies:
            context = Context(strategy, input_data=validate_value)
            if context.do_logic():
                return True
        return False
    except Exception as e:
        raise e

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-v", "--value", required=True, help="Validate value")
    p.add_argument("-t", "--type", choices=["phone", "mail"], required=True, help="Validate type")

    args = p.parse_args()

    value = args.value
    input_type = args.type

    res = validate_human_identity_value(validate_value=value, input_type=input_type)
    print(f"Validation result: {res}")


if __name__ == "__main__":
    main()
