from typing import List

import pandas as pd

from ndbc_api.api.parsers._base import BaseParser


class AdcpParser(BaseParser):

    INDEX_COL = 0
    NAN_VALUES = None
    REVERT_COL_NAMES = [
        'YY',
        'MM',
        'DD',
        'hh',
        'mm',
        'DEP01',
        'DIR01',
        'SPD01',
        'DEP02',
        'DIR02',
        'SPD02',
        'DEP03',
        'DIR03',
        'SPD03',
        'DEP04',
        'DIR04',
        'SPD04',
        'DEP05',
        'DIR05',
        'SPD05',
        'DEP06',
        'DIR06',
        'SPD06',
        'DEP07',
        'DIR07',
        'SPD07',
        'DEP08',
        'DIR08',
        'SPD08',
        'DEP09',
        'DIR09',
        'SPD09',
        'DEP10',
        'DIR10',
        'SPD10',
        'DEP11',
        'DIR11',
        'SPD11',
        'DEP12',
        'DIR12',
        'SPD12',
        'DEP13',
        'DIR13',
        'SPD13',
        'DEP14',
        'DIR14',
        'SPD14',
        'DEP15',
        'DIR15',
        'SPD15',
        'DEP16',
        'DIR16',
        'SPD16',
        'DEP17',
        'DIR17',
        'SPD17',
        'DEP18',
        'DIR18',
        'SPD18',
        'DEP19',
        'DIR19',
        'SPD19',
        'DEP20',
        'DIR20',
        'SPD20',
        'DEP21',
        'DIR21',
        'SPD21',
        'DEP22',
        'DIR22',
        'SPD22',
        'DEP23',
        'DIR23',
        'SPD23',
        'DEP24',
        'DIR24',
        'SPD24',
        'DEP25',
        'DIR25',
        'SPD25',
        'DEP26',
        'DIR26',
        'SPD26',
        'DEP27',
        'DIR27',
        'SPD27',
        'DEP28',
        'DIR28',
        'SPD28',
        'DEP29',
        'DIR29',
        'SPD29',
        'DEP30',
        'DIR30',
        'SPD30',
        'DEP31',
        'DIR31',
        'SPD31',
        'DEP32',
        'DIR32',
        'SPD32',
        'DEP33',
        'DIR33',
        'SPD33',
        'DEP34',
        'DIR34',
        'SPD34',
        'DEP35',
        'DIR35',
        'SPD35',
        'DEP36',
        'DIR36',
        'SPD36',
        'DEP37',
        'DIR37',
        'SPD37',
        'DEP38',
        'DIR38',
        'SPD38',
    ]

    @classmethod
    def df_from_responses(cls, responses: List[dict],
                          use_timestamp: bool) -> pd.DataFrame:
        return super(AdcpParser, cls).df_from_responses(responses,
                                                        use_timestamp)
