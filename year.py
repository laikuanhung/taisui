# 定義六十甲子的列表
GANYI = [
    "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
    "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
    "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
    "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
    "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
    "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"
]

# 六十太歲列表
TAISUI = [
    "甲子太歲金辨大將軍", "乙丑太歲陳林大將軍", "丙寅太歲耿章大將軍", "丁卯太歲沉興大將軍",
    "戊辰太歲趙達大將軍", "己巳太歲郭燦大將軍", "庚午太歲王清大將軍", "辛未太歲李素大將軍",
    "壬申太歲劉旺大將軍", "癸酉太歲康志大將軍", "甲戌太歲施廣大將軍", "乙亥太歲任保大將軍",
    "丙子太歲郭嘉大將軍", "丁丑太歲汪文大將軍", "戊寅太歲曾光大將軍", "己卯太歲龍仲大將軍",
    "庚辰太歲董德大將軍", "辛巳太歲鄭但大將軍", "壬午太歲陸明大將軍", "癸未太歲魏仁大將軍",
    "甲申太歲方查大將軍", "乙酉太歲蔣崇大將軍", "丙戌太歲白敏大將軍", "丁亥太歲封濟大將軍",
    "戊子太歲鄒鏜大將軍", "己丑太歲潘佐大將軍", "庚寅太歲鄔桓大將軍", "辛卯太歲范寧大將軍",
    "壬辰太歲彭泰大將軍", "癸巳太歲徐單大將軍", "甲午太歲章詞大將軍", "乙未太歲楊仙大將軍",
    "丙申太歲管仲大將軍", "丁酉太歲唐查大將軍", "戊戌太歲姜武大將軍", "己亥太歲謝太大將軍",
    "庚子太歲盧秘大將軍", "辛丑太歲楊信大將軍", "壬寅太歲賀諤大將軍", "癸卯太歲皮時大將軍",
    "甲辰太歲李誠大將軍", "乙巳太歲吳遂大將軍", "丙午太歲文哲大將軍", "丁未太歲謬丙大將軍",
    "戊申太歲徐浩大將軍", "己酉太歲程寶大將軍", "庚戌太歲倪秘大將軍", "辛亥太歲葉堅大將軍",
    "壬子太歲丘德大將軍", "癸丑太歲朱得大將軍", "甲寅太歲張朝大將軍", "乙卯太歲萬清大將軍",
    "丙辰太歲辛亞大將軍", "丁巳太歲楊彦大將軍", "戊午太歲黎卿大將軍", "己未太歲傅賞大將軍",
    "庚申太歲毛梓大將軍", "辛酉太歲石政大將軍", "壬戌太歲洪充大將軍", "癸亥太歲虞程大將軍"
]

# 本命星官
BENMING_STAR_OFFICIAL = {
    "甲子": {"name": "王文卿", "officials": 18},
    "乙丑": {"name": "龍季卿", "officials": 16},
    "丙寅": {"name": "張仲卿", "officials": 14},
    "丁卯": {"name": "司馬卿", "officials": 12},
    "戊辰": {"name": "季楚卿", "officials": 10},
    "己巳": {"name": "何文昌", "officials": 13},
    "庚午": {"name": "馮仲卿", "officials": 17},
    "辛未": {"name": "王文章", "officials": 15},
    "壬申": {"name": "侯博卿", "officials": 13},
    "癸酉": {"name": "孫仲房", "officials": 11},
    "甲戌": {"name": "展子江", "officials": 14},
    "乙亥": {"name": "龐明心", "officials": 12},
    "丙子": {"name": "邢孫卿", "officials": 16},
    "丁丑": {"name": "趙子玉", "officials": 14},
    "戊寅": {"name": "虞子張", "officials": 12},
    "己卯": {"name": "石文陽", "officials": 15},
    "庚辰": {"name": "尹佳卿", "officials": 13},
    "辛巳": {"name": "陽仲公", "officials": 11},
    "壬午": {"name": "馬子明", "officials": 15},
    "癸未": {"name": "呂威明", "officials": 13},
    "甲申": {"name": "扈文長", "officials": 16},
    "乙酉": {"name": "孔利公", "officials": 14},
    "丙戌": {"name": "車元昇", "officials": 12},
    "丁亥": {"name": "張文通", "officials": 10},
    "戊子": {"name": "樂石陽", "officials": 14},
    "己丑": {"name": "范仲陽", "officials": 17},
    "庚寅": {"name": "褚進卿", "officials": 15},
    "辛卯": {"name": "郭子良", "officials": 13},
    "壬辰": {"name": "武稚卿", "officials": 11},
    "癸巳": {"name": "史公來", "officials": 9},
    "甲午": {"name": "衛上卿", "officials": 18},
    "乙未": {"name": "杜仲陽", "officials": 16},
    "丙申": {"name": "朱伯眾", "officials": 14},
    "丁酉": {"name": "臧文公", "officials": 12},
    "戊戌": {"name": "范少卿", "officials": 10},
    "己亥": {"name": "鄧都卿", "officials": 13},
    "庚子": {"name": "楊仲昇", "officials": 17},
    "辛丑": {"name": "林衛公", "officials": 15},
    "壬寅": {"name": "丘孟卿", "officials": 13},
    "癸卯": {"name": "蘇他家", "officials": 11},
    "甲辰": {"name": "孟非卿", "officials": 14},
    "乙巳": {"name": "唐文卿", "officials": 12},
    "丙午": {"name": "魏文公", "officials": 16},
    "丁未": {"name": "石叔通", "officials": 14},
    "戊申": {"name": "范伯陽", "officials": 12},
    "己酉": {"name": "成文長", "officials": 15},
    "庚戌": {"name": "史子仁", "officials": 13},
    "辛亥": {"name": "左子行", "officials": 11},
    "壬子": {"name": "宿上卿", "officials": 15},
    "癸丑": {"name": "江漢卿", "officials": 13},
    "甲寅": {"name": "明文章", "officials": 16},
    "乙卯": {"name": "戴公陽", "officials": 14},
    "丙辰": {"name": "霍叔英", "officials": 12},
    "丁巳": {"name": "崔巨卿", "officials": 10},
    "戊午": {"name": "從天光", "officials": 14},
    "己未": {"name": "時通卿", "officials": 17},
    "庚申": {"name": "華文陽", "officials": 15},
    "辛酉": {"name": "邴元玉", "officials": 13},
    "壬戌": {"name": "樂進卿", "officials": 11},
    "癸亥": {"name": "左石松", "officials": 9}
}

# 元辰星官
YUANCHEN_STAR_OFFICIAL = {
    "男": {
        "甲子": {"name": "杜仲陽", "officials": 16, "year": "乙未"},
        "乙丑": {"name": "衛上卿", "officials": 18, "year": "甲午"},
        "丙寅": {"name": "臧文公", "officials": 12, "year": "丁酉"},
        "丁卯": {"name": "朱伯眾", "officials": 14, "year": "丙申"},
        "戊辰": {"name": "鄧都卿", "officials": 13, "year": "己亥"},
        "己巳": {"name": "范少卿", "officials": 10, "year": "戊戌"},
        "庚午": {"name": "林衛公", "officials": 15, "year": "辛丑"},
        "辛未": {"name": "楊仲昇", "officials": 17, "year": "庚子"},
        "壬申": {"name": "蘇他家", "officials": 11, "year": "癸卯"},
        "癸酉": {"name": "丘孟卿", "officials": 13, "year": "壬寅"},
        "甲戌": {"name": "唐文卿", "officials": 12, "year": "乙巳"},
        "乙亥": {"name": "孟非卿", "officials": 14, "year": "甲辰"},
        "丙子": {"name": "石叔通", "officials": 14, "year": "丁未"},
        "丁丑": {"name": "魏文公", "officials": 16, "year": "丙午"},
        "戊寅": {"name": "成文長", "officials": 15, "year": "己酉"},
        "己卯": {"name": "范伯陽", "officials": 12, "year": "戊申"},
        "庚辰": {"name": "左子行", "officials": 11, "year": "辛亥"},
        "辛巳": {"name": "史子仁", "officials": 13, "year": "庚戌"},
        "壬午": {"name": "江漢卿", "officials": 13, "year": "癸丑"},
        "癸未": {"name": "宿上卿", "officials": 15, "year": "壬子"},
        "甲申": {"name": "戴公陽", "officials": 14, "year": "乙卯"},
        "乙酉": {"name": "明文章", "officials": 16, "year": "甲寅"},
        "丙戌": {"name": "崔巨卿", "officials": 10, "year": "丁巳"},
        "丁亥": {"name": "霍叔英", "officials": 12, "year": "丙辰"},
        "戊子": {"name": "時通卿", "officials": 17, "year": "己未"},
        "己丑": {"name": "從元光", "officials": 14, "year": "戊午"},#(從天光?)
        "庚寅": {"name": "邴元玉", "officials": 13, "year": "辛酉"},
        "辛卯": {"name": "華文陽", "officials": 15, "year": "庚申"},
        "壬辰": {"name": "左石松", "officials": 9, "year": "癸亥"},
        "癸巳": {"name": "樂進卿", "officials": 11, "year": "壬戌"},
        "甲午": {"name": "龍季卿", "officials": 16, "year": "乙丑"},
        "乙未": {"name": "王文卿", "officials": 18, "year": "甲子"},
        "丙申": {"name": "司馬卿", "officials": 11, "year": "丁卯"},#從官數有問題(應為十二)
        "丁酉": {"name": "張仲卿", "officials": 14, "year": "丙寅"},
        "戊戌": {"name": "何文昌", "officials": 13, "year": "己巳"},
        "己亥": {"name": "季楚卿", "officials": 10, "year": "戊辰"},
        "庚子": {"name": "王文章", "officials": 15, "year": "辛未"},
        "辛丑": {"name": "馮仲卿", "officials": 17, "year": "庚午"},
        "壬寅": {"name": "孫仲房", "officials": 11, "year": "癸酉"},
        "癸卯": {"name": "侯博卿", "officials": 13, "year": "壬申"},
        "甲辰": {"name": "龐明心", "officials": 12, "year": "乙亥"},
        "乙巳": {"name": "展子江", "officials": 14, "year": "甲戌"},
        "丙午": {"name": "趙子玉", "officials": 14, "year": "丁丑"},
        "丁未": {"name": "邢孫卿", "officials": 16, "year": "丙子"},
        "戊申": {"name": "石文陽", "officials": 15, "year": "己卯"},
        "己酉": {"name": "虞子張", "officials": 12, "year": "戊寅"},
        "庚戌": {"name": "陽仲公", "officials": 11, "year": "辛巳"},
        "辛亥": {"name": "尹佳卿", "officials": 13, "year": "庚辰"},
        "壬子": {"name": "呂威明", "officials": 13, "year": "癸未"},
        "癸丑": {"name": "馬子明", "officials": 15, "year": "壬午"},
        "甲寅": {"name": "孔利公", "officials": 14, "year": "乙酉"},
        "乙卯": {"name": "扈文長", "officials": 16, "year": "甲申"},
        "丙辰": {"name": "張文通", "officials": 10, "year": "丁亥"},
        "丁巳": {"name": "車元昇", "officials": 12, "year": "丙戌"},
        "戊午": {"name": "范仲陽", "officials": 17, "year": "己丑"},
        "己未": {"name": "樂石陽", "officials": 14, "year": "戊子"},
        "庚申": {"name": "郭子良", "officials": 13, "year": "辛卯"},
        "辛酉": {"name": "褚進卿", "officials": 15, "year": "庚寅"},
        "壬戌": {"name": "史公來", "officials": 9, "year": "癸巳"},
        "癸亥": {"name": "武稚卿", "officials": 11, "year": "壬辰"}
    },
    "女": {
        "甲子": {"name": "史公來", "officials": 9, "year": "癸巳"},
        "乙丑": {"name": "朱伯眾", "officials": 14, "year": "丙申"},
        "丙寅": {"name": "杜仲陽", "officials": 16, "year": "乙未"},
        "丁卯": {"name": "范少卿", "officials": 10, "year": "戊戌"},
        "戊辰": {"name": "臧文公", "officials": 12, "year": "丁酉"},
        "己巳": {"name": "楊仲昇", "officials": 17, "year": "庚子"},
        "庚午": {"name": "鄧都卿", "officials": 13, "year": "己亥"},
        "辛未": {"name": "丘孟卿", "officials": 13, "year": "壬寅"},
        "壬申": {"name": "林衛公", "officials": 15, "year": "辛丑"},
        "癸酉": {"name": "孟非卿", "officials": 14, "year": "甲辰"},
        "甲戌": {"name": "蘇他家", "officials": 11, "year": "癸卯"},
        "乙亥": {"name": "魏文公", "officials": 16, "year": "丙午"},
        "丙子": {"name": "唐文卿", "officials": 12, "year": "乙巳"},
        "丁丑": {"name": "范伯陽", "officials": 12, "year": "戊申"},
        "戊寅": {"name": "石叔通", "officials": 14, "year": "丁未"},
        "己卯": {"name": "史子仁", "officials": 13, "year": "庚戌"},
        "庚辰": {"name": "成文長", "officials": 15, "year": "己酉"},
        "辛巳": {"name": "宿上卿", "officials": 15, "year": "壬子"},
        "壬午": {"name": "左子行", "officials": 11, "year": "辛亥"},
        "癸未": {"name": "明文章", "officials": 16, "year": "甲寅"},
        "甲申": {"name": "江漢卿", "officials": 13, "year": "癸丑"},
        "乙酉": {"name": "霍叔英", "officials": 12, "year": "丙辰"},
        "丙戌": {"name": "戴公陽", "officials": 14, "year": "乙卯"},
        "丁亥": {"name": "從元光", "officials": 14, "year": "戊午"},
        "戊子": {"name": "崔巨卿", "officials": 10, "year": "丁巳"},
        "己丑": {"name": "華文陽", "officials": 15, "year": "庚申"},
        "庚寅": {"name": "時通卿", "officials": 17, "year": "己未"},
        "辛卯": {"name": "樂進卿", "officials": 11, "year": "壬戌"},
        "壬辰": {"name": "邴元玉", "officials": 13, "year": "辛酉"},
        "癸巳": {"name": "王文卿", "officials": 18, "year": "甲子"},
        "甲午": {"name": "左石松", "officials": 9, "year": "癸亥"},
        "乙未": {"name": "張仲卿", "officials": 14, "year": "丙寅"},
        "丙申": {"name": "龍季卿", "officials": 16, "year": "乙丑"},
        "丁酉": {"name": "季楚卿", "officials": 10, "year": "戊辰"},
        "戊戌": {"name": "司馬卿", "officials": 12, "year": "丁卯"},
        "己亥": {"name": "馮仲卿", "officials": 17, "year": "庚午"},
        "庚子": {"name": "何文昌", "officials": 13, "year": "己巳"},
        "辛丑": {"name": "侯博卿", "officials": 13, "year": "壬申"},
        "壬寅": {"name": "王文章", "officials": 15, "year": "辛未"},
        "癸卯": {"name": "展子江", "officials": 14, "year": "甲戌"},
        "甲辰": {"name": "孫仲房", "officials": 11, "year": "癸酉"},
        "乙巳": {"name": "邢孫卿", "officials": 16, "year": "丙子"},
        "丙午": {"name": "龐明心", "officials": 12, "year": "乙亥"},
        "丁未": {"name": "虞子張", "officials": 12, "year": "戊寅"},
        "戊申": {"name": "趙子玉", "officials": 14, "year": "丁丑"},
        "己酉": {"name": "尹佳卿", "officials": 13, "year": "庚辰"},
        "庚戌": {"name": "石文陽", "officials": 15, "year": "己卯"},
        "辛亥": {"name": "馬子明", "officials": 15, "year": "壬午"},
        "壬子": {"name": "陽仲公", "officials": 11, "year": "辛巳"},
        "癸丑": {"name": "扈文長", "officials": 16, "year": "甲申"},
        "甲寅": {"name": "呂威明", "officials": 13, "year": "癸未"},
        "乙卯": {"name": "車元昇", "officials": 12, "year": "丙戌"},
        "丙辰": {"name": "孔利公", "officials": 14, "year": "乙酉"},
        "丁巳": {"name": "樂石陽", "officials": 14, "year": "戊子"},
        "戊午": {"name": "張文通", "officials": 10, "year": "丁亥"},
        "己未": {"name": "褚進卿", "officials": 15, "year": "庚寅"},
        "庚申": {"name": "范仲陽", "officials": 17, "year": "己丑"},
        "辛酉": {"name": "武稚卿", "officials": 11, "year": "壬辰"},
        "壬戌": {"name": "郭子良", "officials": 13, "year": "辛卯"},
        "癸亥": {"name": "衛上卿", "officials": 18, "year": "甲午"}
    }
}

# 本命星君
BENMING_STAR = {
    "子": "北斗第一陽明貪狼太星君",
    "丑": "北斗第二陰精巨門元星君",
    "寅": "北斗第三真人祿存貞星君",
    "卯": "北斗第四玄冥文曲紐星君",
    "辰": "北斗第五丹元廉貞綱星君",
    "巳": "北斗第六北極武曲紀星君",
    "午": "北斗第七天關破軍關星君",
    "未": "北斗第六北極武曲紀星君",
    "申": "北斗第五丹元廉貞罡星君",
    "酉": "北斗第四玄冥文曲紐星君",
    "戌": "北斗第三真人祿存貞星君",
    "亥": "北斗第二陰精巨門元星君"
}

# 元辰星君
YUANCHEN_STAR = {
    "男": {
        "子": "北斗第八洞明外輔星君",
        "丑": "北斗第九隱光內弼星君",
        "寅": "北斗第八洞明外輔星君",
        "卯": "北斗第九隱光內弼星君",
        "辰": "北斗第八洞明外輔星君",
        "巳": "北斗第九隱光內弼星君",
        "午": "北斗第八洞明外輔星君",
        "未": "北斗第九隱光內弼星君",
        "申": "北斗第八洞明外輔星君",
        "酉": "北斗第九隱光內弼星君",
        "戌": "北斗第八洞明外輔星君",
        "亥": "北斗第九隱光內弼星君"
    },
    "女": {
        "子": "北斗第九隱光內弼星君" ,
        "丑": "北斗第八洞明外輔星君",
        "寅": "北斗第九隱光內弼星君",
        "卯": "北斗第八洞明外輔星君",
        "辰": "北斗第九隱光內弼星君",
        "巳": "北斗第八洞明外輔星君",
        "午": "北斗第九隱光內弼星君",
        "未": "北斗第八洞明外輔星君",
        "申": "北斗第九隱光內弼星君",
        "酉": "北斗第八洞明外輔星君",
        "戌": "北斗第九隱光內弼星君",
        "亥": "北斗第八洞明外輔星君"
    }
}

# 根據輸入的干支和性別輸出對應的太歲神、本命星君、元辰星君、本命星官和元辰星官
def find_taisui_and_stars(birth_gan_yi, gender):
    if birth_gan_yi not in GANYI:
        return "输入的干支不正確，請輸入正確的干支組合（如甲子、乙丑等）。"
    if gender not in ["男", "女"]:
        return "性別輸入錯誤，請輸入'男'或'女'。"

    # 取得出生年份對應的地支
    birth_zhi = birth_gan_yi[-1]

    # 獲取對應的太歲
    birth_taisui = TAISUI[GANYI.index(birth_gan_yi)]

    # 獲取對應的本命星君
    birth_star = BENMING_STAR[birth_zhi]

    # 獲取對應的元辰星君
    birth_yuanchen_star = YUANCHEN_STAR[gender][birth_zhi]

    # 獲取對應的本命星官
    birth_star_official = BENMING_STAR_OFFICIAL[birth_gan_yi]

    # 獲取對應ˇ的元辰星官
    birth_yuanchen_official = YUANCHEN_STAR_OFFICIAL[gender][birth_gan_yi]

    return birth_taisui, birth_star, birth_yuanchen_star, birth_star_official, birth_yuanchen_official

# 主程序
if __name__ == "__main__":
    birth_gan_yi = input("請輸入您的出生干支（如甲子、乙丑等）：")
    gender = input("請輸入您的性別（男/女）：")
    result = find_taisui_and_stars(birth_gan_yi, gender)

    if isinstance(result, str):  # 如果返回的是錯误信息
        print(result)
    else:
        birth_taisui, birth_star, birth_yuanchen_star, birth_star_official, birth_yuanchen_official = result
        print(f"出生年：{birth_gan_yi}年")
        print(f"本命日：{birth_gan_yi}日")
        print(f"太歲：{birth_taisui}")
        print(f"本命星君：{birth_star}")
        print(f"元辰星君：{birth_yuanchen_star}")
        print(f"本命星官：{birth_gan_yi}本命星官{birth_star_official['name']}，從官{birth_star_official['officials']}人")
        print(f"元辰星官：{birth_yuanchen_official['year']}元辰星官{birth_yuanchen_official['name']}，從官{birth_yuanchen_official['officials']}人")