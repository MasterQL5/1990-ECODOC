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
("Fannie Mae (privatized, merged into FHFA)",6900,0,None,"GSE: no federal outlay line in doc"),
("Freddie Mac (privatized, merged into FHFA)",2250,0,None,"GSE: no federal outlay line in doc"),
("Federal Home Loan Banks de-subsidized",40,0,None,"no line in doc"),
("NPR federal workforce reduction (108B to ~95B)",108000,95000,None,"steady-state, cross-cutting"),
("Departmental consolidations (overhead, minimum)",2500,0,None,"cross-cutting"),
]
INCR=[ # (item, $M, line or new line name, category, idx, note)
("NASA (12.3B to 15.27B)",2970,"*NASA","Science, space and technology",0,"bill lists NASA twice (14.3B to 23.853B on p.15; 12.3B to 15.27B on p.17); used the latter, which fits the bill's Budget Increases total"),
("National Science Foundation (+12M)",12,"National Science Foundation",None,None,""),
("Atomic Energy Commission (~1.0B to ~1.08B)",80,"Nuclear Regulatory Commission",None,None,""),
("Technology & Manufacturing Extension Program",79.9,"Commerce science and technology (NOAA, NIST)",None,None,""),
("U.S. Public Service Academy (replaces OPM)",425,"U.S. Public Service Academy","Education, training and social services",1,"new line"),
("U.S. Digital Service",21.3,"U.S. Digital Service","General government",1,"new line"),
("DoJ Civil Rights Division (expanded to ~385M)",385,"DoJ Civil Rights Division (expanded)","Administration of justice",0,"new line (absorbs five bodies + 65M existing)"),
]
ledger=[]; pool=0.0; applied_total=0.0
touched=set()
for item,b,a,line,note in CUTS:
    s=(b-a)*M
    if line is None:
        pool+=s; ledger.append(dict(item=item,saving_bill=s,applied=0,to_pool=s,line=None,note=note)); continue
    cur=L[line]['amt']
    take=min(s,max(cur,0))
    L[line]['amt']=cur-take; touched.add(line)
    pool+=s-take; applied_total+=take
    ledger.append(dict(item=item,saving_bill=s,applied=take,to_pool=s-take,line=line,note=note))
# increases
inc_total=0
for item,m,line,cat,idx,note in INCR:
    amt=m*M; inc_total+=amt
    if line=="*NASA":
        ns=[n for n in L if n.startswith("NASA:")]; tot=sum(L[n]['amt'] for n in ns)
        for n in ns: L[n]['amt']+=amt*L[n]['amt']/tot; touched.add(n)
    elif line in L: L[line]['amt']+=amt; touched.add(line)
    else:
        L[line]=dict(name=line,amt=round(amt),cat=cat,flag=idx,tag='D',src='Budget Omnibus & Restructuring Act of 1993',parent=item,pre=0); order.append(line); touched.add(line)
    ledger.append(dict(item="INCREASE: "+item,saving_bill=-amt,applied=-amt,to_pool=0,line=line,note=note))
# pool distribution: all positive non-Social-Security lines not touched, excluding IRS lines
excl_cat={"Social security","Net interest"}
elig=[n for n in order if L[n]['cat'] not in excl_cat and L[n]['amt']>0 and n not in touched and not n.startswith("Internal Revenue") and not n.startswith("Other fiscal operations")]
elig_sum=sum(L[n]['amt'] for n in elig)
pct=pool/elig_sum
by_cat=collections.OrderedDict()
for n in elig:
    cut=L[n]['amt']*pct; by_cat[L[n]['cat']]=by_cat.get(L[n]['cat'],0)+cut
    L[n]['pool_cut']=cut; L[n]['amt']-=cut
out=[]
for n in order:
    r=L[n]; r['amt']=round(r['amt']); out.append(r)
json.dump(out,open('step2_xl.json','w'),indent=1); json.dump(ledger,open('step2_ledger.json','w'),indent=1)
tot_bill=sum(x['saving_bill'] for x in ledger if x['saving_bill']>0)
print('bill savings total (listed items) $B',tot_bill/1e9,' applied to named lines',applied_total/1e9,' pooled',pool/1e9,' increases',inc_total/1e9)
print('pool eligible base $B',elig_sum/1e9,' pool cut pct',pct*100)
for c,v in by_cat.items(): print(f'  {c:42s}{v/1e9:7.2f}')
old=sum(r['amt'] for r in base if r['cat']!='Net interest'); new=sum(r['amt'] for r in out if r['cat']!='Net interest')
print('program total before',old/1e9,'after',new/1e9,'delta',(new-old)/1e9)
