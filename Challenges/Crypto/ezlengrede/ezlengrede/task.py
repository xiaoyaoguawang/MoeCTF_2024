from sympy import *
from Crypto.Util.number import *

p = getPrime(128)
a = randprime(2, p)

FLAG = b'moectf{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for bit in plaintext:
        e = randprime(2, p)
        n = pow(int(bit) + a, e , p)
        ciphertext.append(n)
    return ciphertext

print(encrypt_flag(FLAG))

'''
p = 303597842163255391032954159827039706827
a = 34032839867482535877794289018590990371
[278121435714344315140568219459348432240, 122382422611852957172920716982592319058, 191849618185577692976529819600455462899, 94093446512724714011050732403953711672, 201558180013426239467911190374373975458, 68492033218601874497788216187574770779, 126947642955989000352009944664122898350, 219437945679126072290321638679586528971, 10408701004947909240690738287845627083, 219535988722666848383982192122753961, 173567637131203826362373646044183699942, 80338874032631996985988465309690317981, 61648326003245372053550369002454592176, 277054378705807456129952597025123788853, 17470857904503332214835106820566514388, 107319431827283329450772973114594535432, 238441423134995169136195506348909981918, 99883768658373018345315220015462465736, 188411315575174906660227928060309276647, 295943321241733900048293164549062087749, 262338278682686249081320491433984960912, 22801563060010960126532333242621361398, 36078000835066266368898887303720772866, 247425961449456125528957438120145449797, 843438089399946244829648514213686381, 134335534828960937622820717215822744145, 74167533116771086420478022805099354924, 249545124784428362766858349552876226287, 37282715721530125580150140869828301122, 196898478251078084893324399909636605522, 238696815190757698227115893728186526132, 299823696269712032566096751491934189084, 36767842703053676220422513310147909442, 281632109692842887259013724387076511623, 205224361514529735350420756653899454354, 129596988754151892987950536398173236050, 97446545236373291551224026108880226180, 14756086145599449889630210375543256004, 286168982698537894139229515711563677530, 100213185917356165383902831965625948491, 268158998117979449824644211372962370753, 264445941122079798432485452672458533870, 87798213581165493463875527911737074678, 131092115794704283915645135973964447801, 164706020771920540681638256590936188046, 178911145710348095185845690896985420147, 154776411353263771717768237918437437524, 260700611701259748940616668959555019434, 222035631087536380654643071679210307962, 281292430628313502184158157303993732703, 24585161817233257375093541076165757776, 269816384363209013058085915818661743171, 39975571110634682056180877801094873602, 125235869385356820424712474803526156473, 218090799597950517977618266111343968738, 144927096680470512196610409630841999788, 213811208492716237073777701143156745108, 64650890972496600196147221913475681291, 302694535366090904732833802133573214043, 214939649183312746702067838266793720455, 219122905927283854730628133811860801459, 224882607595640234803004206355378578645, 260797062521664439666117613111279885285, 279805661574982797810336125346375782066, 147173814739967617543091047462951522968, 23908277835281045050455945166237585493, 186338363482466926309454195056482648936, 295140548360506354817984847059061185817, 151948366859968493761034274719548683660, 96829048650546562162402357888582895187, 61129603762762161772506800496463804206, 83474322431616849774020088719454672415, 25094865151197136947956010155927090038, 86284568910378075382309315924388555908, 269311313874077441782483719283243368999, 293865655623484061732669067594899514872, 42618744258317592068586041005421369378, 54330626035773013687614797098120791595, 147903584483139198945881545544727290390, 290219451327796902155034830296135328101, 147951591390019765447087623264411247959, 176721307425594106045985172455880551666, 10617017342351249793850566048327751981, 166002147246002788729535202156354835048, 43653265786517886972591512103899543742, 191250321143079662898769478274249620839, 142288830015965036385306900781029447609, 231943053864301712428957240550789860578, 259705854206260213018172677443232515015, 42547692646223561211915772930251024103, 210863755365631055277867177762462471179, 140297326776889591830655052829600610449, 136970598261461830690726521708413303997, 93221970399798040564077738881047391445, 192314170920206027886439562261321846026, 95904582457122325051140875987053990027, 158334009503860664724416914265160737388, 134039922705083767606698907224295596883, 7789601161004867293103537392246577269, 261069289329878459425835380641261840913, 123743427894205417735664872035238090896, 20126583572929979071576315733108811761, 5317214299018099740195727361345674110, 68965882674411789667953455991785095270, 235934145208367401015357242228361016868, 250709310980093244562698210062174570956, 167048130489822745377277729681835553856, 122439593796334321806299678109589886368, 117953800124952553873241816859976377866, 226311466875372429157352019491582796620, 301401080214561977683439914412806833619, 255816105091394723475431389696875064495, 73243049441397892506665249226961409560, 226985189100195407227032930008331832009, 164462051705780513134747720427967016844, 97905180778488273557095248936896399883, 40737879120410802220891174679005117779, 180413920169781019749877067396006212488, 171309368917976988181007951396904157090, 215065878665354148046787050342635722874, 54225964222741166664978354789209176721, 179980445108969868669560591527220171967, 39118880593034932654127449293138635964, 170210538859699997092506207353260760212, 62152643864232748107111075535730424573, 28285579676042878568229909932560645217, 69823876778445954036922428013285910904, 170371231064701443428318684885998283021, 211884923965526285445904695039560930451, 2912793651373467597058997684762696593, 220544861190999177045275484705781090327, 142755270297166955179253470066788794096, 264271123927382232040584192781810655563, 214901195876112453126242978678182365781, 252916600207311996808457367909175218824, 176399700725319294248909617737135018444, 230677646264271256129104604724615560658, 1568101696521094800575010545520002520, 276644650735844694794889591823343917140, 185355461344975191330786362319126511681, 248497269558037476989199286642120676823, 27426372552503547932146407600438894266, 99885839446999373024614710052031031159, 238693364649026611386487480573211208980, 27047849084544903200283111147329657123, 261687609401872239323715016608713989139, 34926503987070847956303036393611830590, 252495954285655595492775877967398282722, 249358827602419141539353237669905281246, 42551212101869966935955269842854722856, 286527336123436427709115043975536071462, 158097411156207320921055042509886995091, 40982984899524424348979403377331335675, 87268254405858939730919659372073314983, 142920872841164853694746048293715385493, 280344634952903421792629929689092857993, 203584314487374069738101729666435007339, 76747904284507590577908045394001414841, 18608573158088521401404614102481693137, 104158289118605398449367221892619783009, 182616719368573751169836443225324741716, 272025723760783252166092979911587562064, 24194069309604403496494752448487752613, 71973842397785917741048132725314885345, 281558046604363121112749722271741416764, 66965324704079734796576428718112513855, 105222756356650324548621319241035836840, 331654051401420900830576011369146182, 131087815164777263900650262777429797113, 76104729920151139813274463849368737612, 163253554841934325278065946152769269296, 35973933431510942249046321254376084104, 223355354158871484030430212060934655984, 181704973473887713398031933516341967465, 131391458395622565487686089688656869743, 153029062510158353978320224242258979076, 75598349867958834632866616947240059419, 107656133091853571710502064573530657194, 261653899003034450454605322537555204702, 102387069931966536076616272953425585051, 174654548539988861301269811985320013260, 30731762585661721683653192240732246059, 265493340795853624586170054917042208660, 174818040730242275465453007894471517233, 99514915046145707535310601810631334278, 133978892607644700903700803642408771370, 216019770199630171637325931783378096100, 76687884966028369399497157007109898467, 262185741950606001987209986574269562289, 101935410844521914696784339882721918198, 85956270718878931834010975962772401589, 117578315837774870077915813512746446219, 209811226703488479967593762805568394383, 85782228978690599612110880989543246041, 234993402267259336147096170367513324439, 158487299348452041021565296682698871789, 159701431055714867184644360639841355076, 109022557288733938098734847159477770521, 20764822884655633017647117775843651332, 144987524936939260617020678038224835887, 214906746504968333094519539609226540495, 61852186870193663367998110214331582115, 90175894032076080713807606548780168998, 283504071501037047650569090140982777586, 267695305479884628857258564337611106120, 2466175482923380874813569827625743835, 62561740902965346823256447383892272796, 181458673990444296212252831090106274182, 151903421483215372136947284355251617709, 19545903652854510304023406921387221130, 219205004027218279279153442572018305650, 62495663621315535552427938857863551873, 12365469869484359722316573851483855865, 84444120685499458796249283893323932282, 240719245204462516267560756675192129462, 27868242791206675092288978266113368469, 231956104988320170956546781095814860314, 238410591787987745803829175586952288627, 290649141309468101840354611586699479851, 288298044918505512172272603794059992911, 43375655853069820305921366762777897508, 195308577786654489057887409352840304641, 184459971400898842809886506207633536394, 255884612697066296714973816950917234211, 8695922085804648269560669225439485137, 109407350389195091443836128149623969417, 40151058765649465408124869078260007620, 125484946058191366826510549493690011718, 71132588066103752922321942940739808864, 74434669478187680319595294456652807097, 187368213679294937718535073296853726111, 63461505676143678393259420949793811831, 131619805472714703711458729455838994067, 8579657158619864010437706463902003097, 60626278761876782233388469543817973673, 44776499706241603722632560896220653186, 257249861781237389988455384617803171877, 161899873165011719282095749671993720527, 73303482092538159761390536102771615311, 141674253732456103774983358188317473860, 112299149158347774069079224861237069975, 192409969047313867540459549167233638120, 52560717143548208264188844553309600513, 209294007943747095607573416682772182613, 65285862009539442533024037477398617382, 141465096635701758351979378177631042196, 282970656853503001128091562858564344839, 50475483578642585644452991078499278745, 162546597698227455939743094437394415689, 65258447920153625609456176138520078583, 25184730952052088803921023041299838584, 228883100940853988548836641050823478387, 234342509561041384559923481191578502671, 96929129863331626375704681481278825323, 288533470498072097357398960101692503873, 202238020435442160571930572760188491021, 179010548891454398845389500871076122861, 210509821764943794358893224681677583929, 301357944197101288505771002301759006254, 188933290023352627523422420332593360537, 207946655777875200521742190622482472884, 288626263488145443150622420747070805416, 75616301779108425588545170038742534166, 58163857263381687168244101022135667109, 297006021514663344215599115965804102114, 297690420826548736122127126645053452341, 88307045391242971429880119414942510712, 186427606153958359494215188169120285788, 135488686276533521058776859854524444361, 185380054960856211260651416683468161990, 175033658667416561573078028845860911744, 223026004671602541191897755812121342354, 34657268786986063209312902409995458857, 120560332690000675303295481174067849230, 55304621833927249516093996383526467671, 111480233798478730015825495041130765708, 188996716801525995463705449722399676888, 276300230605454487705048192796463035731, 195951365841304132244984630163178946841, 97383655947416522972353051984313703380, 94486945760999630041197414137963583839, 180706938513681126017333618518691884990, 291355503207799224380050183085704824037, 69034413486375685936282884707402207337, 147750870458026934714106830614187010708, 45030500748522416863096615057804736553, 242760053973560804002707125041520857401, 78549841097746795170488790352479728712, 2356186555504071026416878904180857750, 250486437623828232647064146324392061051, 23443836455198610186212360005846025976, 174557226633145985326629017377610499133, 105578481831185315088267357915446186040, 275620780071666328887795273613981325091, 23435505408737317601794562472269448966, 153209223406380813663608757935808571040, 298537417505667302508269715871007454162, 203833907122687718347615710181705388877, 41923370405573382737900061813058979798, 3762696947926387653032627637114050038, 201362054098012734707571348865729525585, 285561801443127226417656620776228615886, 111526376057659222252771678197929357387, 203857473647840873587593099562928738804, 44500972779851392967974092230683443589, 131565609415497588649207556985146740667, 118140388348838985266223643241117982200, 151449885527204880099343472664885565851, 296392921256617994387220911796693904909, 171323803851876663161606688343678019752, 77152982746512263077542395226111426871, 71648764903315646849225859605038798241, 204032734481806785543119754456569617316, 6308687907566364067313782129902290691, 16601010504475415688487155708691097587, 267844409827567109183739120606590016153, 8224746302136608660764206696943998066, 66759882079234093195284745682061177129, 246382951504754280882643835151081337286, 255668159720160142170457715248631352728, 198682585307670767869381177003851088434, 52435298055396076040371814840062860322, 71487031168170283085378067681578926209, 19270201008106231446848331516948751837, 259975200953378762173082382130139147342, 100957428421542421187997144087873975651, 208596806512779765020431672051552927799, 299145970783704112359526450087000033589, 150947534399996219237186223933189906692, 2048564430495506099844799218948689248, 18962488382754079143174369765373573160, 123031997265327646442638576943887737076, 244982544573374061178705105734141424990, 146410849043938910996544914770892579969, 223289253099676841267315311685506771609, 51374350072145272462874563304717832675, 11071799523780604861063183113721965515, 64879815349665030137608387728274669513, 80407660651138778640313857555610913997, 303240361297474032656368918727922343524, 103535171867293830164396688627880762056, 80560992291681297484967629700766125368, 143230791823232014720768325847406122476, 188716605362804777650654549500430035344, 232870220205325961834389425482865329315, 283584919111555062850512413920721407255, 206566027046056486360456937040463884619, 157265544558229360994066706355140059167, 234540100059557817987307855523008271441, 145080729935010940836509908225154438654, 87632901547252991486640361323948527297, 132851295075144433057295220850764336697, 119332580967710872282556206817561230364, 252662535367310697404410284791596079390, 116953597995893914045234747272641030589, 100249498080127826743176896590140549012, 136127222991007877469608037092253387587, 293872159333237281344632727438901916796, 188380258232793584033919525452891729603, 1610116068556601814921533488550773010, 227538093179017809788576278302184723209, 96083211912155805281570727244009758189, 177565192075026414675108774674272650977, 48610376097473152433617435307712235835, 247706157308906487216795222963091222950, 158089460554439410339817265377357657075, 242596743543458727108836420358578527964, 157838486547678450498998359338995593594, 154936428786673098370270244313756793764, 230069001282099253337070315838992422706, 302203905412042965194022309363722872023, 278925578180003228386990239779184911424, 2121847168422140085785053284950978779, 88186566913792352545205577594300112005, 127051055548524716972172930848069016819, 216775577660712694343189516378309335187, 44934779747684486400910901018161470888, 32429597712898788634301884219187226083, 219683174528279300995710495669083670544, 37001671152735870067433052249003677244, 40408367335919429215031155701333780256, 156957056705864208022145617831060134907, 180077610045061934161783737112285900966, 59357544819520045255625797086421901884, 77751400794807935281264495346525107329, 4517615764752715802675887411287287137, 76319782726782483955139757169428276003, 176009402215469456144386392247781430661, 283055695252017869386094188584670242363, 20001716567499724882317501875143788088, 125228382132280749989067609697418628387, 144053090751393640875176862167012247830, 15289106046221987660093620422889539867, 111243866573605033251079958638430165633, 169264885994758018612038619809803723688, 11895954311759483419234457833286931577, 273147053963507607445612310063799123998, 158981773284803069491507978382595811562, 41293513794446810141896116395025053234, 57441237860743029006005815967510568612, 109171476551418034153338841133917497633, 136539712287056106151501004438585146777, 278918550892367788720071091355436733468, 211360251223022250021398148918837686812, 254351242496347083009146404917085951637, 130260153203964833202474997491055897705, 221930288825889900517852991745469270910, 66354211799382156899053592476719001842, 127898620670768976254134750731374490934, 298131830425274848646460016809595859328, 132109510144911727511061804395381822418, 210917766469026421985352121201196497206, 5441137715689271309917542693016936841, 209516950406881264617228336887254107528, 92275151703152148383106907311559718841, 46255650973652148247469464088017660080, 182628529221607295465655096378164148336, 52574278547120304143820897608762444985, 63698472804719856407197390836793525437, 30457182690865024857724004613999433676, 212073418196280214618461610817423630022, 48875930775858981513092672396243080640, 113234797533868946026347891158142991388, 256534108458875318962058222544020064164, 22522715662428558833985333846937440705, 97553118958308509177643330175409499003, 197088081433425221073434635573357125592, 157303116668734020456228309942188293059, 110316346669278795114546305726864504681, 228887397917708007004920589862367347873, 112210930213921962308944716344585917343, 95017760786235266842788931502689331157, 303479014347753799316861720146531596843, 138677197920058856282155251074088437081, 285912176726299387362893467150449209426, 120309832759140713296686339140142433386, 279125897926861811239250830750932241600, 289502053647872994218190050825294169535, 262459212837236162171047720358005836712, 290390838897912466575239533978002826151, 292988850197951752250595007039860868400, 34796135808311610468205608686622819504, 25206338413385638687826160218013868658, 42180804482932648992176529097078580055, 195897225052351816559125785179252565465, 290060760535408066224831756224248708027, 34243626514368402883316460494646065629, 159497726968729366867935528734367549832, 267785772871046662107247674801793846921, 47342328853090920958565777290912999560, 194980176549393239742230551297786993434, 88020247887557921707284362381274951852, 255474100333005567974457204812640809071, 93324791124684170744053910877870176609, 69542826141091170218040988642070014011, 188678529221313094426441439309063681864, 56030802691247887446204447769438570825, 74312207153349149422500961216106557393, 153811406554673020809393530896156460494, 130232956128662318657579623819323546361, 241587755919930468705435097001858194189, 150548598672513907492388638742866339038, 38780469811591978249139697733603217652, 237554030153815380781978075720171312418, 96541634878634946114738393982914693394, 83284071476491638125716901346418260661, 277535192833115492238855935055373371297, 92291115416977028401374199691398676627, 105634075531674200869064066234662065605, 59669321288506854711632528171527160495, 24913178886798791108798737682436779604, 191902245938756063865405758957515936934, 200833770402179506644143905670947994664, 249327029439265065126080906281744759655, 2368715218056973901783211260781833927, 133209645820509536502329231321782644514, 170083361139958757944996287868734988169, 143242266754832252556264383809361085258, 198438133508477313319510861550461456953, 226416574016152349355240811564666677855, 131995850810926550122710727062184985075, 206211971624338783828953817981719254101, 95022339713176475801874420969255633409, 39239785273544046574575511790952158726, 6761950061835300419279903725369635970, 160849355761964483498641169767552240859, 44129081383649229398785011378026849128, 116611486899507912253396257166983831123, 102748760887182142877957834312659347601, 100973668783270797012352094429175531207, 110548564207426762905750742091610942634, 205424582078496700107783237952155124442, 210932790939110827079725957948996247757, 54413304958149902897514912130730392489, 181315803651356180100745517014898850424, 183346938138867395962624263310328788228, 133507835720650939452036529283981720094, 244220649646693249242542702657146329679, 111814540087048948955999016117121133729, 210757262617434713384638061648414714521, 31712005436857719771604404352654183712, 299210790483067037892753875410776716305, 34216439939230284515095120240039231491, 246820219620854547856488049434101568744, 298588211282375015522910461809769779222, 53320103067319149790078933423751044737, 164977173816081040725650999609390274279, 234782977255751828939911143180631329578, 61521250269407451751766565186333346163, 119529895182262920689181379893081203421, 154588465395872896210615516764102943961, 153034255402211966905777978896125271527, 65497510688725487475002809757533544579, 76824114145168270682129892469858568031, 218064880554787781811938382300930885801, 196850060586188141836799779247809406205, 176023892018381269394229104598502170110, 32491776807255207889633110137157036238, 41150198830446315717651890670848632754, 260753023840843193587871227195221789744, 48345408122882987831052823644867513356, 80045935233531979816083287928071697883, 131878104259519592871955471048058374000, 15534379538690707223440448056318568055, 131291412522855581131329717355299310716, 37018675243998552749630837151597269431, 144343493968520204610097930388908478903, 67236444178494959708570043908346657722, 102574100831305499879105427279131095784, 249069309513964056714882166119752611668, 210718130986716991560768592011623825976, 266242407402824082344585571101593909650, 205203132247422842477137158586071965100, 301157372202750742637385626243753030679, 40886620741595313792996852647181029560, 253361171396328884567373946949359324229, 50071128101197582041162516700015376269, 106002417001877546867386840932652850816, 224086864980106045542532841236299648038, 42103921294151508500634063253613482845, 49777138159264482913170680298952908154, 24324534484842395819609478778764950811, 204106593629836179932302789646808274058, 266707066043760482642609614924857456238, 18723835069315957900598472598907945204, 244338819469013923747256697307964210342, 36296287172854997655950896217230267111, 292888671179451539882069138267865661448, 287111415651274690627399445990831389362, 79940439572496625318602146625920961720, 288270505176661814341807462681727466925, 153921178962139214138689743179633342125, 263564317934507756965522450042219801757, 197993323684501153884855839599466707355, 72143993205715719344183507132882267579, 67511075584002491895239101559049103979, 231396344630318648781207380069016790960, 268490084177254392405211695854127631350, 45968181401712207064942095991325993181, 34472329776995578971329318400545600788, 112967316661320871429337739209994987784, 209508577387521479468956337084132598710, 194445696189141465862938111222574992064, 229942079198360020568341753187100646148, 47944382795398541172186729027517882654, 54806201653083974379270761512143387910, 93457347627015900562505045196097224001, 152033139738914238723733340538181549419, 123719026823969669345162603978875451754, 154704533151410142607151617227929824563, 32428281285686815618553795197210513625, 265229864831280807254743597731258298440, 14904705423314872103792141735779112532, 177442398230615511669857060547212895616, 144918716871520627851549439448066637518, 203019416536984157536348865479415073573, 288452420706913930307744155709559750006, 282516471994395201735206793889605510595, 150722332251745138694381051866105655391, 234504581837296595003379465512031425988, 44178766618576668748878202507789103195, 217129489675072754441642067295058817201, 245087939287551829934600756568137757979, 240954534396950014938672406581264782638]
'''

