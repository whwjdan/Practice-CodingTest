def solution(cacheSize, cities):
    """
    캐시 교체 알고리즘
    LRU -> 가장 오랫동안 사용하지 않은 것
    주어진 데이터가 캐시에 없다면 넣어주고, 캐시가 가득 차있다면 가장 오래된 데이터 제외하고 넣는다.
    동일한 값이 캐시에 있다면 해당값을 빼고 가장 최근 위치로 넣어준다.
    
    cache hit : 주어진 데이터가 캐시에 존재할 경우
    cache miss : 주어진 데이터가 캐시에 존재하지 않는 경우
    
    """
    
    time = 0
    caches = []
    
    cities = [city.lower() for city in cities]
    print(cities)
    
    if cacheSize != 0:
        for city in cities:
            if city in caches:
                caches.append(city)
                caches.pop(caches.index(city))
                time += 1
            # 캐시에 현재 도시가 없을때
            else:
                # 캐시 크기보다 작을때 -> pop X
                if len(caches) <= cacheSize:
                    caches.append(city)
                    time += 5
                else:
                    caches.append(city)
                    caches.pop(0)
                    time += 5
    else:
        time += len(cities)*5
    return time
