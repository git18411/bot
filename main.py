from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError
import json

def like(username, password, post_url):
    print("Début de la fonction like")
    print(username, password, post_url)
    print("Initialisation du client...")
    #input("Appuyez sur Entrée pour continuer...")
    try:
        print("🔗 Connexion à Instagram...")
        
        # Client avec configuration réduite
        cl = Client()
        
        try : 
            cl.load_settings(f"session_{username}.json")
            print("Session loaded")
        except :
            cl.login(username, password)
            cl.dump_settings(f"session_{username}.json")
            print("Session created and saved")

        
        print("✅ Connecté avec succès")
        
        # Récupérer le media_pk
        print("📱 Récupération des informations du post...")
        media_pk = cl.media_pk_from_url(post_url)
        print(f"Media PK: {media_pk}")
        
        # Liker directement avec media_pk (évite la conversion en media_id)
        print("❤️  Tentative de like...")
        result = cl.media_like(media_pk)
        
        print("✅ Publication likée avec succès !")
        return True
        
    except LoginRequired:
        print("❌ Erreur de connexion - vérifiez vos identifiants")
        return False
    except ClientError as e:
        print(f"❌ Erreur Instagram: {e}")
        return False
    except Exception as e:
        print(f"⚠️  Erreur technique: {e}")
        print("Tentative avec une approche alternative...")
        
        
        def like2(cl, post_url):
            """Méthode alternative en cas d'erreur de validation"""
            try:
                # Utiliser l'API bas niveau
                media_pk = cl.media_pk_from_url(post_url)
                
                # Appel direct à l'endpoint API
                cl.private_request(f"media/{media_pk}/like/")
                
                print("✅ Like réussi avec méthode alternative !")
                return True
            except Exception as e:
                print(f"❌ L'alternative a échoué: {e}")
                return False
        
        return like2(cl, post_url)





username = "tsanta.aaaa2"
password = "nantoooo1."
post_url = "https://www.instagram.com/p/DRmkvBPDQ3f/"

like(username, password, post_url)


    
# instagrapi (GitHub version 2.0+)
# pydantic==2.11.10
# pydantic-core==2.33.2
# annotated-types==0.7.0
# typing-extensions==4.15.0
# typing-inspection==0.4.2
# requests==2.32.3
# pycryptodome==3.21.0


