import asyncio
import discord
import time
from discord.channel import CategoryChannel
import requests
import json
import re #계산을 위한 특수문자 제거

client = discord.Client()

korea = "http://api.corona-19.kr/korea/beta/?serviceKey=" # 국내 코로나 발생 동향
vaccine = "https://api.corona-19.kr/korea/vaccine/?serviceKey=" # 예방접종 현황
key = "SECRET" #API 키(https://api.corona-19.kr/ 에서 무료 발급 가능)

@client.event
async def on_ready():
    client_id = str(client.user.id)
    print('Client ID: ' + client_id)
    game = discord.Game("!코로나, !백신 - 코로나19, 백신현황 상태 보기")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("")


@client.event
async def on_message(message):
    if message.content == "!코로나":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= data["API"]["updateTime"],  description= "국내 코로나바이러스감염증-19 현황입니다." ,  color=0x62c1cc)
          embed.add_field(name="국내 확진자", value=format(int(data["korea"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["korea"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="국내 사망자", value=format(int(data["korea"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="국내 완치자", value=format(int(data["korea"]["recCnt"]), ',') + "명") 
          embed.add_field(name="국내 치료중", value=format(int(data["korea"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["korea"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928991458097258546/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 국내 코로나 감염 동향")

    if message.content == "!백신":
          response2 = requests.get(vaccine + key)
          text2 = response2.text
          data = json.loads(text2)
          embed = discord.Embed(title= data["API"]["apiName"] + "(" + data["API"]["dataTime"] + ")",  description= "현재 대한민국의 코로나바이러스감염증-19 예방접종 현황입니다." ,  color=0x62c1cc)
          embed.add_field(name="1차 접종", value=format(int(data["korea"]["vaccine_1"]["vaccine_1"]), ',') +  "명" + "(+" + format(int(data["korea"]["vaccine_1"]["vaccine_1_new"]), ',') + "명)", inline=False)
          embed.add_field(name="2차 접종", value=format(int(data["korea"]["vaccine_2"]["vaccine_2"]), ',') +  "명" + "(+" + format(int(data["korea"]["vaccine_2"]["vaccine_2_new"]), ',') + "명)", inline=False)
          embed.add_field(name="3차 접종", value=format(int(data["korea"]["vaccine_3"]["vaccine_3"]), ',') +  "명" + "(+" + format(int(data["korea"]["vaccine_3"]["vaccine_3_new"]), ',') + "명)", inline=False)
          embed.set_image(url="https://cdn.discordapp.com/attachments/923205330039636059/928970841272746034/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다. : 국내 예방접종 정보")

    if message.content == "!코로나 지역":
          response2 = requests.get(vaccine + key)
          text2 = response2.text
          data = json.loads(text2)
          embed = discord.Embed(title="지역별 코로나 감염 정보",  description= "다음 명령어를 통해 지역별 감염 정보를 확인하실 수 있습니다." ,  color=0x62c1cc)
          embed.add_field(name="서울특별시", value="**!서울**", inline=True)
          embed.add_field(name="부산광역시", value="**!부산**", inline=True)
          embed.add_field(name="대구광역시", value="**!대구**", inline=True)
          embed.add_field(name="인천광역시", value="**!인천**", inline=True)
          embed.add_field(name="광주광역시", value="**!광주**", inline=True)
          embed.add_field(name="대전광역시", value="**!대전**", inline=True)
          embed.add_field(name="울산광역시", value="**!울산**", inline=True)
          embed.add_field(name="세종특별자치시", value="**!세종**", inline=True)
          embed.add_field(name="경기도", value="**!경기**", inline=True)
          embed.add_field(name="강원도", value="**!강원**", inline=True)
          embed.add_field(name="충청북도", value="**!충북**", inline=True)
          embed.add_field(name="충청남도", value="**!충남**", inline=True)
          embed.add_field(name="전라북도", value="**!전북**", inline=True)
          embed.add_field(name="전라남도", value="**!전남**", inline=True)
          embed.add_field(name="경상북도", value="**!경북**", inline=True)
          embed.add_field(name="경상남도", value="**!경남**", inline=True)
          embed.add_field(name="제주도", value="**!제주**", inline=True)
          embed.add_field(name="검역", value="**!검역**", inline=True)
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928991497884426280/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)

          print("정보 요청이 확인되었습니다. : 국내 예방접종 정보")

# 다음부터 지역별 코로나 감염 정보입니다. 제작자가 뉴비라 일일히 추가했어요 ㅠ
    if message.content == "!서울":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "서울 코로나 감염 정보",  description= "서울특별시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["seoul"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["seoul"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["seoul"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["seoul"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["seoul"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["seoul"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996534048149514/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 서울 코로나 감염 동향")

    if message.content == "!부산":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "부산 코로나 감염 정보",  description= "부산광역시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["busan"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["busan"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["busan"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["busan"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["busan"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["busan"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997107862487060/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 부산 코로나 감염 동향")

    if message.content == "!대구":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "대구 코로나 감염 정보",  description= "대구광역시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["daegu"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["daegu"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["daegu"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["daegu"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["daegu"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["daegu"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996974752067594/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 대구 코로나 감염 동향")

    if message.content == "!인천":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "인천 코로나 감염 정보",  description= "인천광역시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["incheon"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["incheon"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["incheon"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["incheon"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["incheon"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["incheon"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996934948114522/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 인천 코로나 감염 동향")

    if message.content == "!광주":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "광주 코로나 감염 정보",  description= "광주광역시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["gwangju"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["gwangju"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["gwangju"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["gwangju"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["gwangju"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["gwangju"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996731557924915/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 광주 코로나 감염 동향")

    if message.content == "!대전":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "대전 코로나 감염 정보",  description= "대전광역시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["daejeon"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["daejeon"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["daejeon"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["daejeon"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["daejeon"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["daejeon"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996634921156668/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 대전 코로나 감염 동향")

    if message.content == "!울산":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "울산 코로나 감염 정보",  description= "울산광역시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["ulsan"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["ulsan"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["ulsan"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["ulsan"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["ulsan"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["ulsan"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997134978674688/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 울산 코로나 감염 동향")

    if message.content == "!세종":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "세종 코로나 감염 정보",  description= "세종특별자치시 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["sejong"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["sejong"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["sejong"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["sejong"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["sejong"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["sejong"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997186342105118/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 세종 코로나 감염 동향")

    if message.content == "!경기":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "경기 코로나 감염 정보",  description= "경기도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["gyeonggi"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["gyeonggi"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["gyeonggi"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["gyeonggi"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["gyeonggi"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["gyeonggi"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/929000998075265044/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 경기도 코로나 감염 동향")

    if message.content == "!강원":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "강원 코로나 감염 정보",  description= "강원도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["gangwon"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["gangwon"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["gangwon"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["gangwon"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["gangwon"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["gangwon"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997216796946442/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 강원도 코로나 감염 동향")

    if message.content == "!충북":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "충북 코로나 감염 정보",  description= "충청북도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["chungbuk"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["chungbuk"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["chungbuk"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["chungbuk"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["chungbuk"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["chungbuk"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996664428081212/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 충청북도 코로나 감염 동향")

    if message.content == "!충남":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "충남 코로나 감염 정보",  description= "충청남도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["chungnam"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["chungnam"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["chungnam"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["chungnam"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["chungnam"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["chungnam"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996698343239710/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 충청남도 코로나 감염 동향")

    if message.content == "!전북":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "전북 코로나 감염 정보",  description= "전라북도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["jeonbuk"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["jeonbuk"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["jeonbuk"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["jeonbuk"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["jeonbuk"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["jeonbuk"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996765619879946/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 전라북도 코로나 감염 동향")

    if message.content == "!전남":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "전남 코로나 감염 정보",  description= "전라남도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["jeonnam"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["jeonnam"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["jeonnam"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["jeonnam"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["jeonnam"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["jeonnam"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928996829645930506/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 전라남도 코로나 감염 동향")

    if message.content == "!경북":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "경북 코로나 감염 정보",  description= "경상북도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["gyeongbuk"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["gyeongbuk"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["gyeongbuk"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["gyeongbuk"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["gyeongbuk"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["gyeongbuk"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997000228274196/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 경상북도 코로나 감염 동향")

    if message.content == "!경남":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "경남 코로나 감염 정보",  description= "경상남도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["gyeongnam"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["gyeongnam"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["gyeongnam"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["gyeongnam"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["gyeongnam"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["gyeongnam"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997160496824370/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 경상남도 코로나 감염 동향")

    if message.content == "!제주":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "제주 코로나 감염 정보",  description= "제주특별자치도 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["jeju"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["jeju"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["jeju"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["jeju"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["jeju"]["isolCnt"]), ',') + "명") 
          embed.add_field(name="코로나 발생률", value=str(data["jeju"]["qurRate"]) + "%")
          embed.set_image(url="https://cdn.discordapp.com/attachments/928991449616384001/928997247088197702/2x1.png")
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 제주도 코로나 감염 동향")

    if message.content == "!검역":
          response = requests.get(korea + key)
          text = response.text 
          data = json.loads(text)
          embed = discord.Embed(title= "검역 감염 정보",  description= "해외 입국 검역의 코로나 감염 정보입니다." ,  color=0x62c1cc)
          embed.add_field(name="전체 확진자", value=format(int(data["quarantine"]["totalCnt"]), ',') +  "명" + "(+" + format(int(data["quarantine"]["incDec"]), ',') + "명)", inline=True)
          embed.add_field(name="전체 사망자", value=format(int(data["quarantine"]["deathCnt"]), ',') + "명") 
          embed.add_field(name="전체 완치자", value=format(int(data["quarantine"]["recCnt"]), ',') + "명") 
          embed.add_field(name="치료중 환자", value=format(int(data["quarantine"]["isolCnt"]), ',') + "명") 
          embed.set_footer(text="Copyright © DevEnne. All rights reserved.")
          await message.channel.send(embed=embed)
          print("정보 요청이 확인되었습니다.: 검역 감염 동향")






client.run("Client.key")
