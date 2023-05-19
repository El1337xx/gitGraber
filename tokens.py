CLEAN_TOKEN_STEP1 = '[\=;\\"\<\>,)(]'
CLEAN_TOKEN_STEP2 = "[']"

def initTokensMap():
    tokensList = []
    tokensCombo = []
    tokensList.append(Token('AMAZON_AWS', '([^A-Z0-9]|^)(AKIA|A3T|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{12,}',['EXAMPLE']))
#   tokensList.append(Token('JSON_WEB_TOKEN', '(eyJ[a-zA-Z0-9]{10,}\.eyJ[a-zA-Z0-9]{10,}\.[a-zA-Z0-9_-]{10,})'))
    tokensList.append(Token('MAILGUN', '(key-[0-9a-f]{32})'))
    tokensList.append(Token('SENDGRID_API_KEY', '(SG\.[a-zA-Z0-9-_]{22}\.[a-zA-Z0-9_-]{43})'))

## Tokens which need two keys to be interesting ##

    googleSecret = Token('GOOGLE_SECRET', r'(\'|\"|\=)(?=(.*[0-9].*))(?=(.*[A-Z].*))(?=([0-9A-Za-z-_]{24})(\1|\'|\"|(\s*(\r\n|\r|\n))))(?!.*\1.*\1.*)(?=(.*[a-z].*))(.*)(\1|\'|\"|(\s*(\r\n|\r|\n)))', None, 2)
    googleUrl = Token('GOOGLE_URL', '([0-9]{12}-[a-z0-9]{32}.apps.googleusercontent.com)', None, 1)
    tokensCombo.append(TokenCombo('GOOGLE', [googleSecret, googleUrl]))

    twilioSID = Token('TWILIO_SID', '(AC[a-f0-9]{32}[^a-f0-9])', None, 1)
    twilioAUTH = Token('TWILIO_AUTH', '\W[a-f0-9]{32}\W', None, 2)
    tokensCombo.append(TokenCombo('TWILIO', [twilioSID, twilioAUTH]))
 
    return tokensList, tokensCombo

class Token:

    def __init__(self, name, regex, blacklist = [], displayOrder = 1):
        self.name = name
        self.regex = regex
        self.blacklist = blacklist
        self.displayOrder = displayOrder
    
    def getName(self):
        return self.name
    
    def getRegex(self):
        return self.regex

    def getBlacklist(self):
        return self.blacklist

    def getDisplayOrder(self):
        return self.displayOrder

class TokenCombo:

    def __init__(self, name, tokensList = []):
        self.tokensList = tokensList
        self.name = name
    
    def getTokens(self):
        return self.tokensList
    
    def getName(self):
        return self.name


