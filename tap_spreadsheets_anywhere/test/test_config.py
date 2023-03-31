import unittest

import dateutil
from io import StringIO
from tap_spreadsheets_anywhere import configuration, file_utils, csv_handler, json_handler

TEST_CRAWL_SPEC = {
    "tables": [
        {
            "crawl_config": "true",
            "path": "file://./tap_spreadsheets_anywhere/test",
            "pattern": ".*\\.xlsx",
            "start_date": "2017-05-01T00:00:00Z"
        }
    ]
}


class TestFormatHandler(unittest.TestCase):

    def test_config_by_crawl(self):
        crawl_paths = [x for x in TEST_CRAWL_SPEC['tables'] if "crawl_config" in x and x["crawl_config"]]
        config_struct = file_utils.config_by_crawl(crawl_paths)
        for row in config_struct['tables']:
            # os.walk uses os.listdir which return a list in arbitrary order
            # https://docs.python.org/3/library/os.html#os.listdir
            # the first file returned by the function would be different
            # depending on the target file system
            self.assertTrue(row['name'] in ('excel_with_bad_newlinesxlsx', 'excel_with_no_errorsxlsx'),
                        "config did not crawl and parse as expected!")



