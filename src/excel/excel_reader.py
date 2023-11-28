import pandas as pd


class ExcelReader:
    def __init__(self, file_path, security_manager):
        self.file_path = file_path
        self.security_manager = security_manager

    def read_and_update_securities(self):
        # Read the Excel file
        xls = pd.ExcelFile(self.file_path)
        current_tickers = set()  # Set to hold tickers present in the Excel file

        # Read each sheet and update current_tickers
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name, usecols=['Ticker', 'Sub Category'])

            # Filter out rows with NaN in 'Ticker'
            df = df.dropna(subset=['Ticker'])

            if df.empty:
                print(f"Warning: Sheet '{sheet_name}' is empty or does not have the expected format.")
                continue

            # Add securities in bulk
            securities = df.apply(
                lambda row: (row['Ticker'], row['Sub Category'] if pd.notna(row['Sub Category']) else None, sheet_name),
                axis=1)
            self.security_manager.add_securities(
                securities.tolist())  # Assuming add_securities can handle a list of tuples
            current_tickers.update(df['Ticker'])

        # Efficient removal of securities not in current_tickers
        all_tickers = set(security.ticker for security in self.security_manager.securities)
        securities_to_remove = all_tickers - current_tickers
        self.security_manager.remove_securities(
            list(securities_to_remove))  # Assuming remove_securities can handle a list
