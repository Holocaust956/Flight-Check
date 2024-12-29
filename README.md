# Flight-Check
A scraper can look for the flight information of fliggy
# how to use 
1.pull the iamge
docker pull python:3.9-slim
docker pull selenium/standalone-chrome:latest
2.build the real iamges
docker-compose buil
3.run the containers
docker-compose run scraper python scraper/main.py --dep NKG(the IATA code of the airport in china) --arr WUH(the IATA code of the airport in china) --date 2024-12-31
4.wait for seconds then you can get the result
## the usual IATA code of the airport in china
ATA 代码	城市	机场名称
PEK	北京	北京首都国际机场
PKX	北京	北京大兴国际机场
SHA	上海	上海虹桥国际机场
PVG	上海	上海浦东国际机场
CAN	广州	广州白云国际机场
SZX	深圳	深圳宝安国际机场
CTU	成都	成都双流国际机场
TFU	成都	成都天府国际机场
CKG	重庆	重庆江北国际机场
XIY	西安	西安咸阳国际机场
HGH	杭州	杭州萧山国际机场
TAO	青岛	青岛流亭国际机场
XMN	厦门	厦门高崎国际机场
NKG	南京	南京禄口国际机场
WUH	武汉	武汉天河国际机场
CSX	长沙	长沙黄花国际机场
KMG	昆明	昆明长水国际机场
SHE	沈阳	沈阳桃仙国际机场
DLC	大连	大连周水子国际机场
TSN	天津	天津滨海国际机场
HAK	海口	海口美兰国际机场
SYX	三亚	三亚凤凰国际机场
URC	乌鲁木齐	乌鲁木齐地窝堡国际机场
HRB	哈尔滨	哈尔滨太平国际机场
TNA	济南	济南遥墙国际机场
NNG	南宁	南宁吴圩国际机场
FOC	福州	福州长乐国际机场
JJN	泉州	泉州晋江国际机场
ZUH	珠海	珠海金湾国际机场
SJW	石家庄	石家庄正定国际机场
TYN	太原	太原武宿国际机场
CGO	郑州	郑州新郑国际机场
NGB	宁波	宁波栎社国际机场
WNZ	温州	温州龙湾国际机场
HET	呼和浩特	呼和浩特白塔国际机场
XNN	西宁	西宁曹家堡国际机场
LHW	兰州	兰州中川国际机场
KHN	南昌	南昌昌北国际机场
KWL	桂林	桂林两江国际机场
LYG	连云港	连云港白塔埠机场
YNT	烟台	烟台蓬莱国际机场
WEH	威海	威海大水泊国际机场
JHG	西双版纳	西双版纳嘎洒国际机场
LXA	拉萨	拉萨贡嘎国际机场
DLU	大理	大理荒草坝机场
LJG	丽江	丽江三义国际机场
DNH	敦煌	敦煌莫高国际机场

