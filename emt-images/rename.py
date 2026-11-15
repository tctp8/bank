import os, shutil

ROOT = os.path.expanduser("~/Desktop/emt-images")
EMBED = os.path.join(ROOT, "embedded")

# 完整檔名 → (年度, 題號, 選項)
mapping = {
    # 108
    "q013-C55cl90B.png": ("108", "q013", None),
    "q026-1dTcMEsL.png": ("108", "q026", None),
    "q036-OepLRMdK.png": ("108", "q036", None),
    "q037-CxgrhlhX.png": ("108", "q037", None),
    "q040-BsObgDOr.png": ("108", "q040", None),
    "q046-BXZRQUq9.png": ("108", "q046", None),
    "q067_1-DAMBIg78.png": ("108", "q067", "1"),
    "q067_2-dVadf9_7.png": ("108", "q067", "2"),
    "q073-Beq-1HMl.png": ("108", "q073", None),
    "q074-XNUEdech.png": ("108", "q074", None),
    # 109
    "q009_1-Dnij3Zkd.png": ("109", "q009", "1"),
    "q009_2-D9WYpWAS.png": ("109", "q009", "2"),
    "q009_3-lT9oecg4.png": ("109", "q009", "3"),
    "q009_4-bGCUeXTB.png": ("109", "q009", "4"),
    "q014-zfw5Dbge.png": ("109", "q014", None),
    "q045-C8UjJiyf.png": ("109", "q045", None),
    "q055-B-T-gZQv.png": ("109", "q055", None),
    "q064-CeK2dCuy.png": ("109", "q064", None),
    "q068-B0lK0uOd.png": ("109", "q068", None),
    # 110
    "q024-CxRERLwY.png": ("110", "q024", None),
    "q035-dRWY75ou.png": ("110", "q035", None),
    "q039-ChCtjzM8.png": ("110", "q039", None),
    "q054-BYgwn0cl.png": ("110", "q054", None),
    "q058-CRa7Ma1l.png": ("110", "q058", None),
    "q059-XAgmXLpR.png": ("110", "q059", None),
    "q063-BAfF4Hw1.png": ("110", "q063", None),
    # 111（base64 解出的 4 張在 embedded/）
    "q015_1.png": ("111", "q015", "1"),
    "q015_2.png": ("111", "q015", "2"),
    "q015_3.png": ("111", "q015", "3"),
    "q015_4.png": ("111", "q015", "4"),
    "q039-CgHIcJ43.png": ("111", "q039", None),
    "q061-CLhYhL8U.png": ("111", "q061", None),
    # 112
    "q009_1-D-k-v-te.png": ("112", "q009", "1"),
    "q009_2-DRW50ik4.png": ("112", "q009", "2"),
    "q056-D8gLZPra.png": ("112", "q056", None),
    "q057-B1gsFeYV.png": ("112", "q057", None),
    "q058_1-Bn-_2Htr.png": ("112", "q058", "1"),
    "q058_2-AJsjkr90.png": ("112", "q058", "2"),
    "q058_3-CDSzIti2.png": ("112", "q058", "3"),
    "q058_4-BpyFIElE.png": ("112", "q058", "4"),
    "q060-CRii4xjQ.png": ("112", "q060", None),
    "q083_1-DouFtrIO.png": ("112", "q083", "1"),
    "q083_2-CHmDLpTe.png": ("112", "q083", "2"),
    "q083_3-CQVna1YF.png": ("112", "q083", "3"),
    "q083_4-B6NnPIH9.png": ("112", "q083", "4"),
    "q088-C6Aj_2AA.png": ("112", "q088", None),
    # 113
    "q054-Bxi2bHrA.png": ("113", "q054", None),
    "q056-D152P2Hg.png": ("113", "q056", None),
    # 114
    "q055-CQ4A192j.png": ("114", "q055", None),
}

def new_name(year, q, opt):
    return f"{year}_{q}_{opt}.png" if opt else f"{year}_{q}.png"

def rename_in(folder, mapping):
    for old, (year, q, opt) in mapping.items():
        src = os.path.join(folder, old)
        if not os.path.exists(src):
            continue
        dst = os.path.join(ROOT, new_name(year, q, opt))  # 一律放到根目錄
        if os.path.exists(dst) and not os.path.samefile(src, dst):
            print(f"SKIP（目標已存在）{old} -> {os.path.basename(dst)}")
            continue
        shutil.move(src, dst)
        print(f"OK {old} -> {os.path.basename(dst)}")

# 先處理根目錄的 45 張
rename_in(ROOT, mapping)
# 再處理 embedded/ 的 4 張，並搬到根目錄
rename_in(EMBED, mapping)

# 清掉空的 embedded/
if os.path.isdir(EMBED) and not os.listdir(EMBED):
    os.rmdir(EMBED)
    print("已移除空的 embedded/")

print("\n完成。")