import youtube_dl

ydl_opt = {
    # 이거 쓰면 다운 안받아짐 지우고 해야함
    # 'listformats': True,  # 다운로드가 가능한 모든 포맷 출력함
    # 보통 best 인 포맷을 다운 받음 dash 붙은건 비디오나 오디오만 있는거
    # 'format': '22', # 리스트에서 해당 번호 써주면됨
    # 'format': 'best[height<=480]', # 이렇게 포맷 쓸 수도 있음
    'format': 'best[filesize<10M]', # 이렇게 포맷 쓸 수도 있음
    'outtmpl': '%(title)s %(resolution)s.%(ext)s',
    # 파일 이름 자동으로 만들어주는거 '제목 뒤에 파일 해상도 파일 형식으로 쓰겠다는거
}

# YoutubeDL 객체 생성해서 ydl 변수에 저장
with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    # 파라미러로 다운받고 싶은 영상 주소 넣으면 됨, 재생 목록의 주소를 넣어도 됨
    ydl.download(['https://youtu.be/fqePssqQ6BY'])
