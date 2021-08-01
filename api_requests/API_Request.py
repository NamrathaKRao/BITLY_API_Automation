import requests
import logging
import utilities.custome_logger as cl
import re

class APIRequest:
    log = cl.customLogger(logging.DEBUG)

    def Post_bitlinks(self,access_token,long_url,domain,group_guid,title,tags,deeplinks,request_endpoint):
        headers = {
            'Authorization':access_token,
            'Content-Type': 'application/json'
        }

        data ='{ "long_url": "'+long_url+'", "domain": "'+domain+'", "group_guid": "'+group_guid+'","title": "'+str(title)+'","tags": '+tags+',"deeplinks":'+deeplinks+'}'
        response = requests.post(''+request_endpoint+'', headers=headers, data=data)
        self.result = response.status_code
        print(f"\nSTATUS CODE: {self.result}")
        self.result_content = response.content
        print(f"RESPONSE CONTENT: {self.result_content}")
        return response.status_code

    def GetSortedBitlinks_ForGroups(self,access_token,unit,units,unit_reference,size,request_endpoint):
        headers = {
            'Authorization': access_token,
        }
        params = (
            ('unit', ''+unit+''),
            ('units', ''+units+''),
            ('unit_reference', ''+unit_reference+''),
            ('size', ''+size+''),
        )
        response = requests.get(''+request_endpoint+'', headers=headers, params=params)
        self.result = response.status_code
        print(f"\nSTATUS CODE: {self.result}")
        self.result_content = response.content
        print(f"RESPONSE CONTENT: {self.result_content}")
        return response.status_code

    def Get_group_groupid(self, access_token,request_endpoint):
        headers = {
            'Authorization': access_token,
        }

        response = requests.get('' + request_endpoint + '', headers=headers)
        self.result = response.status_code
        print(f"\nSTATUS CODE: {self.result}")
        self.result_content = response.content
        print(f"RESPONSE CONTENT: {self.result_content}")
        return response.status_code

    def VerifyGetGroup(self):
        actual_result = "200"
        if re.search(actual_result, str(self.result)):
            self.log.info(f"Group details got successfully:\n{self.result_content}")
            return True
        else:
            self.log.info("Getting  failed")
            return False

    def VerifyPostBitlinks_Successful(self):
         actual_result = "200"
         if re.search(actual_result, str(self.result)):
             self.log.info(f"Bitlink got created successfully:\n{self.result_content}")
             return True
         else:
             self.log.info("Bitlink creation failed")
             return False

    def VerifySortedBitlinksFOrGroup_BasedOnClicks_Successful(self):
         actual_result = "200"
         if re.search(actual_result, str(self.result)):
             self.log.info(f"Bitlink sorted based on number of clicks successfully:\n{self.result_content}")
             return True
         else:
             self.log.info("Bitlink sorting failed")
             return False

    def Verify_BadRequest(self):
         actual_result = "400"
         if re.search(actual_result, str(self.result)):
             self.log.info(f"Invalid Domain:\n{self.result_content}")
             return True
         else:
             self.log.info("Did not get invalid Domain")
             return False

    def VerifyPostBitlinks_Only_Available_with_Upgrade(self):
        actual_result = "402"
        if re.search(actual_result, str(self.result)):
            self.log.info(f"Upgrade Required:\n{self.result_content}")
            return True
        else:
            self.log.info("Did not get  message Upgrade required")
            return False


    def Verify_Forbidden(self):
        actual_result = "403"
        if re.search(actual_result, str(self.result)):
            self.log.info(f"Forbidden:\n{self.result_content}")
            return True
        else:
            self.log.info("Did not get message Forbidden")
            return False

    def Verify_NotFound(self):
        actual_result = "404"
        if re.search(actual_result, str(self.result)):
            self.log.info(f"Not Found:\n{self.result_content}")
            return True
        else:
            self.log.info("Did not get message Not Found")
            return False

    def Verify_UnprocessableEnity(self):
        actual_result = "422"
        if re.search(actual_result, str(self.result)):
            self.log.info(f"Unprocessable Enity:\n{self.result_content}")
            return True
        else:
            self.log.info("Did not get message Unprocessable Enity ")
            return False

    def Verify_InternalError(self):
         actual_result = "500"
         if re.search(actual_result, str(self.result)):
             self.log.info(f"Internal Error:\n{self.result_content}")
             return True
         else:
             self.log.info("Did not get Internal Error")
             return False


