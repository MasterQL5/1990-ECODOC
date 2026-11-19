const { chromium } = require('playwright'); const fs=require('fs'); const {L}=require('./rev_spec.js');
const x1=JSON.parse(fs.readFileSync('new_xl.json')), x2=JSON.parse(fs.readFileSync('step3_xl.json'));
const VAR=process.env.VAR||'a';(async()=>{ const b=await chromium.launch(); const p=await b.newPage(); p.on('pageerror',e=>console.log('ERR',e.message));
 await p.goto('file:///home/claude/ecodoc1990/index.html');
 const live={dt:[{id:"new",adj:275143361493.4612,amt:0,name:"New debt"}],il:[{id:"0rnswi0",to:"TUR",amt:4.5e9,name:"Turkish-held Bonds",rate:0.01}],pol:{def:"debt"},gadj:-4.5e9,inflate:false};
 const mechs=L.map(r=>Object.assign({kind:r[1],name:r[0],amt:r[2]*1e6},r[3]||{})); mechs.push({kind:"tariff",name:"Tariffs",amt:0,avg:.05,tar:0});
 const o=await p.evaluate(({mechs,x1,x2,live,VAR})=>{
  S.year=1993; S.credit.USA='AAA+'; Object.assign(nxw('USA'),live); fxClear();
  txApply('USA',{scope:"US federal government only. FY1993 Table 22-6 base (existing law), with the Budget Omnibus & Restructuring Act of 1993 tax provisions applied.",mechs});
  const X=nxw('USA'); X.xl=x1.map(r=>[r.name,r.amt,r.cat,r.flag]);
  const gen=genOf('USA'), dtp=dtOf('USA').reduce((t,d)=>t+Math.max(0,dtAmt(d)),0)*tierMk(creditOf('USA')); X.irl=(214.6e9-dtp)/gen*100; fxClear();
  const before=fxT('USA'); const bpm={}; X.tx.m.forEach(m=>{bpm[m.name]=txSum(mechEval(txCtx('USA'),m))});
  const c=txCtx('USA'), mn=c.mn, get=n=>X.tx.m.find(m=>m.name===n);
  const pit=get("Individual income tax"); const V=VAR; const B=[[38700/mn,.25],[93700/mn,.33],[195450/mn,.35],[426700/mn,.37]]; if(V==='a'){pit.bk=[[0,0],[9525/mn,.15]].concat(B); pit.std=0;} else if(V==='b'){pit.bk=[[0,.15]].concat(B); pit.std=7800/mn;} else if(V==='c'){pit.bk=[[0,0],[9525/mn,.15]].concat(B); pit.std=0; } else {pit.bk=[[0,.15]].concat(B); pit.std=pit.std;} 
  const cit=get("Corporate income tax"); cit.rate=.37; cit.allow=0; cit.shift=0; cit.k=221.693e9/(c.g*cit.bs);
  const cg=get("Excise: Cigarettes"); cg.rate=0.683; const ot=get("Excise: Other tobacco"); ot.rate=0.594; get("Excise: Beer").rate=0.624; get("Excise: Distilled spirits").rate=0.728;
  const mk=(name,amt)=>{const m={kind:"flat",name,amt,id:uid(),m0:mn}; m.k=amt/c.g; X.tx.m.push(m);};
  mk("Capital gains tax abolition (static loss)",-28976232116); mk("R&D&E tax credit, 3-tier 25%+25%+25% (static cost)",-24.9e9); mk("Patent Box royalty exemption (static loss)",-3.2e9); mk("Universal Savings Accounts (static cost, year 1)",-1.5e9); mk("SALT deduction cap at $10,000 (static gain)",6e9); mk("Non-primary residence mortgage interest deduction eliminated",2e9); mk("Alternative minimum tax abolition (static loss)",-4e9);
  X.xl=x2.map(r=>[r.name,r.amt,r.cat,r.flag]); fxClear();
  const after=fxT('USA'); const apm={}; X.tx.m.forEach(m=>{apm[m.name]=txSum(mechEval(txCtx('USA'),m))});
  return {Rb:before.R/1e9,Xb:before.X/1e9,Ra:after.R/1e9,Xa:after.X/1e9,neta:after.net/1e9,int:interestOf('USA')/1e9,bpm,apm,tx:X.tx,sumxl2:X.xl.filter(e=>e[2]!=="Net interest").reduce((t,e)=>t+e[1],0)/1e9};
 },{mechs,x1,x2,live,VAR});
 console.log(JSON.stringify({Rb:o.Rb,Xb:o.Xb,Ra:o.Ra,Xa:o.Xa,net:o.neta,int:o.int,sumxl2:o.sumxl2}));
 for(const n in o.apm){const d=(o.apm[n]-(o.bpm[n]||0))/1e9; if(Math.abs(d)>0.05) console.log(n.padEnd(48),(o.bpm[n]/1e9||0).toFixed(2).padStart(8),(o.apm[n]/1e9).toFixed(2).padStart(8),d.toFixed(2).padStart(8));}
 fs.writeFileSync('out3.json',JSON.stringify(o)); await b.close(); })();
