import random
import urllib.request
import time
start_time = time.time()

def ping():
    var1 = ['Da']
    var2 = [
        'Heterosexual%C4%83+(atrac%C8%9Bie+numai+fa%C8%9B%C4%83+de+persoane+de+sexul+opus)',
        'Homosexual%C4%83+(atrac%C8%9Bie+numai+fa%C8%9B%C4%83+de+persoanele+de+acela%C8%99i+sex)',
        'Bisexual%C4%83+(atrac%C8%9Bie+fa%C8%9B%C4%83+de+ambele+sexe)',
        'Asexual%C4%83+(nu+are+atrac%C8%9Bie+sexual%C4%83+fa%C8%9B%C4%83+de+niciun+sex+sau+gen).'
    ]

    var3 = [

        'Op%C8%9Biunea+B',
        'Op%C8%9Biunea+A'
    ]



    var14 = ['1', '2', '3', '4', '5']
    var15 = ['1', '2', '3', '4', '5']
    var16 = ['1', '2', '3', '4', '5']
    var17 = ['1', '2', '3', '4', '5']
    var18 = ['1', '2', '3', '4', '5']
    var19 = ['1', '2', '3', '4', '5']
    var20 = ['1', '2', '3', '4', '5']
    var21 = ['1', '2', '3', '4', '5']
    var22 = ['1', '2', '3', '4', '5']
    var23 = ['1', '2', '3', '4', '5']
    var24 = ['1', '2', '3', '4', '5']
    var25 = ['1', '2', '3', '4', '5']
    var26 = ['1', '2', '3', '4', '5']
    var27 = ['1', '2', '3', '4', '5']
    var28 = ['1', '2', '3', '4', '5']
    var29 = ['1', '2', '3', '4', '5']
    var30 = ['1', '2', '3', '4', '5']
    var31 = ['1', '2', '3', '4', '5']
    var32 = ['1', '2', '3', '4', '5']
    var33 = ['1', '2', '3', '4', '5']
    var34 = ['1', '2', '3', '4', '5']
    var35 = ['1', '2', '3', '4', '5']
    var36 = ['1', '2', '3', '4', '5']
    var37 = ['1', '2', '3', '4', '5']
    var38 = ['1', '2', '3', '4', '5']
    var39 = ['1', '2', '3', '4', '5']
    var40 = ['1', '2', '3', '4', '5']
    var41 = ['1', '2', '3', '4', '5']
    var42 = ['1', '2', '3', '4', '5']
    var43 = ['1', '2', '3', '4', '5']
    var44 = ['1', '2', '3', '4', '5']
    var45 = ['1', '2', '3', '4', '5']
    var46 = ['1', '2', '3', '4', '5']
    var47 = ['1', '2', '3', '4', '5']
    var48 = ['1', '2', '3', '4', '5']
    var49 = ['1', '2', '3', '4', '5']
    var50 = ['1', '2', '3', '4', '5']
    var51 = ['1', '2', '3', '4', '5']
    var52 = ['1', '2', '3', '4', '5']
    var53 = ['1', '2', '3', '4', '5']
    var54 = ['1', '2', '3', '4', '5']
    var55 = ['1', '2', '3', '4', '5']
    var56 = ['1', '2', '3', '4', '5']
    var57 = ['1', '2', '3', '4', '5']
    var58 = ['1', '2', '3', '4', '5']
    var59 = ['1', '2', '3', '4', '5']
    var60 = ['Angajat']
    var61 = ['1', '2', '3', '4', '5']
    var62 = ['1', '2', '3', '4', '5']
    var63 = ['1', '2', '3', '4', '5']
    var64 = ['1', '2', '3', '4', '5']
    var65 = ['1', '2', '3', '4', '5']
    var66 = ['1', '2', '3', '4', '5']
    var67 = ['1', '2', '3', '4', '5']
    var68 = ['1', '2', '3', '4', '5']
    var69 = ['1', '2', '3', '4', '5']
    var70 = ['1', '2', '3', '4', '5']
    var71 = ['1', '2', '3', '4', '5']
    var72 = ['1', '2', '3', '4', '5']
    var73 = ['1', '2', '3', '4', '5']
    var74 = ['1', '2', '3', '4', '5']
    var75 = ['1', '2', '3', '4', '5']
    var76 = ['1', '2', '3', '4', '5']
    var77 = ['1', '2', '3', '4', '5']
    var78 = ['1', '2', '3', '4', '5']
    var79 = ['1', '2', '3', '4', '5']
    var80 = ['1', '2', '3', '4', '5']

    link = "https://docs.google.com/forms/d/e/1FAIpQLSdajkC2Y9bgcjdL4OCwwvvpx9W1vM10ApiPA0t6pHKo__-_OA/formResponse?usp=pp_url&entry.2098263493=%s&entry.1497167764=%s&entry.1495890103=%s&&entry.878824247=%s&entry.191527542=%s&entry.1249069091=%s&entry.1948437240=%s&entry.2101716554=%s&entry.459684729=%s&entry.738055451=%s&entry.1157299153=%s&entry.1676283875=%s&entry.149184897=%s&entry.1387901439=%s&entry.369864373=%s&entry.34781371=%s&entry.1634826413=%s&entry.116547836=%s&entry.633538413=%s&entry.1301739020=%s&entry.1116985856=%s&entry.1298171401=%s&entry.1048195479=%s&entry.11921290=%s&entry.861289069=%s&entry.552270372=%s&entry.1428212545=%s&entry.1254648214=%s&entry.1376975919=%s&entry.927374066=%s&entry.502207017=%s&entry.665783085=%s&entry.1958877850=%s&entry.1115074390=%s&entry.1148898843=%s&entry.254418=%s&entry.1666792128=%s&entry.1576477473=%s&entry.669154977=%s&entry.1539534802=%s&entry.1324829331=%s&entry.761830038=%s&entry.1938866727=%s&entry.1954765330=%s&entry.682436656=%s&entry.1702714142=%s&entry.184950505=%s&entry.559718648=%s&entry.1173716465=%s&entry.554365494=%s&entry.485271122=%s&entry.1697032384=%s&entry.1065944024=%s&entry.1491744212=%s&entry.902310139=%s&entry.1426285537=%s&entry.1243065005=%s&entry.236542799=%s&entry.92052687=%s&entry.809913012=%s&entry.1206683461=%s&entry.805607913=%s&entry.1277348542=%s&entry.537863305=%s&entry.59428512=%s&entry.1007406158=%s&entry.960706476=%s&entry.2010185824=%s&entry.1335994241=%s&entry.326540379=%s"\
        % \
        (random.choice(var1),
         random.choice(var2),
         random.choice(var3),
         random.choice(var14),
         random.choice(var15),
         random.choice(var16),
         random.choice(var17),
         random.choice(var18),
         random.choice(var19),
         random.choice(var20),
         random.choice(var21),
         random.choice(var22),
         random.choice(var23),
         random.choice(var24),
         random.choice(var25),
         random.choice(var26),
         random.choice(var27),
         random.choice(var28),
         random.choice(var29),
         random.choice(var30),
         random.choice(var31),
         random.choice(var32),
         random.choice(var33),
         random.choice(var34),
         random.choice(var35),
         random.choice(var36),
         random.choice(var37),
         random.choice(var38),
         random.choice(var39),
         random.choice(var40),
         random.choice(var41),
         random.choice(var42),
         random.choice(var43),
         random.choice(var44),
         random.choice(var45),
         random.choice(var46),
         random.choice(var47),
         random.choice(var48),
         random.choice(var49),
         random.choice(var50),
         random.choice(var51),
         random.choice(var52),
         random.choice(var53),
         random.choice(var54),
         random.choice(var55),
         random.choice(var56),
         random.choice(var57),
         random.choice(var58),
         random.choice(var59),
         random.choice(var60),
         random.choice(var61),
         random.choice(var62),
         random.choice(var63),
         random.choice(var64),
         random.choice(var65),
         random.choice(var66),
         random.choice(var67),
         random.choice(var68),
         random.choice(var69),
         random.choice(var70),
         random.choice(var71),
         random.choice(var72),
         random.choice(var73),
         random.choice(var74),
         random.choice(var75),
         random.choice(var76),
         random.choice(var77),
         random.choice(var78),
         random.choice(var79),
         random.choice(var80)
    )

    getSite = urllib.request.urlopen(link)


def loop(N):
    for x in range(0, N):
        ping()
        print("Done: %s" % x)


# cate raspunsuri vrei
loop(96)
print("Time while running: %s seconds." % (time.time() - start_time))