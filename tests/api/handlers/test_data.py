import logging
from functools import partial

import pandas as pd
import pytest

from ndbc_api.api.handlers.http.data import DataHandler
from ndbc_api.api.requests.http.adcp import AdcpRequest
from ndbc_api.api.requests.http.cwind import CwindRequest
from ndbc_api.api.requests.http.ocean import OceanRequest
from ndbc_api.api.requests.http.spec import SpecRequest
from ndbc_api.api.requests.http.stdmet import StdmetRequest
from ndbc_api.api.requests.http.supl import SuplRequest
from ndbc_api.api.requests.http.swden import SwdenRequest
from ndbc_api.api.requests.http.swdir import SwdirRequest
from ndbc_api.api.requests.http.swdir2 import Swdir2Request
from ndbc_api.api.requests.http.swr1 import Swr1Request
from ndbc_api.api.requests.http.swr2 import Swr2Request
from ndbc_api.exceptions import RequestException, ResponseException
from ndbc_api.utilities.req_handler import RequestHandler
from tests.api.handlers._base import TEST_END, TEST_START, mock_register_uri

TEST_STN_ADCP = '41117'
TEST_STN_CWIND = 'TPLM2'
TEST_STN_OCEAN = '41024'
TEST_STN_SPEC = '41001'
TEST_STN_STDMET = 'TPLM2'
TEST_STN_SUPL = '41001'
TEST_STN_SWDEN = '41001'
TEST_STN_SWDIR = '41001'
TEST_STN_SWDIR2 = '41001'
TEST_STN_SWR1 = '41001'
TEST_STN_SWR2 = '41001'
TEST_LOG = partial(logging.getLogger('TestDataHandler').log, msg="")


@pytest.fixture
def data_handler():
    yield DataHandler


@pytest.fixture(scope='module')
def request_handler():
    yield RequestHandler(cache_limit=10000,
                         log=TEST_LOG,
                         delay=1,
                         retries=1,
                         backoff_factor=0.5)


@pytest.mark.slow
@pytest.mark.private
@pytest.mark.usefixtures('mock_socket', 'read_responses', 'read_parsed_df')
def test_attrs(
    monkeypatch,
    data_handler,
    request_handler,
    read_responses,
    read_parsed_df,
    mock_socket,
):
    _ = mock_socket
    monkeypatch.setenv('MOCKDATE', '2022-08-13')
    for name in [v for v in vars(data_handler) if not v.startswith('_')]:
        reqs = globals()[f'{name.capitalize()}Request'].build_request(
            station_id=globals()[f'TEST_STN_{name.upper()}'],
            start_time=TEST_START,
            end_time=TEST_END,
        )
        assert len(reqs) == len(read_responses[name])
        mock_register_uri(reqs, read_responses[name])
        want = read_parsed_df[name]
        got = getattr(data_handler, name)(
            handler=request_handler,
            station_id=globals()[f'TEST_STN_{name.upper()}'],
            start_time=TEST_START,
            end_time=TEST_END,
        )
        pd.testing.assert_frame_equal(
            want[TEST_START:TEST_END].sort_index(axis=1),
            got[TEST_START:TEST_END].sort_index(axis=1),
            check_dtype=False,
            check_index_type=False,
        )
        with pytest.raises(RequestException):
            _ = getattr(data_handler, name)(
                handler=request_handler,
                station_id=globals()[f'TEST_STN_{name.upper()}'],
                start_time='foo',
                end_time='bar',
            )
        with pytest.raises(ResponseException) as e_info:
            _ = getattr(data_handler, name)(
                handler=None,
                station_id=globals()[f'TEST_STN_{name.upper()}'],
                start_time=TEST_START,
                end_time=TEST_END,
            )
