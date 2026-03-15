import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import quote
import time
import threading
import random

# === CONFIGURACIÓN ===
EXCEL_PATH = r"C:\Users\eder2\OneDrive\Escritorio\Book2.xlsx"
COLUMNA_SKU = 'SKU'
NUM_HILOS = 5
SALIDA_FINAL = 'urls_imagenes_duck.xlsx'

# === HEADERS ROTATIVOS ===
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Android 11; Mobile; rv:89.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64)",
    "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X)"
]

def get_random_headers():
    return {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

# === FUNCIONES ===
def buscar_urls_duckduckgo(sku, max_urls=1):
    try:
        query = quote(sku)
        url = f"https://duckduckgo.com/?q={query}&iax=images&ia=images"
        headers = get_random_headers()
        session = requests.Session()
        resp = session.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')

        # DuckDuckGo carga imágenes vía JS, así que necesitamos el token
        token_script = soup.find("script", string=lambda s: s and "vqd='" in s)
        if not token_script:
            return []

        token = token_script.string.split("vqd='")[1].split("'")[0]
        api_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={query}&vqd={token}"
        api_resp = session.get(api_url, headers=headers, timeout=10)
        data = api_resp.json()
        results = data.get("results", [])
        urls = [img["image"] for img in results if img.get("image")]
        return urls[:max_urls]
    except Exception as e:
        print(f"Error con SKU {sku}: {e}")
        return []

def procesar_bloque(bloque, resultados, lock, hilo_id):
    for sku in bloque:
        print(f"[Hilo {hilo_id}] Procesando: {sku}")
        urls = buscar_urls_duckduckgo(sku)
        url_final = urls[0] if urls else 'NO ENCONTRADA'
        with lock:
            resultados[sku] = url_final

# === MAIN ===
df = pd.read_excel(EXCEL_PATH)
skus = df[COLUMNA_SKU].astype(str).tolist()
bloques = [skus[i::NUM_HILOS] for i in range(NUM_HILOS)]

resultados_dict = {}
lock = threading.Lock()
hilos = []

for i, bloque in enumerate(bloques):
    hilo = threading.Thread(target=procesar_bloque, args=(bloque, resultados_dict, lock, i+1))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

# === GUARDAR RESULTADOS ===
resultados_ordenados = [{'SKU': sku, 'URL': resultados_dict.get(sku, 'NO ENCONTRADA')} for sku in skus]
df_resultado = pd.DataFrame(resultados_ordenados)

try:
    df_resultado.to_excel(SALIDA_FINAL, index=False)
    print("URLs guardadas en:", SALIDA_FINAL)
except PermissionError:
    nuevo_path = SALIDA_FINAL.replace('.xlsx', '_nuevo.xlsx')
    df_resultado.to_excel(nuevo_path, index=False)
    print("Archivo bloqueado, guardado como:", nuevo_path)