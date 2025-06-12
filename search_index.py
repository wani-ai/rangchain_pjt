import meilisearch
# meilisearch의 클라이언트의 객체
# client = meilisearch.Client('로컬호스트', '서버의키')
client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

# 서치하기
# def 
# # client.index('nasdaq').search("Apple")
#     client.index('nasdaq').search("AAPL")


def search_company(symbol):
# nasdaq :인덱스 객체(검색창 목록)
    return client.index('nasdaq').search(symbol)


# 자료 서칭을 위한 클래스
class SearchResult:
    # 객체 생성자, 클래스 객체화 할때 무조건 실행
    def __init__(self, item):
        self.item = item
    
    #심볼값 갖고오기
# property: 파이썬 데코레이터
    @property 
    def symbol(self):
        return self.item['Symbol']

    #회사명 가져오기
    @property 
    def name(self):
        return self.item['Name']
    
    def __str__(self):
        return f"{self.symbol}: {self.name}"


# 모듈테스트
if __name__=="__main__":


    #서치 키워드"
    # symbol = "AAPL"
    symbol = "AAPL"
    hits = search_company(symbol)['hits'][0]['Name']
    print(hits)
    # company_info = search_company['hits'][0]
    # company_name = search_company['hits'][0]
    # print(company_info)
    # print(f"{company_info}:{'hits'}")
    # result = []
    #리스트 컴프리핸선으로 변경
    result = [SearchResult(hit) for hit in hits]
    # result 최종 결과
    print(result[0].name)
    print(result[0].symbol)


  



