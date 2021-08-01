import unittest
from api_requests.API_Request import APIRequest
from utilities.teststatus import Status
from ddt import ddt, data, unpack ,file_data
from utilities.read_data import JSON_Reader

@ddt
class APITestCase(unittest.TestCase):
    ts = Status()


    """Get group deatils successfully.Response 200 """
    @unpack
    @data(*JSON_Reader("data/test_data_getGroups.json", "TS1"))
    def test_T01_GetGroup_Successful(self,access_token="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Get_group_groupid(access_token,request_endpoint)
        result = self.aa.VerifyGetGroup()
        self.ts.markFinal("test_T01_GetGroup_Successful",result,"Group details got successfully.Got response:200")


    # Passing invalid value for: 1.access_token 2.group_guid.Getting Response FORBIDDEN:403
    @unpack
    @data(*JSON_Reader("data/test_data_getGroups.json", "TS2"))
    def test_T02_GetGroup_Forbidden(self,access_token="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Get_group_groupid(access_token,request_endpoint)
        result = self.aa.Verify_Forbidden()
        self.ts.markFinal("test_T02_GetGroup_Forbidden",result,"Got response:403")

