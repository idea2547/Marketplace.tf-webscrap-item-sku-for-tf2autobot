


item_data = ['/items/tf2/-100;6', '/items/tf2/398;6', '/items/tf2/1186;6', '/items/tf2/101;6', '/items/tf2/615;6', '/items/tf2/980;6', '/items/tf2/30136;6', '/items/tf2/877;6', '/items/tf2/314;6', '/items/tf2/612;6', '/items/tf2/935;6', '/items/tf2/184;6', '/items/tf2/481;6', '/items/tf2/253;6', '/items/tf2/146;6', '/items/tf2/652;6', '/items/tf2/480;6', '/items/tf2/341;6', '/items/tf2/30416;6', '/items/tf2/30114;6', '/items/tf2/30307;6', '/items/tf2/30093;6', '/items/tf2/847;6', '/items/tf2/259;6', '/items/tf2/174;6;uncraftable', '/items/tf2/436;6', '/items/tf2/437;6', '/items/tf2/30327;6', '/items/tf2/30313;6', '/items/tf2/30081;6', '/items/tf2/395;6', '/items/tf2/181;6', '/items/tf2/263;6', '/items/tf2/254;6', '/items/tf2/841;6', '/items/tf2/753;6', '/items/tf2/30316;6', '/items/tf2/100;6', '/items/tf2/95;6', '/items/tf2/379;6', '/items/tf2/321;6', '/items/tf2/313;6', '/items/tf2/290;6', '/items/tf2/247;6', '/items/tf2/523;6', '/items/tf2/521;6', '/items/tf2/216;6', '/items/tf2/844;6', '/items/tf2/30567;6', '/items/tf2/291;6', '/items/tf2/604;6', '/items/tf2/523;6;uncraftable', '/items/tf2/346;6', '/items/tf2/30037;6', '/items/tf2/30029;6', '/items/tf2/179;6', '/items/tf2/30346;6', '/items/tf2/137;6', '/items/tf2/309;6', '/items/tf2/30008;6', '/items/tf2/30040;6', '/items/tf2/30005;6', '/items/tf2/30004;6', '/items/tf2/109;6', '/items/tf2/345;6', '/items/tf2/30006;6', '/items/tf2/30059;6', '/items/tf2/602;6', '/items/tf2/104;6', '/items/tf2/251;6', '/items/tf2/180;6', '/items/tf2/399;6', '/items/tf2/318;6', '/items/tf2/30393;6', '/items/tf2/30326;6', '/items/tf2/30135;6', '/items/tf2/30094;6', '/items/tf2/174;6', '/items/tf2/1018;6', '/items/tf2/435;6', '/items/tf2/30418;6', '/items/tf2/30022;6', '/items/tf2/30019;6', '/items/tf2/30001;6', '/items/tf2/108;6', '/items/tf2/846;6', '/items/tf2/633;6', '/items/tf2/30318;6', '/items/tf2/30031;6', '/items/tf2/30827;6', '/items/tf2/30836;6', '/items/tf2/31080;6', '/items/tf2/30039;6', '/items/tf2/30021;6', '/items/tf2/323;6', '/items/tf2/30034;6', '/items/tf2/30429;6', '/items/tf2/31112;6', '/items/tf2/30974;6', '/items/tf2/30065;6', '/items/tf2/30547;6', '/items/tf2/324;6', '/items/tf2/30404;6', '/items/tf2/120;6', '/items/tf2/825;6', '/items/tf2/538;6', '/items/tf2/391;6', '/items/tf2/388;6']

command_list = []

for i in item_data:
    datas = ('!add sku='+i[11:])

    with open("item_data.txt", mode="a") as data:
        data.write(f"{datas}\n")

print(command_list)


