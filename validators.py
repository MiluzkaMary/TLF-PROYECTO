import re
from dataclasses import dataclass
from typing import Pattern, Tuple, Dict

@dataclass(frozen=True)
class PatternDef:
    name: str
    regex: Pattern
    example_ok: str
    example_bad: str
    explain: str

def _compile(pattern: str, flags=0) -> Pattern:
    return re.compile(pattern, flags)

PATTERNS: Dict[str, PatternDef] = {
    "email": PatternDef(
        name="Correo electrónico",
        regex=_compile(r"(?i)\b[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}\b"),
        example_ok="usuario.nombre@dominio.com",
        example_bad="usuario@@dominio..com",
        explain="Formato estándar local@dominio.tld."
    ),

    "telefono_co": PatternDef(
    name="Teléfono colombiano",
    regex=_compile(r"\b(?:\+?57[\s\-]?)?3\d{2}[\s\-]?\d{3,4}[\s\-]?\d{3,4}\b"),
    example_ok="+57 322 9137 132",
    example_bad="123-456-789",
    explain="Debe comenzar con +57 o con 3. Acepta espacios o guiones; total 10 dígitos."
    ),


    "fecha_ddmmyyyy": PatternDef(
        name="Fecha dd/mm/yyyy",
        regex=_compile(r"\b(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}\b"),
        example_ok="05/12/2002",
        example_bad="32/15/2020",
        explain="Día 01–31, mes 01–12, año 1900–2099."
    ),

    "cedula_co": PatternDef(
        name="Cédula Colombiana",
        regex=_compile(r"\b\d{10}\b"),
        example_ok="1032456789",
        example_bad="7654321",
        explain="Debe contener exactamente 10 dígitos numéricos."
    ),

    "codigo_postal": PatternDef(
        name="Código postal colombiano",
        regex=_compile(r"\b\d{6}\b"),
        example_ok="050022",
        example_bad="0500-22",
        explain="Debe tener exactamente 6 dígitos."
    ),

    "url": PatternDef(
        name="URL",
        regex=_compile(r"(?i)\bhttps?://[^\s/$.?#].[^\s]*\b"),
        example_ok="https://ejemplo.com",
        example_bad="htp:/ejemplo",
        explain="URL http/https válida."
    ),

    "placa_co": PatternDef(
        name="Placa colombiana",
        regex=_compile(r"\b[A-Z]{3}\d{3}\b|\b[A-Z]{3}\d{2}[A-Z]\b"),
        example_ok="ABC123",
        example_bad="AB1234",
        explain="Formato vehicular colombiano (autos o motos)."
    ),

    "direccion": PatternDef(
        name="Dirección",
        regex=_compile(r"\b(?:(Calle|Carrera|Cra|Cl|Av|Avenida|Transversal|Tv)\s+\d+[A-Z]?)(?:\s*#\s*\d+[A-Z]?(?:-\d+)?)?\b"),
        example_ok="Calle 45 # 12-34",
        example_bad="cll12",
        explain="Dirección colombiana típica."
    ),

    "monto_dinero": PatternDef(
    name="Monto de dinero (COP o pesos)",
    regex=_compile(r"\b(?:COP\s?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?(?:\s?pesos)?)|\b(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?\s?pesos)\b"),
    example_ok="COP 5.000.000 pesos",
    example_bad="5000",
    explain="Debe iniciar con COP o finalizar con 'pesos'. Ej: 'COP 5.000.000' o '5.000.000 pesos'."
    ),


    "hora": PatternDef(
        name="Hora",
        regex=_compile(r"\b(0?\d|1\d|2[0-3]):[0-5]\d(?:\s?(AM|PM|am|pm))?\b"),
        example_ok="14:30",
        example_bad="25:69",
        explain="Formato 24h y 12h con AM/PM."
    ),

    "nit": PatternDef(
        name="NIT/RUT",
        regex=_compile(r"\b\d{3}\.\d{3}\.\d{3}-\d\b"),
        example_ok="900.123.456-7",
        example_bad="900123456",
        explain="Formato colombiano NIT/RUT."
    ),

    "hashtag": PatternDef(
        name="Hashtag",
        regex=_compile(r"#[A-Za-z0-9_ÁÉÍÓÚáéíóúñ]+"),
        example_ok="#EventoUQ",
        example_bad="# evento",
        explain="Texto precedido por #, sin espacios."
    ),
    
    "password_segura": PatternDef(
    name="Contraseña segura",
    regex=_compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_\-#])[A-Za-z\d@$!%*?&_\-#]{8,}$"),
    example_ok="MiClave_2025!",
    example_bad="abc123",
    explain="Debe tener mínimo 8 caracteres, con mayúscula, minúscula, número y símbolo."
    ),

}

def validate(name: str, text: str) -> Tuple[bool, str]:
    p = PATTERNS[name]
    m = p.regex.fullmatch(text.strip())
    if m:
        return True, f"✓ {p.name} válido."
    return False, f"✗ {p.name} inválido. Ejemplo válido: {p.example_ok}. Detalle: {p.explain}"

def findall(name: str, text: str):
    p = PATTERNS[name]
    return [m.group(0) for m in p.regex.finditer(text)]
