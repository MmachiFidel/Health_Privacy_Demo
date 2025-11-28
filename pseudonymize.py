import hashlib
import hmac
import os

# A simple, deterministic pseudonymization function using HMAC with a secret key.
# In production, store the key in a secure vault (not in code).
_SECRET_KEY = os.environ.get('PSEUDO_KEY', 'sanitized-demo-key-please-change')

def pseudonymize_record(identifier: str) -> str:
    """Return a deterministic pseudonym for an identifier (e.g., patient ID)."""
    if not isinstance(identifier, str):
        identifier = str(identifier)
    # Use HMAC-SHA256 to avoid reversible mapping with a salted key
    mac = hmac.new(_SECRET_KEY.encode('utf-8'), identifier.encode('utf-8'), hashlib.sha256)
    # Return a short hex pseudonym
    return mac.hexdigest()[:16]
