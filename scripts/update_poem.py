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
