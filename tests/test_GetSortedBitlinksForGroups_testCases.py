import unittest
from api_requests.API_Request import APIRequest
from utilities.teststatus import Status
from ddt import ddt, data, unpack ,file_data
from utilities.read_data import JSON_Reader

@ddt
class APITestCase(unittest.TestCase):
    ts = Status()


    """Get Sorted BitLink successfully.
     1.Passing all values
     2. Passing only mandatory values.Response 200 """
    @unpack
    @data(*JSON_Reader("data/test_data_getsorted_bitlinks.json", "TS1"))
    def test_T01_GetSortedBitlinks_Successful(self,access_token="",unit="",units="",unit_reference="",size="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.GetSortedBitlinks_ForGroups(access_token,unit,units,unit_reference,size,request_endpoint)
        result = self.aa.VerifySortedBitlinksFOrGroup_BasedOnClicks_Successful()
        self.ts.markFinal("test_T01_GetSortedBitlinks_Successful",result,"Bitlink sorted successfully.Got response:200")



    """Passing Invalid and null vlaue for 
    1.Unit
    2.Units : negative value, 
    3.Units :more than max value
    4.Unit_reference 
    5.Invalid sort value
    BadReqest-response:400"""
    @unpack
    @data(*JSON_Reader("data/test_data_getsorted_bitlinks.json", "TS2"))
    def test_T02_GetSortedBitlinks_BadRequest(self, access_token="", unit="", units="", unit_reference="", size="",
                                              request_endpoint=""):
        self.aa = APIRequest()
        self.aa.GetSortedBitlinks_ForGroups(access_token, unit, units, unit_reference, size, request_endpoint)
        result = self.aa.Verify_BadRequest()
        self.ts.markFinal("test_T02_GetSortedBitlinks_BadRequest",result,"Invalid inputs.Got response:400")



    # Passing invalid value for: 1.access_token 2.group_guid.Getting Response FORBIDDEN:403
    @unpack
    @data(*JSON_Reader("data/test_data_getsorted_bitlinks.json", "TS3"))
    def test_T03_GetSortedBitlinks_Forbidden(self, access_token="", unit="", units="", unit_reference="", size="",
                                                  request_endpoint=""):
        self.aa = APIRequest()
        self.aa.GetSortedBitlinks_ForGroups(access_token, unit, units, unit_reference, size, request_endpoint)

        result = self.aa.Verify_Forbidden()
        self.ts.markFinal("test_T02_GetSortedBitlinks_Forbidden", result, ".Got response:403")

    # Passing invalid request end point.Getting Response NOT FOUND:404
    @unpack
    @data(*JSON_Reader("data/test_data_getsorted_bitlinks.json", "TS4"))
    def test_T04_GetSortedBitlinks_NotFound(self, access_token="", unit="", units="", unit_reference="", size="",
                                                 request_endpoint=""):
            self.aa = APIRequest()
            self.aa.GetSortedBitlinks_ForGroups(access_token, unit, units, unit_reference, size, request_endpoint)
            result = self.aa.Verify_NotFound()
            self.ts.markFinal("test_T03_GetSortedBitlinks_NotFound", result, ".Got response:404")

    """ Passing invalid values in: 
        1.size
        2.unit_reference
         Getting Response INTERNAL ERROR:500"""
    @unpack
    @data(*JSON_Reader("data/test_data_getsorted_bitlinks.json", "TS5"))
    def test_T05_GetSortedBitlinks_InternalError(self, access_token="", unit="", units="", unit_reference="", size="",
                                                 request_endpoint=""):
            self.aa = APIRequest()
            self.aa.GetSortedBitlinks_ForGroups(access_token, unit, units, unit_reference, size, request_endpoint)
            result = self.aa.Verify_InternalError()
            self.ts.markFinal("test_T05_GetSortedBitlinks_InternalError", result, ".Got response:500")






