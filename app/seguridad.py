import hashlib


def hash_clave(clave: str) -> str:
    """Hash simple de la contraseña (fines didácticos)."""
    return hashlib.sha256(clave.encode("utf-8")).hexdigest()