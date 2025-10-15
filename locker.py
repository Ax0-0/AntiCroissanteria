"""
Module pour verrouiller le PC Windows - VERSION ULTRA RAPIDE
"""
import ctypes
import platform


def lock_computer():
    """
    Verrouille l'ordinateur Windows IMMÉDIATEMENT
    Optimisé pour une exécution en moins de 10ms
    Retourne True si succès, False sinon
    """
    try:
        if platform.system() != "Windows":
            print("❌ Ce programme fonctionne uniquement sur Windows")
            return False
        
        # Appel DIRECT à l'API Windows pour verrouillage instantané
        # Pas de print avant pour gagner du temps !
        result = ctypes.windll.user32.LockWorkStation()
        
        # Message APRÈS le verrouillage (ne ralentit pas)
        if result:
            print("🔒 PC VERROUILLÉ INSTANTANÉMENT !")
            return True
        else:
            print("❌ Erreur lors du verrouillage")
            return False
            
    except Exception as e:
        print(f"❌ Erreur : {e}")
        return False


# Pré-charger la fonction Windows pour accès ultra-rapide
try:
    _lock_function = ctypes.windll.user32.LockWorkStation
except:
    _lock_function = None


def lock_computer_ultrafast():
    """
    Version ultra-optimisée - appel direct sans vérification
    Utilisez seulement si vous êtes SÛR d'être sur Windows
    """
    if _lock_function:
        return _lock_function()
    return False
