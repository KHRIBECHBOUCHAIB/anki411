import streamlit as st
import random
# Load CSS styles
def load_css():
    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load your logo image
def load_logo():
    logo = "images/logo.jpg"
    st.image(logo, width=100)
# Load your logo image
def load_logo1():
    logo = "images/logo1.png"
    st.image(logo, width=180)
# Define initial list of categories, years, decks, and subdecks
def get_categories_and_decks():
    return {
        "Académie": {
            "2024": {
                "Mathématiques": {
                    "Subdeck 1": [
                        {"question": "Quelle est la valeur de pi ?", "answer": "Approximativement 3.14159."},
                        {"question": "Comment calcule-t-on l'aire d'un cercle ?", "answer": "Aire = π x rayon²."},
                        {"question": "Qu'est-ce qu'un nombre premier ?", "answer": "Un nombre premier est un nombre qui n'a que deux diviseurs distincts : 1 et lui-même."},
                    ],
                },
                "Physique": {
                    "Subdeck 1": [
                        {"question": "Qu'est-ce que la force ?", "answer": "La force est une interaction entre deux objets qui peut provoquer une accélération."},
                        {"question": "Quelle est la formule de la force ?", "answer": "F = m * a (Force = masse * accélération)"},
                        {"question": "Comment explique-t-on le mouvement des planètes ?", "answer": "Le mouvement des planètes est expliqué par la gravitation universelle de Newton, où chaque objet dans l'univers attire chaque autre objet avec une force directionnelle qui est proportionnelle à la masse des objets et inversement proportionnelle au carré de la distance entre eux."},
                    ],
                },
                  "Biologie": {
                    "Système circulatoire":  [
                        {"question": "De quoi se compose le sang ?", "answer": "Le sang se compose de plasma, de globules rouges, de globules blancs et de plaquettes."},
                        {"question": "Quelle est la fonction principale des globules rouges ?", "answer": "Les globules rouges assurent le transport de l’oxygène."},
                        {"question": "À quoi servent les globules blancs ?", "answer": "Les globules blancs servent à défendre notre organisme contre les microbes."},
                        {"question": "Dans quoi le sang circule-t-il ?", "answer": "Le sang circule dans des vaisseaux sanguins : les artères, les veines et les capillaires."},
                        {"question": "Les veines sont-elles plus ou moins rigides que les artères ?", "answer": "Les veines sont moins rigides que les artères."},
                        {"question": "Quelles sont les deux types de circulation distinguées dans le fonctionnement du cœur ?", "answer": "La grande circulation et la petite circulation."},
                        {"question": "Que comprend la grande circulation ?", "answer": "La grande circulation comprend la partie gauche du cœur, l'aorte, et elle distribue l'oxygène à tout l'organisme."},
                        {"question": "Que permet la petite circulation ?", "answer": "La petite circulation permet au sang de se recharger en oxygène."},
                        {"question": "Où contient-on le sang chargé d'oxygène ?", "answer": "Dans les artères."},
                        {"question": "Quel est le nom de l'artère qui sort du ventricule gauche ?", "answer": "L'aorte."},
                        {"question": "Quel est le nom de l'artère qui sort du ventricule droit ?", "answer": "L'artère pulmonaire."},
                        {"question": "Quelle est la fonction des veines ?", "answer": "Les veines ramènent le sang chargé de déchets de l'ensemble du corps jusqu'au cœur."},
                        {"question": "Comment s'appellent les veines qui rentrent dans l'oreillette gauche ?", "answer": "Les veines pulmonaires."},
                        {"question": "Comment s'appellent les deux veines qui rentrent dans l'oreillette droite ?", "answer": "Les veines caves."},
                        {"question": "Quelle est la particularité des capillaires ?", "answer": "Ils sont très fins, relient les artères et les veines à l'intérieur de nos organes, et permettent l'échange d'oxygène et de dioxyde de carbone."},
                        {"question": "Qu'est-ce que le plasma ?", "answer": "Le plasma est un liquide incolore qui compose une partie du sang."},
                        {"question": "Pourquoi les globules rouges sont-ils rouges ?", "answer": "Les globules rouges sont rouges à cause de l’hémoglobine."},
                        {"question": "Quels organes sont en particulier approvisionnés en oxygène par la grande circulation ?", "answer": "La grande circulation approvisionne en oxygène le cerveau, les reins, le foie, entre autres organes vitaux."},
                        {"question": "Quelles parties du cœur sont impliquées dans la grande circulation ?", "answer": "L'oreillette gauche et le ventricule gauche sont impliqués dans la grande circulation."},
                        {"question": "Quelles parties du cœur sont impliquées dans la petite circulation ?", "answer": "L'oreillette droite et le ventricule droit sont impliqués dans la petite circulation."},
                        {"question": "Qu'est-ce qui relie les artères et les veines à l'intérieur de nos organes ?", "answer": "Les capillaires relient les artères et les veines à l'intérieur de nos organes."},
                    ],
                },
            },
        },
        "Langues": {
            "2024": {
                "Français": {
                    "Débutant": [
                        {"question": "Qu'est-ce qu'un verbe ?", "answer": "Un verbe est un mot qui exprime une action, un état ou une situation."},
                        {"question": "Qu'est-ce qu'un adjectif ?", "answer": "Un adjectif est un mot qui qualifie un nom ou un pronom."},
                        {"question": "Qu'est-ce qu'un nom ?", "answer": "Un nom est un mot qui désigne une personne, un animal, un lieu, une chose, une idée, etc."},
                    ],
                },
                "English": {
                    "Beginner": [
                        {"question": "What is a verb?", "answer": "A verb is a word that expresses an action, state, or occurrence."},
                        {"question": "What is an adjective?", "answer": "An adjective is a word that describes a noun or pronoun."},
                        {"question": "What is a noun?", "answer": "A noun is a word that names a person, place, thing, idea, or event."},
                    ],
                },
                "Español": {
                    "Principiante": [
                        {"question": "¿Qué es un verbo?", "answer": "Un verbo es una palabra que expresa una acción, estado o suceso."},
                        {"question": "¿Qué es un adjetivo?", "answer": "Un adjetivo es una palabra que describe un sustantivo o pronombre."},
                        {"question": "¿Qué es un sustantivo?", "answer": "Un sustantivo es una palabra que nombra a una persona, lugar, cosa, idea o evento."},
                    ],
                },
            },
        },
        "Personnel": {
            "2024": {
                "Développement personnel": {
                    "Subdeck 1": [
                        {"question": "Qu'est-ce que la gestion du temps ?", "answer": "La gestion du temps est l'art de planifier et de contrôler consciemment le temps passé sur des activités spécifiques pour augmenter l'efficacité ou la productivité."},
                        {"question": "Comment améliorer sa confiance en soi ?", "answer": "Améliorer sa confiance en soi peut être atteint par la pratique régulière de l'auto-affirmation, l'établissement d'objectifs réalisables et le développement de compétences."},
                        {"question": "Qu'est-ce que le bien-être ?", "answer": "Le bien-être est un état de satisfaction et de bonheur général, où une personne se sent équilibrée et en paix avec elle-même et son environnement."},
                             ],
                },
            },
        },
    }



# Initialize session and state variables if they don't exist
def initialize_session():
    if 'questions_reponses' not in st.session_state:
        st.session_state.questions_reponses = []
    if 'index_actuel' not in st.session_state:
        st.session_state.index_actuel = 0
    if 'voir_reponse' not in st.session_state:
        st.session_state.voir_reponse = False
    if 'quitter' not in st.session_state:
        st.session_state.quitter = False
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = None
    if 'selected_deck' not in st.session_state:
        st.session_state.selected_deck = None

# Display question or answer
def afficher_question():
    index = st.session_state.index_actuel
    qr = st.session_state.questions_reponses[index]
    if not st.session_state.voir_reponse:
        st.markdown(f"<div class='card-question'><h4>{qr['question']}</h4></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='card-reponse'><h4>{qr['answer']}</h4></div>", unsafe_allow_html=True)

# Show answer button
def bouton_voir_reponse():
    st.session_state.voir_reponse = not st.session_state.voir_reponse
    if not st.session_state.voir_reponse:
        bouton_cacher_reponse()

# Hide answer button
def bouton_cacher_reponse():
    st.session_state.voir_reponse = False

# Move to the next question
def bouton_next():
    if len(st.session_state.questions_reponses) == 2:
        # Move the current card to the end of the list
        st.session_state.questions_reponses.append(st.session_state.questions_reponses.pop(st.session_state.index_actuel))
        st.session_state.index_actuel = 0
    else:
        st.session_state.index_actuel = (st.session_state.index_actuel + 1) % len(st.session_state.questions_reponses)
    bouton_cacher_reponse()


# Move to the previous question
def bouton_previous():
    if st.session_state.index_actuel > 0:
        question = st.session_state.questions_reponses.pop(st.session_state.index_actuel)
        insert_at = (st.session_state.index_actuel - 1) % len(st.session_state.questions_reponses)
        st.session_state.questions_reponses.insert(insert_at, question)
    bouton_cacher_reponse()

# Remove the current question
def bouton_down():
    if len(st.session_state.questions_reponses) > 1:
        del st.session_state.questions_reponses[st.session_state.index_actuel]
        st.session_state.index_actuel %= len(st.session_state.questions_reponses)
    else:
        st.error("C'est la dernière carte. Vous pouvez actualiser la page pour reprendre la même catégorie, ou choisir une autre catégorie pour élargir vos connaissances.")
    bouton_cacher_reponse()

# Move the current question to the end of the deck
def bouton_fullback():
    current_card = st.session_state.questions_reponses[st.session_state.index_actuel]
    current_card.setdefault('fullback_count', 0)
    current_card['fullback_count'] += 1
    if current_card['fullback_count'] == 2:
        bouton_down()
    else:
        st.session_state.questions_reponses.append(st.session_state.questions_reponses.pop(st.session_state.index_actuel))
    bouton_cacher_reponse()

# Quit the session
def bouton_quitter():
    st.session_state.quitter = True

# Restart the session
def recommencer():
    st.session_state.questions_reponses = get_deck()
    st.session_state.index_actuel = 0
    bouton_cacher_reponse()
    st.session_state.quitter = False

# Get the selected deck
def get_deck():
    category = st.session_state.selected_category
    deck = st.session_state.selected_deck
    return get_categories_and_decks()[category][deck]

# Get the list of categories
def get_categories():
    return list(get_categories_and_decks().keys())

# Get the list of years for a given category
def get_years(category):
    return list(get_categories_and_decks()[category].keys())

# Get the list of decks for a given year
def get_decks(year, category=None):
    if category:
        decks = get_categories_and_decks()[category].get(year, {})
    else:
        decks = {}
        for cat in get_categories_and_decks():
            decks.update(get_categories_and_decks()[cat].get(year, {}))
    return list(decks.keys())

# Get the list of subdecks for a given deck and year
def get_subdecks(deck, year, category=None):
    if category:
        subdecks = get_categories_and_decks()[category][year].get(deck, {})
    else:
        subdecks = {}
        for cat in get_categories_and_decks():
            subdecks.update(get_categories_and_decks()[cat][year].get(deck, {}))
    return list(subdecks.keys())

# Main function
def main():
    load_css()
    load_logo1()
    initialize_session()

    st.markdown("""
<style>
.title {
    color: #007bff;  /* This is a common blue color, but you can adjust the hex code to any shade of blue you prefer */
}
</style>
<h1 class="title">Cartes Éducatives : Explore et Apprends</h1>
""", unsafe_allow_html=True)


    # Sidebar for category, year, deck, and subdeck selection
    with st.sidebar:
        load_logo()
        st.subheader('Sélectionner une catégorie, une année, un deck et un sous-deck')
        category = st.selectbox('Catégorie', get_categories())
        year = st.selectbox('Année', get_years(category))
        deck = st.selectbox('Deck', get_decks(year, category))
        subdeck = st.selectbox('sous-deck', get_subdecks(deck, year, category))

        mix_learning = st.checkbox('Mélanger tous les sous-decks')

        # Update session state with selected category, year, deck, and subdeck
        if st.button('Charger les cartes'):
            if mix_learning:
                questions_reponses = []
                for cat in get_categories_and_decks():
                    for yr in get_categories_and_decks()[cat]:
                        for d in get_categories_and_decks()[cat][yr]:
                            for sd in get_categories_and_decks()[cat][yr][d]:
                                questions_reponses.extend(get_categories_and_decks()[cat][yr][d][sd])
                st.session_state.questions_reponses = questions_reponses
                random.shuffle(st.session_state.questions_reponses)
            else:
                st.session_state.questions_reponses = get_categories_and_decks()[category][year][deck][subdeck]
            st.session_state.selected_category = category
            st.session_state.selected_year = year
            st.session_state.selected_deck = deck
            st.session_state.selected_subdeck = subdeck
            st.session_state.index_actuel = 0
            bouton_cacher_reponse()
        load_logo()
    # Display questions and answers
    if st.session_state.selected_category and st.session_state.selected_year and st.session_state.selected_deck and st.session_state.selected_subdeck:
        afficher_question()

        # Bouton pour voir/cacher la réponse
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("Fullback", on_click=bouton_fullback)
        with col2:
            st.button("Swap", on_click=bouton_voir_reponse)
        with col3:
            st.button("Next", on_click=bouton_next)
        st.button("Down", on_click=bouton_down)

# Add a blue footer with centered text
footer = f"""
<div style="position:fixed;bottom:0;width:100%;background-color:#007bff;color:white;padding:10px;text-align:center;">
<span style="display: block; margin: auto;">Tous les droits réservés ClinicoG 2024</span>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)



if __name__ == '__main__':
    main()

