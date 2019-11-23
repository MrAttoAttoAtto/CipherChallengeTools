
import itertools
import re
from utils import EXCEPT_LOWER_ALPHABET

LIKELY_WORDS = ["the", "and", "tha"]

def decrypt_rows(ciphertext, order):
    kwlen = len(order)
    rows = [ciphertext[i:i+kwlen] for i in range(0, len(ciphertext), kwlen)]
    result = ""
    for row in rows:
        for i in order:
            try:
                result += row[i]
            except IndexError:
                break
    return result

def rows_from_columns(ciphertext, kwlen):
    # Order has length of rows
    std_col_len = int(len(ciphertext)/kwlen)
    extra_cols = len(ciphertext) % kwlen
    col_lens = [std_col_len + 1 if i < extra_cols else std_col_len for i in range(kwlen)]

    cols = []
    prev_index = 0
    for i in col_lens:
        cols.append(ciphertext[prev_index: prev_index+i])
        prev_index = prev_index + i
    rows = [''.join(x) for x in itertools.zip_longest(*cols, fillvalue='')]
    return rows


def try_find_anagram(ciphertext, kwlen):
    rows = [ciphertext[i:i+kwlen] for i in range(0, len(ciphertext), kwlen)]
    attempt_words = []
    for attempt_word in LIKELY_WORDS:
        for i in range(len(attempt_word)-kwlen+1):
            attempt_words.append(attempt_word[i:i+kwlen])
    print(attempt_words)
    count = 0
    orders = []
    for row in rows:
        for word in attempt_words:
            for letter in row:
                if letter not in word:
                    break
            else:
                count += 1
                recommended_orders = [[]]
                for letter in row:
                    for i_record in range(len(recommended_orders)):
                        first = False
                        for n, pos in enumerate([i for i,x in enumerate(word) if x==letter]):
                            if pos not in recommended_orders[i_record]:
                                if first:
                                    recommended_orders[i_record].append(pos)
                                    first = False
                                else:
                                    recommended_orders.append(recommended_orders[i_record][:]+[pos])
                orders.extend([tuple(x) for x in recommended_orders if len(x) == kwlen])
    order_counts = {}
    for recommended_order in orders:
        if recommended_order in order_counts:
            order_counts[recommended_order] += 1
        else:
            order_counts[recommended_order] = 1
    print(order_counts)
    return (sorted(order_counts.items(), key=lambda kv: kv[1])[-1]) if len(order_counts) else ((), 0)

def brute_force(text, likely_words=LIKELY_WORDS, kwlens=None, columnar=True):
    """Not attractive, but effective and fast enough"""
    ciphertext = re.sub(EXCEPT_LOWER_ALPHABET, "", text.lower())
    possibles = []
    try:
        if kwlens is None:
            kwlens = range(2, 12)
        elif type(kwlens) == type(1): # If it's an int, make it a list with only itself in it
            kwlens = [kwlens]

        for kwlen in kwlens:
            print(kwlen)
            if columnar:
                colsolved = ''.join(rows_from_columns(ciphertext, kwlen))
            else:
                colsolved = ciphertext
            for l in itertools.permutations(range(kwlen)):
                trans = decrypt_rows(colsolved, l)
                for w in likely_words:
                    if w not in trans: 
                        break
                else:
                    print(trans[:30],l, len(possibles))
                    possibles.append(trans)
    except KeyboardInterrupt:
        pass
    choice = input("Full Text? ")
    try:
        n = int(choice)
        print(possibles[n])
    except (ValueError, IndexError):
        print("Bye!")


if __name__ == "__main__":
    ciphertext = """kdIgb oimce idkot seeii huotn pteho mmswi heeoa taoue taebw niInc fnkll flnho unwtd mamtg maera ieanw ronko tsstn kemta rahdn heIpo nsiac oiaeh lntai lbhsh oesoh lhtka rttts aehhI vldTh tunau ehshe noceI aireh rvsrw thett tuaea eseid eeeem topeh eohfB eoodn pafto enect dvasi bpsti xtrrp hfost wiekh Idnpb chrls fidoa atwit urgsd nedao hhgsh iaoeo ricot sgnrg ktedr hanoh tsmao Tehtf morsi ngkhe phtat bmrtt ooeap ctdJt marcs eedad bnier nrhhm rkshg eodBf emahf oeocr ctdfc tvMsy rlneu ooklu nobks nnhhe snosd naenu ueknh noydd Isiwl hseei uibby hatdo ybaeo pAntT sftek atpwa neuoo plttt abtte etioh mrhuh cfsto aeaip otiVc olsgI asstt atyla oodsu ebple rlecs acles hsham ierth ocoen etatn eluhn ehtnw auaih eerje hsaea kshtw cslrh eohin euteI ldelo trele aiutm mesrr oleet setwi naerw aouhe aiawy dycsu tltgu eecni atdte whiks ldlre uoaeg iivsn noleI atorn uscen heuaa tcplr dwato Imath eengb rafal bhade phdgh tgees eniat chdsa dmept oiiku ceuii ereyd ttsun cetTs oieeg naetn sligi tepod legtI oiors rhaaf hgpuc doite tdplh nlell irhpo Scrie eerTo wahto roesi efedu eoanb ahwae Vnnkt oueaS cober seeht rseha rtsda ntmia ahute ebhmI lbnot eyatt ndnht uHoht leade osytl ylwut uoIoa cwmll eints eIoeu retlu ekycb Iuime fnhmi orehv piafe ostto rnhoi lsnne alacn fndof eIhhi cttrh hhltf teipd rTnes ethtp bwenr rpksr mmein tiioa loamr achti deeuw lanse pohhi lidtk achce ynaoh oswum tlond eelaa dmiLd hhrii rhhue tettv eycet aceeo syIhr tcdan orcuo iwvlt wtror Ibdbt ebgal iulrt bduns nswva talsn gfois dytvd tadlk lniwh etcsi kasle yrtda inmen eeacd nluIa hotga ityet erbyt crebc hsead nuIop nolwy daoek iceuw iauan otdaa efood ddhnh octle itehd rfbls adfeo cemla kMkeh Aaiai tmhet udren tiate tuacy adsso eHlai inald oahhA tluwe errre iysta aihko lhymh lelos strmi rnadt asbde dpwdn ennet ttuol wlhni vtoew tidtn ceoeo cfhno rtorh errdt oepmc ceacl heeil eeagn wydnm heaew dnece hngpe tietw wumnp oanee ihitt gsalt hgrhc evett anaaa rtrnl sdenc uagcc dktdo uloyt aucth otnse eaard tdvdr siafn smuey hceha asnke oeett acitn ktnfd nidto dvdee eaone fifim elahr ohnao iweii aatgd sldeI iweuo sncle etrea eaaea oarrt csdal nweet lehwr xeaue eefno ggatt idctt kinet htuss hnctt netot eoanc wrhts rutee ooanh oeehe dlnny tdwed feapw cpdet hnmab ngtyr atnbc anmpl feiet hhdtn obeio asmmn uotio rapre yider rmtbh anlhf timtl klhHa rnobs motfc eefna actfb feerc ysetr ktiAt bwtsf fawod ewyed nyvmm teela idnhn eunae Utnot vtnic hlwpa laato Ilrot stsdk aurrh ianre oroef sepho loyko ltkei rytoi mtoth hIgei rtboi tttre oehde n"""
    brute_force(ciphertext, LIKELY_WORDS)
    
