from django.urls import path, re_path, include
from . import views
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    ##########################################################
    #evaluations
    path('evaluations', views.evaluations, name='evaluations'),
    ############################################
    ########## TRAITEMENTS SUR LES NOMBRES ##########
    path('decimaux', views.decimaux, name='decimaux'),
    path('entiers', views.entiers, name='entiers'),
    #diviseurs
    path('diviseur', views.diviseur, name='diviseur'),
    path('calculDiviseur', views.calculDiviseur, name='calculDiviseur'),
    #multiple
    path('multiple', views.multiple, name='multiple'),
    path('calculMultiple', views.calculMultiple, name='calculMultiple'),
    #division_euclidienne
    path('division_euclidienne', views.division_euclidienne, name='division_euclidienne'),
    #division_euclidienne_result
    path('division_euclidienne_result', views.division_euclidienne_result, name='division_euclidienne_result'),
    
    #nombres_premiers
    path('nombres_premiers', views.nombres_premiers, name='nombres_premiers'),
    #facteurs_premiers
    path('facteurs_premiers', views.facteurs_premiers, name='facteurs_premiers'),
    #facteurs_premiers_result
    path('facteurs_premiers_result', views.facteurs_premiers_result, name='facteurs_premiers_result'),
    #division_euclidienne
    path('division_euclidienne', views.division_euclidienne, name='division_euclidienne'),
    #fraction_irreductible
    path('fraction_irreductible', views.fraction_irreductible, name='fraction_irreductible'),
    #fraction_irreductible_result
    path('fraction_irreductible_result', views.fraction_irreductible_result, name='fraction_irreductible_result'),
     ########## TRAITEMENTS SUR LES NOMBRES RELATIFS ##########

    path('relatifs', views.relatifs, name='relatifs'),
    #addition_relatifs
    path('addition_relatifs', views.addition_relatifs, name='addition_relatifs'),
    #addition_relatifs_result
    path('addition_relatifs_result', views.addition_relatifs_result, name='addition_relatifs_result'),
    #soustraction_relatifs
    path('soustraction_relatifs', views.soustraction_relatifs, name='soustraction_relatifs'),
    #soustraction_relatifs_result
    path('soustraction_relatifs_result', views.soustraction_relatifs_result, name='soustraction_relatifs_result'),
    #multiplication_relatifs
    path('multiplication_relatifs', views.multiplication_relatifs, name='multiplication_relatifs'),
    #multiplication_relatifs_result
    path('multiplication_relatifs_result', views.multiplication_relatifs_result, name='multiplication_relatifs_result'),
    #division_relatifs
    path('division_relatifs', views.division_relatifs, name='division_relatifs'),
    #division_relatifs_result
    path('division_relatifs_result', views.division_relatifs_result, name='division_relatifs_result'),
    ######################################################################################################################
    ################TRAITEMENTS SUR LES NOMBRES RATIONNELS################################################################
    path('rationnels', views.rationnels, name='rationnels'),
    #addition_rationnels
    path('addition_rationnels', views.addition_rationnels, name='addition_rationnels'),
    #addition_rationnels_result
    path('addition_rationnels_result', views.addition_rationnels_result, name='addition_rationnels_result'),
    #soustraction_rationnels
    path('soustraction_rationnels', views.soustraction_rationnels, name='soustraction_rationnels'),
    #soustraction_rationnels_result
    path('soustraction_rationnels_result', views.soustraction_rationnels_result, name='soustraction_rationnels_result'),
    #multiplication_rationnels
    path('multiplication_rationnels', views.multiplication_rationnels, name='multiplication_rationnels'),
    #multiplication_rationnels_result
    path('multiplication_rationnels_result', views.multiplication_rationnels_result, name='multiplication_rationnels_result'),
    #division_rationnels
    path('division_rationnels', views.division_rationnels, name='division_rationnels'),
    #division_rationnels_result
    path('division_rationnels_result', views.division_rationnels_result, name='division_rationnels_result'),

    path('puissances', views.puissances, name='puissances'), 
    #puissanceForm
    path('puissanceForm', views.puissanceForm, name='puissanceForm'), 
    #puissanceFormResult
    path('puissanceFormResult', views.puissanceFormResult, name='puissanceFormResult'), 
    #puissanceDixForm
    path('puissanceDixForm', views.puissanceDixForm, name='puissanceDixForm'),
    #puissanceDixFormResult
     path('puissanceDixFormResult', views.puissanceDixFormResult, name='puissanceDixFormResult'),
    ##########################################################
    ####################################################
    ########## TRAITEMENTS SUR LES FONCTIONS   ##########
    path('grandeurs_mesures', views.grandeurs_mesures, name='grandeurs_mesures'), 
    ########### TRAITEMENTS SUR LA PROPORTIONNALITE ##########
    path('proportionnalite', views.proportionnalite, name='proportionnalite'), 
    #displayProportionnalite
    path('displayProportionnalite', views.displayProportionnalite, name='displayProportionnalite'), 
    
    #echelle
    path('echelle', views.echelle, name='echelle'),
    #situation_proportionnalite
    path('situation_proportionnalite', views.situation_proportionnalite, name='situation_proportionnalite'),
    #tableauProportionnalite
    path('tableauProportionnalite', views.tableauProportionnalite, name='tableauProportionnalite'),
    
    #pourcentage
    path('pourcentage', views.pourcentage, name='pourcentage'),
    #probleme_proportionnalite
    path('probleme_proportionnalite', views.probleme_proportionnalite, name='probleme_proportionnalite'),
    

    path('statistique_probabilite', views.statistique_probabilite, name='statistique_probabilite'), 
    #effectif_frequence
    path('effectif_frequence', views.effectif_frequence, name='effectif_frequence'), 
    #representation_lecture_donnees
    path('representation_lecture_donnees', views.representation_lecture_donnees, name='representation_lecture_donnees'), 
    #mediane_etendue
    path('mediane_etendue', views.mediane_etendue, name='mediane_etendue'), 
    
    #moyenne
    path('moyenne', views.moyenne, name='moyenne'), 
    #probabilite
    path('probabilite', views.probabilite, name='probabilite'), 
    path('fonctions_role_lettre_egal', views.fonctions_role_lettre_egal, name='fonctions_role_lettre_egal'), 
    #role_lettre_egal
    path('role_lettre_egal', views.role_lettre_egal, name='role_lettre_egal'), 
    #fonctionsCollege
    path('fonctionsCollege', views.fonctionsCollege, name='fonctionsCollege'),
    path('calcul_litteral_in_equations', views.calcul_litteral_in_equations, name='calcul_litteral_in_equations'), 
    #calcul_litteral
    path('calcul_litteral', views.calcul_litteral, name='calcul_litteral'), 
    #inequations
    path('inequations', views.inequations, name='inequations'), 
    #####################################################
    ##########################################################
    ########## TRAITEMENTS SUR LA GEOMETRIE   ##########
    path('angles_triangles', views.angles_triangles, name='angles_triangles'),
    path('espace_reperage', views.espace_reperage, name='espace_reperage'),
    #repere_terre
    path('repere_terre', views.repere_terre, name='repere_terre'),
    #displayTerreGeographie
     path('displayTerreGeographie', views.displayTerreGeographie, name='displayTerreGeographie'),
    path('transformation_parallelogramme', views.transformation_parallelogramme, name='transformation_parallelogramme'),
    path('triangles_rectangles', views.triangles_rectangles, name='triangles_rectangles'),
    path('triangles_proportionnalite', views.triangles_proportionnalite, name='triangles_proportionnalite'), 
    ###########################################################################
    ########## TRAITEMENTS SUR LES ALGORITHMES ET LA PROGRAMMATION   ##########
    path('algorithmes_variables', views.algorithmes_variables, name='algorithmes_variables'),
    path('tests_si_sinon', views.tests_si_sinon, name='tests_si_sinon'),
    path('boucles_for_while', views.boucles_for_while, name='boucles_for_while'),
    path('liste_tableaux', views.liste_tableaux, name='liste_tableaux'),
    path('fonctions_procedures', views.fonctions_procedures, name='fonctions_procedures'), 
    #re_path(r'^_Matplotlib/Bar/$', include('visualization.views.GraphsViewBar')),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#