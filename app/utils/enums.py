from enum import Enum
class Subs(str, Enum):
    FREE = "Free"
    PRO = "Pro"
    PREMIUM = "Premium"
    
class RsdOps(str, Enum):
    CONCISE = "concise"
    STANDARD = "standard"
    DETAILED = "detailed"
    
class EnableNotification(Enum):
    YES = True
    NO = False
    
class Language(str, Enum):
    # English
    ENG = "en"