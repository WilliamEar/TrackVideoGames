import requests
import json


class ClientIGDB(object):
    """Make api calls"""
    BASE_URL = "https://igdbcom-internet-game-database-v1.p.mashape.com/"
    ENDPOINTS_URL = { "characters"  : "characters/"
                    , "companies"   : "companies/"
                    , "franchises"  : "franchises/"
                    , "games"       : "games/"
                    , "genres"     : "genres/"
                    , "platforms"   : "platforms/"
                    }

    @staticmethod
    def api_call(endpoint, fields, limit, extra_params={}):
        url = ClientIGDB.BASE_URL + ClientIGDB.ENDPOINTS_URL[endpoint]
        parameters = "?fields=" + ",".join(fields) if fields != [] else "?fields=*"
        parameters += "&limit=" + str(limit)
        for key, value in extra_params.iteritems():
            parameters += "&" + key + "=" + value

        response = requests.get(url + parameters,
                                headers={
                                    "X-Mashape-Key": "np5Va5DGhjmshPjLgqDRq2VZ1Z0Np16UieLjsnTsXEaeTqcMaf",
                                    "Accept": "application/json"
                                }).text
        return json.loads(response)
