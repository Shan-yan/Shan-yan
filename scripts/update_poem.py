from __future__ import annotations

from datetime import date
from pathlib import Path


START_MARKER = "<!-- POEM-START -->"
END_MARKER = "<!-- POEM-END -->"
README_PATH = Path(__file__).resolve().parents[1] / "README.md"


POEMS = [
    {
        "title": "题西林壁",
        "author": "苏轼",
        "content": ["横看成岭侧成峰，远近高低各不同。", "不识庐山真面目，只缘身在此山中。"],
    },
    {
        "title": "饮湖上初晴后雨",
        "author": "苏轼",
        "content": ["水光潋滟晴方好，山色空蒙雨亦奇。", "欲把西湖比西子，淡妆浓抹总相宜。"],
    },
    {
        "title": "六月二十七日望湖楼醉书",
        "author": "苏轼",
        "content": ["黑云翻墨未遮山，白雨跳珠乱入船。", "卷地风来忽吹散，望湖楼下水如天。"],
    },
    {
        "title": "惠崇春江晚景",
        "author": "苏轼",
        "content": ["竹外桃花三两枝，春江水暖鸭先知。", "蒌蒿满地芦芽短，正是河豚欲上时。"],
    },
    {
        "title": "赠刘景文",
        "author": "苏轼",
        "content": ["荷尽已无擎雨盖，菊残犹有傲霜枝。", "一年好景君须记，最是橙黄橘绿时。"],
    },
    {
        "title": "和子由渑池怀旧",
        "author": "苏轼",
        "content": ["人生到处知何似，应似飞鸿踏雪泥。", "泥上偶然留指爪，鸿飞那复计东西。"],
    },
    {
        "title": "春宵",
        "author": "苏轼",
        "content": ["春宵一刻值千金，花有清香月有阴。", "歌管楼台声细细，秋千院落夜沉沉。"],
    },
    {
        "title": "花影",
        "author": "苏轼",
        "content": ["重重叠叠上瑶台，几度呼童扫不开。", "刚被太阳收拾去，却教明月送将来。"],
    },
    {
        "title": "海棠",
        "author": "苏轼",
        "content": ["东风袅袅泛崇光，香雾空蒙月转廊。", "只恐夜深花睡去，故烧高烛照红妆。"],
    },
    {
        "title": "望江南·超然台作",
        "author": "苏轼",
        "content": ["春未老，风细柳斜斜。", "试上超然台上看，半壕春水一城花。烟雨暗千家。"],
    },
    {
        "title": "南乡子·送述古",
        "author": "苏轼",
        "content": ["回首乱山横，不见居人只见城。", "谁似临平山上塔，亭亭。迎客西来送客行。"],
    },
    {
        "title": "虞美人·春花秋月何时了",
        "author": "李煜",
        "content": ["春花秋月何时了，往事知多少。", "小楼昨夜又东风，故国不堪回首月明中。"],
    },
    {
        "title": "相见欢·无言独上西楼",
        "author": "李煜",
        "content": ["无言独上西楼，月如钩。", "寂寞梧桐深院锁清秋。"],
    },
    {
        "title": "浪淘沙令·帘外雨潺潺",
        "author": "李煜",
        "content": ["帘外雨潺潺，春意阑珊。", "罗衾不耐五更寒。"],
    },
    {
        "title": "乌夜啼·昨夜风兼雨",
        "author": "李煜",
        "content": ["昨夜风兼雨，帘帏飒飒秋声。", "烛残漏断频欹枕，起坐不能平。"],
    },
    {
        "title": "清平乐·别来春半",
        "author": "李煜",
        "content": ["别来春半，触目柔肠断。", "砌下落梅如雪乱，拂了一身还满。"],
    },
    {
        "title": "长相思·一重山",
        "author": "李煜",
        "content": ["一重山，两重山。", "山远天高烟水寒，相思枫叶丹。"],
    },
    {
        "title": "望江南·闲梦远",
        "author": "李煜",
        "content": ["闲梦远，南国正芳春。", "船上管弦江面渌，满城飞絮辊轻尘。"],
    },
    {
        "title": "破阵子·四十年来家国",
        "author": "李煜",
        "content": ["四十年来家国，三千里地山河。", "凤阁龙楼连霄汉，玉树琼枝作烟萝。"],
    },
    {
        "title": "子夜歌·人生愁恨何能免",
        "author": "李煜",
        "content": ["人生愁恨何能免，销魂独我情何限。", "故国梦重归，觉来双泪垂。"],
    },
    {
        "title": "捣练子令·深院静",
        "author": "李煜",
        "content": ["深院静，小庭空，断续寒砧断续风。", "无奈夜长人不寐，数声和月到帘栊。"],
    },
    {
        "title": "定风波·莫听穿林打叶声",
        "author": "苏轼",
        "content": ["竹杖芒鞋轻胜马，谁怕？", "一蓑烟雨任平生。"],
    },
    {
        "title": "浣溪沙·细雨斜风作晓寒",
        "author": "苏轼",
        "content": ["细雨斜风作晓寒，淡烟疏柳媚晴滩。", "人间有味是清欢。"],
    },
    {
        "title": "临江仙·夜饮东坡醒复醉",
        "author": "苏轼",
        "content": ["长恨此身非我有，何时忘却营营。", "小舟从此逝，江海寄余生。"],
    },
    {
        "title": "定风波·南海归赠王定国侍人寓娘",
        "author": "苏轼",
        "content": ["万里归来颜愈少，微笑。", "此心安处是吾乡。"],
    },
    {
        "title": "水调歌头·明月几时有",
        "author": "苏轼",
        "content": ["人有悲欢离合，月有阴晴圆缺。", "但愿人长久，千里共婵娟。"],
    },
    {
        "title": "念奴娇·赤壁怀古",
        "author": "苏轼",
        "content": ["大江东去，浪淘尽，千古风流人物。", "人生如梦，一尊还酹江月。"],
    },
    {
        "title": "江城子·密州出猎",
        "author": "苏轼",
        "content": ["鬓微霜，又何妨！", "会挽雕弓如满月，西北望，射天狼。"],
    },
    {
        "title": "江城子·乙卯正月二十日夜记梦",
        "author": "苏轼",
        "content": ["十年生死两茫茫，不思量，自难忘。", "料得年年肠断处，明月夜，短松冈。"],
    },
    {
        "title": "卜算子·黄州定慧院寓居作",
        "author": "苏轼",
        "content": ["谁见幽人独往来，缥缈孤鸿影。", "拣尽寒枝不肯栖，寂寞沙洲冷。"],
    },
    {
        "title": "西江月·世事一场大梦",
        "author": "苏轼",
        "content": ["世事一场大梦，人生几度秋凉。", "中秋谁与共孤光，把盏凄然北望。"],
    },
    {
        "title": "满庭芳·蜗角虚名",
        "author": "苏轼",
        "content": ["蜗角虚名，蝇头微利，算来著甚干忙。", "且趁闲身未老，尽放我、些子疏狂。"],
    },
    {
        "title": "和子由渑池怀旧",
        "author": "苏轼",
        "content": ["人生到处知何似，应似飞鸿踏雪泥。", "泥上偶然留指爪，鸿飞那复计东西。"],
    },
    {
        "title": "题西林壁",
        "author": "苏轼",
        "content": ["横看成岭侧成峰，远近高低各不同。", "不识庐山真面目，只缘身在此山中。"],
    },
    {
        "title": "六月二十七日望湖楼醉书",
        "author": "苏轼",
        "content": ["黑云翻墨未遮山，白雨跳珠乱入船。", "卷地风来忽吹散，望湖楼下水如天。"],
    },
    {
        "title": "饮湖上初晴后雨",
        "author": "苏轼",
        "content": ["水光潋滟晴方好，山色空蒙雨亦奇。", "欲把西湖比西子，淡妆浓抹总相宜。"],
    },
    {
        "title": "赠刘景文",
        "author": "苏轼",
        "content": ["荷尽已无擎雨盖，菊残犹有傲霜枝。", "一年好景君须记，最是橙黄橘绿时。"],
    },

    {
        "title": "虞美人·春花秋月何时了",
        "author": "李煜",
        "content": ["雕栏玉砌应犹在，只是朱颜改。", "问君能有几多愁？恰似一江春水向东流。"],
    },
    {
        "title": "相见欢·无言独上西楼",
        "author": "李煜",
        "content": ["无言独上西楼，月如钩。", "剪不断，理还乱，是离愁。"],
    },
    {
        "title": "浪淘沙令·帘外雨潺潺",
        "author": "李煜",
        "content": ["梦里不知身是客，一晌贪欢。", "流水落花春去也，天上人间。"],
    },
    {
        "title": "破阵子·四十年来家国",
        "author": "李煜",
        "content": ["四十年来家国，三千里地山河。", "最是仓皇辞庙日，教坊犹奏别离歌。"],
    },
    {
        "title": "清平乐·别来春半",
        "author": "李煜",
        "content": ["别来春半，触目柔肠断。", "离恨恰如春草，更行更远还生。"],
    },
    {
        "title": "相见欢·林花谢了春红",
        "author": "李煜",
        "content": ["林花谢了春红，太匆匆。", "自是人生长恨水长东。"],
    },
    {
        "title": "子夜歌·人生愁恨何能免",
        "author": "李煜",
        "content": ["人生愁恨何能免，销魂独我情何限。", "故国梦重归，觉来双泪垂。"],
    },
    {
        "title": "望江南·多少恨",
        "author": "李煜",
        "content": ["多少恨，昨夜梦魂中。", "还似旧时游上苑，车如流水马如龙。"],
    },
    {
        "title": "望江南·多少泪",
        "author": "李煜",
        "content": ["多少泪，断脸复横颐。", "心事莫将和泪说，凤笙休向泪时吹。"],
    },
    {
        "title": "捣练子令·深院静",
        "author": "李煜",
        "content": ["深院静，小庭空，断续寒砧断续风。", "无奈夜长人不寐，数声和月到帘栊。"],
    },
    {
        "title": "蝶恋花·遥夜亭皋闲信步",
        "author": "李煜",
        "content": ["一片芳心千万绪，人间没个安排处。", "桃李依依春暗度，谁在秋千，笑里轻轻语。"],
    },
    {
        "title": "乌夜啼·昨夜风兼雨",
        "author": "李煜",
        "content": ["昨夜风兼雨，帘帏飒飒秋声。", "烛残漏断频欹枕，起坐不能平。"],
    },
    {
        "title": "长相思·一重山",
        "author": "李煜",
        "content": ["一重山，两重山。", "山远天高烟水寒，相思枫叶丹。"],
    },
    {
        "title": "浪淘沙·往事只堪哀",
        "author": "李煜",
        "content": ["往事只堪哀，对景难排。", "秋风庭院藓侵阶，一任珠帘闲不卷。"],
    },
    {
        "title": "临江仙·樱桃落尽春归去",
        "author": "李煜",
        "content": ["樱桃落尽春归去，蝶翻金粉双飞。", "小楼吹彻玉笙寒，梦回芳草思依依。"],
    },

    {
        "title": "菩萨蛮·大柏地",
        "author": "毛泽东",
        "content": ["装点此关山，今朝更好看。", "雨后复斜阳，关山阵阵苍。"],
    },
    {
        "title": "忆秦娥·娄山关",
        "author": "毛泽东",
        "content": ["雄关漫道真如铁。", "苍山如海，残阳如血。"],
    },
    {
        "title": "沁园春·长沙",
        "author": "毛泽东",
        "content": ["怅寥廓，问苍茫大地，谁主沉浮？", "到中流击水，浪遏飞舟。"],
    },
    {
        "title": "沁园春·雪",
        "author": "毛泽东",
        "content": ["江山如此多娇，引无数英雄竞折腰。", "数风流人物，还看今朝。"],
    },
    {
        "title": "七律·长征",
        "author": "毛泽东",
        "content": ["红军不怕远征难，万水千山只等闲。", "更喜岷山千里雪，三军过后尽开颜。"],
    },
    {
        "title": "清平乐·六盘山",
        "author": "毛泽东",
        "content": ["不到长城非好汉。", "今日长缨在手，何时缚住苍龙？"],
    },
    {
        "title": "采桑子·重阳",
        "author": "毛泽东",
        "content": ["人生易老天难老，岁岁重阳。", "战地黄花分外香。"],
    },
    {
        "title": "清平乐·会昌",
        "author": "毛泽东",
        "content": ["踏遍青山人未老，风景这边独好。", "会昌城外高峰，颠连直接东溟。"],
    },
    {
        "title": "浪淘沙·北戴河",
        "author": "毛泽东",
        "content": ["萧瑟秋风今又是，换了人间。", "往事越千年，魏武挥鞭。"],
    },
    {
        "title": "水调歌头·重上井冈山",
        "author": "毛泽东",
        "content": ["可上九天揽月。", "世上无难事，只要肯登攀。"],
    },
]


def choose_poem(today: date | None = None) -> dict[str, object]:
    current_day = today or date.today()
    return POEMS[current_day.toordinal() % len(POEMS)]


def build_poem_block(poem: dict[str, object]) -> str:
    title = poem["title"]
    author = poem["author"]
    content = poem["content"]

    if not isinstance(content, list):
        raise TypeError("Poem content must be a list of strings.")

    lines = [
        f"### 《{title}》",
        "",
        f"**{author}**",
        "",
    ]
    lines.extend(f"> {line}" for line in content)
    return "\n".join(lines)


def update_readme() -> None:
    if not README_PATH.exists():
        raise FileNotFoundError(f"README.md not found at: {README_PATH}")

    readme = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        raise ValueError(
            f"Poem markers not found. README.md must contain {START_MARKER} and {END_MARKER}."
        )

    start_index = readme.index(START_MARKER) + len(START_MARKER)
    end_index = readme.index(END_MARKER)

    if start_index > end_index:
        raise ValueError("Poem markers are in the wrong order.")

    poem_block = build_poem_block(choose_poem())
    updated = f"{readme[:start_index]}\n{poem_block}\n{readme[end_index:]}"
    README_PATH.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
