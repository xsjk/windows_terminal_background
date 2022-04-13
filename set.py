import requests,json,os,random
config_path = rf"C:\Users\{os.getenv('USERNAME')}\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
config = json.load(open(config_path))
print(config['profiles']['list'][0]['backgroundImage'])
IMG_PATH = 'imgs'
if not os.path.exists(IMG_PATH):
    os.mkdir(IMG_PATH)
res = requests.get('https://ntp.msn.cn/resolver/api/resolve/v3/config/?expType=AppConfig&expInstance=default&apptype=edgeChromium&v=20220412.423&targetScope={"audienceMode":"adult","browser":{"browserType":"edgeChromium","version":"100","ismobile":"false"},"deviceFormFactor":"desktop","domain":"ntp.msn.cn","locale":{"content":{"language":"zh","market":"cn"},"display":{"language":"zh","market":"cn"}},"os":"windows","platform":"web","pageType":"ntp","pageExperiments":["prg-1s1-cryptd","prg-1sw-3dcrsl2","prg-1sw-accu10","prg-1sw-acrlc","prg-1sw-curr3","prg-1sw-dsdtc","prg-1sw-gevte","prg-1sw-grevtt","prg-1sw-hdukr","prg-1sw-mend","prg-1sw-ms-cloud","prg-1sw-mscloudn","prg-1sw-multif2","prg-1sw-nen3di","prg-1sw-pbpf1","prg-1sw-pcfc","prg-1sw-pr2fuzal","prg-1sw-pr2sdfuz","prg-1sw-pr2sdfze","prg-1sw-rndw","prg-1sw-sdset-c","prg-1sw-sp5mats","prg-1sw-sphn2msn","prg-1sw-splog","prg-1sw-spvdf","prg-1sw-spvdot2","prg-ad-cta-st","prg-adspeek","prg-atts-ctrl","prg-cidb-t","prg-ctr-pnpc","prg-dp-cb","prg-dp-cbsp","prg-ent-dynrankc","prg-entcomp-c","prg-favor-expc","prg-ias","prg-magicc","prg-ms-cloud","prg-ndauthrf2","prg-newpc-ctrl","prg-newsinte-staginc","prg-nodualauth","prg-onenavc","prg-pill-sp","prg-prmt-crtdv2","prg-prodicon-c1","prg-qna-staging","prg-rs-reorder3","prg-sbdarkt3","prg-social-weacf","prg-tel-refactor","prg-translvfeedc","prg-url-build","prg-wea-skipauth","prg-winline","prg-wpo-entfuzz","prg-wpo-rech5t","prg-wpo-sccls1g","prg-wpo-sdga","prg-wpo-stopwpocrs","prg-wtchcard1"]}').json()['configs']['BackgroundImageWC/default']['properties']
name,url = random.choice(list(zip(res['localizedStrings']['video_titles'].values(),[d['video']['v1080'] for d in res['video']['data']])))
if not os.path.exists(f'{IMG_PATH}/{name}.gif'):
    open(f'{IMG_PATH}/{name}.mp4', 'wb').write(requests.get(url).content)
    os.system(f'ffmpeg -i "{IMG_PATH}/{name}.mp4" "{IMG_PATH}/{name}.gif"')
    os.remove(f'{IMG_PATH}/{name}.mp4')
config['profiles']['list'][0]['backgroundImage'] = os.path.abspath(f'{IMG_PATH}/{name}.gif')
json.dump(config,open(config_path,'w'))