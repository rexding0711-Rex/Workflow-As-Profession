#!/usr/bin/env python3
"""Flow 项目验证脚本 — 检查 YAML/元技能/引用完整性。
用法: python3 validate.py
放在 flow/references/ 目录下运行。
"""

import os, re, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FLOW_DIR = os.path.join(SCRIPT_DIR, "workflows")
SKILLS_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

# 元技能别名映射
MAP = {
    "analyze":"analyze-all", "create":"create-all", "review":"review-all",
    "decide":"decide-all", "execute":"execute-all", "monitor":"monitor-all",
    "quick":"quick-check", "dd":"due-diligence", "plan":"plan-on-the-spot",
    "format":"data-formatter", "geo":"content-engine", "summary":"doc-summary",
    "interview":"interview-simulator", "meeting":"meeting-to-action",
    "deal":"deal-analyzer", "graph":"graph-builder",
}

def check_references():
    """验证所有 YAML 引用的元技能都存在"""
    orphans = []
    all_refs = set()
    for dirpath, _, filenames in os.walk(FLOW_DIR):
        for fn in filenames:
            if fn.endswith('.yaml'):
                with open(os.path.join(dirpath, fn)) as f:
                    all_refs.update(re.findall(r'skill:\s*(/\S+)', f.read()))

    for ref in sorted(all_refs):
        s = ref.lstrip('/')
        resolved = MAP.get(s, s)
        if not os.path.isdir(os.path.join(SKILLS_DIR, resolved)):
            orphans.append(f"{ref} → {resolved}/")

    return len(all_refs), orphans

def check_structure():
    """验证 YAML 结构完整性"""
    yaml_count = 0
    bad = []
    for dirpath, _, filenames in os.walk(FLOW_DIR):
        for fn in filenames:
            if not fn.endswith('.yaml'): continue
            yaml_count += 1
            fpath = os.path.join(dirpath, fn)
            with open(fpath) as f:
                c = f.read()
            for field in ['name', 'description', 'daily', 'projects', 'skills', 'output']:
                if not re.search(rf'^{field}:', c, re.M):
                    bad.append(f"{os.path.relpath(fpath, FLOW_DIR)} 缺 {field}")
    return yaml_count, bad

def check_skills_field():
    """验证 skills 字段与实际引用一致"""
    missing = []
    extra = []
    for dirpath, _, filenames in os.walk(FLOW_DIR):
        for fn in filenames:
            if not fn.endswith('.yaml'): continue
            fpath = os.path.join(dirpath, fn)
            rel = os.path.relpath(fpath, FLOW_DIR)
            with open(fpath) as f:
                c = f.read()
            dm = re.search(r'^daily:.*?^skills:', c, re.DOTALL | re.M)
            sm = re.search(r'^skills:(.*?)^output:', c, re.DOTALL | re.M)
            if not dm or not sm: continue
            actual = set(re.findall(r'skill:\s*(/\S+)', dm.group(0)))
            declared = set(re.findall(r'^\s+-\s+(/\S+)', sm.group(1), re.M))
            if actual - declared:
                missing.append(f"{rel}: 用了未声明 {sorted(actual - declared)}")
            if declared - actual:
                extra.append(f"{rel}: 声明未使用 {sorted(declared - actual)}")
    return missing, extra

def check_skill_dirs():
    """验证所有 Skill 目录有 SKILL.md"""
    bad = []
    ok = 0
    for d in os.listdir(SKILLS_DIR):
        dp = os.path.join(SKILLS_DIR, d)
        if os.path.isdir(dp):
            if os.path.isfile(os.path.join(dp, "SKILL.md")):
                ok += 1
            else:
                bad.append(d)
    return ok, bad

def main():
    print("=" * 60)
    print("  Flow 项目验证")
    print("=" * 60)

    ref_count, orphans = check_references()
    print(f"\n📌 元技能引用: {ref_count} 个")
    if orphans:
        for o in orphans:
            print(f"  ❌ {o}")
    else:
        print("  ✅ 全部可解析")

    yaml_count, bad_struct = check_structure()
    print(f"\n📌 YAML 结构: {yaml_count} 个")
    if bad_struct:
        for b in bad_struct:
            print(f"  ❌ {b}")
    else:
        print("  ✅ 全部完整")

    missing, extra = check_skills_field()
    print(f"\n📌 Skills 字段一致性")
    if missing:
        for m in missing:
            print(f"  ➕ {m}")
    if extra:
        for e in extra:
            print(f"  ➖ {e}")
    if not missing and not extra:
        print("  ✅ 完全一致")

    ok_dirs, bad_dirs = check_skill_dirs()
    print(f"\n📌 Skill 目录: {ok_dirs} 个")
    if bad_dirs:
        for b in bad_dirs:
            print(f"  ❌ {b}/ 缺 SKILL.md")
    else:
        print("  ✅ 全部正常")

    # 总结
    errors = len(orphans) + len(bad_struct) + len(missing) + len(extra) + len(bad_dirs)
    print(f"\n{'='*60}")
    print(f"  错误总数: {errors}")
    if errors == 0:
        print("  ✅ 全部通过，可以上 GitHub")
    else:
        print("  ❌ 有问题，修完再上")
    print(f"{'='*60}")

    return 0 if errors == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
