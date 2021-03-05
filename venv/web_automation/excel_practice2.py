"""
SBS 프로그램 엑셀 파일로 저장해 보기

티비랭킹닷컴의 SBS 프로그램 정보들만 모은 다음
SBS_데이터.xlsx 파일에 저장하기
    다른 방송사는 제외하고 채널 정보가 SBS인 프로그램의 정보들만 모으기
    티비랭킹닷컴에 있는 모든 기간의 데이터를 모아주기
        기간은 '_년_월_주차'형식으로 저장
    연도별 워크시트를 만들 필요 없이 하나의 워크시트에 쭉 저장하기
        워크시트 이름은 따로 설정 안해줘도 됨
    해더 행, 즉 테이블 열은 '기간', '순위', 프로그램', '시청률'로
"""

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()

ws.append(['기간', '순위', '프로그램', '시청률'])

for year in range(2010, 2019):
    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = "https://workey.codeit.kr/ratings/index" \
                  "?year={}&&month={}&&weekIndex={}" \
                .format(year, month, weekIndex)
            response = requests.get(url)
            rating_page = response.text
            soup = BeautifulSoup(rating_page, 'html.parser')

            for tr_tag in soup.select('tr')[1:]:
                td_tags = tr_tag.select('td')
                # channel = td_tags[1].get_text()
                channel = tr_tag.select_one('td.channel').get_text()
                if channel == 'SBS':
                    period = '{}년{}월{}주차'.format(year, month, weekIndex+1)
                    # row = [
                    #     period,
                    #     td_tags[0].get_text(),  # 순위
                    #     td_tags[2].get_text(),  # 프로그램
                    #     td_tags[3].get_text(),  # 시청률
                    # ]
                    # ws.append(row)
                    rank = td_tags[0].get_text()
                    program = td_tags[2].get_text()
                    percent = td_tags[3].get_text()
                    ws.append([period, rank, program, percent])

wb.save('SBS_데이터.xlsx')
