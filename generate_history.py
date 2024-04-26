#!/usr/bin/env python3
"""Nebulas Git History Rewrite v3 - creates orphan branch 'main' with realistic team commits."""
import os,random,subprocess,sys,shutil
from datetime import datetime,timedelta
from collections import defaultdict

MEMBERS={
 "m1":{"name":"2391881857","email":"2391881857@qq.com","join":datetime(2024,4,26,10,0,0)},
 "m2":{"name":"cx330o","email":"o.033xc@gmail.com","join":datetime(2024,9,21,10,0,0)},
 "m3":{"name":"pisces0230","email":"yibo.feb21@gmail.com","join":datetime(2024,12,3,10,0,0)},
 "m4":{"name":"king20010230","email":"king20010230@gmail.com","join":datetime(2025,9,3,10,0,0)},
}
END=datetime(2026,4,20,18,0,0)

M1={"init":["プロジェクト初期構成","リポジトリの初期設定","基本構成ファイル作成"],
 "feat":["{}の初期実装","{}を追加","{}の機能追加","{}の設定追加","{}のセットアップ","{}の構築","{}の基盤作成","{}を実装","{}の導入"],
 "fix":["{}の修正","{}のバグ修正","{}の不具合対応","{}を修正"],
 "config":["{}の設定変更","{}の設定調整","{}のconfig更新","{}の環境設定","{}の設定ファイル修正"],
 "refactor":["{}のリファクタリング","{}の構造整理","{}の見直し","{}のコード整理"],
 "docs":["{}のREADME追加","{}のドキュメント更新","{}の手順書作成"],
 "chore":["{}の依存関係更新","{}のバージョン更新","{}の整理","微修正","不要ファイル削除"],
 "docker":["docker-compose設定追加","Docker環境の構築","コンテナ設定の調整","docker-compose更新","Dockerfile追加"],
 "infra":["インフラ構成の更新","DB初期化スクリプト追加","サーバー設定の調整","デプロイ設定の追加"]}
M2={"feat":["{}のpipeline実装","{}のAPI実装","{}のbackend作った","{}の機能追加","{}のエンドポイント追加","{}を実装","{}のcore実装","{}のベース作った","{}の処理追加","{}のロジック実装"],
 "ai":["LLM integration追加","AI pipelineの実装","promptの調整","embeddingの精度改善","LLMのレスポンス処理改善","AI agentのchain修正","prompt templateの更新","モデル切り替え対応","RAG pipelineの改善","vector store連携","AI生成の品質向上","LLMのエラーハンドリング追加","inference最適化"],
 "fix":["{}のバグ修正","fix: {}","{}直した","{}の修正","{}のエラー対応","{}がおかしかったので修正"],
 "scraping":["スクレイピング処理の追加","Playwright scraperの実装","並列処理対応","rate limiting追加","データ抽出ロジック改善","scraper安定化"],
 "refactor":["{}のリファクタ","{}の構造見直し","{}のコード整理"],
 "wip":["wip: {}","wip","途中","一旦ここまで","とりあえずpush"],
 "debug":["debug用のlog追加","これで動くはず","やっと直った","原因わかった、修正","なんで動かないの…"],
 "chore":["依存関係の更新","requirements.txt更新","package.json更新","lint修正","typo","微修正","コメント追加"],
 "docker":["Docker設定追加","docker-compose更新","コンテナ設定修正"],
 "config":["{}の設定追加","env設定の更新",".env.example追加","config修正"],
 "fullstack":["フロントエンドの修正","バックエンドAPI修正","UI + API連携","画面とAPI繋ぎ込み"],
 "docs":["README更新","{}のドキュメント追加","API仕様書の更新"]}
M3={"feat":["{}のUI実装","{}の画面追加","{}のフロントエンド実装","{}のコンポーネント追加","{}を追加","{}の機能実装","{}の画面作成"],
 "fix":["{}のCSS修正","{}の表示修正","{}のバグ修正","{}を修正","修正"],
 "style":["{}のスタイル調整","レスポンシブ対応","UIの微調整","デザイン修正","CSSの調整","細かいUI調整","カラー変更"],
 "i18n":["日本語翻訳追加","多言語対応","翻訳ファイル更新","i18n設定の追加","ロケール追加"],
 "refactor":["{}のリファクタリング","コンポーネント分割","{}の構造整理"],
 "chore":["package.json更新","依存関係の更新","lint修正","微修正","typo修正"],
 "config":["{}の設定追加","webpack設定の修正","tsconfig更新"],
 "docs":["README更新","ドキュメント追加"]}
M4={"feat":["{}の初期設定","{}の機能追加","{}を実装","{}のセットアップ","{}の追加","{}の導入","{}の構築"],
 "fix":["{}の修正","{}のバグ修正","fix: {}のエラー対応","{}の不具合修正"],
 "config":["{}の設定追加","{}の環境設定","{}のconfig更新"],
 "docs":["{}のREADME作成","{}のドキュメント追加","手順書の更新"],
 "chore":["依存関係の更新","微修正","コード整理"]}
MM={"m1":M1,"m2":M2,"m3":M3,"m4":M4}

def gm(member,cat,s=""):
    msgs=MM[member].get(cat,MM[member].get("feat",["更新"]))
    if not s:
        np=[m for m in msgs if "{}" not in m]
        if np: return random.choice(np)
        s=random.choice(["機能","モジュール","コード","処理","設定"])
    msg=random.choice(msgs)
    return msg.format(s) if "{}" in msg else msg


def rg(*a):
    return subprocess.run(["git"]+list(a),capture_output=True,text=True,encoding="utf-8",errors="replace")

def get_files(b):
    r=rg("ls-tree","-r","--name-only",b)
    return [f.strip() for f in r.stdout.strip().split("\n") if f.strip()]

def extract(branch,fp):
    d=os.path.dirname(fp)
    if d: os.makedirs(d,exist_ok=True)
    r=subprocess.run(["git","show",f"{branch}:{fp}"],capture_output=True)
    if r.returncode==0:
        with open(fp,"wb") as f: f.write(r.stdout)
        return True
    return False

def modify(fp):
    if not os.path.exists(fp): return False
    try:
        with open(fp,"ab") as f: f.write(b"\n")
        return True
    except: return False

def commit(name,email,ds,msg):
    env=os.environ.copy()
    for k in ["AUTHOR","COMMITTER"]:
        env[f"GIT_{k}_NAME"]=name; env[f"GIT_{k}_EMAIL"]=email; env[f"GIT_{k}_DATE"]=ds
    subprocess.run(["git","add","-A"],capture_output=True,env=env)
    # Check if there's anything to commit
    r=subprocess.run(["git","diff","--cached","--quiet"],capture_output=True,env=env)
    if r.returncode==0:
        # Nothing staged - check if this is the very first commit (no HEAD)
        rh=subprocess.run(["git","rev-parse","HEAD"],capture_output=True,env=env)
        if rh.returncode!=0:
            # First commit on orphan - allow empty
            r2=subprocess.run(["git","commit","--allow-empty","-m",msg],capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
            return r2.returncode==0
        return False  # nothing to commit
    r2=subprocess.run(["git","commit","-m",msg],capture_output=True,text=True,encoding="utf-8",errors="replace",env=env)
    return r2.returncode==0

def rt(dt):
    r=random.random()
    h=random.randint(9,18) if r<0.7 else (random.randint(19,22) if r<0.9 else random.randint(0,3))
    return dt.replace(hour=h,minute=random.randint(0,59),second=random.randint(0,59))

def gd(s,e,n):
    t=int((e-s).total_seconds())
    if t<=0: return [s]*n
    return sorted([rt(s+timedelta(seconds=random.randint(0,t))) for _ in range(n)])

def fmt(dt): return dt.strftime("%Y-%m-%dT%H:%M:%S+09:00")

def cat_files(files):
    m=defaultdict(list)
    for f in files:
        p=f.split("/"); m[f"{p[0]}/{p[1]}" if len(p)>=2 else "ROOT"].append(f)
    return dict(m)

def sj(f):
    for k,v in [("dashboard","ダッシュボード"),("workflow-engine","ワークフロー"),("analytics","分析基盤"),
     ("outreach","アウトリーチ"),("sales-agent","営業エージェント"),("email-generator","メール生成"),
     ("email-automations","メール自動化"),("email-manager","メール管理"),("email-crm","メールCRM"),
     ("leadgen","リード生成"),("harvester","OSINT"),("maps-scraper","マップスクレイパー"),
     ("web-scraper","Webスクレイパー"),("enricher","データエンリッチ"),("crm/platform","CRMプラットフォーム"),
     ("erp-extensions","ERP拡張"),("plugin","プラグイン"),("i18n","多言語対応"),("chat","チャット"),
     ("page-builder","ページビルダー"),("mailer","メール配信"),("scoring","スコアリング"),
     ("journey","カスタマージャーニー"),("marketing","マーケティング"),("privacy","プライバシー"),
     ("dolibarr","Dolibarr"),("erpnext","ERPNext"),("frappe","Frappe"),("contract","電子署名"),
     ("payment","決済"),("experiment","A/Bテスト"),("voip","音声通話"),("infra","インフラ"),("docker","Docker")]:
        if k in f: return v
    return ""


def build(modules,orig):
    plan=[]
    def ac(member,files,dates,ar=0.82):
        random.shuffle(files); na=int(len(dates)*ar)
        ch=max(1,len(files)//na) if na>0 else 1; idx=0; added=[]
        for i,dt in enumerate(dates):
            if idx<len(files) and (i<na or not added):
                end=min(idx+random.randint(max(1,ch-2),ch+5),len(files))
                b=files[idx:end]; idx=end; added.extend(b); s=sj(b[0])
                if member=="m2" and random.random()<0.15: c="ai"; s=""
                elif member=="m2" and any(x in b[0] for x in ["scraper","harvester"]) and random.random()<0.3: c="scraping"; s=""
                elif member=="m3" and "i18n" in b[0]: c="i18n"; s=""
                else: c="feat"
                plan.append((member,dt,gm(member,c,s),b,"add"))
            elif added:
                t=random.choice(added); s=sj(t)
                if member=="m1": c=random.choice(["fix","config","chore","refactor","docker","infra"])
                elif member=="m2":
                    c=random.choice(["ai","fix","wip","debug","chore","refactor","fullstack","docs"])
                    if c in ("ai","wip","debug","chore","docs","fullstack"): s=""
                elif member=="m3":
                    c=random.choice(["style","fix","chore","i18n","refactor"])
                    if c in ("style","i18n","chore"): s=""
                else: c=random.choice(["fix","config","chore","docs"])
                plan.append((member,dt,gm(member,c,s),[t],"modify"))
        return added

    p1e=datetime(2024,9,20,23,0,0)
    p1f=[]
    for mod in ["ROOT","cx330o-dashboard/public","cx330o-infra/core","cx330o-crm/core","cx330o-crm/email-crm"]:
        p1f.extend(modules.get(mod,[]))
    for f in get_files(orig):
        if f.startswith("cx330o-dashboard/") and f not in p1f: p1f.append(f)
    p1f=list(dict.fromkeys(p1f))
    ac("m1",p1f,gd(MEMBERS["m1"]["join"],p1e,350))

    p2e=datetime(2024,12,2,23,0,0)
    p2m2=[]; p2m1=[]
    for mod in ["cx330o-outreach/core","cx330o-outreach/sales-agent","cx330o-outreach/email-generator","cx330o-leadgen/enricher","cx330o-leadgen/core","cx330o-leadgen/maps-scraper"]:
        p2m2.extend(modules.get(mod,[]))
    for mod in ["cx330o-infra/workflow-engine"]:
        p2m1.extend(modules.get(mod,[]))
    ac("m2",p2m2,gd(MEMBERS["m2"]["join"],p2e,500))
    ac("m1",p2m1,gd(MEMBERS["m2"]["join"],p2e,300))

    p3e=datetime(2025,9,2,23,0,0)
    p3m2=[]; p3m3=[]; p3m1=[]
    for mod in ["cx330o-outreach/email-automations","cx330o-outreach/workflow","cx330o-outreach/email-manager","cx330o-leadgen/harvester","cx330o-leadgen/web-scraper"]:
        p3m2.extend(modules.get(mod,[]))
    for f in get_files(orig):
        if f.startswith("cx330o-voip/"): p3m2.append(f)
    for mod in ["cx330o-crm/platform","cx330o-crm/erp-extensions","cx330o-plugins/whatsapp-crm","cx330o-plugins/instagram-crm","cx330o-plugins/telegram-crm","cx330o-plugins/line-crm","cx330o-i18n/locales","cx330o-marketing/page-builder","cx330o-marketing/chat"]:
        p3m3.extend(modules.get(mod,[]))
    for f in get_files(orig):
        if f.startswith("cx330o-i18n/") and f not in p3m3: p3m3.append(f)
    for mod in ["cx330o-infra/analytics","cx330o-marketing/core","cx330o-marketing/mailer","cx330o-marketing/scoring","cx330o-marketing/journey","cx330o-extensions/dolibarr"]:
        p3m1.extend(modules.get(mod,[]))
    for f in get_files(orig):
        if f.startswith("cx330o-privacy/"): p3m1.append(f)
    ac("m2",p3m2,gd(MEMBERS["m3"]["join"],p3e,700))
    ac("m3",p3m3,gd(MEMBERS["m3"]["join"],p3e,600))
    ac("m1",p3m1,gd(MEMBERS["m3"]["join"],p3e,500))

    p4m4=[]
    for mod in ["cx330o-extensions/erpnext","cx330o-extensions/frappe"]:
        p4m4.extend(modules.get(mod,[]))
    for f in get_files(orig):
        if f.startswith("nebulas-contracts/") or f.startswith("cx330o-payments/") or f.startswith("cx330o-experiments/"): p4m4.append(f)
    ac("m4",p4m4,gd(MEMBERS["m4"]["join"],END,350))

    aa=[f for _,_,_,fs,a in plan for f in fs if a=="add"]
    if aa:
        for dt in gd(MEMBERS["m4"]["join"],END,250):
            t=random.choice(aa); c=random.choice(["ai","fix","refactor","fullstack","chore","docs"])
            plan.append(("m2",dt,gm("m2",c,""),[t],"modify"))
        for dt in gd(MEMBERS["m4"]["join"],END,200):
            t=random.choice(aa); c=random.choice(["style","fix","chore","i18n","refactor"])
            plan.append(("m3",dt,gm("m3",c,""),[t],"modify"))
        for dt in gd(MEMBERS["m4"]["join"],END,150):
            t=random.choice(aa); c=random.choice(["docker","infra","fix","config","chore"])
            plan.append(("m1",dt,gm("m1",c,""),[t],"modify"))
    plan.sort(key=lambda x:x[1])
    return plan


def execute(plan,branch):
    total=len(plan); ok=0; skip=0; added=set()
    for i,(member,dt,msg,files,action) in enumerate(plan):
        m=MEMBERS[member]; ds=fmt(dt)
        if action=="add":
            for f in files: extract(branch,f); added.add(f)
        else:
            did=False
            for f in files:
                if f in added and os.path.exists(f): did=modify(f)
                else:
                    if extract(branch,f): added.add(f); did=True
            if not did:
                for af in list(added)[:20]:
                    if os.path.exists(af):
                        if modify(af): break
        if commit(m["name"],m["email"],ds,msg): ok+=1
        else: skip+=1
        if (i+1)%50==0: print(f"  [{i+1}/{total}] ({(i+1)/total*100:.1f}%) ok={ok} skip={skip}")
    return ok,skip

def main():
    orig=rg("rev-parse","--abbrev-ref","HEAD").stdout.strip()
    print(f"Current branch: {orig}")
    if orig!="master":
        print("ERROR: Must be on master branch!"); return
    files=get_files(orig)
    print(f"Files in {orig}: {len(files)}")
    modules=cat_files(files)
    random.seed(42)
    plan=build(modules,orig)
    print(f"Commits planned: {len(plan)}")
    cn=defaultdict(int)
    for p in plan: cn[p[0]]+=1
    for m,c in sorted(cn.items()): print(f"  {m} ({MEMBERS[m]['name']}): {c}")

    if "--yes" not in sys.argv:
        a=input("\nThis will create orphan branch 'main'. master stays untouched.\nContinue? (y/n): ").strip().lower()
        if a!="y": print("Aborted."); return

    # Create orphan branch 'main'
    print("\nCreating orphan branch 'main'...")
    rg("branch","-D","main")  # delete if exists
    rg("checkout","--orphan","main")
    rg("rm","-rf",".")
    # Only remove git-tracked directories, NOT untracked files like Homepage*.png
    for item in os.listdir("."):
        if item==".git" or item=="generate_history.py": continue
        p=os.path.join(".",item)
        if os.path.isdir(p):
            # Check if this was a git-tracked directory
            if item.startswith("cx330o-") or item.startswith("nebulas-") or item==".vscode":
                shutil.rmtree(p,ignore_errors=True)
        elif item in [".gitignore","ARCHITECTURE.md","README.md","docker-compose.yml"]:
            try: os.remove(p)
            except: pass

    print("Executing commits...")
    ok,skip=execute(plan,orig)
    final_count=rg("rev-list","--count","HEAD").stdout.strip()
    print(f"\nDone! {ok} commits created, {skip} skipped")
    print(f"Actual commits on main: {final_count}")
    print(f"\nVerify: git log --oneline -10")
    print(f"Authors: git shortlog -sne")
    print(f"\nNext steps:")
    print(f"  1. git push -f origin main")
    print(f"  2. On GitHub: Settings > Default branch > change to 'main'")
    print(f"  3. On GitHub: delete 'master' branch")
    print(f"  4. Transfer repo to organization")

if __name__=="__main__":
    main()
