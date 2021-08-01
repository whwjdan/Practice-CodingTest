def solution(word, pages):
    answer = 0
    basic_score = {}
    ext_link = {}
    total_score = {}
    #기본 -> 등장횟수
    #링크 점수 -> 링크가 걸린 페이지의 기본점수 / 링크가 걸린 페이지의 외부링크 수
    
    for page in pages:
        page = page.split('\n')
        print(page)
        
        head = page[page.index('<head>')+1:page.index('</head>  ')]
        #print(head)
        #print(head[1][head[1].index('content')+9:])
        url = ""
        for h in head:
            if "content" in h:
                url = h[h.index('content')+17:]
        url = url.split('\"')[0]
        print(url)
        body = page[page.index('<body>')+1:page.index('</body>')]
        print(body)
        word = word.lower()
        cnt = 0
        ext_urls = []
        for b in body:
            if "<a href=" in b:
                href = b[b.index("<a href="):]
                href = href.split('"')[1][8:]
                print('href',href)
                ext_urls.append(href)
            else:
                if word in b.lower():
                    cnt += 1
        print(cnt)
        basic_score[url] = cnt
        total_score[url] = cnt
        ext_link[url] = ext_urls
    print(basic_score)
    print(ext_link)


    for pre_url in basic_score:
        total_cnt = 0
        print('현재 페이지',pre_url)
        pre_url_score = basic_score[pre_url]
        print('현재 페이지 기본 점수 :',pre_url_score)
        #링크 점수 -> 링크가 걸린 페이지의 기본점수 / 링크가 걸린 페이지의 외부링크 수
        
        #현재 페이지의 링크 된 페이지들
        print(ext_link[pre_url])
        for link_page in ext_link[pre_url]:
            link_score = 0
            if len(ext_link[link_page]) != 0:
                link_score = basic_score[link_page] / len(ext_link[link_page])
            total_cnt += link_score
        total_score[pre_url] += total_cnt
    total = []
    for t in total_score.values():
        total.append(t)
    answer = total.index(max(total))
    return answer

solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"])

#feat(Jeongmu-Jo): [카카오, 2019블라인드] 매칭점수
