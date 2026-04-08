import requests

NOMINATIM_URL = "https://nominatim.openstreetmap.org/reverse"

def reverse_geocode_city(lat: float, lon: float, user_agent: str = "supply_chain_ai_mvp"):
    params = {"format": "jsonv2", "lat": lat, "lon": lon, "zoom": 10, "addressdetails": 1}
    headers = {"User-Agent": user_agent}
    r = requests.get(NOMINATIM_URL, params=params, headers=headers, timeout=20)
    r.raise_for_status()
    data = r.json()
    addr = data.get("address", {})
    city = addr.get("city") or addr.get("town") or addr.get("village") or addr.get("county") or "Unknown"
    state = addr.get("state") or "Unknown"
    country = addr.get("country") or "Unknown"
    return f"{city}, {state}, {country}"
