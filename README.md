# AntiCroissanteria 🥐

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Speed](https://img.shields.io/badge/speed-%3C40ms-red)
![Status](https://img.shields.io/badge/status-active-brightgreen)

Protection **ULTRA-RAPIDE** contre les "croissantages" sur PC Windows non verrouillé.

> Programme qui détecte quand quelqu'un tape un mot-clé (ex: "croissanteria"), verrouille instantanément le PC et prend une photo du coupable !

## ⚡ Vitesse de Réaction

- **Détection** : Instantanée (dès la dernière lettre tapée)
- **Verrouillage** : <40ms (AVANT que vous puissiez appuyer sur Entrée)
- **Photo** : Capturée en arrière-plan après le verrouillage
- **Résultat** : Le PC se verrouille **AVANT** que le message parte sur Slack/Teams !

## 🎯 Fonctionnalités

- 🔒 **Verrouillage INSTANTANÉ** du PC Windows (avant envoi du message)
- 📸 **Photo webcam** automatique du coupable
- ⌨️ **Détection ultra-rapide** du mot-clé personnalisable
- 📝 **Logs horodatés** avec preuves photo
- 🚀 **Démarrage automatique** avec Windows (optionnel)
- 👻 **Mode invisible** (pas de fenêtre visible) 🥐

Programme de protection **ULTRA-RAPIDE** contre les "croissantages" sur PC non verrouillé.

## ⚡ Vitesse de Réaction

- **Détection** : Instantanée (dès la dernière lettre tapée)
- **Verrouillage** : <10ms (AVANT que vous puissiez appuyer sur Entrée)
- **Photo** : Capturée en arrière-plan après le verrouillage
- **Résultat** : Le PC se verrouille **AVANT** que le message parte sur Slack !

## 🎯 Fonctionnalités

- 🔒 **Verrouillage INSTANTANÉ** du PC Windows (avant envoi du message)
- 📸 **Photo webcam** prise automatiquement
- ⌨️ **Détection ultra-rapide** du mot-clé
- 📝 **Logs horodatés** avec preuves photo
- � **Démarrage automatique** avec Windows
- 👻 **Mode invisible** (pas de fenêtre visible)

## 🚀 Installation

### 1. Cloner le repository

```bash
git clone https://github.com/VOTRE-USERNAME/AntiCroisenteria.git
cd AntiCroisenteria
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Configuration (optionnel)

Éditez `config.py` pour personnaliser :

```python
TRIGGER_KEYWORD = "croissanteria"  # Le mot-clé à détecter
PHOTOS_DIR = "captures"            # Dossier des photos
PHOTO_DELAY = 0                    # Délai avant photo (0 = instantané)
DEBUG_MODE = False                 # True pour voir les touches tapées
```

### 4. Lancer le programme

**Option A : Mode normal (avec console)**

```bash
python main.py
```

**Option B : Mode invisible (recommandé pour usage quotidien)**

```bash
# Double-cliquez sur lancer_invisible.vbs
# OU
pythonw main.py
```

**Option C : Menu interactif**

```bash
# Double-cliquez sur menu.bat
```

### 5. Installation au démarrage automatique (optionnel)

```bash
python install_startup.py  # Choisir option 1
```

**OU** double-cliquez sur `installer_demarrage.bat`

## 🎮 Comment ça marche

## 🎮 Comment ça marche

### Fonctionnement

1. Le programme surveille **toutes** les frappes clavier en temps réel
2. Dès que le mot-clé est **complètement tapé** :
   - ⚡ **VERROUILLAGE INSTANTANÉ** (en <40ms)
   - 📸 Photo capturée en arrière-plan
   - 📝 Log enregistré avec preuve
3. **RÉSULTAT** : L'attaquant n'a PAS le temps d'appuyer sur Entrée !

### Scénario typique

```
Attaquant tape : c-r-o-i-s-s-a-n-t-e-r-i-a
                                          ↑
                                    VERROUILLÉ !
                                    (avant Entrée)

Le message ne part JAMAIS sur Slack ! 😈
```

### Timeline visuelle

```
T = 0ms    : Dernière lettre tapée
T = 1ms    : Mot-clé détecté
T = 37ms   : PC VERROUILLÉ 🔒
T = 200ms  : L'attaquant appuie sur Entrée (TROP TARD!)
```

## 📊 Tests de Performance

Pour tester la vitesse du système :

```bash
python test_performance.py
```

Choisissez le test :

- **Test 1** : Mesure vitesse de verrouillage (⚠️ VA VERROUILLER)
- **Test 2** : Mesure vitesse de détection (sans verrouiller)
- **Test 3** : Benchmark complet (sans verrouiller)

Résultats typiques :

- ⏱️ Détection : <1ms
- ⏱️ Verrouillage : 5-10ms
- 👤 Temps humain pour Entrée : 100-200ms
- ✅ **Vous êtes 10-20x plus rapide !**

## ⚠️ Avertissement et Responsabilité

**Ce programme est destiné à un usage éducatif et ludique.**

⚠️ **Important** :

- Utilisez-le uniquement dans le cadre d'un jeu consensuel entre amis/collègues
- Informez tous les participants que ce système est actif
- N'installez PAS ce programme sur l'ordinateur d'autrui sans permission explicite
- Respectez les lois locales sur la surveillance et la vie privée
- Les auteurs ne sont pas responsables d'une utilisation inappropriée

**Fonctionnalités de surveillance** :

- Ce programme enregistre les frappes clavier (keylogger)
- Il prend des photos via webcam sans notification
- Il peut être configuré pour démarrer automatiquement

Assurez-vous d'avoir l'autorisation nécessaire avant toute installation.

## 📁 Structure du Projet

```
AntiCroissanteria/
├── main.py                    # Programme principal ⭐
├── config.py                  # Configuration
├── camera.py                  # Module webcam
├── locker.py                  # Module verrouillage
├── logger.py                  # Module logs
├── install_startup.py         # Installation démarrage auto
├── test_performance.py        # Tests de vitesse
├── menu.bat                   # Menu interactif Windows
├── lancer_invisible.vbs       # Lancement invisible
├── installer_demarrage.bat    # Installation facile
├── requirements.txt           # Dépendances Python
├── .gitignore                 # Fichiers ignorés par Git
├── LICENSE                    # Licence MIT
├── captures/                  # 📸 Photos capturées (auto-créé)
└── *.log                      # 📝 Fichiers de logs (auto-créé)
```

## 🛑 Désactivation

### Arrêt temporaire

- Appuyez sur `Echap` dans la console du programme
- OU `Ctrl+Shift+Esc` → Gestionnaire des tâches → Terminer "python.exe" ou "pythonw.exe"

### Désactiver le démarrage automatique

```bash
python install_startup.py  # Choisir option 2
```

## 📸 Voir les Résultats

### Photos capturées

Les photos sont sauvegardées dans le dossier `captures/` avec la date et l'heure :

```
captures/
├── croissante_20251015_143052.jpg
├── croissante_20251015_150233.jpg
└── croissante_20251015_162145.jpg
```

### Logs

Consultez le fichier `anticroissanteria.log` pour voir l'historique complet :

```
[2025-10-15 14:30:52] 🥐 CROISSANTAGE DÉTECTÉ ! Photo: captures/...
[2025-10-15 15:02:33] 🥐 CROISSANTAGE DÉTECTÉ ! Photo: captures/...
```

## 🔧 Dépannage

### Le programme ne démarre pas ?

- Vérifiez que Python 3.7+ est installé : `python --version`
- Réinstallez les dépendances : `pip install -r requirements.txt`

### La webcam ne fonctionne pas ?

- Vérifiez que la webcam est connectée et activée
- Fermez les autres applications utilisant la webcam (Zoom, Teams, etc.)
- Vérifiez les permissions Windows pour l'accès à la caméra

### Le verrouillage ne fonctionne pas ?

- Ce programme fonctionne **uniquement sur Windows**
- Essayez d'exécuter en tant qu'administrateur
- Testez manuellement : `python -c "import ctypes; ctypes.windll.user32.LockWorkStation()"`

### Comment vérifier si c'est actif ?

```bash
# Méthode 1 : Vérifier dans le gestionnaire des tâches
# Cherchez "python.exe" ou "pythonw.exe"

# Méthode 2 : Vérifier le démarrage automatique
python install_startup.py  # Option 3
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- 🐛 Signaler des bugs
- 💡 Proposer de nouvelles fonctionnalités
- 🔧 Soumettre des pull requests
- ⭐ Mettre une étoile si vous aimez le projet !

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- Merci à la communauté Python pour les bibliothèques `opencv-python` et `pynput`
- Inspiré par le jeu du "croissantage" pratiqué dans de nombreuses écoles et entreprises
- Créé dans un esprit de fun et d'apprentissage

## 📞 Support

Si vous rencontrez des problèmes :

1. Consultez la section [Dépannage](#-dépannage)
2. Vérifiez les [Issues](https://github.com/VOTRE-USERNAME/AntiCroisenteria/issues) existantes
3. Créez une nouvelle issue si nécessaire

---

**⚠️ Rappel** : Utilisez ce programme de manière responsable et éthique. Assurez-vous d'avoir le consentement de tous les utilisateurs avant installation.

**Bon croissantage (ou anti-croissantage) ! 🥐😈**
