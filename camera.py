"""
Module pour capturer des photos avec la webcam
"""
import cv2
import os
from datetime import datetime
import config


def take_photo():
    """
    Prend une photo avec la webcam et la sauvegarde
    Retourne le chemin du fichier ou None en cas d'erreur
    """
    try:
        # Créer le dossier de captures s'il n'existe pas
        if not os.path.exists(config.PHOTOS_DIR):
            os.makedirs(config.PHOTOS_DIR)
        
        # Ouvrir la webcam (0 = webcam par défaut)
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Erreur : Impossible d'accéder à la webcam")
            return None
        
        # Laisser la caméra s'initialiser
        import time
        time.sleep(config.PHOTO_DELAY)
        
        # Capturer plusieurs frames pour avoir une meilleure image
        for _ in range(5):
            ret, frame = cap.read()
        
        # Capturer l'image finale
        ret, frame = cap.read()
        
        if ret:
            # Générer un nom de fichier avec timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"croissante_{timestamp}.jpg"
            filepath = os.path.join(config.PHOTOS_DIR, filename)
            
            # Sauvegarder l'image
            cv2.imwrite(filepath, frame, [cv2.IMWRITE_JPEG_QUALITY, config.IMAGE_QUALITY])
            print(f"📸 Photo capturée : {filepath}")
            
            # Libérer la webcam
            cap.release()
            
            return filepath
        else:
            print("❌ Erreur : Impossible de capturer l'image")
            cap.release()
            return None
            
    except Exception as e:
        print(f"❌ Erreur lors de la capture : {e}")
        return None
