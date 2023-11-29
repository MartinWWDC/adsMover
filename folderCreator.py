import os

def create_folder_structure(ad_id):
    # Directory paths
    base_path = "./public/"
    ad_path = os.path.join(base_path, str(ad_id))
    conversions_path = os.path.join(ad_path, "conversions")
    responsive_images_path = os.path.join(ad_path, "responsive-images")

    # Create directories
    os.makedirs(ad_path)
    os.makedirs(conversions_path)
    os.makedirs(responsive_images_path)

    # Create placeholder image files in conversions folder
    for i in range(1, 2):
        img_path = os.path.join(conversions_path, f"img{i}")
        with open(img_path, "w") as f:
            f.write(f"This is img{i}")

    # Create placeholder image files in responsive-images folder
    for i in range(3, 5):
        img_path = os.path.join(responsive_images_path, f"img{i}")
        with open(img_path, "w") as f:
            f.write(f"This is img{i}")



def genSingleAd():
    ad_id = input("Inserisci l'ID dell'annuncio: ")
    create_folder_structure(ad_id)
    print("Struttura delle cartelle creata con successo.")

