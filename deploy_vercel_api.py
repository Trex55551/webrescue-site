#!/usr/bin/env python
"""Deploy the static WebRescue business site directly with Vercel's public API."""
import base64, json, mimetypes, os, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT=Path(r"C:\Users\desir\webrescue\business-site")
ENV=Path(r"C:\Users\desir\AppData\Local\hermes\.env")
for raw in ENV.read_text(encoding="utf-8-sig").splitlines():
    if raw.startswith("VERCEL_TOKEN="): os.environ["VERCEL_TOKEN"]=raw.split("=",1)[1].strip()
token=os.environ["VERCEL_TOKEN"]
include=["index.html","styles.css","script.js","privacy.html","terms.html","vercel.json","public/assets/webrescue-avatar.png","public/assets/webrescue-logo.png","public/assets/verified-before-bachulaw.png"]
files=[]
for rel in include:
    p=ROOT/rel
    target=rel.removeprefix("public/")
    b=p.read_bytes()
    files.append({"file":target,"data":base64.b64encode(b).decode(),"encoding":"base64"})
payload={"name":"webrescue-studio","target":"production","projectSettings":{"framework":None,"buildCommand":None,"outputDirectory":None,"installCommand":None},"files":files}
req=Request("https://api.vercel.com/v13/deployments?teamId=team_9u8eeuVX1ncFgEHeC8tbiNGH",data=json.dumps(payload).encode(),method="POST",headers={"Authorization":"Bearer "+token,"Content-Type":"application/json"})
try:
    with urlopen(req,timeout=180) as r: out=json.load(r)
except HTTPError as e:
    print(e.read().decode("utf-8","replace")); raise
print(json.dumps({k:out.get(k) for k in ("id","url","readyState","alias","name")},indent=2))
(Path(__file__).with_name("vercel_deployment.json")).write_text(json.dumps(out,indent=2),encoding="utf-8")
