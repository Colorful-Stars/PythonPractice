def getMoviePakge():
    pakge_urls = []
    for i in range(0, 7781, 20):
        url = 'https://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=' + str(i) + '&type=T'
        # print(url)
        pakge_urls.append(url)
    return pakge_urls

print(getMoviePakge())