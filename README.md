# 🎭 git-mood
### Descubra seu humor de programador a partir dos seus commits

Ninguém coloca sentimento no GitHub. O git-mood analisa suas mensagens de commit e gera um perfil psicológico-humorístico de dev.

[git-mood demo](https://img.shields.io/badge/mood-caf%C3%A9%20em%20p%C3%A2nico-orange)

## Como funciona
```bash
pip install git-mood
git-mood --repo . --output MOOD.md
```

Ele lê seus últimos 200 commits e detecta padrões:
- `fix`, `urgente`, `pelo amor` → **Modo Apaga-Incêndio 🔥**
- `wip`, `teste`, `vamos ver` → **Modo Cientista Maluco 🧪**
- `refactor`, `clean` → **Modo Marie Kondo ✨**

## Exemplo de saída
> **Seu mood essa semana: ☕ Café em Pânico**
> 67% dos commits foram fixes depois das 22h. Recomendação: dormir.

## Diferencial (por que ninguém tem isso)
1. Roda 100% via GitHub Action e atualiza seu perfil todo dia sozinho
2. Gera um gráfico de humor semanal em SVG sem dependências externas
3. Detecta "commits fantasmas" (aqueles `a`, `.`, `fix`) e te zoa por isso

## Roadmap
- [ ] Integração com Spotify (gera playlist pro seu mood)
- [ ] Badge dinâmico pro seu perfil
