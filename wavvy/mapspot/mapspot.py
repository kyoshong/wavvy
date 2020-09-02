
N = 100 
data = np.array( 
    [ 
        np.random.uniform(low=35, high=60, size=N), # Random latitudes in Europe. 
        np.random.uniform(low=-12, high=30, size=N), # Random longitudes in Europe. 
    ] 
).T 
popups = [str(i) for i in range(N)] # Popups texts are simple numbers. 
m = folium.Map([45, 3], zoom_start=4) 
plugins.MarkerCluster(data, popups=popups).add_to(m) 
m.save(os.path.join('results', 'mapspot.html')) 
m
