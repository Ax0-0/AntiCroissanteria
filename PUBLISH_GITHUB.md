# 🚀 Guide de Publication sur GitHub

## Étapes pour publier AntiCroissanteria sur GitHub

### 1. Créer un repository sur GitHub

1. Allez sur [github.com](https://github.com)
2. Cliquez sur le **+** en haut à droite → **New repository**
3. Remplissez :
   - **Repository name** : `AntiCroissanteria`
   - **Description** : `Protection ultra-rapide contre les croissantages sur PC Windows 🥐`
   - **Public** ou **Private** (votre choix)
   - **N'ajoutez PAS** de README, .gitignore ou License (on les a déjà)
4. Cliquez sur **Create repository**

### 2. Initialiser Git localement

Ouvrez PowerShell dans le dossier `AntiCroissanteria` et exécutez :

```bash
# Initialiser le repository
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit: AntiCroissanteria v1.0 - Protection ultra-rapide"

# Ajouter le remote (remplacez VOTRE-USERNAME par votre nom d'utilisateur GitHub)
git remote add origin https://github.com/VOTRE-USERNAME/AntiCroissanteria.git

# Renommer la branche en main
git branch -M main

# Push vers GitHub
git push -u origin main
```

### 3. Vérifier sur GitHub

Retournez sur votre repository GitHub et actualisez la page. Vous devriez voir tous vos fichiers ! ✅

### 4. Personnaliser (optionnel)

#### Ajouter des topics/tags :

- Cliquez sur l'engrenage ⚙️ à côté de "About"
- Ajoutez des topics : `python`, `windows`, `security`, `keylogger`, `webcam`, `opensource`

#### Ajouter une image de profil :

- Créez un logo ou un screenshot
- Mettez-le dans le README avec : `![Logo](lien-vers-image)`

#### Activer GitHub Pages (optionnel) :

- Settings → Pages → Source : `main branch`

### 5. Protéger votre code

#### Ajouter un .github/workflows (CI/CD) :

```bash
mkdir .github\workflows
# Ajoutez des tests automatiques
```

#### Ajouter des badges au README :

```markdown
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-MIT-green)
```

### 6. Partager votre projet

Partagez le lien de votre repository :

```
https://github.com/VOTRE-USERNAME/AntiCroissanteria
```

Les utilisateurs pourront cloner avec :

```bash
git clone https://github.com/VOTRE-USERNAME/AntiCroissanteria.git
```

## 📝 Commandes Git Utiles

### Mettre à jour après modifications :

```bash
git add .
git commit -m "Description des modifications"
git push
```

### Créer une nouvelle version :

```bash
git tag v1.0.0
git push --tags
```

### Voir l'historique :

```bash
git log --oneline
```

### Annuler des modifications :

```bash
git checkout -- fichier.py  # Annuler un fichier
git reset HEAD~1            # Annuler le dernier commit
```

## 🎯 Checklist avant publication

- [ ] Tous les fichiers sensibles sont dans `.gitignore`
- [ ] Le README est clair et complet
- [ ] La LICENSE est présente
- [ ] Le code fonctionne correctement
- [ ] Les dépendances sont dans `requirements.txt`
- [ ] Aucun mot de passe ou token dans le code
- [ ] Les commentaires sont clairs
- [ ] Le `.gitignore` exclut `captures/` et `*.log`

## 🔒 Sécurité

**N'ajoutez JAMAIS au repository** :

- ❌ Vos photos capturées (`captures/`)
- ❌ Vos logs (`*.log`)
- ❌ Vos informations personnelles
- ❌ Des tokens ou mots de passe

Ces fichiers sont déjà exclus par le `.gitignore`.

## 🎉 C'est fait !

Votre projet est maintenant open-source et disponible pour tous !

N'oubliez pas de :

- ⭐ Encourager les gens à mettre une étoile
- 📢 Partager sur les réseaux sociaux
- 🐛 Répondre aux issues
- 🤝 Accepter les pull requests

**Bon succès avec votre projet ! 🥐😈**
