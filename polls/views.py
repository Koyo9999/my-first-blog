from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from .forms import InputForm
import datetime

def index(request):
    form = InputForm()
    return render(request, 'polls/index.html', {'form' : form})

def result(request):
    age = request.GET.get('age')
    sign = request.GET.get('sign')
#    param = {
#    'age' : age,
#    'sign' : sign,
#    }

    #変数を設定
    num1 = int(age.replace(' ',''))
    num2 = 0 if sign == "星座は？" else 1 if sign == "おひつじ座" else 2 if sign == "おうし座" else 3 if sign == "ふたご座" else 4 if sign == "かに座" else 5 if sign == "しし座" else 6 if sign == "おとめ座" else 7 if sign == "てんびん座" else 8 if sign == "さそり座" else 9 if sign == "いて座" else 10 if sign == "やぎ座" else 11 if sign == "みずがめ座" else 12 if sign == "うお座" else 0
    num3 = datetime.datetime.now().day * 10
    num4 = num1 + num2 + num3

    #num4をもとに占う
    if num4 % 9 == 0:
        fate = "<p><strong>他人にも自分にも厳しいけどいざという時には誰よりも優しいあなた。<br>あなたの本来持っている優しさが周囲の人にも伝わるような一日となるでしょう。<br>ラッキーアイテムは『アマギフ』。<br>アマギフをもらった人はもらっていない人に比べて幸福度が５０％高いことが、近年の行動心理学の研究で実証されています。</strong></p>"
    elif num4 % 8 == 0:
        fate = "<p><strong>一見ガンコに見えて実は柔軟な考えをもつあなた。<br>今日はとてもHAPPYな一日となるでしょう。<br>ラッキーアイテムは『傘』。<br>行動心理学的に人は雨が降ると傘を差しがち。なぜなら濡れたくないから。</strong></p>"
    elif num4 % 7 == 0:
        fate = "<p><strong>いつも儚げな雰囲気をまとっているけどその実芯の強いあなた。<br>今日の運勢は可もなく不可もなく。<br>ラッキーアイテムは『現金(CASH)』。<br>あなたは今が人生の分かれ道。行動心理学的に見て、お金はあればあるほど心強いわ。</strong></p>"
    elif num4 % 6 == 0:
        fate = "<p><strong>大きな才能を持っているけれどまだそれを活かしきれていないあなた。<br>今日の一日は絶好調。<br>ラッキーアイテムは『頼れるメンター』。<br>あなたが絶大な信頼を寄せるメンターが、行動心理学的にあなたを高みへ導いてくれるでしょう。</strong></p>"
    elif num4 % 5 == 0:
        fate = "<p><strong>内向的なようでいて本質的には外交的なあなた。<br>今日はやや災難な一日となるでしょう。<br>ラッキーアイテムは『腕力』。<br>本質的に外交的なあなたは突然奇声を上げて周囲の人に取り押さえられることでしょう。ですが行動心理学に見て、腕力があればそれらを退けることができます。</strong></p>"
    elif num4 % 4 == 0:
        fate = "<p><strong>いい加減なように見えていつも本当の正義を探しているあなた。<br>今日、あなたの人生は変わるでしょう。<br>ラッキーアイテムは『拳銃』。<br>行動心理学的な見解によるところ、これさえあればあなたは、あなたの信じる正義を実行することができるでしょう。</strong></p>"
    elif num4 % 3 == 0:
        fate = "<p><strong>倹約家に見えて実は浪費家の傾向もあるあなた。<br>今日あなたは、あなたがずっと欲しかったものに出会うでしょう。<br>ラッキーアイテムは『信用』。<br>行動心理学的に、人は信用のおける人物への融資に積極的です。逆に信用が足りなければ融資を受けることは難しいでしょう。</strong></p>"
    elif num4 % 2 == 0:
        fate = "<p><strong>平和主義に見えて時おり攻撃的になるあなた。<br>今日の運勢は強いて言うならば中吉でしょう。<br>ラッキーアイテムは『敏腕弁護士』。<br>友人と些細なことから口論となったあなたは心の奥深くにある暴力衝動により、友人へ怪我を負わせることが行動心理学的に予測できます。敏腕弁護士がいれば裁判沙汰は回避できるかもしれません。</strong></p>"
    else:
        fate = "<p><strong>アウトドア派に見えて実際はひきこもりなあなた。<br>今日の運勢は小吉です。<br>ラッキーアイテムは『靴』。<br>靴を持っている人は持っていない人に比べて行動範囲が５０％広がることが、近年の行動心理学研究により明らかとなっています。</strong></p>"
    
    param = {
    'age' : age,
    'sign' : sign,
    'fate' : fate,
    }


    return render(request, 'polls/result.html',param)