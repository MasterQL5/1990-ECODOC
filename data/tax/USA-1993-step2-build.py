import json,collections
base=json.load(open('new_xl.json'))   # step-1 baseline
L={r['name']:dict(r) for r in base}
order=[r['name'] for r in base]
M=1e6
# (item, bill_before_$M, bill_after_$M, target line or None, note)
CUTS=[
("Export-Import Bank",600,0,"Export-Import Bank","Sec.V self-sufficient"),
("Overseas Private Investment Corp.",650,0,"Other development programs, net of allowances","terminated"),
("FDR Memorial Commission",48,0,"Other general government programs","terminated"),
("U.S. Institute of Peace",15,0,"Other foreign affairs","privatized"),
("North-South Center",2,0,"Other foreign affairs","privatized"),
("East-West Center",22,0,"Other foreign affairs","privatized"),
("Inst. of American Indian Arts",6,0,"Research and general education aids","terminated"),
("Japan-US Friendship Commission",14.9,0,"Research and general education aids","terminated"),
("Commission of Fine Arts",2.2,0,"Other general government programs","terminated"),
("National Endowment for the Arts",154,0,"Research and general education aids","terminated"),
("National Endowment for the Humanities",177,0,"Research and general education aids","terminated"),
("ACTION",224,0,"Domestic volunteer programs","terminated"),
("Advisory Council on Historic Preservation",1.8,0,"Other resources management","terminated"),
("Interagency Council on the Homeless",819,0,"Homeless shelter and transitional housing","terminated"),
("Civil Aeronautics Board (residual)",829,0,"Aeronautical research, carrier subsidies and other (derived)","terminated"),
("Admin. Conference of the US",1.9,0,"Other general government programs","terminated"),
("Board for International Broadcasting",425.2,0,"Board for International Broadcasting","disbanded"),
("Consumer Product Safety Commission",33.6,0,"Consumer safety (FDA, USDA inspection)","privatized"),
("Advisory Commission on Intergovt. Relations",1.3,0,"Other general government programs","terminated"),
("Appalachian Regional Commission",200,0,"Appalachian Regional Commission","abolished"),
("Arms Control and Disarmament Agency (net of ACISA $25M)",33.9,25,"Other foreign affairs","replaced by Under Sec. State"),
("Natl Capital Arts & Cultural Affairs",7,0,"Research and general education aids","abolished"),
("Commission on National Community Service",0.5,0,"Domestic volunteer programs","terminated"),
("Corporation for Public Broadcasting",298.9,0,"Research and general education aids","privatized"),
("Delaware River Basin Commission",0.6,0,"Other water resources","offloaded"),
("Interstate Commission on Potomac River Basin",0.4,0,"Other water resources","terminated"),
("Susquehanna River Basin Commission",13.6,0,"Other water resources","terminated"),
("Marine Mammal Commission",1.1,0,"Other resources management","terminated"),
("Natl Commission on Libraries and Info Science",1.0,0,"Research and general education aids","terminated"),
("Office of Government Ethics",8.0,0,"Other general government programs","terminated"),
("Pennsylvania Avenue Development Corp.",184,0,"Pennsylvania Avenue Development Corporation","privatized"),
("Corp. for National and Community Service",100,0,"Domestic volunteer programs","privatized"),
("Legal Services Corporation",415,0,"Representation of indigents in civil cases","federal funding ended"),
("National Capital Planning Commission",8,0,"Other general government programs","terminated"),
("Neighborhood Reinvestment Corp.",36,0,"Other community development","terminated"),
("State Justice Institute",13.9,0,"Other litigative activities","terminated"),
("Thomas Jefferson Commemorative Commission",1.3,0,"Other general government programs","terminated"),
("Small Business Administration (1.1B to 201M)",1100,201,"Small and minority business assistance","wound down"),
("Office of Personnel Management",197,0,"Central personnel management","terminated"),
("Peace Corps (halved)",200,100,"Peace Corps","halved"),
("Tennessee Valley Authority econ. development",79.3,0,"Tennessee Valley Authority (regional)","subsidies terminated (unquantified in bill: line zeroed)"),
("Selective Service System (to ~$4M in DoD)",24,4,"Defense-related activities","reduced"),
("FMCS + NMB merged (net)",40,38,"Other labor services","merged"),
("African Development Fdn + Inter-American Fdn",34.32,0,"Agency for International Development","merged into USAID, budget cut"),
("Postal Regulatory Commission",15,0,"Payments to the Postal Service fund","terminated"),
("FCC (-20%)",128.5,102.8,"International trade and other commerce","reduced"),
("Rural Electrification Administration",36,0,"Rural development","wound down"),
("CSRS + Extension merged into CSREES",910,900,"Agricultural research and extension (derived)","merged"),
("Foreign Agricultural Service",130,0,"Other agricultural programs and overhead","terminated"),
("Commodity Credit Corporation",30300,0,"Commodity Credit Corporation","terminated"),
("USDA Office of Consumer Affairs",2,0,"Other agricultural programs and overhead","terminated"),
("Federal Agricultural Mortgage Corp.",40.3,0,"Agricultural credit, TEFAP and other (derived)","terminated"),
("Economics and Statistics Admin. umbrella",10,0,"Economic and demographic statistics","terminated"),
("Economic Development Administration",400,0,"Economic development assistance","terminated"),
("Minority Business Development Agency",44,0,"Small and minority business assistance","terminated"),
("National Technical Information Service",4,0,"International trade and other commerce","privatized"),
("US Travel and Tourism Administration",17,0,"International trade and other commerce","terminated"),
("Commerce Office of Consumer Affairs",2,0,"International trade and other commerce","terminated"),
("Ballistic Missile Defense Organization",3800,2800,"Research, development, test and evaluation","reduced"),
("Education Office of Educ. Research and Improvement",360,340,"Research and general education aids","overhead cut"),
("Public Health Service umbrella",225,125,"Other health care services (HRSA, IHS, CDC)","consolidated"),
("HHS Office of Consumer Affairs",1,0,"Other health care services (HRSA, IHS, CDC)","terminated"),
("HUD field office network",450,280,"Other housing assistance","consolidated"),
("Bureau of Mines",170,0,"Other natural resource programs","terminated"),
("Women's Bureau",8,0,"Other labor services","terminated"),
("Office of the American Workplace",15,0,"Other labor services","terminated"),
("Bureau of Democracy, Human Rights and Labor",300,0,"State Department salaries and expenses","merged, funding ended"),
("USAID (7.0B to 6.6B)",7000,6600,"Agency for International Development","reorganized"),
("Interstate Commerce Commission (STB ~15M)",55,15,"Surface transportation regulation","terminated"),
("Office of Revenue Sharing",2,0,"Other fiscal assistance","terminated"),
("National Critical Materials Council",0.5,0,"Other general government programs","terminated"),
("Points of Light Foundation appropriation",6,0,"Domestic volunteer programs","terminated"),
("Student loans: FFEL to Direct Lending (~4.3B/5y)",860,0,"Guaranteed student loan program","replaced"),
# civil-rights consolidation: predecessors removed, CRD expanded below
("EEOC (into DoJ CRD)",221,0,"Other labor services","consolidated"),
("Commission on Civil Rights (into DoJ CRD)",9.5,0,"Other litigative activities","consolidated"),
("HUD Fair Housing office (into DoJ CRD)",40,0,"Other housing assistance","consolidated"),
("HHS Office for Civil Rights (into DoJ CRD)",18,0,"Other health care services (HRSA, IHS, CDC)","consolidated"),
("Education Office of Civil Rights (into DoJ CRD)",59,0,"Research and general education aids","consolidated"),
("Community Relations Service (into DoJ CRD)",5,0,"Other litigative activities","consolidated"),
("DoJ Civil Rights Division pre-expansion",65,0,"Civil and criminal prosecution and representation","absorbed into expanded CRD"),
# no matching line in the doc: pure pool
]
INCR=[ # (item, $M, line or new line name, category, idx, note)
("NASA (14.3B to 23.853B)",9553,"*NASA","Science, space and technology",0,"bill lists NASA twice; the larger raise (14.3B to 23.853B) is used per user instruction"),
("National Science Foundation (+12M)",12,"National Science Foundation",None,None,""),
("Atomic Energy Commission (~1.0B to ~1.08B)",80,"Nuclear Regulatory Commission",None,None,""),
("Technology & Manufacturing Extension Program",79.9,"Commerce science and technology (NOAA, NIST)",None,None,""),
("U.S. Public Service Academy (replaces OPM)",425,"U.S. Public Service Academy","Education, training and social services",1,"new line"),
("U.S. Digital Service",21.3,"U.S. Digital Service","General government",1,"new line"),
("Patent and Trademark Office (fee retention, +660M)",660,"Patent and Trademark Office (fee-retained)","Commerce and housing credit",0,"new line; bill: 418M to 1.08B"),
("Earned income tax credit extended to all taxpayers (s.201a), childless workers",1200,"Earned income tax credit (outlay portion)",None,None,"estimate: ~5M childless filers x ~$240 (1994-96 childless credit schedule)"),
("DoJ Civil Rights Division (expanded to ~385M)",385,"DoJ Civil Rights Division (expanded)","Administration of justice",0,"new line (absorbs five bodies + 65M existing)"),
]

GSE=[("Fannie Mae (privatized, merged into FHFA)",6900),("Freddie Mac (privatized, merged into FHFA)",2250),("Federal Home Loan Banks de-subsidized",40)]
NPR=[("NPR federal workforce reduction (108B to ~95B)",13000),("Departmental consolidations (overhead, minimum)",2500)]
ledger=[]; applied_total=0.0; touched=set(); comp=collections.defaultdict(lambda: collections.defaultdict(float))
left=[]  # (item, leftover, line)
for item,b,a,line,note in CUTS:
    s_=(b-a)*M; cur=L[line]['amt']; take=min(s_,max(cur,0))
    L[line]['amt']=cur-take; comp[line]['named']+=take; touched.add(line); applied_total+=take
    if s_-take>0.5: left.append((item,s_-take,line))
    ledger.append(dict(item=item,saving_bill=s_,applied=take,to_pool=s_-take,line=line,note=note))
cat=lambda c:[n for n in order if L[n]['cat']==c and L[n]['tag']!='IRS']
USDA=cat("Agriculture")+["Food stamps","Aid to Puerto Rico (nutrition)","Child nutrition and other food programs","Forest Service and other land management","Conservation reserve program","Other agricultural land conservation","Rural housing programs (FmHA)","Rural development","Food aid (P.L. 480)"]
HUD=["Subsidized housing (Section 8 and others)","Renewal of Section 8 contracts","HOPE grants","Public housing operating subsidies","Low-rent public housing loans","HOME investment partnerships","Shelter plus care","Other housing assistance","Community development block grants","Housing for the elderly or handicapped"]
HFIN=HUD+["FHA mortgage credit","GNMA mortgage-backed securities"]
GENGOV=["Legislative functions","Executive direction and management","Federal buildings fund","Records management","Other property management","Other general government programs","Central personnel management"]
HOME={"Commodity Credit Corporation":("USDA",USDA),"Homeless shelter and transitional housing":("HUD",HUD),
"Export-Import Bank":("International affairs",cat("International affairs")),"Other development programs, net of allowances":("International affairs",cat("International affairs")),"Board for International Broadcasting":("International affairs",cat("International affairs")),
"Domestic volunteer programs":("Education/social services",cat("Education, training and social services")),
"Aeronautical research, carrier subsidies and other (derived)":("Transportation",cat("Transportation")),"Surface transportation regulation":("Transportation",cat("Transportation")),
"Economic development assistance":("Community/regional development",cat("Community and regional development")),"Appalachian Regional Commission":("Community/regional development",cat("Community and regional development")),"Pennsylvania Avenue Development Corporation":("Community/regional development",cat("Community and regional development")),
"Representation of indigents in civil cases":("Justice",cat("Administration of justice")),"Other litigative activities":("Justice",cat("Administration of justice")),
"Small and minority business assistance":("Commerce",["Commerce science and technology (NOAA, NIST)","Economic and demographic statistics","International trade and other commerce"]),
"Central personnel management":("General government",GENGOV),"Other general government programs":("General government",GENGOV)}
PROT=["Food stamps","Aid to Puerto Rico (nutrition)","Child nutrition and other food programs"]
def spread(amount,group,key,label):
    names=[n for n in dict.fromkeys(group) if n not in PROT and n in L and L[n]['amt']>0 and L[n]['cat'] not in ("Social security","Net interest") and not n.startswith("Internal Revenue")]
    tot=sum(L[n]['amt'] for n in names); take=min(amount,tot)
    if tot<=0: return amount
    for n in names:
        c_=take*L[n]['amt']/tot; comp[n][label]+=c_; L[n]['amt']-=c_; touched.add(n)
    return amount-take
overflow=0.0; home_tot=collections.defaultdict(float)
# 1) leftover of agency cuts goes to that agency's / function's other lines
for item,amt,line in left:
    lab,grp=HOME[line]; home_tot[lab]+=amt
    if lab=="USDA":
        NUTR=["Food stamps","Aid to Puerto Rico (nutrition)","Child nutrition and other food programs"]
        o=spread(amt,[n for n in grp if n!=line and n not in NUTR],lab,'leftover: USDA farm/rural/conservation lines')
    else: o=spread(amt,[n for n in grp if n!=line],lab,'leftover: '+lab)
    overflow+=o
# 2) GSEs -> housing finance agencies
for item,b in GSE:
    amt=b*M; home_tot['Housing (HUD/FHA/GNMA)']+=amt
    o=spread(amt,HFIN,'gse','leftover: housing (GSE)'); overflow+=o
    ledger.append(dict(item=item,saving_bill=amt,applied=amt-o,to_pool=o,line=None,note='no outlay line; spread over HUD/FHA/GNMA lines'))
# 3) NPR workforce + consolidations by department (FY1993 FTE, Budget FY1997 Hist. Tab 19.3; 'Other' split by estimate)
nasa=[n for n in L if n.startswith("NASA:")]
DEPT=[("Defense",932,["Operation and maintenance","Research, development, test and evaluation"]),
("Veterans Affairs",234,["Veterans medical care and hospital services","Veterans medical administration and research","Cemeteries and administration of veterans benefits"]),
("Justice",95,["Criminal investigations (DEA, FBI)","Other federal law enforcement","Civil and criminal prosecution and representation","Federal correctional activities"]),
("Treasury excl. IRS",51,["Alcohol, tobacco and firearms investigation","Secret Service protection","Border enforcement (Customs and INS)"]),
("Agriculture",114,["Agricultural research and extension (derived)","Marketing programs","Animal and plant health inspection","Economic intelligence","Other agricultural programs and overhead","Crop insurance","Agricultural credit, TEFAP and other (derived)","Forest Service and other land management"]),
("HHS/Education",71,["Other health care services (HRSA, IHS, CDC)","National Institutes of Health","Other health research and training","Health professional education","Consumer safety (FDA, USDA inspection)","ACF service programs (Head Start and others)","Research and general education aids"]),
("Interior",78,["Bureau of Land Management","Operation of recreational resources (NPS)","Mining reclamation and enforcement","Bureau of Reclamation","Other resources management","Other natural resource programs","Indian programs","Other water resources"]),
("Transportation",69,["Airports and airways (FAA)","Marine safety and transportation (Coast Guard)","Highway safety","Railroads (Amtrak and FRA)","Miscellaneous transportation programs"]),
("Commerce",36,["Commerce science and technology (NOAA, NIST)","Economic and demographic statistics","International trade and other commerce"]),
("Labor",17,["Other labor services","Occupational safety and health","Other training and employment"]),
("State",25,["State Department salaries and expenses","Foreign buildings","Other foreign affairs"]),
("Energy",20,["DOE weapons activities","Energy R&D (DOE)","DOE general science programs","Other energy programs","Energy conservation","Emergency energy preparedness","Defense environmental restoration and waste management","Materials production and other defense programs"]),
("EPA",18,["EPA regulatory, enforcement and research","Superfund (hazardous substance response)","Oil pollution funds","Leaking underground storage tank fund"]),
("HUD",12,["Other housing assistance"]),
("NASA",24,nasa),
("Other independents, GSA, legislative",168,[])]
W=sum(d[1] for d in DEPT); npr_by={}
for item,m in NPR:
    amt=m*M; got=0
    for d,w,grp in DEPT:
        part=amt*w/W; o=spread(part,grp,'npr','NPR/consolidation: '+d); got+=part-o; overflow+=o; npr_by[d]=npr_by.get(d,0)+part-o
    ledger.append(dict(item=item,saving_bill=amt,applied=got,to_pool=amt-got,line=None,note='split by department FTE share; each department cut over its own operating lines'))
# 4) only overflow (home group exhausted) goes to the global pool
excl_cat={"Social security","Net interest"}
NUTR=["Food stamps","Aid to Puerto Rico (nutrition)","Child nutrition and other food programs"]
elig=[n for n in order if n not in NUTR and L[n]['cat'] not in excl_cat and L[n]['amt']>0 and not n.startswith("Internal Revenue") and not n.startswith("Other fiscal operations")]
overflow=spread(overflow,elig,'overflow','overflow (agency lines exhausted)')
# 5) increases
inc_total=0
for item,m,line,cat_,idx,note in INCR:
    amt=m*M; inc_total+=amt
    if line=="*NASA":
        ns=[n for n in L if n.startswith("NASA:")]; tot=sum(L[n]['amt'] for n in ns)
        for n in ns: L[n]['amt']+=amt*L[n]['amt']/tot; comp[n]['increase']+=amt*L[n]['amt']/tot
    elif line in L: L[line]['amt']+=amt; comp[line]['increase']+=amt
    else:
        L[line]=dict(name=line,amt=round(amt),cat=cat_,flag=idx,tag='D',src='Budget Omnibus & Restructuring Act of 1993',parent=item,pre=0); order.append(line)
    ledger.append(dict(item="INCREASE: "+item,saving_bill=-amt,applied=-amt,to_pool=0,line=line,note=note))
out=[]
for n in order:
    r=L[n]; r['amt']=round(r['amt']); c_=comp.get(n)
    if c_: r['note']='; '.join(f"{k} {v/1e6:+.1f}M" if k=='increase' else f"{k} -{v/1e6:.1f}M" for k,v in c_.items() if abs(v)>5e4)
    out.append(r)
json.dump(out,open('step4_xl.json','w'),indent=1); json.dump(ledger,open('step4_ledger.json','w'),indent=1)
old=sum(r['amt'] for r in base if r['cat']!='Net interest'); new=sum(r['amt'] for r in out if r['cat']!='Net interest')
print('named applied',applied_total/1e9,'leftover by agency',{k:round(v/1e9,2) for k,v in home_tot.items()},'overflow to global',overflow/1e9)
print('npr by dept $B',{k:round(v/1e9,2) for k,v in npr_by.items()})
print('increases',inc_total/1e9,'program total before',old/1e9,'after',new/1e9,'delta',(new-old)/1e9)
neg=[r['name'] for r in out if r['amt']<0 and L[r['name']].get('pre',0)>=0 and L[r['name']]['cat'] not in('Net interest',)]
print('lines turned negative:',[r['name'] for r in out if r['amt']<0 and r['name'] in {x['name'] for x in base if x['amt']>=0}])
