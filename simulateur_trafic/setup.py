from setuptools import setup, find_packages

setup(
    name='simulateur_trafic_package',
    version='0.1.1',
    author='Amaidi Chaima',
    author_email='amaidiamaidi13@gmail.com',
    description=(
        "Un simulateur modulaire du trafic routier permettant de modéliser des routes, intersections et véhicules, "
        "et de visualiser les résultats de simulation sous forme graphique."
    ),
    long_description=(
        "Ce package Python vise à concevoir une application orientée objet complète "
        "pour simuler un réseau routier comportant plusieurs routes, intersections "
        "et véhicules. Il met en œuvre des techniques avancées de programmation objet "
        "et propose une architecture modulaire et testable.\n\n"
        "Le simulateur permet de :\n"
        "- Modéliser un réseau routier (routes, intersections, véhicules)\n"
        "- Simuler la circulation et analyser les comportements\n"
        "- Générer des statistiques (embouteillages, vitesses moyennes, temps de parcours)\n"
        "- Visualiser les résultats sous forme graphique ou cartographique\n"
        "- Fournir des rapports via la console, des fichiers ou des cartes interactives.\n\n"
        "Développé dans le cadre d’un projet de mobilité intelligente, ce simulateur est "
        "réutilisable et extensible pour des travaux de recherche ou des applications "
        "industrielles dans le domaine du transport."
    ),
    long_description_content_type='text/plain',
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.7.1',
        'numpy>=1.26.0',
        'numba>=0.58.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',

    ],
    python_requires='>=3.8',
)
