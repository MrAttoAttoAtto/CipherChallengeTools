
import itertools
LIKELY_WORDS = ["CONSTANTINOPLE"]

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
        

ciphertext = """HCOOT HEAOT DHEYM AAUHA MARRA RWBEH WNDNE ESEER ETNTI RWHAT NRTRY FMRSO VEHSB RNAUT SELTE GOUEG SDENH HEYDE SEERI OEUAI SHVLS RDAEO MACDN IFDNE IAEAS EANFO AHEEA ELNFM SREHI KHABT ICLIT CTFPV ETEII AHSIS PODIS GLLSI TOIIA DHLVA OTTGE OIIHT OGEES NGURF ISRRT TUUNB ANECS DAETS SGICE LTERV MHCIE ITCAO HIOTC ESTMO TWLPT AWRAN EINWC ELUON INISS SNHFH LSTDN CSTAJ AODHE AAOTE FEADT TSEWS PESAA HHMDO OEOET EETSF HORAI OLNYO EITUI EESSA UACET NAEER EVECT IEYNO HEOEH ECHEI SEEEI NAHAU EOUAF EORSO NNNEC UMFRS IRNSI UEOIE RTUCI REIAZ IOINP FRTTE FEPHI OENCS TLTET TCHWE RCLIF DTTTT ATLUB WTLLH ESRUE MNWAN ISOFM RSOFC CIARL SSTSR DCIIR NTWEE ONETP FIEEE ISNRE GNELI IECNN ENGUE RGNIN CTNEN EDEVL CEGTS CIIAN TAIOW OTMFO EHNTA SOEOR ITURA ILTDI HURMR ACUAE ALLSE GRSGU ENAEE ITTAO TTUMT OLLRA EGDTI TSRET RASCL NOEEC DIFDC MWCEA GPAAS TSTGO ATAHA FDRTE EYEBH DMWID NAAGU STRRI EAABO NEAGO OTEIE IEOSA NANRA ROLII NRETT ELEHE TNADI CANTO DOIUO NMGIO SYEIS ANIRF MSMEH CEOSH CRHRH AERRG GWTEA TTLEO NETDE NSEFH SHMRH LIHOE TESIN DEUHG TNLHT SFOGT SRNRC TWTTV RMHSO NTEOG DUARA AOORI IPUNN NHESD ARCHL SHPIE TANTR INLST LHSIV ISORO STOYM OASAT LEINT EFCOD ITAIA ATSST NANIU NNSAI FOSMR SPRDS ECNOO OLODO TUEET TENIY TIRSV RONTL ETTMP ANTHA IODCD EUDHE AIAED SWIVE TEFTE LEFTH GGTSE TTDDT HRNAY COSDP ETORC EOFOO EEOSA OEITU TRTRH SMWED CSNTN NIRNC HAISE SIRNH ITAOH GEEFA IREYI TOVOA EEOER EFASS ISTNA BFTBN POROI EMARI NOREI TRTSN LAWII IEOEN MMUER EHHCO CSOLF MVVTI OEHEA HNLWU EOORU LRHFN OLIXA AOIHE WABAH ANUNG RLONI VCTRA IIRBC RACAT MEPTD PUSML NNPTF PGONU RCGTI UAROA SAORD RCMMS IEHNE OOSNI LERHF NEROI EHFIO IDPIF RHTEN STEIT GETHI OLGAS GSERI SGHEO AGDIE LGNTR EGTNE ERROT NAUMW TPYWG TRDKT EPSDD HDEWG MEONP LTAHA INDID ETTHU EHESN GAABN GWFTA ORTCA DSRLS AEOFN NEDTT KERSR OTUTT HOENE ODMME ILHTE DANTI THOFE TEETL NTLHC MSDIN VRNNR ALTHI NEEYA OIENN ERSNU NTUCI UVEER BLOEF MIERE ODEAI TSUEG AUTIE SMSEI IRSOB IAEGF TNGEH EOOGR AHUOR PNMAL DSOAV GRIAS ADDTM FKEAE HAARI ITMLS TIERI EOAEH EANWT GLOEA HRROL EATEN TUTOH AONLH SESMH ATTFB NNCET RNOYD VHEEE STITT ROERE POOTN AIETS UEEAT OISSR SNETL SGGTH NDCIV RTRCN PMCSA ENTTR ESVES NRSNO NEELE IDTNN ELOTC NFNTI CKOTP GRBFF DICMT RKEUE OERIW EAIEA NEIOO TEROI RYPNF TETSE EUIOP WODTB HFSAT IOUET TTHCN NNLEI LONDI CTRNT OAYGH ITSSU NTOII ETEHI TEFEN HADEE ERONR AIESL ECURA NPOUU IEEEI KNANI OEEIE OORNS NFOMT IAEAO EUNBI KTENO NRIUD NCIHR RANWA HTTOA LNNTT EOPNN NMNFO TAHAU AWEDN REIRH PRWTN SLFSU NCLWH ANVRE REROH NNIDN EUFNI POESC ELTIS DNASR ESNNT EMEIR VNADO BPWSD OEEIR SOTNR SHSON IXNAE ANSSL OAOHA UPAIR NFOAE HLEAA HEEAT DCYST FHIHP NILRR ITEUE RAORS TTOJD MTTAI SCTEO USCAE TIIOG AEGNI CHAEF MFIAL ORIOR NCSNF OCROS LFROO GDALH ETSMG URENW SSWEI ONRWS ETTMS RRNNI WESTV TFEON TBTUE OOLAN ECREN ESEIM NHSNI LWDTT RGTAR SOLID NHENK FRTTW TLOSN FOPHC HGTAH ECBOA ORMT""".replace(" ", "")
for kwlen in range(3, 12):
    x = ''.join(rows_from_columns(ciphertext, kwlen))
    c, _ = try_find_anagram(x, kwlen)
    print(kwlen, c)
    print("HELLO")
    if c is not ():
        print(decrypt_rows(x, c)[:20])
