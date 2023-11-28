from securities.security_type.alternative import Alternative
from securities.security_type.bond import Bond
from securities.security_type.equity import Equity


class SecurityManager:

    def __init__(self):
        self.securities = []

    def add_security(self, ticker, sub_category, security_type):
        if not self.__security_exists(ticker):
            match security_type:
                case "Equity":
                    self.securities.append(Equity(ticker, sub_category))
                case "Bond":
                    self.securities.append(Bond(ticker, sub_category))
                case "Alternative":
                    self.securities.append(Alternative(ticker, sub_category))
                case _:
                    print("Unknown type.")
        else:
            print(f"Security with ticker {ticker} already exists.")

    def add_securities(self, securities_info):
        for ticker, sub_category, security_type in securities_info:
            if not self.__security_exists(ticker):
                match security_type:
                    case "Equity":
                        self.securities.append(Equity(ticker, sub_category))
                    case "Bond":
                        self.securities.append(Bond(ticker, sub_category))
                    case "Alternative":
                        self.securities.append(Alternative(ticker, sub_category))
                    case _:
                        print(f"Unknown type for ticker {ticker}.")
            else:
                print(f"Security with ticker {ticker} already exists.")

    def __security_exists(self, ticker):
        return any(security.ticker == ticker for security in self.securities)

    def remove_security(self, ticker):
        # Remove security with the specified ticker
        self.securities = [security for security in self.securities if security.ticker != ticker]

    def remove_securities(self, tickers_to_remove):
        self.securities = [security for security in self.securities if security.ticker not in tickers_to_remove]
