if __name__ == '__main__':
    metro_areas = [
        ('Tokyo', 'JP', 136.933, (135.68, 139.69)),
        ('Shanghai', 'CN', 23, (12.34, 130.57)),
    ]
    print('{:15} | {:^15} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:^15.4f} | {:^9.4f}'
    for city, *_, (lat, long) in metro_areas:
        print(fmt.format(city, lat, long))
    print('done!')
    
