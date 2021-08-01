import unittest
from api_requests.API_Request import APIRequest
from utilities.teststatus import Status
from ddt import ddt, data, unpack ,file_data
from utilities.read_data import JSON_Reader

@ddt
class APITestCase(unittest.TestCase):
    ts = Status()


    # Post BitLink successfully. Response 200
    @unpack
    @data(*JSON_Reader("data/test_data_postbitlinks.json", "TS1"))
    def test_T01_PosBitlink_Successful(self,access_token="",long_url="",domain="",group_guid="",title="",tags="",deeplinks="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Post_bitlinks(access_token,long_url,domain,group_guid,title,tags,deeplinks,request_endpoint)
        result = self.aa.VerifyPostBitlinks_Successful()
        self.ts.markFinal("test_T01_SuccessfulScenario",result,"Bitlink posted successfully.Got response:200")

    #Passing Invalid and null vlaue for 1. Domain name.2.Long_url.BadReqest-response:400
    @unpack
    @data(*JSON_Reader("data/test_data_postbitlinks.json", "TS2"))
    def test_T02_PosBitlink_BadRequest(self,access_token="",long_url="",domain="",group_guid="",title="",tags="",deeplinks="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Post_bitlinks(access_token,long_url,domain,group_guid,title,tags,deeplinks,request_endpoint)
        result = self.aa.Verify_BadRequest()
        self.ts.markFinal("test_T02_PosBitlink_BadRequest",result,"Invalid inputs.Got response:400")


    #Passing value to deeplink which is available only in Upgraded version.Upgrade Required-response:402
    @unpack
    @data(*JSON_Reader("data/test_data_postbitlinks.json", "TS3"))
    def test_T03_PosBitlink_UpgradeRequired(self,access_token="",long_url="",domain="",group_guid="",title="",tags="",deeplinks="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Post_bitlinks(access_token,long_url,domain,group_guid,title,tags,deeplinks,request_endpoint)
        result = self.aa.VerifyPostBitlinks_Only_Available_with_Upgrade()
        self.ts.markFinal("test_T03_PosBitlink_UpgradeRequired",result,".Got response:402")

    # Passing invalid value for: 1.access_token 2.group_guid.Getting Response FORBIDDEN:403
    @unpack
    @data(*JSON_Reader("data/test_data_postbitlinks.json", "TS4"))
    def test_T04_PosBitlink_Forbidden(self, access_token="", long_url="", domain="", group_guid="", title="",
                                            tags="", deeplinks="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Post_bitlinks(access_token, long_url, domain, group_guid, title, tags, deeplinks,request_endpoint)
        result = self.aa.Verify_Forbidden()
        self.ts.markFinal("test_T04_PosBitlink_Forbidden", result, ".Got response:403")

    # Passing invalid request end point.Getting Response NOT FOUND:404
    @unpack
    @data(*JSON_Reader("data/test_data_postbitlinks.json", "TS5"))
    def test_T05_PosBitlink_NotFound(self, access_token="", long_url="", domain="", group_guid="", title="",
                                            tags="", deeplinks="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Post_bitlinks(access_token, long_url, domain, group_guid, title, tags, deeplinks,request_endpoint)
        result = self.aa.Verify_NotFound()
        self.ts.markFinal("test_T05_PosBitlink_NotFound", result, ".Got response:404")

    # Passing unprocessable entity into 1.Tags 2.Deeplinks .Getting Response UNPROCESSABLE_ENTITY:422
    @unpack
    @data(*JSON_Reader("data/test_data_postbitlinks.json", "TS6"))
    def test_T06_PosBitlink_UnprocessableEnity(self, access_token="", long_url="", domain="", group_guid="", title="",
                                            tags="", deeplinks="",request_endpoint=""):
        self.aa = APIRequest()
        self.aa.Post_bitlinks(access_token, long_url, domain, group_guid, title, tags, deeplinks,request_endpoint)
        result = self.aa.Verify_UnprocessableEnity()
        self.ts.markFinal("test_T06_PosBitlink_UnprocessableEnity", result, ".Got response:422")




