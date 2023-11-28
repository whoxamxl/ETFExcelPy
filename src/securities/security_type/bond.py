from ..security import Security


class Bond(Security):
    class_risk_weight = None
    class_asset_weight = None

    def __init__(self, ticker, sub_category):
        super().__init__(ticker, sub_category)
