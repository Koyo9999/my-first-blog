from django import forms

INTEGER_CHOICES= [tuple([x,x]) for x in range(0,100)]
SIGN_CHOICES= [("星座は？","星座は？"),("おひつじ座","おひつじ座"),
                ("おうし座","おうし座"),("ふたご座","ふたご座"),
                ("かに座","かに座"),("しし座","しし座"),
                ("おとめ座","おとめ座"),("てんびん座","てんびん座"),
                ("さそり座","さそり座"),("いて座","いて座"),
                ("やぎ座","やぎ座"),("みずがめ座","みずがめ座"),
                ("うお座","うお座")]
class InputForm(forms.Form):
    age= forms.IntegerField(widget=forms.Select(choices=INTEGER_CHOICES))
    sign= forms.CharField(widget=forms.Select(choices=SIGN_CHOICES))
