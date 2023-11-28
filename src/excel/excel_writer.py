import pandas as pd


class ExcelWriter:
    def __init__(self, file_path, security_manager):
        self.file_path = file_path
        self.security_manager = security_manager

    def update_excel(self):
        try:
            # Read existing data from the file
            with pd.ExcelFile(self.file_path) as xls:
                existing_data = {sheet_name: pd.read_excel(xls, sheet_name) for sheet_name in xls.sheet_names}

            # Update data
            updated_data = {}
            for security_type in set(type(s).__name__ for s in self.security_manager.securities):
                securities_data = []
                for security in self.security_manager.securities:
                    if type(security).__name__ == security_type:
                        securities_data.append({
                            'Ticker': security.ticker,
                            'Sub Category': security.sub_category,
                            'Name': security.name,
                            'Category Name': security.category_name,
                            'Exchange Name': security.exchange_name,
                            'Traded Currency': security.traded_currency,
                            'Expense Ratio': round(security.expense_ratio * 100, 4),
                            'Dividend Yield': round(security.dividend_yield * 100, 2),
                            'Simple Return': round(security.geometric_mean_5y * 100, 2),
                            'Total Return': round(security.adjusted_geometric_mean_5y * 100, 2),
                            'Standard Deviation': round(security.standard_deviation_5y * 100, 2),
                            'Downside Deviation': round(security.downside_deviation_5y * 100, 2),
                            'Value at Risk 95%': round(security.var_95 * 100, 2),
                            'Sharpe Ratio': security.sharpe_ratio,
                        })

                updated_data[security_type] = pd.DataFrame(securities_data)

            # Write updated data to file
            with pd.ExcelWriter(self.file_path, engine='openpyxl') as writer:
                for sheet_name, df in updated_data.items():
                    df.to_excel(writer, sheet_name=sheet_name, index=False)

                # Keep existing sheets not being updated
                for sheet_name, df in existing_data.items():
                    if sheet_name not in updated_data:
                        df.to_excel(writer, sheet_name=sheet_name, index=False)

        except Exception as e:
            print(f"An error occurred: {e}")
