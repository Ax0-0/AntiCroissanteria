"""
AntiCroisenteria - Programme principal
Détecte un mot-clé, prend une photo et verrouille le PC
VERSION ULTRA-RAPIDE
"""
import sys
import threading
from pynput import keyboard
import config
from camera import take_photo
from locker import lock_computer
from logger import log_event, print_stats


class AntiCroisenteria:
    def __init__(self):
        self.current_keys = []
        self.running = True
        self.defense_active = False
        
    def on_press(self, key):
        """Appelé à chaque touche pressée - RÉACTION INSTANTANÉE"""
        try:
            # Récupérer le caractère de la touche
            if hasattr(key, 'char') and key.char:
                self.current_keys.append(key.char.lower())
                
                # Garder seulement les derniers caractères
                max_length = len(config.TRIGGER_KEYWORD) + 10
                if len(self.current_keys) > max_length:
                    self.current_keys = self.current_keys[-max_length:]
                
                # Vérifier si le mot-clé est présent
                current_string = ''.join(self.current_keys)
                
                if config.DEBUG_MODE:
                    print(f"Buffer: {current_string}")
                
                # DÉCLENCHEMENT IMMÉDIAT dès que le mot-clé complet est tapé
                if config.TRIGGER_KEYWORD.lower() in current_string and not self.defense_active:
                    print(f"\n⚠️  MOT-CLÉ DÉTECTÉ : {config.TRIGGER_KEYWORD}")
                    self.defense_active = True
                    
                    # VERROUILLAGE IMMÉDIAT dans le thread principal (le plus rapide)
                    # Pas de thread séparé pour éviter tout délai !
                    lock_computer()  # VERROUILLAGE INSTANTANÉ !
                    
                    # Photo et log en arrière-plan après le verrouillage
                    defense_thread = threading.Thread(target=self.capture_evidence)
                    defense_thread.daemon = True
                    defense_thread.start()
                    
        except Exception as e:
            if config.DEBUG_MODE:
                print(f"Erreur : {e}")
    
    def on_release(self, key):
        """Appelé quand une touche est relâchée"""
        # Arrêter le programme avec Ctrl+C ou Echap
        if key == keyboard.Key.esc:
            print("\n👋 Arrêt du programme...")
            self.running = False
            return False
    
    def capture_evidence(self):
        """Capture la preuve en arrière-plan (APRÈS le verrouillage)"""
        try:
            print("\n" + "="*50)
            print("🚨 VERROUILLAGE ACTIVÉ - Capture des preuves...")
            print("="*50 + "\n")
            
            # Prendre une photo (en arrière-plan)
            print("📸 Capture de l'intrus...")
            photo_path = take_photo()
            
            # Logger l'événement
            log_event(photo_path=photo_path)
            
            # Réinitialiser
            self.current_keys = []
            self.defense_active = False
            
            print("\n✅ Preuves capturées et sauvegardées !")
            print("="*50 + "\n")
            
        except Exception as e:
            print(f"❌ Erreur capture: {e}")
            self.defense_active = False
    
    def start(self):
        """Démarre l'écoute du clavier"""
        print("="*50)
        print("🥐 AntiCroisenteria - ACTIF 🥐")
        print("="*50)
        print(f"\n⚙️  Configuration :")
        print(f"   - Mot-clé : '{config.TRIGGER_KEYWORD}'")
        print(f"   - Photos : {config.PHOTOS_DIR}/")
        print(f"   - Logs : {config.LOG_FILE}")
        print(f"\n👀 En attente de détection...")
        print(f"💡 Appuyez sur Echap pour quitter\n")
        
        # Afficher les stats
        print_stats()
        print()
        
        # Démarrer l'écoute du clavier
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()


def main():
    """Point d'entrée du programme"""
    try:
        anti_croissant = AntiCroisenteria()
        anti_croissant.start()
    except KeyboardInterrupt:
        print("\n\n👋 Programme arrêté par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur fatale : {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
