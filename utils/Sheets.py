import pygsheets
from typing import List, Union

class GoogleTable:
    def __init__(
        self, credence_service_file: str = "creds.json", 
        googlesheet_file_key: str = "1bZ6dgp-lAeRP3viYW6ENgaIrvcy6LZnXtgd2G2rjeJU"
    ) -> None:
        self.credence_service_file = credence_service_file
        self.googlesheet_file_key = googlesheet_file_key

    def _get_googlesheet_by_key(
        self, googlesheet_client: pygsheets.client.Client
    ) -> pygsheets.Spreadsheet:
        """Get Google.Docs Table sheet by document url"""
        sheets: pygsheets.Spreadsheet = googlesheet_client.open_by_key(
            self.googlesheet_file_key
        )
        return sheets.sheet1

    def _get_googlesheet_client(self):
        """It is authorized using the service key and returns the Google Docs client object"""
        return pygsheets.authorize(
            service_file=self.credence_service_file
        )
    
    def _next_available_row(self, worksheet):
        str_list = list(filter(None, worksheet.get_col(1)))
        return str(len(str_list)+1)

    def insert(self,
        data,
        categ,
        subcateg,
        price,
        who
    ):
        gc = self._get_googlesheet_client()
        wks = self._get_googlesheet_by_key(gc)

        next_row = self._next_available_row(wks)

        wks.update_value("A{}".format(next_row), data)
        wks.update_value("B{}".format(next_row), categ)
        wks.update_value("C{}".format(next_row), subcateg)
        wks.update_value("D{}".format(next_row), price)
        wks.update_value("E{}".format(next_row), who)