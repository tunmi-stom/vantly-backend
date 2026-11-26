import secrets
import re
from passlib.context import CryptContext


"""
    STRING GENERATOR HELPER FUNCTIONS
"""

def generate_slug(string: str) -> str:
    # Let the slug be lowercase, trimmed, and replace spaces and special characters with hyphens
    string = string.lower().strip()
    
    # Get rid of any character that is not a letter, number, or hyphen
    string = re.sub(r'[^a-z0-9]+', '-', string)
    
    # Also remove any leading or trailing hyphens
    string = re.sub(r'(^-|-$)+', '', string)
    
    # return the slug
    return string

def generate_random_key():
    return secrets.token_urlsafe(256)


"""
    PASSWORD HELPER FUNCTIONS
"""

def hash_password(password: str) -> str:
    pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)


"""
    VALIDATION HELPER FUNCTION
"""
def check_email_str(email: str) -> bool:
    email = email.lower().strip()
    
    # Split the email string from its "@" character
    seq = re.split('@', email)
    if len(seq) != 2:
        return False
    
    local_part = seq[0]
    domain = seq[1]
    
    # Check if local part is empty in other 
    # words, if email begins with @
    if local_part == '':
        return False
    
    # Return false if email starts or ends with "."
    if re.search(r"(^\.)|(\.$)", local_part):
        return False
    
    # Return False if "." folows each other
    local_part_split = re.split(r'\.', local_part)
    
    for i in local_part_split:
        if i == '':
            return False
        
    # Check if the first item in the list contain acceptable characters
    x = re.search(r'[^\w+.-]+', local_part)
    if x:
        return False
    
    # The second Part
    # Return False if domain starts or ends with "." or "-"
    if re.search(r"^\.|^-|\.$|-$", domain):
        return False
    
    domain_parts = re.split(r'\.', domain)
    if len(domain_parts) == 1:
        return False
    
    a_part = domain_parts[0]
    if re.search(r'[^a-z0-9-]', a_part):
        return False
    elif re.search(r'^-|-$', a_part):
        return False
    
    b_part = domain_parts[1:]
    for i in b_part:
        if i == '':
            return False
        if re.search(r'[^a-z0-9-]+', i):
            return False
        if i == b_part[-1]:
            if re.search(r'[^a-z]+', b_part[-1]):
                return False
    
    return True