import re

from validation_strategy.base import Strategy


class PhoneRegexStrategy(Strategy):
    def do_algorithm(self, validate_field: str):
        pattern = re.compile(
            r'^(?:'
            r'\+380(?:[ \-]?\d){9}'  # +380XXXXXXXXX
            r'|'  # або
            r'\+7(?:[ \-]?\d){10}'  # +7XXXXXXXXXX
            r'|'  # або
            r'0(?:\(?\d{2,4}\)?[ \-]?\d{7})'  # 0XXXXXXXXX
            r'|'  # або
            r'8(?:\(?\d{3}\)?[ \-]?\d{7})'  # 8XXXXXXXXXX
            r'|'  # або
            r'9\(?\d{2}\)?[ \-]?\d{7}'  # 9XXXXXXXXX
            r')$'
        )
        return bool(pattern.fullmatch(validate_field))


class MailRegexStrategy(Strategy):
    def do_algorithm(self, validate_field: str):
        pattern = re.compile(
            r'^(?:[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)'  # local part: letters/digits/_/- (dots as separators)
            r'@'  # @ symbol
            r'(?:(?!-)[A-Za-z0-9\u0400-\u04FF-]+(?<!-))'  # first domain label: letters (Latin/Cyrillic), digits, hyphen not at start/end
            r'(?:\.(?:(?!-)[A-Za-z0-9\u0400-\u04FF-]+(?<!-)))*'  # optional subdomains separated by dots (also checks for hyphen position)
            r'\.[A-Za-z\u0400-\u04FF]{2,}$'  # dot + top-level domain (minimum 2 letters)
        )
        return bool(pattern.fullmatch(validate_field))