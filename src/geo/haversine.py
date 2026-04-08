import numpy as np

def haversine_km(lat1, lon1, lat2, lon2):
    R = 6371.0088
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2.0)**2
    return 2 * R * np.arcsin(np.sqrt(a))

def pairwise_haversine_km(coords):
    # coords: (n,2) => [lat, lon]
    lat = coords[:, 0][:, None]
    lon = coords[:, 1][:, None]
    return haversine_km(lat, lon, lat.T, lon.T)
