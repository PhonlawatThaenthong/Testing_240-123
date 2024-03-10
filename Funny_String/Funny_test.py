from Funny_String.Funny_string import funnyString
import unittest

class Test_Funny(unittest.TestCase):
    def test_acxz(self):
        input = 'acxz'
        test = funnyString(input)
        self.assertEqual('Funny',test)

    def test_bcxz(self):
        input = 'bcxz'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_ivvkxq(self):
        input = 'ivvkxq'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_extra(self):
        input = '@#&*$'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_ivvkx(self):
        input = 'ivvkx'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_longtext(self):
        input = 'djaddsadssadajdasdasjdhuxyxycxhwnqndbasvcxzdadasdsadcxzgtuysawdsa'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_verylongtext(self):
        input = '''rtuntvyqsyqxqrxsvwryqytlpsxptxysxyuxztv
        zwxzxzsyunpryzsytuxtxrvwzvzuopvwsywryqsvos
        wrvxzrtxtywpuyvnvnotlprskltuxrvprzrvopwysk
        lnqtvxzxrsxpqumuywqyryrxzunovzrytwxrvxqsux
        ywqyzxystmrytzwztuounpxqyvntxyzvxruxqtlsuy
        tzxpxqytxqwzuztyvwruzskrszxpuxtvnstmpxuntl
        mpuovovyzwxpqrxzyvzvzwostvyvnorsvouvquxsyu
        yrvxptxtmtztvowstmqtmstysxpqrxtyuntwzystmq
        xprxuwszuxtyrtvprtwrxruxytwqwxyumopswstlrv
        zvqvxryuwsuzsuvwpvxpqrstwsxuxzsztwzstuwytw
        qtxqtwswytywrystvnqyskmntvwptywxqvoqxuzryz
        xumtxysyquzyuwzvntuvpwqvnrytxsxszvywskruxu
        yswqswzxtltuyqvxtlrzvquounsxzrytyvxrxtmnqx
        zsysklqwowyvqxzyvyqszuyqstwxytmorvorvyqtvw
        qwpwprsyvoqwquowsyuwovqwxpqywyqxpvqwpuxyvq
        wowzsvwzvnowrszumununtxuxumruwxyworzxuwrtv
        zsuwzywxqysvxpuvqxuzswrtwquzwqwqumuowxqxpt
        uvzuworvzxqyvwqwrzwzuoquyzvxqtyrvnqvoumpwq
        stzsyvpqvysystzxzuyruntzwruwpqxpqvounrxuos
        kosxsyzrvzstuvqtwzwxuxstlosytvwsxtuvwxptxr
        wszystxpqwysywopwrtmuoqysvwqwsvxpqtyztywzt
        muntlqsuxzsxytmnptyuosxpxsxtzsuyskmrwztmqv
        ytuvqsxytvzyzvpunqtlskskosuwysytvpuovwpsuw
        suzyswzruvoqyvqswpwxumszuyqtzytuxyzrvzryuo
        wskpuxuxuzxpsyvxyzwrsxsuyzuxqyztwoqxuyzumo
        twovzryswoqyztlqyswoszrwrtuoumtvxrsytmpxrw
        ouwprsxrskowsklpuoswotumouotyuvzywzwyrzxru
        vwyzunumouywrxqsuytvouxyqunuostzuwpqytlmor
        uowxqrvzxuvzwowysxsywxqyzswovqtuwywxuzvzsw
        oqtmpxunsworvnovnvzxpuxytysklpskpuovzrxpsx
        uosvqtvnrtxqstwpxuxuwpwpvysvxyrvprywrzyqrw
        qtyzyuxuotvqtmtuvnovztlnvzyquwstxpquyunowo
        tvpsuortxrzwpwpwqskmorsvosytytxystxpvpqrum
        pqwxquwpuyzuovwzwrysxtzruxswzsvpwxrxtlpxuy
        umptvqyqtyvnrxuvwryvxrumpvouzyzyqtxyqumowy
        zwpsvowywxqumnpvpvpvpuvxskptuystzvzyvywsvn
        uxpxpuouwzxzvopxzyvoqruzytmowxysvntwsvnsxy
        rszskltwpqtuzwruyuxtvpszrxyrtyrzuovqwqxtzy
        tvyzvpuopvyvzxptlmunotxqrswptunvxyzuotvprw
        otzskqxqunqxsvowxzrywxqsxtzstmpxumsuzumuxu
        owrvouovzszwosytvorvpuxtzrzunpwrswowxsyuxt
        zxquowyqtmqwyzuvpsvzsvovxqtmpvyqxyvqrvzwzr
        zvnrwryrsxyruxrxyqtwpquwrvqrxqysvopwszuyuz
        xryrumsxzuotzxprtzyzwzruvywrxstmowqvorskrx
        swosyzysuxpqworyumptzvyvnouvwsytlqytzywpst
        mumntwowqvzyqtuzwxpqvotyvxswovztmpvzuzvywp
        stuxswswsknvzuwopqxtmryumpqtywxqsuwqvqrzvy
        rzrzsklqtmnoqrvxumptmqvnoptvnuysyvpuwqrwsu
        zuwovzrsztyvqvyqwysumquzrxzrtyztuwqxrwosuy
        rxpqvpsunpuwqunuyqtxruortwpqwoswruzyqxztls
        kprxuztyzwpvqyqtlqsvwqwrxsvortywqxqyvzvysu
        moqxtuytxtvwovqsyruwowovortvqyvqrvytystlmp
        xpquvpsvnpryqyzxystxzyrvqtvprtlmowrtzsxskq
        tlrvwqrstvwotzxruyqswxyqsysywquzuvnsyqvopu
        otvorvxzuoqwruxuvqyuvzvnvwptmtlpsuxsxtzxyr
        ysuvnpunsxzrvwoqunvywzvzstlqsknvqumqvqstux
        puxpvpvpqxptwquwytuzvpxtuzruzrwrvnrtyzsxqw
        xyvzxstwxtltmuysuvpwrsyqsumuntyryqskoqswqr
        uyzsuwpworytvwpqytzuxtxtxqwrtwquouwpwotmos
        vyuvyvqryrvxunvnrsuvqxrxrvprtmrwyqvzwyuvnv
        ywqstuxzyrsyuoqryvnryzwswrwouyrztxysxumrsk
        nsxtyvptzuyzrzuyrtmrswoqswstuzruvztysvwszv
        ztwopqskpruzwskrvnqtvyszswyryqtvpuvpvxsuyq
        wqtzvotzyrzsxqsytlryzwstlmpuwqumpvqxtuytmq
        txzvwqtzuxpxumuzvwyrzuyuxpuosvwqwyzsknrvqu
        xqtvztvquwxqvystuvzystwqxzruzvpwzrztyzxpru
        ovqunswysuxpwxyruzxpswprsvxuwsxprsvntzxunr
        tzvxtmsxrzytuvoqtuzskqywqvovouworwxruoqrwy
        tyvysxuxtvnqtyrtwryuyzyuorszwrszyvxryumoum
        qyuwxqwprszxtxswzskntlqxruwrwptlskmtzsyrzv
        wzrwpruoskqysvxpwqwztxzsvotlquxszxytwsuory
        tuvowosxzyzwpstxzunrtysuvnsvpxywoqyrswzxtw
        svquoumqstunqrxqtwquzuzvytmsyvnotyuwyvqtxs
        tztmqyzxuztmnorysklqytuxruorwxqwquyzvzxrsk
        pqyrytmuvptvwyuoskqsxuowzyuztxtvzwxzszyrvq
        yuorstwqszryrunpwrwyskouvxtvnvpxuxzvyuvzwx
        uvyzxytzxuzumrxtzuxuytyskrstwzytwzuyvxyuyt
        loqvpwxprwrxzvqswpuyvounqyqtwzrtzysvovyqtm
        swywrxpqrtlskmskopruwpskmouyzrtzwzszrxpqxq
        xqyuorvououmryzxzxyvorwqrwzrwysvnsytlnqvow
        svpuyrxtuysyztvztzuxptlqyrxzwsuounpqwptzwx
        uxquostvpxsxswzxrwqxuxswsuxqytlnuouzysysyv
        ywqvyvxpquxryszyuotwoskpxprwqxqyqvzwpuwows
        xqrunstxqyryuouzxuyzxuztyvxqsuwqyvwqxyzumt
        wzvwpvywqvqsuvzwpvzyvyvyzyvwrtltxumpxzvqwo
        unoqszsxqrzyumntlrzsxuwsxytuorzwxptvoqxsvp
        vpuorvywzsxtvwszyzyzvwovystuxuowoqvxskovpx
        zrztzysyzyskskqyqywryztwyvxstlpszvnrvqrvpv
        ytzrvqxsuzunvpqruwouystwxtmnuyrtlpqtltmnru
        mpqyuxyvnrstzyuzxumuyqtxzxuvyruwxuvzuwpuzs
        xunvowyszuzyzsvyrwxysuysxpwzvzyqwowszyztzt
        ztxpxzvwyzxsztytumuvnskrzszyuystuvwxzvwzuw
        oryunuxqywzsknszwoqyzwopstxuxptvxzuvwovnop
        vwzwpuwosuwzxtwqwqvwpwzvoruzxuzsvnoptwxptv
        xrxsvywptlqwzwotmnvzsuxpsywzuzvoqruyuyvory
        uoqtvnqruvytlqtunuoqvoryvprwsxunptuxtwsyvp
        svxsvnqyzryvpqyqvyunotwxqwzxuovqyqrtmqsknv
        xpxzswsuwrxtytumswrwoswxsvztvpuxswswpxstxu
        yqxszvnqyrxtmpvxpwpuvzrwpwsvovqvovswpwrzvu
        pwpxvpmtxryqnvzsxqyuxtsxpwswsxupvtzvsxwsow
        rwsmutytxrwuswszxpxvnksqmtrqyqvouxzwqxwton
        uyvqyqpvyrzyqnvsxvspvyswtxutpnuxswrpvyrovq
        ounutqltyvurqnvtqouyrovyuyurqovzuzwyspxusz
        vnmtowzwqltpwyvsxrxvtpxwtponvszuxzurovzwpw
        vqwqwtxzwusowupwzwvponvowvuzxvtpxuxtspowzy
        qowzsnkszwyqxunuyrowuzwvzxwvutsyuyzszrksnv
        umutytzsxzywvzxpxtztztzyzswowqyzvzwpxsyusy
        xwryvszyzuzsywovnuxszupwuzvuxwuryvuxzxtqyu
        muxzuyztsrnvyxuyqpmurnmtltqpltryunmtxwtsyu
        owurqpvnuzusxqvrztyvpvrqvrnvzspltsxvywtzyr
        wyqyqksksyzysyztzrzxpvoksxvqowouxutsyvowvz
        yzyzswvtxszwyvroupvpvsxqovtpxwzroutyxswuxs
        zrltnmuyzrqxszsqonuowqvzxpmuxtltrwvyzyvyvy
        zvpwzvusqvqwyvpwvzwtmuzyxqwvyqwusqxvytzuxz
        yuxzuouyryqxtsnurqxswowupwzvqyqxqwrpxpksow
        touyzsyrxuqpxvyvqwyvysysyzuounltyqxuswsxux
        qwrxzwsxsxpvtsouqxuxwztpwqpnuouswzxryqltpx
        uztzvtzysyutxryupvswovqnltysnvsywrzwrqwrov
        yxzxzyrmuouovrouyqxqxqpxrzszwztrzyuomkspwu
        rpoksmksltrqpxrwywsmtqyvovsyztrzwtqyqnuovy
        upwsqvzxrwrpxwpvqoltyuyxvyuzwtyzwtsrksytyu
        xuztxrmuzuxztyxzyvuxwzvuyvzxuxpvnvtxvuoksy
        wrwpnuryrzsqwtsrouyqvryzszxwzvtxtzuyzwouxs
        qksouywvtpvumtyryqpksrxzvzyuqwqxwrourxutyq
        lksyronmtzuxzyqmtztsxtqvywuytonvysmtyvzuzu
        qwtqxrqnutsqmuouqvswtxzwsryqowyxpvsnvusytr
        nuzxtspwzyzxsowovutyrouswtyxzsxuqltovszxtz
        wqwpxvsyqksourpwrzwvzrysztmksltpwrwurxqltn
        kszwsxtxzsrpwqxwuyqmuomuyrxvyzsrwzsrouyzyu
        yrwtrytqnvtxuxsyvytywrqourxwrowuovovqwyqks
        zutqovutyzrxsmtxvztrnuxztnvsrpxswuxvsrpwsp
        xzuryxwpxusywsnuqvourpxzytzrzwpvzurzxqwtsy
        zvutsyvqxwuqvtzvtqxuqvrnkszywqwvsoupxuyuzr
        ywvzumuxpxuztqwvzxtqmtyutxqvpmuqwupmltswzy
        rltysqxszryztovztqwqyusxvpvupvtqyrywszsyvt
        qnvrkswzurpksqpowtzvzswvsytzvurzutswsqowsr
        mtryuzrzyuztpvytxsnksrmuxsyxtzryuowrwswzyr
        nvyrqouysryzxutsqwyvnvuywzvqywrmtrpvrxrxqv
        usrnvnuxvryrqvyvuyvsomtowpwuouqwtrwqxtxtxu
        ztyqpwvtyrowpwuszyurqwsqoksqyrytnumusqysrw
        pvusyumtltxwtsxzvyxwqxszytrnvrwrzurzutxpvz
        utywuqwtpxqpvpvpxupxutsqvqmuqvnksqltszvzwy
        vnuqowvrzxsnupnvusyryxztxsxuspltmtpwvnvzvu
        yqvuxurwqouzxvrovtoupovqysnvuzuqwysysqyxws
        qyurxztowvtsrqwvrltqksxsztrwomltrpvtqvryzx
        tsyxzyqyrpnvspvuqpxpmltsytyvrqvyqvtrovowow
        urysqvowvtxtyutxqomusyvzvyqxqwytrovsxrwqwv
        sqltqyqvpwzytzuxrpksltzxqyzurwsowqpwtrourx
        tqyunuqwupnuspvqpxryusowrxqwutzytrzxrzuqmu
        sywqyvqvytzsrzvowuzuswrqwupvysyunvtponvqmt
        pmuxvrqonmtqlkszrzryvzrqvqwusqxwytqpmuyrmt
        xqpowuzvnkswswsxutspwyvzuzvpmtzvowsxvytovq
        pxwzutqyzvqwowtnmumtspwyztyqltyswvuonvyvzt
        pmuyrowqpxusyzysowsxrksrovqwomtsxrwyvurzwz
        yztrpxztouzxsmuryrxzuyuzswpovsyqxrqvrwuqpw
        tqyxrxuryxsryrwrnvzrzwzvrqvyxqyvpmtqxvovsz
        vspvuzywqmtqywouqxztxuysxwowsrwpnuzrztxupv
        rovtysowzszvouovrwouxumuzusmuxpmtsztxsqxwy
        rzxwovsxqnuqxqksztowrpvtouzyxvnutpwsrqxton
        umltpxzvyvpoupvzyvtyztxqwqvouzrytryxrzspvt
        xuyurwzutqpwtlkszsryxsnvswtnvsyxwomtyzurqo
        vyzxpovzxzwuoupxpxunvswyvyzvztsyutpksxvupv
        pvpvpnmuqxwywovspwzywomuqyxtqyzyzuovpmurxv
        yrwvuxrnvytqyqvtpmuyuxpltxrxwpvszwsxurztxs
        yrwzwvouzyupwuqxwqpmurqpvpxtsyxtytysovsrom
        ksqwpwpwzrxtrouspvtowonuyuqpxtswuqyzvnltzv
        onvutmtqvtouxuyzytqwrqyzrwyrpvryxvsyvpwpwu
        xuxpwtsqxtrnvtqvsouxspxrzvoupksplksytyxupx
        zvnvonvrowsnuxpmtqowszvzuxwywutqvowszyqxwy
        sxsywowzvuxzvrqxwouromltyqpwuztsounuqyxuov
        tyusqxrwyuomunuzywvurxzrywzwyzvuytouomutow
        souplkswoksrxsrpwuowrxpmtysrxvtmuoutrwrzso
        wsyqltzyqowsyrzvowtomuzyuxqowtzyqxuzyusxsr
        wzyxvyspxzuxuxupkswouyrzvrzyxutyztqyuzsmux
        wpwsqvyqovurzwsyzuswuspwvoupvtysywusoksksl
        tqnupvzyzvtyxsqvutyvqmtzwrmksyusztxsxpxsou
        ytpnmtyxszxusqltnumtzwytzytqpxvswqwvsyqoum
        trwpowysywqpxtsyzswrxtpxwvutxswvtysoltsxux
        wzwtqvutszvrzysxsoksouxrnuovqpxqpwurwztnur
        yuzxztsysyvqpvysztsqwpmuovqnvrytqxvzyuqouz
        wzrwqwvyqxzvrowuzvutpxqxwoumuqwqwzuqwtrwsz
        uxqvupxvsyqxwyzwuszvtrwuxzrowyxwurmuxuxtnu
        numuzsrwonvzwvszwowqvyxupwqvpxqywyqpxwqvow
        uyswouqwqovysrpwpwqwvtqyvrovromtyxwtsqyuzs
        qyvyzxqvywowqlksyszxqnmtxrxvytyrzxsnuouqvz
        rltxvqyutltxzwsqwsyuxurkswyvzsxsxtyrnvqwpv
        utnvzwuyzuqysyxtmuxzyrzuxqovqxwytpwvtnmksy
        qnvtsyrwytywswtqxtqwtywutszwtzszxuxswtsrqp
        xvpwvuszuswuyrxvqvzvrltswspomuyxwqwtyxurxr
        wtrpvtrytxuzswuxrpxqmtsyzwtnuytxrqpxsytsmt
        qmtswovtztmtxtpxvryuysxuqvuovsronvyvtsowzv
        zvyzxrqpxwzyvovoupmltnuxpmtsnvtxupxzsrkszu
        rwvytzuzwqxtyqxpxztyusltqxurxvzyxtnvyqxpnu
        outzwztyrmtsyxzyqwyxusqxvrxwtyrzvonuzxryry
        qwyumuqpxsrxzxvtqnlksywpovrzrpvrxutlksrplt
        onvnvyupwytxtrzxvrwsovsqyrwyswvpouzvzwvrxt
        xutyszyrpnuyszxzxwzvtzxuyxsyxtpxspltyqyrwv
        sxrqxqysqyvtngfd'''
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_have_x_y(self):
        input = 'x*y = 6'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_number(self):
        input = '23414'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    
    