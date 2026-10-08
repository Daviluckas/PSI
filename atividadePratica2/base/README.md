# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
Para saber se aquele livro está disponível ou não

2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
Para que aquela alteração seja registarda no sistema

3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
Não fiz as consultas