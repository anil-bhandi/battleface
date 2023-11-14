import configparser
config = configparser.RawConfigParser()
config.read(".\\configrations\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info','basURL')
        return  url
    @staticmethod
    def privacyPolicyURL():
        privacyPolicyURL = config.get("common info","privacyPolicyURL")
        return  privacyPolicyURL
    @staticmethod
    def termsAndConditionURL():
        termsAndConditionURL = config.get("common info","termsAndConditionURL")
        return termsAndConditionURL
