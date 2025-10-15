"""
Configuration pour AntiCroisenteria
"""

# Mot-clé qui déclenche le verrouillage
TRIGGER_KEYWORD = "croissanteria"

# Dossier où sauvegarder les photos
PHOTOS_DIR = "captures"

# Nom du fichier de log
LOG_FILE = "anticroissanteria.log"

# Délai en secondes avant de prendre la photo (pour capturer le coupable)
# 0 = instantané (mais peut avoir une image sombre)
# 0.1-0.3 = compromis rapidité/qualité
PHOTO_DELAY = 0

# Qualité de l'image (1-100)
IMAGE_QUALITY = 85

# Afficher les touches tapées (pour debug, mettre False en production)
DEBUG_MODE = False
