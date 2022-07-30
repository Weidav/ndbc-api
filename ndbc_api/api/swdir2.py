from datetime import datetime
from typing import List

from api._base_request import BaseRequst

class Swdir2(BaseRequst):

    FORMAT = 'swdir2'
    FILE_FORMAT = '.swdir2'

    @classmethod
    def build_request(
        cls,
        station_id: str,
        start_time: datetime,
        end_time: datetime
        ) -> List[str]:
        return BaseRequst._build_base_request(
            fmt=cls.FORMAT,
            file_fmt=cls.FILE_FORMAT,
            station_id=station_id,
            start_time=start_time,
            end_time=end_time
        )
