프로젝트 02 숫자 야구
규칙
컴퓨터는 0과 9사이의 서로 다른 숫자 3개를 무작위로 뽑음
사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야함
컴퓨터는 사용자가 입력한 숫자 3개에 대해서,

아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줌
숫자의 값과 위치가 모두 일치하면 S
숫자의 값은 일치하지만 위치가 틀렸으면 B

기회는 무제한, 하지만 몇 번의 시도 끝에 맞췄는지 기록
3S가 나오면 게임이 끝남

진행 방식
“0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.” 출력
“숫자 3개를 하나씩 차례대로 입력하세요.” 출력
“1번째 숫자를 입력하세요: “가 출력되고, 사용자로부터 입력을 받음
같은 방법으로 3번째까지 받되,
만약 사용자가 중복되는 숫자를 입력하거나 범위에서 벗어나는 숫자를 입력하면, 다시 입력 받음
올바르게 3개를 입력하면, 규칙에 따라 “*S * B” 출력
3S가 아닌 경우, 2번부터 다시 진행
사용자가 3S를 달성하면, “축하합니다. *번만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.” 출력, 게임 종료
