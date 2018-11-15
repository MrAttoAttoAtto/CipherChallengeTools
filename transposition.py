
LIKELY_WORDS = ["PLAYFAIR", "EMPERORS"]

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
                recommended_order = []
                for letter in row:
                    recommended_order.append(word.find(letter))
                orders.append(tuple(recommended_order))
    order_counts = {}
    for recommended_order in orders:
        if recommended_order in order_counts:
            order_counts[recommended_order] += 1
        else:
            order_counts[recommended_order] = 1
    print(order_counts)
    return sorted(order_counts.items(), key=lambda kv: kv[1])[-1]
        


ciphertext = """NILIF RTITA GNEHT EDBIL REITA NOFOS UONER MESEI SIRPA NIPIC LAAOG BLFTU LOWOL NIYMG IDUCS SSNOI WSHTI LPFYA IAHIR VAOCE EMSOT EEAHT TTCEH ALISS ACTSL ARGET OYRTF IYTGN TONRU SAINE ROMEM EBFOR HTEDE ELTAG OIISN BSHTO IRYKS NANUD ENSEC ASAYR YNPPA ORHCA OTCUS AHNIN IDDIV AUIRL KSISS NGLLA NIUOG IRETN TNNOI ASUDN DNMRE NIOSE RUIBA ILTYT AOPAD OTPRU ALSSN CECER IYVES REHTY NISAG LPFYA IAOPR NIOST TUOHT ESDNI VIUDI LAFOS ETAHN EVTIL LTNIE LFNEU ECYNA AWHTY YEERA HTERE OTERP ESATN OPTNI FOEIV AWTDN EHSEB OTHTF MELTA AETTS LOTSI NETUB HTHYE VAILE TTAEL TUROH TIHTY JEINU ROFFO CILAI OSHTN OEEHT HRDNA AHAEV MLTSO OTLAT OCRTN LOEFO EVSTN HTSYE TEEHT GADNE IAIDN CSSSU OIIWN HTENO NAHTO REDNA HTRIE ESOIN SRDNA OMIER PMTRO NAYLT HTTYE KAHTE REOCE DRTFO EHEEM ITAGN TFTRE EHLED GEETA HSEVA ERRUT ENOTD HTRIE OHSEM TITSI AHERT OCTDR AHEBT OCSEM HTERE LAYTI EWNOD TOEEN TDEBO HTERE ROEVE TNNKO WOAHW WTSSA IAEWD ENODE LNOTY NKWWO AHAHT BSNEE ERROC EDSAD HTRTE TUNAH WDREH PESSO BITEL SOPAH TETAH RTHTU NIRUO EBITS TNERE TSHTS SIEBI ILEVE OTAEB ENITN ERNYL WERTS TAYGE NIEHT OWDLR FOPID OLCAM AYIDN MAELP SATDE BOBAE ELDOT VEOLE IPIWT HTEHT EHOPL SFHCU DATSI NIIUG HSFDE IRDNE LPFYA IASIR MAONA CFNNU NINAG IDJNE YOROW IKWGN TIIHH NMHWO REAHE TSSIH UCINN GNEEB MNERO FECEF ITTEV AHNIN IHTSS ARGET FYTRO EHNAM GAEME TNTFO EHIER HCATS TDEEM ITAGN ELNAX EDRFR NAOJZ ESOGF CRKAH VODNA NAARD SSEMY TTGAO ERETE MRNOS URISS SAVNI LOMEV NENIT HTABE KLSNA NAHTD REAWE ASAER RLKSI HTTTA EHOWY LUNUD TINAE FDHGI TTOCO TNLOR UORTR DAORE TUWSE TIUSH HCGIH LHEVE ILOVN VLEME TNTNI EHSID UCISS NOTIS AWLCS AEHTR TAWEW UOHDL VAILE TTTEL NOOHO EPIFO FNEUL CNGNI HTRPE NIPIC LANAS SDEWO EDDIC DEFOT LOWOL HTLPE YAIAF SRART ETAYG PPIYL GNRAC FEPLU ERUSS ERTOT EHNUJ OIEMR BMSRE FOEHT ERNIT EUUOS ARNEG STDNA FOCIF REEPS SRDAU DEEHT TMERO OPOTR TNPEH OREEC IDSGN RPIVO IDUGN WSHTI HTNIE ETILL EGECN EWEEN EDOTD RPAPE ERROF HTOFE TROCH IMWGN RATEB EWRNE SUAIS NAHTD OEOTT AMMEN IPBER TUFFO RAERG TASRE GIFIN CICNA TEYEH EWAER LBOTE NERUS MEIXA UMOCM FNISU NOOMA GNRUO NEIME SETYB EHSOM MTVRA LEUOL SSART ATMEG HWHCI WILLI ERREF OTTSA EHALP FYRIA AGIBM TTOEH FFICI LAEWS ERLBA TEEPO SRDAU TEIEH LRDAE REHTS TAWTI UOBDL BETTE RETON OTKAT OEIFF ICMLA NIETU OSHTF METEE NIHWG LIEWE ERIEC EVFAD LUNAL ADUCC ARAET CCNUO OTLAF TLDEH SISUC ISSNO HTURE SSNAI NAUAD TSHOR NURAG AIFON IFAIC SLREW LETFE NOWYL TINIH OFAMR PLSRE NONLA TOOSE TFDEH SISUC ISSNO NAOND GAEER RDOCE DRTFO EHEEM ITOGN IRAST RGDEE UOOCT EMEWS UFYLL NINET TDXEO LPTIO HTUSI CNTRE IAYTN TAEHT OFHTR OCNIM CGFNO RECNE IEOCN SNNAT ITPON LE""".replace(" ", "")

for i in range(3, 8):
    c, _ = try_find_anagram(ciphertext, i)
    print(i, c)
    print(decrypt_rows(ciphertext, c)[:20])
