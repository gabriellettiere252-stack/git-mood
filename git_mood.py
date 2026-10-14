"""
git-mood.py - adicione humor/emoji aos seus commits de forma padronizada.

Uso:
    python git_mood.py
    python git_mood.py --mood feliz --msg "adiciona login"
    python git_mood.py --list
"""
import argparse, subprocess, sys

MOODS = {
    "feliz": "😄",
    "triste": "😢",
    "focado": "🎯",
    "cansado": "😴",
    "empolgado": "🚀",
    "bug": "🐛",
    "fix": "🔧",
    "docs": "📚",
    "refactor": "♻️",
    "teste": "🧪",
}

def list_moods():
    print("Moods disponíveis:")
    for k,v in MOODS.items():
        print(f"  {v}  {k}")

def make_message(mood, msg):
    emoji = MOODS.get(mood, "✨")
    return f"{emoji} [{mood}] {msg}"

def main():
    p = argparse.ArgumentParser(description="Git Mood - commits com humor")
    p.add_argument("--mood", help="seu humor atual")
    p.add_argument("--msg", "-m", help="mensagem do commit")
    p.add_argument("--list", action="store_true", help="listar moods")
    p.add_argument("--commit", action="store_true", help="já fazer git commit")
    args = p.parse_args()

    if args.list:
        list_moods(); return

    mood = args.mood or input(f"Como você está? {list(MOODS.keys())}: ").strip().lower()
    if mood not in MOODS:
        print(f"Mood '{mood}' não conhecido, usando ✨. Use --list para ver opções.")
    msg = args.msg or input("Mensagem do commit: ").strip()
    if not msg:
        print("Mensagem vazia, saindo."); sys.exit(1)

    final = make_message(mood, msg)
    print(f"\nMensagem gerada:\n{final}\n")

    if args.commit or input("Fazer commit agora? [s/N]: ").lower() == "s":
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", final])
        print("Commit feito!")

if __name__ == "__main__":
    main()