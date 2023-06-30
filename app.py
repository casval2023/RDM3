import streamlit as st

# 問題と解答のデータ
data = {
    "問1": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。日本では糖尿病、高血圧、高脂血症、心臓病、脳卒中、がんなどは主に中年以降の成人が患うものとされ、昭和30年代から「成人病」と呼び、全死因の中で上位を占める疾患として広く知られてきました。平成8年には食習慣・運動習慣・休養・喫煙・飲酒等の生活習慣がその発症や進行に関与する疾患群と定義し、成人病から（　A　）病に改めました。",
        "options": ["①生活習慣病", "②内臓疾患病", "③中年病"],
        "answers": ["①生活習慣病"]
    },
    "問2":{
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。日本人の3分の２近くが生活習慣病でなくなっていますが、（　A　）を防止することで予防できる病気です。早期発見という（「　B　」）よりも、早期予防である（「　C　」）に、より重点を置く必要があります。",
        "options": ["①飲みすぎ", "②肥満", "③一次予防", "④二次予防", "⑤三次予防", "⑥ダイエット"],
        "answers": ["②肥満", "④二次予防", "③一次予防"]
    },
    "問3": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。食べ物に含まれる糖質は腸から吸収されて（　A　）糖という活動エネルギーになります。（　A　）は血液の中に溶け込んで、身体中の細胞に運ばれます。血液中の血糖値が上昇すると、すい臓からそれを抑える（　B　）というホルモンが分泌されます。脂肪組織が多いと（　B　）の作用が悪くなり血糖値が高くなっている状態を（　C　）病といいます。",
        "options": ["①ブドウ", "②オリゴ", "③レプチン", "④インスリン", "⑤糖尿", "⑥高血圧"],
        "answers": ["①ブドウ", "④インスリン", "⑤糖尿"]
    },
    "問4": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。糖尿病は「小児糖尿病」と呼ばれる「1型糖尿病」とインスリンの働きが次第に悪くなって起こる「2型糖尿病」、「その他糖尿病」の3種にわかれます。日本人の場合、（　A　）％以上が「2型糖尿病」です。",
        "options": ["①75", "②85", "③95"],
        "answers": ["③95"]
    },
    "問5": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。血圧は年齢が上がるにつれ、（　A　）なります。これは体内の脂肪、なかでも（　B　）が増えるため、増えた脂肪組織に送られる血液量も増え、さらに、（　B　）からは血圧を上昇させるアンジオテンシノーゲンが分泌されますので、（　B　）が多ければ多いほど（　C　）は上がります。",
        "options": ["①高く", "②低く", "③皮下脂肪", "④内臓脂肪", "⑤血糖値", "⑥血圧"],
        "answers": ["①高く", "④内臓脂肪", "⑥血圧"]
    },
    "問6": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。高血圧は（　A　）の摂りすぎ、ストレス、過労など様々な要因が関係していますので、太ってない人にも起こります。しかし（　B　）は高血圧と密接に関係していて、（　C　）を減らしたことで血圧が正常になったという人は少なくありません。
",
        "options": ["①糖分", "②塩分", "③肥満", "④運動", "⑤体脂肪", "⑥体重"],
        "answers": ["②塩分", "③肥満", "⑥体重"]
    },
    "問7": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。高脂血症は血液中の（　A　）成分が、通常より多くなる状態です。動脈硬化の原因となるLDLコレステロールの処理能力が低下し、（　B　）濃度が高くなります。飲みすぎや食べすぎで余ったエネルギーは、体内ですべて（　C　）に変わってしまいます。",
        "options": ["①脂肪", "②たんぱく", "③脂質", "④コレステロール", "⑤体脂肪", "⑥中性脂肪"],
        "answers": ["①脂肪", "④コレステロール", "⑥中性脂肪"]
    },
    "問8": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。高脂血症の治療は基本的には、活性酸素を増やし、（　A　）（善玉コレステロール）を低下させるタバコを止め、肉などの動物性脂肪の摂りすぎを防ぐことです。",
        "options": ["①LDLコレステロール", "②HDLコレステロール", "③トリグリセライト"],
        "answers": ["②HDLコレステロール"]
    },
    "問9": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。動脈硬化の危険因子のうち、糖尿病、高血圧、高脂血症、高インスリン血症、高尿酸値症、そして運動不足は太った人によく見られ、動脈硬化の予防にはまず、（　A　）を減らすことが重要なポイントとなってきます。",
        "options": ["①体脂肪", "②体重", "③水分"],
        "answers": ["①体脂肪"]
    },
    "問10": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。脳卒中は血液中の脂質が（　A　）を硬化させたときにおこる病気です。血圧が高くなって（　B　）が破れ脳出血をを起こしたり、（　B　）を塞いで脳梗塞を起こします。脳卒中の中では脳出血、脳血栓、脳塞栓が（　C　）と深い関係があります。
",
        "options": ["①脳動脈", "②動脈", "③血管", "④肥満", "⑤内臓脂肪", "⑥皮下脂肪"],
        "answers": ["①脳動脈", "③血管", "④肥満"]
    },
    "問11": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。高尿酸血症は尿酸の産生と排泄のバランスが崩れることによって起こるといわれます。崩れ方で産生過剰型と、排泄低下型に分類され、それらの合併症を一般的に（　A　）といいます。
",
        "options": ["①脂肪肝", "②関節炎", "③通風"],
        "answers": ["③通風"]
    },
    "問12": {
        "question": "A～Cの言葉を下記の語群から選び、文章を完成させましょう。(　A　）は肝臓の中に中性脂肪が溜まりすぎることを言い、自覚症状があまりなく食事や運動による療法で跡形もなく治癒しますが放っておくと慢性的な（　B　）障害を引き起こすことがあり、とくに糖尿病がある
ときには（　C　）から肝臓へ中性脂肪が送られるようになるので要注意です。
",
        "options": ["①脂肪肝", "②胆石", "③肝機能", "④身体", "⑤皮下脂肪", "⑥内臓脂肪"],
        "answers": ["①脂肪肝", "③肝機能", "⑤皮下脂肪"]
    },
    "問13": {
        "question": "Aにあてはまる言葉を下記①～③から１つ選び、文章を完成させましょう。特定のがんはホルモンの影響というほかに脂肪過多な食生活の影響も無視できません。日本では欧米型の食事になり始めた70年代以降から（　A　）がんや前立腺がんが急増しています。女性のがんでは、肥満の人の乳がんの脂肪率が最も高く、肥満でない人の2倍も乳がんになっています。
",
        "options": ["①胃がん", "②食道がん", "③大腸がん"],
        "answers": ["③大腸がん"]
    }
}

def main():
    st.title('レギュラーダイエットマスター第3章復習問題')
    score = 0
    for key, value in data.items():
        st.write(f"### {key}")
        st.write(value["question"])
        answers = st.multiselect("選択肢を選んでください:", value["options"])
        if answers == value["answers"]:
            score += 1
            st.write("正解です！")
        #else:
            #st.write("不正解です。")
            #st.write(f"正解は {value['answers']} です。")
    st.write(f"### スコア: {score}/{len(data)}")
    st.write(f"# 正答率は **{round(score * 100/ len(data))}%** です！")

if __name__ == "__main__":
    main()
