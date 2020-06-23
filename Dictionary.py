from Correlation import correlations

attractions = correlations()
pairs = []
for attraction in attractions:
    pairs.append(attraction.split(' '))

data = {
    '': ' ',
    'Churches': [attr[1] for attr in pairs if 'Churches' == attr[0]],
    'Resorts': [attr[1] for attr in pairs if 'Resorts' == attr[0]],
    'Beaches': [attr[1] for attr in pairs if 'Beaches' == attr[0]],
    'Parks': [attr[1] for attr in pairs if 'Parks' == attr[0]],
    'Theaters': [attr[1] for attr in pairs if 'Theaters' == attr[0]],
    'Museums': [attr[1] for attr in pairs if 'Museums' == attr[0]],
    'Malls': [attr[1] for attr in pairs if 'Malls' == attr[0]],
    'Zoo': [attr[1] for attr in pairs if 'Zoo' == attr[0]],
    'Restaurants': [attr[1] for attr in pairs if 'Restaurants' == attr[0]],
    'Pubs/Bars': [attr[1] for attr in pairs if 'PubsBars' == attr[0]],
    'Burger/Pizza shops': [attr[1] for attr in pairs if 'BurgerPizzaShops' == attr[0]],
    'Hotels': [attr[1] for attr in pairs if 'HotelsOtherLodgins' == attr[0]],
    'Juice bars': [attr[1] for attr in pairs if 'JuiceBars' == attr[0]],
    'Art galleries': [attr[1] for attr in pairs if 'ArtGalleries' == attr[0]],
    'Dance clubs': [attr[1] for attr in pairs if 'DanceClubs' == attr[0]],
    'Swimming pools': [attr[1] for attr in pairs if 'SwimmingPools' == attr[0]],
    'Gyms': [attr[1] for attr in pairs if 'Gyms' == attr[0]],
    'Bakeries': [attr[1] for attr in pairs if 'Bakeries' == attr[0]],
    'Beauty&SPA': [attr[1] for attr in pairs if 'BeautySpas' == attr[0]],
    'Cafes': [attr[1] for attr in pairs if 'Cafes' == attr[0]],
    'View Points': [attr[1] for attr in pairs if 'ViewPoints' == attr[0]],
    'Monuments': [attr[1] for attr in pairs if 'Monuments' == attr[0]],
    'Gardens': [attr[1] for attr in pairs if 'Gardens' == attr[0]]
}
names = ['', 'Churches', 'Resorts', 'Beaches', 'Parks', 'Theaters', 'Museums', 'Malls', 'Zoo', 'Gyms', 'Bakeries',
         'Beauty&SPA', 'Cafes', 'View Points', 'Monuments', 'Gardens', 'Restaurants', 'Pubs/Bars', 'Burger/Pizza shops',
         'Hotels', 'Juice bars', 'Dance clubs', 'Swimming pools', 'Art galleries']