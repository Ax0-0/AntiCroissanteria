"""
Module de logging pour enregistrer les événements
"""
from datetime import datetime
import config
import os


def log_event(photo_path=None, triggered_by="keyboard"):
    """
    Enregistre un événement dans le fichier de log
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = f"[{timestamp}] "
        log_entry += f"🥐 CROISSANTAGE DÉTECTÉ ! "
        
        if photo_path:
            log_entry += f"Photo: {photo_path} "
        
        log_entry += f"Déclenché par: {triggered_by}\n"
        
        # Ajouter au fichier de log
        with open(config.LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
        
        print(log_entry.strip())
        
    except Exception as e:
        print(f"❌ Erreur lors du logging : {e}")


def print_stats():
    """
    Affiche les statistiques depuis le début
    """
    try:
        if not os.path.exists(config.LOG_FILE):
            print("📊 Aucun événement enregistré pour le moment")
            return
        
        with open(config.LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        count = len([l for l in lines if "CROISSANTAGE" in l])
        print(f"📊 Total de croissantages détectés : {count}")
        
        if lines:
            print("\n📜 Derniers événements :")
            for line in lines[-5:]:
                print(line.strip())
                
    except Exception as e:
        print(f"❌ Erreur lors de la lecture des stats : {e}")
