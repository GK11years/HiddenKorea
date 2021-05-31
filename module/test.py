# -*- coding: utf-8 -*-

import imp
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
import re

url = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '+t/RGnLoxMzOUg5Uj/QT8QZQmp849OGnpscGH+TCYnegCW23VlIZti9wnNXRsoWCXOVsCTFI2LzzBZcb8bqXDQ==', quote_plus('pageNo') : '1', quote_plus('numOfRows') : '4', quote_plus('MobileApp') : 'AppTest', quote_plus('MobileOS') : 'ETC', quote_plus('arrange') : 'A', quote_plus('cat1') : '', quote_plus('contentTypeId') : '12', quote_plus('areaCode') : '1', quote_plus('sigunguCode') : '4', quote_plus('cat2') : '', quote_plus('cat3') : '', quote_plus('listYN') : 'Y', quote_plus('modifiedtime') : '' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
output = response_body.decode('utf-8')

print(output.findall('title'))
# relist = re.findall("<title>(.*)</title>",output)
# print(relist)

# 구글 주소 : https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371335%2C4401769%2C4419364%2C4429192%2C4482438%2C4486153%2C4509341%2C4515403%2C4533882%2C4536454%2C4554491%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwj7quHP-_PwAhVaMd4KHW7wBw0QuL0BMAh6BAgXEDg#ttdm=37.567336_126.982808_13&ttdmf=%252Fm%252F02qpf1

# text = "봄에 가야 화사한 절경을 볼 수 있는 고궁!서울 여행 코스 중에서 빼놓을 수 없는 우리나라 3대 궁궐을 다녀왔는데요, 혼자서울여행이라 3곳을 보는것만으로도 힘들어서 덕수궁과 경희궁은 못갔다왔어요 ㅋㅋ꽃피는 봄 얼마나 아름다운지 감상해보세요~​​서울 가볼만한곳 5곳1. 창경궁2. 창덕궁(후원예약 필수예용!)3. 경복궁4. 광장시장 육회5. 북촌한옥마을​​창경궁서울 종로구 창경궁로 185 창경궁매일 09:00 - 21:00매표. 입장시간 20시까지입장료 1,000원​주차정보작은 규모지만 창경궁과 창덕궁 전용주차장이 따로 있어요. 얼마전까지 무료개방을 했었는데요, 4월 27일부로 다시 유료로 정상운영중이랍니다.​​길건너 맞은편에 서울대학교병원 주차장이 있어요.실내이고 더 편하게 차를 댈 수 있는게 장점이었어요.​​요금은 기본 30분까지는 무료이고 40분은 2,000원 이후 10분 초과시마다 500원이에요.한시간에 3,000원이라고 보시면 돼요.저희는 여기에 주차했어요.​​대중교통으로 오신다면 창경궁, 서울대학교 정류장에서 내리면 걸어서 1분거리에 있어서 찾아가기 아주 쉽답니다.덕수궁 돌담길이 서울 가볼만한곳인만큼 그렇게 유명하다지만 철쭉꽃길 화사한 창경궁 돌담길 역시 아름답네요.​​입장요금 시스템이 정말 다양했어요.개별 관람료는 1,000원, 창덕궁 연계관람은 3,000원이고 월요일은 개방하지 않는다는 점 참고하세요.신기한건 1개월 상시관람과 시간제 1년관람권이 있다는거! 근처 사는 분들이라면 30,000원 내고 이거 끊을거 같네요 ㅋㅋ​​천원내고 들어갔어요~입구에서 창경궁 가이드북을 하나 챙기고 하나하나 둘러봤습니다.​​역시 봄은 봄이었어요.푸릇푸릇하고 풍성한 나무들과 파랗게 어우러진 하늘이 그렇게 예쁠 수가 없더라고요.​여행일 : 2021년 4월 18일​​성종 14년에 정희왕후, 안순왕후, 소혜왕후 세분의 대비를 모시기 위해 옛 수강궁터에 창건한 궁으로 수강궁은 세종 즉위년 1418년, 세종이 상왕으로 물러난 태종의 거처를 위해서 마련하였어요.​​창경궁 대온실은 현재 개방되지 않음!보이는 곳에서 안쪽으로 가면 등록문화재인 대온실인데 여기 뿐 아니라 덕수궁 석조전이나 창덕궁 약방같은 실내 관람은 전부 중단된 상태랍니다.​​오랜 역사의 흔적을 그대로 간직하고 있어서 나무로 지은 궁궐에는 오랜 세월이 묻어있었어요.​​통명전 철쭉을 비롯한 봄꽃들이 어찌나 아름다운지 궁녀들이 궐안에서 절경을 보며 꺄르르 웃었을 모습이 연상되더군요. 카메라가 있었으면 셀카 엄청 찍었겠죠? ㅎㅎ​​연달래봄 진달래는 비교도 안될정도로 청초하게 피어난 생명​양화당 뒷산뜰 쪽으로 올라가니 연달래가 만개한 모습을 볼 수 있었어요.태어나서 처음봤는데요~ 벚꽃보다 훨씬 돋보이는 청순미에 매료되어 한참을 넋을 놓고 봤어요.​​인디핑크색상의 큰 꽃망울!조선시대에 이런 볼거리가 있으니 궐밖을 나가지 않고도 살 수 있었겠지요.​​뜰을 지나 한참을 더 올라가면 서울 여행 코스인 대온실이 나오는데, 가이드를 제대로 안봐서 못보고 돌아왔네요​​해시계보는 방법이 상세히 나와있어요. 근데, 이해가 잘 안가더라고요. 그냥 옛 선조들이 대단하다는 생각밖에.. ㅋㅋ​​봄 기운을 누리며 창덕궁 입구인 함양문쪽으로 올라갔어요. 한복입고 왔다면 인생샷 찍을 수 있었겠죠?​​​창덕궁서울 종로구 율곡로 99매일 09:00 - 18:00/18:30 월요일 휴무​세계유산 창덕궁 입장료는 3,000원입니다.연결되어 있는줄 알았다면 미리 연계관람권을 끊는건데, 1,000원 손해봤네요~​​창덕궁 후원예약 방법서울 가볼만한곳으로 손꼽히는 후원은 따로 추가예매를 해야하며(5,000원) 미리 예매를 하거나 당일 현장구매를 해야해요.​관랍일 6일전 10:00 부터 선착순으로 예매가 마감되며 입장마감 2시간전까지만 무료취소가 가능합니다.남아있는 인터넷 예매분량만 현장 매표소에서 선착순 판매한다는 점 참고하세요!​​​​미리 정보를 알고가지 못한 저는 그냥 창덕궁만 구경했어요. 북악산 응봉자락에 자리잡은 서울궁궐!​​굳이 궁에 대해 자세한 정보를 몰라도 다양하게 핀 봄꽃만 구경하며 다녀도 시간이 훌쩍 지나간답니다.두 고궁을 얕게 둘러보는데 한시간이 넘게 소요됐어요.​​여기도 청초함이 빛나는 연달래꽃이 있길래 저도 셀카 한장 찍었는데요, 뒤로 올라가면 창덕궁 후원과 연결되는거 같았어요. 들어가지 못하게 막아놨네요 ㅠㅠ​​연인들도 정말 많았고, 아이들과 함께 온 가족단위 방문객들도 많았어요. 유모차 끌고 대조전 계단을 내려오던 아버님이 넘어지면서 유모차가 뒤집어져 아이가 굴러 떨어지는 바람에 다들 엄청나게 놀랐어요.부모님들은 다니실때 각별히 주의하셔야 할듯요.​​외국인들도 참 많았는데요,역시 우리나라 고유의 유산이 멋있다고 생각되는 순간이었어요. 고궁은 필수 서울 여행 코스니까요~​​더워서 창덕궁 안에 있는 카페로 들어가 청포도 주스 한잔 사먹었습니다. 이거 진짜 맛있더라는요~​한복입으면 무료입장입니다!저도 다음에 오면 꼭 한복입어야겠어요. 뒤에 여러분들은 전부 외국인들이었는데, 그렇게 이쁠 수가 없더라고요 ㅎㅎ​​경복궁서울 종로구 사직로 161 경복궁매일 09:00 - 18:00/18:30 화요일 휴무​마지막으로 소개할 서울 여행 코스는 경복궁이에요.서울 가볼만한곳 광화문으로 들어가면 바로 경복궁인거 아시죠? ㅎㅎ입장료는 3,000원입니다.​​주차정보광화문에서 삼청동으로 가는 길 초입 좌측에 부설주차장이 있어요. 기본 2시간에 3,000원​​경복궁 경회루 꼭 보시는거 추천드려요!다 둘러보는데 2시간은 걸리니까 여유가 없는 분들은 경회루만큼은 꼭 가보셔야해요~한국의 미가 눈부시도록 아름답다는걸 느끼실 수 있을거에요.​​여기가 경회루 들어가는 함홍문인데요, 예약으로 이루어지던 경회루 특별관람은 진행되지 않으니 참고하세요.​경복궁 한복! 붉은치마 입으세요~고즈넉하고 품위있는 고궁과 가장 잘 어울리는 한복이 붉은색과 하늘색 또는 핑크색치마에요. (무료입장)​​광화문을 시작으로 정해진 경복궁 서울 여행 코스가 있으니 미리 알고 가시는게 좋고요, 국립고궁박물관과 국립민속박물관이 붙어 있으니까 같이 보는 일정으로 짜면 딱 좋을듯 합니다.​​광장시장 육회​아침부터 경복궁 - 북촌한옥마을 - 광장시장 - 종묘 - 창경궁 - 창덕궁 서울 가볼만한곳 코스로 둘러보신다면 그날 저녁에 잠은 푹 잘 주무실거에요 ㅋㅋ광장시장 육회는 저렴하고 가성비가 좋은데, 자매집에 가장 유명하답니다.​​"

# if "국립고궁박물관" in text:
#     print("yes")