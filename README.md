# bm25-search

### corpus

1\. 송영숙 님의 챗봇 데이터

**[https://github.com/songys/Chatbot\_data](https://github.com/songys/Chatbot_data)**

2\. AI-HUB 웰니스 상담 데이터

**[https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006)**

3\. AI-HUB 감성대화 말뭉치

[https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=86](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=86) 

### how to use
```python
if __name__ == "__main__":
    print(bm25_search('나 오늘 여친이랑 헤어졌어 ㅠㅠ', n=5))
```

### result
```python
['오늘 헤어졌어.', '오늘 헤어졌습니다.', '오늘 헤어졌어여', '2년 가까이 여친하구 헤어졌습니다', '오늘도 전 여친sns를 봤습니다']
```

